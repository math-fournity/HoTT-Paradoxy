#!/usr/bin/env python3
"""R032: explicit implicational proof certificates, constructive interpretation,
and proof-producing reflection across axiom environments. NOT a HoTT kernel.

All accepted reflection steps expand to an ordinary finite derivation whose
current target environment is checked again. A hash binds data, not its truth.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping
import argparse
import copy
import hashlib
import json

Formula = tuple
Env = Mapping[str, Formula]
BOT = ('bot',)

class Rejected(ValueError):
    pass

def atom(n: int) -> Formula:
    if type(n) is not int or n < 0:
        raise Rejected('atom index must be a natural, not a Boolean')
    return ('atom', n)

def imp(a: Formula, b: Formula) -> Formula:
    validate_formula(a); validate_formula(b)
    return ('imp', a, b)

def validate_formula(a: Any) -> None:
    if type(a) is not tuple or not a:
        raise Rejected('formula must be a tagged tuple')
    if a[0] == 'bot' and len(a) == 1:
        return
    if a[0] == 'atom' and len(a) == 2 and type(a[1]) is int and a[1] >= 0:
        return
    if a[0] == 'imp' and len(a) == 3:
        validate_formula(a[1]); validate_formula(a[2]); return
    raise Rejected('invalid formula')

def valid_env(env: Env) -> None:
    if not isinstance(env, dict):
        raise Rejected('environment must be a dict')
    for name, formula in env.items():
        if type(name) is not str or not name:
            raise Rejected('invalid axiom label')
        validate_formula(formula)

def node(rule: str, **fields: Any) -> dict:
    return dict(rule=rule, **fields)

def var(i: int) -> dict: return node('var', index=i)
def ax(name: str) -> dict: return node('axiom', label=name)
def lam(a: Formula, body: dict) -> dict: return node('lam', domain=a, body=body)
def app(f: dict, a: dict) -> dict: return node('app', function=f, argument=a)
def absurd(a: Formula, proof: dict) -> dict: return node('absurd', target=a, proof=proof)

@dataclass(frozen=True)
class Checked:
    formula: Formula
    support: frozenset[str]
    nodes: int

KEYS = {
    'var': {'rule', 'index'}, 'axiom': {'rule', 'label'},
    'lam': {'rule', 'domain', 'body'},
    'app': {'rule', 'function', 'argument'},
    'absurd': {'rule', 'target', 'proof'},
}

def infer(proof: dict, env: Env, ctx: tuple[Formula, ...] = ()) -> Checked:
    """Total on finite valid input trees; rejects cyclic Python structures.
    Resource limitations of Python on very deep trees are not logical rejection.
    """
    valid_env(env)
    for a in ctx: validate_formula(a)
    active: set[int] = set()
    def go(p: dict, gamma: tuple) -> Checked:
        if type(p) is not dict or type(p.get('rule')) is not str:
            raise Rejected('proof must be a rule object')
        r = p['rule']
        if r not in KEYS or set(p) != KEYS[r]:
            raise Rejected('unknown rule or malformed fields: ' + r)
        if id(p) in active: raise Rejected('cyclic proof is not a finite derivation')
        active.add(id(p))
        try:
            if r == 'var':
                i = p['index']
                if type(i) is not int or not 0 <= i < len(gamma):
                    raise Rejected('unbound variable')
                return Checked(gamma[i], frozenset(), 1)
            if r == 'axiom':
                if type(p['label']) is not str or p['label'] not in env:
                    raise Rejected('missing axiom')
                return Checked(env[p['label']], frozenset({p['label']}), 1)
            if r == 'lam':
                validate_formula(p['domain'])
                b = go(p['body'], (p['domain'],) + gamma)
                return Checked(imp(p['domain'], b.formula), b.support, b.nodes+1)
            if r == 'app':
                f = go(p['function'], gamma); a = go(p['argument'], gamma)
                if f.formula[0] != 'imp' or f.formula[1] != a.formula:
                    raise Rejected('application type mismatch')
                return Checked(f.formula[2], f.support | a.support, f.nodes+a.nodes+1)
            validate_formula(p['target'])
            b = go(p['proof'], gamma)
            if b.formula != BOT: raise Rejected('absurd elimination needs bottom')
            return Checked(p['target'], b.support, b.nodes+1)
        finally:
            active.remove(id(p))
    return go(proof, ctx)

def encode_data(x: Any) -> str:
    return json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def env_hash(env: Env) -> str:
    valid_env(env)
    return hashlib.sha256(encode_data(env).encode('utf-8')).hexdigest()

def quote(env: Env, proof: dict, goal: Formula | None = None) -> dict:
    """Only closed base derivations, never a free contextual assumption."""
    c = infer(proof, env)
    if goal is not None and c.formula != goal: raise Rejected('goal mismatch')
    return {'schema': 'r032-certificate/v1', 'environment': copy.deepcopy(env),
            'environment_hash': env_hash(env), 'goal': c.formula,
            'proof': copy.deepcopy(proof), 'support': sorted(c.support)}

def check_package(package: dict) -> Checked:
    if type(package) is not dict or set(package) != {
        'schema','environment','environment_hash','goal','proof','support'}:
        raise Rejected('incomplete or extra package fields')
    if package['schema'] != 'r032-certificate/v1': raise Rejected('wrong schema')
    if env_hash(package['environment']) != package['environment_hash']:
        raise Rejected('environment digest mismatch')
    c = infer(package['proof'], package['environment'])
    if c.formula != package['goal'] or sorted(c.support) != package['support']:
        raise Rejected('forged conclusion or support')
    return c

def migrate(package: dict, target: Env, bridges: dict[str, dict] | None = None) -> dict:
    """Replace only used source axioms with closed target proofs.
    Unchanged labels/formulas are an implicit identity bridge. Arbitrary bridges
    are checked against the exact source formula, in the TARGET environment.
    """
    c = check_package(package); valid_env(target)
    bridges = {} if bridges is None else bridges
    if type(bridges) is not dict or any(k not in package['environment'] for k in bridges):
        raise Rejected('bridge for unknown source axiom')
    replacements: dict[str, dict] = {}
    for label in c.support:
        expected = package['environment'][label]
        if label in bridges:
            b = bridges[label]
            if infer(b, target).formula != expected:
                raise Rejected('bridge proves the wrong proposition')
            replacements[label] = copy.deepcopy(b)
        elif label in target and target[label] == expected:
            replacements[label] = ax(label)
        else:
            raise Rejected('missing target realization for used axiom: '+label)
    def go(p: dict) -> dict:
        r = p['rule']
        if r == 'axiom': return copy.deepcopy(replacements[p['label']])
        if r == 'var': return copy.deepcopy(p)
        if r == 'lam': return lam(p['domain'], go(p['body']))
        if r == 'app': return app(go(p['function']), go(p['argument']))
        return absurd(p['target'], go(p['proof']))
    result = go(package['proof'])
    # Splicing closed bridges under binders is safe: they have no free indices.
    got = infer(result, target)
    if got.formula != c.formula: raise Rejected('internal migration invariant failed')
    return result

def reflect(package: dict, bridges: dict | None = None) -> dict:
    return node('reflect', certificate=package, bridges={} if bridges is None else bridges)

def expand(proof: dict, target: Env, ctx: tuple[Formula, ...] = ()) -> dict:
    """Proof-producing extension: every reflection leaf carries an actual base
    certificate. No rule turns a bare `accepted=True` into a theorem.
    """
    valid_env(target)
    active: set[int] = set()
    def go(p: dict, gamma: tuple) -> dict:
        if type(p) is not dict or 'rule' not in p: raise Rejected('bad extended proof')
        if id(p) in active: raise Rejected('cyclic macro')
        active.add(id(p))
        try:
            r = p['rule']
            if r == 'reflect':
                if set(p) != {'rule','certificate','bridges'}: raise Rejected('bad reflection leaf')
                result = migrate(p['certificate'], target, p['bridges'])
            else:
                if r not in KEYS or set(p) != KEYS[r]: raise Rejected('bad extended rule')
                if r in ('var','axiom'): result = copy.deepcopy(p)
                elif r == 'lam': result = lam(p['domain'], go(p['body'], (p['domain'],)+gamma))
                elif r == 'app': result = app(go(p['function'], gamma), go(p['argument'], gamma))
                else: result = absurd(p['target'], go(p['proof'], gamma))
            infer(result, target, gamma)
            return result
        finally:
            active.remove(id(p))
    return go(proof, ctx)

def interpret(proof: dict, env: Env, realizers: dict[str, Any],
              values: tuple = (), ctx: tuple = ()) -> Any:
    """Execute the structurally defined proof term as Python functions/data.
    Realizer types are obligations of the caller; this is not a HoTT checker.
    Missing used realizers are rejected. No inhabitant of Bottom is invented.
    """
    c = infer(proof, env, ctx)
    if len(values) != len(ctx): raise Rejected('local semantic environment mismatch')
    if not c.support <= realizers.keys(): raise Rejected('missing used semantic realizer')
    def go(p: dict, vals: tuple) -> Any:
        r = p['rule']
        if r == 'var': return vals[p['index']]
        if r == 'axiom': return realizers[p['label']]
        if r == 'lam': return lambda x: go(p['body'], (x,)+vals)
        if r == 'app': return go(p['function'], vals)(go(p['argument'], vals))
        go(p['proof'], vals)
        raise Rejected('no runtime inhabitant of Bottom was supplied by this semantics')
    return go(proof, values)

def truth(a: Formula, valuation: dict[int, bool]) -> bool:
    validate_formula(a)
    if a[0] == 'bot': return False
    if a[0] == 'atom': return valuation[a[1]]
    return (not truth(a[1], valuation)) or truth(a[2], valuation)

def migration_claims() -> dict:
    p, q = atom(0), atom(1)
    ident = lam(p, var(0))
    old = {'permit':p, 'unused':q}
    newer = {'permit':q, 'unused':q}
    old_cert = quote(old, ax('permit'))
    try:
        expand(reflect(old_cert), newer)
    except Rejected as e:
        rejection = str(e)
    else:
        raise AssertionError('changed-axiom claim was accepted')
    # Explicitly BAD receipt-only interface; it does not form part of expand.
    unsafe_receipt = {'accepted':True, 'claimed_goal':p, 'source_environment_hash':env_hash(old)}
    unsafe_policy_accepts = bool(unsafe_receipt['accepted'])
    id_package = quote({'id':imp(p,p)}, ax('id'))
    lowered = migrate(id_package, {}, {'id':ident})
    unused_changed = migrate(quote(old, ident), newer)
    safe_ext = expand(app(reflect(quote({}, ident)), ax('p')), {'p':p})
    return {
        'changed_axiom': {'source':old,'target':newer,'certificate':old_cert,
                          'safe_rejection':rejection,
                          'explicitly_unsafe_receipt_policy_accepts':unsafe_policy_accepts,
                          'countermodel':{'P':False,'Q':True,'target_axioms_true':True,'source_goal_false':True}},
        'axiom_elimination_bridge': {'source_certificate':id_package,'target':{},
                                    'bridge':ident,'expanded_proof':lowered,
                                    'goal':infer(lowered,{}).formula},
        'unused_changes_do_not_invalidate': {'proof':unused_changed,'support':list(infer(unused_changed,newer).support)},
        'proof_producing_reflection':{'expanded':safe_ext,'checked_goal':infer(safe_ext,{'p':p}).formula},
        'semantic_identity': {'true':interpret(ident,{},{})(True), 'false':interpret(ident,{},{})(False)},
        'limits': ['finite implicational object fragment, not full HoTT',
                   'unsafe receipt policy is an explicit counter-design, not an allegation against a deployed system',
                   'Python realizer typing is not verified; native dependent interpreter source is separate',
                   'general preservation and completeness-of-bridges arguments are paper inductions, not inferred from tests']}

def formula_from_json(a: Any) -> Formula:
    if type(a) is not list or not a: raise Rejected('invalid serialized formula')
    if a[0] == 'atom' and len(a) == 2: return atom(a[1])
    if a == ['bot']: return BOT
    if a[0] == 'imp' and len(a) == 3:
        return imp(formula_from_json(a[1]),formula_from_json(a[2]))
    raise Rejected('invalid serialized formula')

def proof_from_json(p: Any) -> dict:
    if type(p) is not dict: raise Rejected('invalid serialized proof')
    q = copy.deepcopy(p)
    r = q.get('rule')
    if r == 'lam':
        q['domain'] = formula_from_json(q['domain'])
        q['body'] = proof_from_json(q['body'])
    elif r == 'app':
        q['function'] = proof_from_json(q['function'])
        q['argument'] = proof_from_json(q['argument'])
    elif r == 'absurd':
        q['target'] = formula_from_json(q['target'])
        q['proof'] = proof_from_json(q['proof'])
    return q

def package_from_json(p: Any) -> dict:
    if type(p) is not dict: raise Rejected('invalid serialized package')
    q=copy.deepcopy(p)
    q['environment']={name:formula_from_json(a) for name,a in q['environment'].items()}
    q['goal']=formula_from_json(q['goal'])
    q['proof']=proof_from_json(q['proof'])
    check_package(q)
    return q

def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    result = migration_claims()
    result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'SCOPED_CONSTRUCTIONS_REPLAYED','output':str(args.out),
                      'safe_rejection':result['changed_axiom']['safe_rejection']},ensure_ascii=False))

if __name__ == '__main__': main()
