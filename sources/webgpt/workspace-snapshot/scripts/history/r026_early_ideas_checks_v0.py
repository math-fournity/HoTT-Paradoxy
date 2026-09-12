#!/usr/bin/env python3
"""Narrow checks of the early Gemini essay.
Not a HoTT kernel: classical finite valuations, an explicitly defined linear
lambda fragment, finite protocol models, and a bounded proof synthesizer.
No unbounded failure is inferred from a search budget or simulation timeout.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass, asdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse, hashlib, json, sys

@dataclass(frozen=True)
class Atom:
    name: str
@dataclass(frozen=True)
class Arrow:
    domain: object
    codomain: object
@dataclass(frozen=True)
class Tensor:
    left: object
    right: object
@dataclass(frozen=True)
class Var:
    name: str
@dataclass(frozen=True)
class Lam:
    name: str
    domain: object
    body: object
@dataclass(frozen=True)
class App:
    function: object
    argument: object
@dataclass(frozen=True)
class Pair:
    left: object
    right: object

class Rejected(ValueError):
    pass

def merge(left: Counter, right: Counter, linear: bool) -> Counter:
    result = left + right
    if linear and any(n != 1 for n in result.values()):
        raise Rejected('A named resource is reused')
    return result

def infer(term, env: dict[str, object], linear: bool = True):
    """Syntax-directed checking: variables, annotated lambda, application, tensor pair.
    Linear mode splits named resource use at application/tensor and consumes a
    bound variable exactly once. There are no axioms, constants, recursion or !.
    """
    if isinstance(term, Var):
        if term.name not in env:
            raise Rejected('Unbound variable')
        return env[term.name], Counter({term.name: 1})
    if isinstance(term, Lam):
        if term.name in env:
            raise Rejected('Binders must be distinct; alpha-rename first')
        result, used = infer(term.body, {**env, term.name: term.domain}, linear)
        if linear and used[term.name] != 1:
            raise Rejected('A linear binder must be consumed exactly once')
        used = used.copy()
        used.pop(term.name, None)
        return Arrow(term.domain, result), used
    if isinstance(term, App):
        fun, uf = infer(term.function, env, linear)
        arg, ua = infer(term.argument, env, linear)
        if not isinstance(fun, Arrow) or fun.domain != arg:
            raise Rejected('Application domain mismatch')
        return fun.codomain, merge(uf, ua, linear)
    if isinstance(term, Pair):
        a, ua = infer(term.left, env, linear)
        b, ub = infer(term.right, env, linear)
        return Tensor(a, b), merge(ua, ub, linear)
    raise Rejected('Unknown syntax node')

def check(term, env, target, linear=True):
    inferred, used = infer(term, env, linear)
    if inferred != target:
        raise Rejected('Claimed result type mismatch')
    if linear and used != Counter({k: 1 for k in env}):
        raise Rejected('Unused or duplicated free linear resources')
    return {'type': repr(inferred), 'uses': dict(used), 'linear': linear}

def encode_node(value):
    if isinstance(value, (Atom, Arrow, Tensor, Var, Lam, App, Pair)):
        return {'constructor': type(value).__name__, **{k:encode_node(v) for k,v in vars(value).items()}}
    return value

def weight(ty, values):
    if isinstance(ty, Atom):return values[ty.name]
    if isinstance(ty, Arrow):return weight(ty.codomain, values)-weight(ty.domain, values)
    if isinstance(ty, Tensor):return weight(ty.left, values)+weight(ty.right, values)
    raise Rejected('Unknown type')

def synthesize(goal, env, fuel=8):
    """Finite backward search of beta-normal eta-long implicational terms.
    A missing result means NO_WITNESS_WITHIN_BUDGET, not uninhabited HoTT type.
    The general fair-enumeration argument is written separately in PROOF_NOTE.
    """
    if fuel <= 0:return None
    if isinstance(goal, Arrow):
        name='v'+str(len(env))
        while name in env:name+='x'
        body=synthesize(goal.codomain,{**env,name:goal.domain},fuel-1)
        return None if body is None else Lam(name,goal.domain,body)
    for name, ty in env.items():
        args=[]; tail=ty
        while isinstance(tail,Arrow):
            args.append(tail.domain);tail=tail.codomain
        if tail != goal:continue
        term=Var(name);okay=True
        for argtype in args:
            arg=synthesize(argtype,env,fuel-1)
            if arg is None:okay=False;break
            term=App(term,arg)
        if okay:return term
    return None

def expect_rejected(action):
    try:action()
    except Rejected as err:return str(err)
    raise AssertionError('Invalid object unexpectedly accepted')

def truth_checks():
    rows=[]
    for p,r in product((False,True),repeat=2):
        impl=(not p) or r
        mt=(not impl) or (r or not p)
        rows.append({'P':p,'R':r,'P_implies_R':impl,'modus_tollens':mt})
    assert all(r['modus_tollens'] for r in rows)
    bad=[r for r in rows if r['P'] and not r['R']]
    assert len(bad)==1
    # P does not prove independent R: P has models with both values of R.
    assert {r['R'] for r in rows if r['P']}=={False,True}
    # Interpretation/bridge failure need not falsify P.
    p,i,o,r=True,False,True,False
    assert (not (p and i and o)) or r
    assert not r and p
    return {'valuation_rows':rows,'missing_bridge_countermodel':bad[0],
            'joint_contract_countermodel':{'P':p,'Interpretation':i,'Operation':o,'R':r},
            'scope':'Complete four classical valuations of displayed schema; no ontology theorem.'}

def resource_checks():
    a,b,c=Atom('A'),Atom('B'),Atom('C')
    comp=Lam('f',Arrow(a,b),Lam('g',Arrow(b,c),Lam('x',a,App(Var('g'),App(Var('f'),Var('x'))))))
    target=Arrow(Arrow(a,b),Arrow(Arrow(b,c),Arrow(a,c)))
    comp_check=check(comp,{},target)
    pair=Pair(App(Var('f'),Var('a')),App(Var('g'),Var('b')))
    pair_env={'f':Arrow(a,c),'a':a,'g':Arrow(b,c),'b':b}
    pair_check=check(pair,pair_env,Tensor(c,c))
    dup=Lam('x',a,Pair(Var('x'),Var('x')))
    dup_type=Arrow(a,Tensor(a,a))
    assert check(dup,{},dup_type,linear=False)
    rejected={
      'duplicate':expect_rejected(lambda:check(dup,{},dup_type)),
      'discard':expect_rejected(lambda:check(Lam('x',a,Lam('y',b,Var('x'))),{},Arrow(a,Arrow(b,a)))),
      'bad_argument':expect_rejected(lambda:infer(App(Var('f'),Var('b')),{'f':Arrow(a,c),'b':b})),
      'fake_target':expect_rejected(lambda:check(comp,{},Arrow(a,a))),
      'missing_resource':expect_rejected(lambda:check(pair,{k:v for k,v in pair_env.items() if k!='b'},Tensor(c,c))),
      'untyped_payload':expect_rejected(lambda:infer(None,{}))}
    weights={'A':1,'B':3,'C':7}
    assert weight(target,weights)==0 and weight(dup_type,weights)==1
    # Distinct ownership tokens are not forbidden from coexisting.
    available={'p','q'}; used=[]
    for token in ['p','q']:
        assert token in available
        available.remove(token);used.append(token)
    assert not available and used==['p','q']
    available={'p'};success=[]
    for token in ['p','p']:
        success.append(token in available)
        available.discard(token)
    assert success==[True,False]
    return {'accepted_derivations':[{'term':encode_node(comp),'target':encode_node(target),'check':comp_check},
                                   {'term':encode_node(pair),'environment':{k:encode_node(v) for k,v in pair_env.items()},'check':pair_check}],
            'negative_controls':rejected,'contraction_without_linearity':'ACCEPTED',
            'conservation_witness':{'atom_weights':weights,'closed_composition_weight':weight(target,weights),'closed_duplication_weight':weight(dup_type,weights)},
            'two_distinct_tokens':used,'one_token_two_redemptions':success,
            'scope':'Explicit multiplicative linear lambda fragment; not a linear HoTT kernel or general linear decidability result.'}

def identity_checks():
    # Universe paths are instantiated by reflexivity on the same Bool carrier.
    B={0,1};a=0;b=1;c=0
    assert a in B and b in B and c in B
    transport=lambda x:x
    assert transport(a)==c and transport(b)!=c
    return {'carrier':'Bool','A_equals_X':True,'B_equals_X':True,'a':a,'b':b,'c':c,
            'transport_p_a_equals_c':True,'transport_q_b_equals_c':False,'a_equals_b':False,
            'formation_error':'With syntactically distinct A,B and only b:B, Id_A(a,b) has no supplied coercion.',
            'scope':'Finite counterinstance to type-equality-implies-chosen-element-equality; does not model all univalence.'}

def discovery_checks():
    a,b,c=Atom('A'),Atom('B'),Atom('C')
    goals=[Arrow(a,a),Arrow(a,Arrow(b,a)),Arrow(Arrow(a,b),Arrow(Arrow(b,c),Arrow(a,c)))]
    rows=[]
    for goal in goals:
        term=synthesize(goal,{},fuel=10)
        assert term is not None
        checked=check(term,{},goal,linear=False)
        rows.append({'goal':repr(goal),'discovered_term':encode_node(term),'checked':checked})
    missing=synthesize(Arrow(a,b),{},fuel=6)
    assert missing is None
    # A mere formula construction is finite even when its query is not resolved.
    encoded=[{'syntax':'TruncSigmaHalt','code':p,'input':x} for p in range(40) for x in range(4)]
    assert len(encoded)==160
    return {'successful_searches':rows,'negative_search':'NO_WITNESS_WITHIN_BUDGET',
            'finite_question_encodings':len(encoded),'question_answers_computed':0,
            'scope':'Toy propositional fragment demonstrates search distinct from checking, not a HoTT search completeness test.'}

def ambiguity_checks():
    # Common observable text; incompatible but individually satisfiable intentions.
    intentions={'left':{0},'right':{1}}
    candidates={0,1}
    assert set.intersection(*intentions.values())==set()
    selectors=[{'output':o,'correct_for':[k for k,s in intentions.items() if o in s]} for o in candidates]
    assert all(len(s['correct_for'])==1 for s in selectors)
    # A genuine clarification intersects possibilities. Not a computation of intent from nothing.
    clarified=candidates & intentions['right']
    assert clarified=={1}
    # A saved witness survives only a certified implication between successive specs.
    base={0,1};old_witness=0;strengthened={1}
    assert old_witness in base and old_witness not in strengthened
    # Equal mathematical return values do not enforce different temporal acceptance tests.
    requirements={'answer_correct':{0,1},'before_deadline':{0}}
    return {'common_input':'Return the selected bit; intent not supplied',
            'admissible_answers':{k:sorted(v) for k,v in intentions.items()},
            'all_constant_selectors':selectors,'robust_answers':[],
            'clarification_result':sorted(clarified),'stale_witness_counterexample':{'old':sorted(base),'witness':0,'new':sorted(strengthened)},
            'scope':'Finite semantic underspecification and spec-version counterexamples, not natural-language undecidability.'}

def motion_checks():
    # A single-time position is not a test for constancy on an interval.
    samples=[]
    for t in range(-5,6):
        for h in [Fraction(1,2),Fraction(1,3),Fraction(2,5)]:
            x0=Fraction(t);xh=Fraction(t)+h
            assert (xh-x0)/h==1
            samples.append([str(x0),str(h)])
    residual=[Fraction(1,2**n) for n in range(65)]
    assert all(r>0 for r in residual)
    for k in range(1,33):
        assert residual[k+1] < Fraction(1,2**k)
    return {'rational_motion_checks':len(samples),'residual_prefix_steps':64,
            'strict_dyadic_accuracy_cases':32,'exact_final_finite_step_claim':'NOT_INFERRED',
            'physical_spacetime_discreteness':'NOT_TESTED',
            'scope':'Rational algebra and finite prefixes; general formulas justified in note, no historical/physical verdict.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    groups={'logic':truth_checks(),'linear_resources':resource_checks(),'identity_premises':identity_checks(),
            'discovery_and_statement':discovery_checks(),'ambiguity_and_revision':ambiguity_checks(),'motion_and_completion':motion_checks()}
    result={'schema_version':'r026-targeted-checks/v1','status':'PASS_WITH_DECLARED_SCOPE','groups':groups,
            'check_groups':len(groups),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'native_hott_kernel':'NOT_RUN','native_proof_assistant':'NOT_AVAILABLE',
            'shared_fragment_checker':'CUSTOM_PYTHON_RULE_CHECKER_NOT_NATIVE_HOTT',
            'conclusions_not_certified':['HoTT inconsistency','all natural-language translation undecidable','physical time ontology','newness','independent review']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'groups':list(groups),'output':str(args.output)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
