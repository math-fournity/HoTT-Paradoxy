#!/usr/bin/env python3
"""R034: finite path-indexed equations elaborated into the unchanged R032 checker.

This is a declared finite permutation semantics, not a HoTT kernel.  Computation
leaves are individually checked, then passed as explicit assumptions to R032;
R032 acceptance alone does not discharge the model-to-HoTT correspondence.
"""
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
import argparse, copy, hashlib, json
import r032_restricted_reflection as core

class Rejected(ValueError): pass

def need(ok, message):
    if not ok: raise Rejected(message)

def clean_tree(x, stack=None):
    stack=set() if stack is None else stack
    need(type(x) in (dict,list,str,int,bool,type(None)), 'non-JSON node')
    if type(x) not in (dict,list): return
    need(id(x) not in stack, 'cyclic syntax')
    stack.add(id(x))
    try:
        if type(x) is dict:
            need(all(type(k) is str for k in x), 'non-string key')
            for v in x.values():clean_tree(v,stack)
        else:
            for v in x:clean_tree(v,stack)
    finally:stack.remove(id(x))

def fields(x, keys):
    need(type(x) is dict and set(x)==set(keys), 'malformed fields')

def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def then(p,q): return tuple(q[i] for i in p)
def inverse(p):return tuple(p.index(i) for i in range(len(p)))

def validate_env(env):
    clean_tree(env);fields(env,('fibres','generators'))
    need(type(env['fibres']) is dict and bool(env['fibres']), 'empty fibres')
    for obj,n in env['fibres'].items():
        need(type(obj) is str and obj and type(n) is int and n>=0, 'bad fibre')
    need(type(env['generators']) is dict,'bad generators')
    for name,g in env['generators'].items():
        need(bool(name),'empty generator');fields(g,('source','target','table'))
        s,t,table=g['source'],g['target'],g['table']
        need(s in env['fibres'] and t in env['fibres'],'unknown endpoints')
        need(type(table) is list and all(type(i) is int for i in table),'bad permutation entries')
        need(len(table)==env['fibres'][s] and sorted(table)==list(range(env['fibres'][t])), 'not a finite bijection')

def path_semantics(p,env):
    """Free finite groupoid words interpreted as explicit bijections."""
    clean_tree(p)
    def go(x):
        need(type(x) is dict and 'op' in x,'bad path')
        op=x['op']
        if op=='id':
            fields(x,('op','object'));o=x['object'];need(o in env['fibres'],'unknown object')
            return o,o,tuple(range(env['fibres'][o])),frozenset()
        if op=='gen':
            fields(x,('op','name'));n=x['name'];need(n in env['generators'],'missing path generator')
            g=env['generators'][n];return g['source'],g['target'],tuple(g['table']),frozenset([n])
        if op=='inv':
            fields(x,('op','path'));s,t,p,d=go(x['path']);return t,s,inverse(p),d
        if op=='seq':
            fields(x,('op','first','second'));s,t,p,d=go(x['first']);u,v,q,e=go(x['second'])
            need(t==u,'non-composable paths');return s,v,then(p,q),d|e
        # No constructor turns a mere-existence flag into a particular action.
        raise Rejected('unknown path constructor; mere equality is not a path witness')
    return go(p)

def eval_value(t,env):
    clean_tree(t)
    need(type(t) is dict and 'op' in t,'bad value')
    if t['op']=='lit':
        fields(t,('op','object','value'));o,v=t['object'],t['value']
        need(o in env['fibres'] and type(v) is int and 0<=v<env['fibres'][o],'ill-typed literal')
        return o,v,frozenset()
    if t['op']=='cast':
        fields(t,('op','path','value'));s,tgt,p,d=path_semantics(t['path'],env);o,v,e=eval_value(t['value'],env)
        need(o==s,'transport source mismatch');return tgt,p[v],d|e
    raise Rejected('unknown value constructor')

def lit(v,obj='B'):return {'op':'lit','object':obj,'value':v}
def gen(n='p'):return {'op':'gen','name':n}
def ident(o='B'):return {'op':'id','object':o}
def inv(p):return {'op':'inv','path':p}
def seq(p,q):return {'op':'seq','first':p,'second':q}
def cast(p,t):return {'op':'cast','path':p,'value':t}
def eq(a,b):return {'kind':'eq','left':a,'right':b}
def arr(a,b):return {'kind':'imp','domain':a,'codomain':b}
def calc(a,b):return {'rule':'calc','left':a,'right':b}

def check(proof,env):
    """Elaborate path-indexed equations into R032 atoms and replay actual rules."""
    validate_env(env);clean_tree(proof);registry={};decls={};support=set();leaves=[]
    def formula(a):
        need(type(a) is dict and 'kind' in a,'bad indexed formula')
        if a['kind']=='eq':
            fields(a,('kind','left','right'));x=eval_value(a['left'],env);y=eval_value(a['right'],env)
            need(x[0]==y[0],'equality endpoints have different types')
            # Normalization here is THIS finite model, not Book judgmental equality.
            key=(x[0],x[1],y[1]);registry.setdefault(key,len(registry));support.update(x[2]|y[2])
            return core.atom(registry[key])
        if a['kind']=='imp':
            fields(a,('kind','domain','codomain'));return core.imp(formula(a['domain']),formula(a['codomain']))
        if a['kind']=='bot':fields(a,('kind',));return core.BOT
        raise Rejected('unknown indexed formula')
    def go(p,ctx):
        need(type(p) is dict and 'rule' in p,'bad proof');r=p['rule']
        if r=='calc':
            fields(p,('rule','left','right'));a=eq(p['left'],p['right']);f=formula(a)
            x=eval_value(p['left'],env);y=eval_value(p['right'],env);need(x[:2]==y[:2],'computed equality is false')
            name='checked_equation_'+str(len(leaves));decls[name]=f;leaves.append({'label':name,'formula':a,'value':x[1],'status':'finite-model computation checked'})
            return core.ax(name),a
        if r=='var':
            fields(p,('rule','index'));i=p['index'];need(type(i) is int and 0<=i<len(ctx),'unbound variable')
            return core.var(i),ctx[i]
        if r=='lam':
            fields(p,('rule','domain','body'));formula(p['domain']);body,b=go(p['body'],(p['domain'],)+ctx)
            return core.lam(formula(p['domain']),body),arr(p['domain'],b)
        if r=='app':
            fields(p,('rule','function','argument'));f,a=go(p['function'],ctx);v,b=go(p['argument'],ctx)
            need(a['kind']=='imp' and formula(a['domain'])==formula(b),'dependent application mismatch')
            return core.app(f,v),a['codomain']
        if r=='absurd':
            fields(p,('rule','target','proof'));f,a=go(p['proof'],ctx);need(a=={'kind':'bot'},'bottom needed')
            return core.absurd(formula(p['target']),f),p['target']
        raise Rejected('unrecognized proof rule')
    elaborated,goal=go(proof,());expected=formula(goal)
    c=core.infer(elaborated,decls);need(c.formula==expected,'R032 conclusion mismatch')
    return {'goal':goal,'path_support':sorted(support),'equation_leaves':leaves,'r032':core.quote(decls,elaborated,expected),
            'atom_registry':[{'index':i,'normal_equation':k} for k,i in registry.items()],
            'scope':'R032 proof replay plus independently checked finite permutation equations; not a HoTT kernel'}

def quote(proof,env):
    checked=check(proof,env)
    return {'schema':'r034-path-certificate/v1','environment':copy.deepcopy(env),'environment_hash':digest(env),
            'proof':copy.deepcopy(proof),'goal':checked['goal'],'path_support':checked['path_support']}

def validate_package(p):
    clean_tree(p);fields(p,('schema','environment','environment_hash','proof','goal','path_support'))
    need(p['schema']=='r034-path-certificate/v1','wrong schema');need(p['environment_hash']==digest(p['environment']),'environment digest mismatch')
    c=check(p['proof'],p['environment']);need(c['goal']==p['goal'] and c['path_support']==p['path_support'],'forged certificate metadata')
    return c

def replay_receipt(receipt,source_env,target_env):
    """Value y:B(x), plus dependent equation z:y=expected.  Source is rechecked."""
    fields(receipt,('term','expected'));validate_env(source_env);validate_env(target_env)
    c=check(calc(receipt['term'],receipt['expected']),source_env)
    # Exact same indexed claim is rechecked, rather than weakening it to fibre type.
    return check(calc(receipt['term'],receipt['expected']),target_env)

def same_action_on_support(package,target):
    checked=validate_package(package);validate_env(target);source=package['environment']
    for name in checked['path_support']:
        need(name in target['generators'] and source['generators'][name]==target['generators'][name], 'no full-action bridge for '+name)
    # Literal fibres also need their interpretations retained. This is sufficient,
    # not necessary for one particular certificate's conclusion.
    need(source['fibres']==target['fibres'],'fibre interpretation changed')
    return quote(package['proof'],target)

def bool_env(table=(1,0)):
    return {'fibres':{'B':2},'generators':{'p':{'source':'B','target':'B','table':list(table)}}}

def evidence():
    src=bool_env();target=bool_env((0,1));t=cast(gen(),lit(0));receipt={'term':t,'expected':lit(1)}
    actual=check(calc(t,lit(1)),src)
    try:replay_receipt(receipt,src,target)
    except Rejected as e:bad=str(e)
    else:raise AssertionError('false replay accepted')
    erased={'object':'B','value':eval_value(t,target)[1]}
    full=quote(calc(t,lit(1)),src);same=same_action_on_support(full,copy.deepcopy(src))
    # A proof function really goes through R032, including its dependent atom.
    p=eq(t,lit(1));proof={'rule':'app','function':{'rule':'lam','domain':p,'body':{'rule':'var','index':0}},'argument':calc(t,lit(1))}
    composed=check(proof,src)
    # Compress before erasing: keep the semantic action; do not choose it later.
    path=seq(gen(),seq(inv(gen()),gen()));s,u,table,_=path_semantics(path,src)
    compressed={'fibres':src['fibres'],'generators':{'p':{'source':s,'target':u,'table':list(table)}}}
    compression=replay_receipt(receipt,src,compressed)
    # Forming maps for a fixed fibre pair is different from a polymorphic section.
    local_functions=[(0,0),(0,1),(1,0),(1,1)]
    natural=[f for f in local_functions if all(1-f[b]==f[b] for b in (0,1))]
    # A fixed result can be unchanged even when the total action changes.
    tri0={'fibres':{'F':3},'generators':{'p':{'source':'F','target':'F','table':[0,1,2]}}}
    tri1=copy.deepcopy(tri0);tri1['generators']['p']['table']=[1,0,2]
    fixed={'term':cast(gen(),lit(2,'F')),'expected':lit(2,'F')}
    replay_receipt(fixed,tri0,tri1)
    return {'schema':'r034-results/v1','source_output':1,'erased_output':erased['value'],
      'erased_value_still_has_fibre_type':0<=erased['value']<2,'dependent_receipt_rejected':bad,
      'original_indexed_equation':actual['goal'],'r032_roundtrip_checked':core.check_package(composed['r032']).formula,
      'compressed_path_word':path,'retained_action':table,'compression_checked':compression['goal'],
      'same_action_migration':same,'local_bool_functions':len(local_functions),'natural_under_target_flip':natural,
      'fixed_input_2_replay_succeeds_under_changed_action':True,
      'full_polymorphic_no_selector':'paper proof via univalence and a Sigma loop; finite enumeration is not its proof',
      'native_kernel':'NOT_RUN','core_source_sha256':hashlib.sha256(Path(core.__file__).read_bytes()).hexdigest()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    need(not a.output.exists(),'refuse result overwrite');d=evidence();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'SCOPED_PASS','source_output':d['source_output'],'erased_output':d['erased_output'],'dependent_receipt_rejected':d['dependent_receipt_rejected'],'native_kernel':'NOT_RUN'},ensure_ascii=False))
if __name__=='__main__':main()
