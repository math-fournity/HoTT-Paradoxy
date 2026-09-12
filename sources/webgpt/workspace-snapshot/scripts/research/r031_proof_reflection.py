#!/usr/bin/env python3
"""R031 finite certificates for a conditional Loeb derivation.

This checks a declared, small natural-deduction/K4 rule set. It is NOT a
HoTT kernel. 'theorem' leaves are explicit *parameters*: closed T-theorems
whose proofs this checker does not validate. Their dependencies survive
necessitation. Local hypotheses, in contrast, forbid necessitation.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping
import argparse
import hashlib
import json
import shutil
import subprocess

Formula = tuple

class Rejected(ValueError):
    """A finite certificate violates the declared syntax or inference rules."""


def atom(name: str) -> Formula:
    return ('atom', name)


def imp(a: Formula, b: Formula) -> Formula:
    return ('imp', a, b)


def box(a: Formula) -> Formula:
    return ('box', a)

BOTTOM: Formula = ('bottom',)


def formula(obj: Any, depth: int = 0) -> Formula:
    if depth > 150:
        raise Rejected('formula nesting budget exceeded; not a logical refutation')
    if type(obj) not in (list, tuple) or not obj or type(obj[0]) is not str:
        raise Rejected('malformed formula')
    tag = obj[0]
    if tag == 'atom' and len(obj) == 2 and type(obj[1]) is str and obj[1]:
        return atom(obj[1])
    if tag == 'bottom' and len(obj) == 1:
        return BOTTOM
    if tag == 'box' and len(obj) == 2:
        return box(formula(obj[1], depth + 1))
    if tag == 'imp' and len(obj) == 3:
        return imp(formula(obj[1], depth + 1), formula(obj[2], depth + 1))
    raise Rejected('unknown formula constructor or arity')


def display(a: Formula) -> str:
    if a[0] == 'atom':
        return a[1]
    if a[0] == 'bottom':
        return 'BOTTOM'
    if a[0] == 'box':
        return 'Box(' + display(a[1]) + ')'
    return '(' + display(a[1]) + ' -> ' + display(a[2]) + ')'


@dataclass(frozen=True)
class Judgment:
    conclusion: Formula
    hypotheses: frozenset[int]
    theorem_dependencies: frozenset[str]


def replay(certificate: Mapping[str, Any], theorems: Mapping[str, Any]) -> dict[str, Any]:
    """Replay every node, tracking local contexts and external theorem parameters.

    References must point backward. No graph cycles or claimed result labels
    can count as proofs. Returned 'accepted' only means conditional rule-validity.
    """
    if type(certificate) is not dict or set(certificate) != {'schema', 'nodes', 'conclusion'}:
        raise Rejected('certificate header schema mismatch')
    if certificate['schema'] != 'r031-conditional-k4/v1':
        raise Rejected('unsupported certificate schema')
    raw_nodes = certificate['nodes']
    if type(raw_nodes) is not list or not raw_nodes or len(raw_nodes) > 10000:
        raise Rejected('empty certificate or node budget exceeded')
    env: dict[str, Formula] = {}
    if type(theorems) is not dict:
        raise Rejected('theorem environment must be a map')
    for name, value in theorems.items():
        if type(name) is not str or not name:
            raise Rejected('malformed theorem name')
        env[name] = formula(value)
    out: list[Judgment] = []
    trace: list[dict[str, Any]] = []
    for i, node in enumerate(raw_nodes):
        if type(node) is not dict or type(node.get('rule')) is not str:
            raise Rejected(f'node {i}: malformed node')
        rule = node['rule']
        fields = {
            'hyp': {'rule', 'formula'},
            'theorem': {'rule', 'name'},
            'K': {'rule', 'a', 'b'},
            'four': {'rule', 'a'},
            'mp': {'rule', 'function', 'argument'},
            'intro': {'rule', 'hypothesis', 'body'},
            'nec': {'rule', 'body'},
        }
        if rule not in fields or set(node) != fields[rule]:
            raise Rejected(f'node {i}: unknown rule or mismatched fields')

        def ref(key: str) -> tuple[int, Judgment]:
            j = node[key]
            if type(j) is not int or not (0 <= j < i):
                raise Rejected(f'node {i}: {key} must be an earlier integer index')
            return j, out[j]

        deps: frozenset[str] = frozenset()
        ctx: frozenset[int] = frozenset()
        if rule == 'hyp':
            a = formula(node['formula'])
            ctx = frozenset({i})
        elif rule == 'theorem':
            name = node['name']
            if type(name) is not str or name not in env:
                raise Rejected(f'node {i}: undeclared closed-theorem parameter')
            a = env[name]
            deps = frozenset({name})
        elif rule == 'K':
            p, q = formula(node['a']), formula(node['b'])
            a = imp(box(imp(p, q)), imp(box(p), box(q)))
        elif rule == 'four':
            p = formula(node['a'])
            a = imp(box(p), box(box(p)))
        elif rule == 'mp':
            _, f = ref('function')
            _, v = ref('argument')
            if f.conclusion[0] != 'imp' or f.conclusion[1] != v.conclusion:
                raise Rejected(f'node {i}: modus ponens type mismatch')
            a = f.conclusion[2]
            ctx = f.hypotheses | v.hypotheses
            deps = f.theorem_dependencies | v.theorem_dependencies
        elif rule == 'intro':
            j, h = ref('hypothesis')
            _, b = ref('body')
            if raw_nodes[j]['rule'] != 'hyp':
                raise Rejected(f'node {i}: introduction must discharge an actual hypothesis node')
            a = imp(h.conclusion, b.conclusion)
            ctx = b.hypotheses - {j}
            deps = b.theorem_dependencies
        else:
            _, b = ref('body')
            if b.hypotheses:
                raise Rejected(f'node {i}: necessitation on an open derivation is forbidden')
            a = box(b.conclusion)
            deps = b.theorem_dependencies
        item = Judgment(a, ctx, deps)
        out.append(item)
        trace.append({'node': i, 'rule': rule, 'conclusion': display(a),
                      'open_hypotheses': sorted(ctx), 'closed_theorem_parameters': sorted(deps)})
    claimed = formula(certificate['conclusion'])
    last = out[-1]
    if last.conclusion != claimed:
        raise Rejected('claimed final conclusion differs from checked conclusion')
    if last.hypotheses:
        raise Rejected('certificate has undischarged hypotheses')
    return {'accepted': True, 'scope': 'FINITE_RULE_REPLAY_WITH_DECLARED_THEOREM_PARAMETERS',
            'nodes_checked': len(out), 'conclusion': display(last.conclusion),
            'closed_theorem_parameters': sorted(last.theorem_dependencies),
            'trusted_rule_schemata': ['intuitionistic implication introduction/elimination',
                                     'K distribution', 'positive introspection (four)',
                                     'necessitation ONLY with no local hypotheses'],
            'parameter_proofs_checked': False, 'hott_kernel_verification': False, 'trace': trace}


class Builder:
    def __init__(self) -> None:
        self.nodes: list[dict[str, Any]] = []

    def add(self, rule: str, **kw: Any) -> int:
        self.nodes.append({'rule': rule, **kw})
        return len(self.nodes) - 1

    def mp(self, f: int, x: int) -> int:
        return self.add('mp', function=f, argument=x)

    def finish(self, conclusion: Formula) -> dict[str, Any]:
        return {'schema': 'r031-conditional-k4/v1', 'nodes': self.nodes, 'conclusion': conclusion}


def identity_certificate(a: Formula, necessitate: bool = False) -> dict[str, Any]:
    b = Builder()
    h = b.add('hyp', formula=a)
    r = b.add('intro', hypothesis=h, body=h)
    if necessitate:
        b.add('nec', body=r)
    return b.finish(box(imp(a, a)) if necessitate else imp(a, a))


def loeb_certificate(target: Formula = BOTTOM, local_reflection: bool = False):
    """Produce a finite certificate of the CONDITIONAL Loeb transformation.

    The environment entries assert availability of closed T-derivations.
    They are not manufactured proofs of the fixed-point lemma or reflection.
    """
    p, g = formula(target), atom('G')
    bg, bp = box(g), box(p)
    env = {'FP_forward': imp(g, imp(bg, p)),
           'FP_backward': imp(imp(bg, p), g),
           'Reflection': imp(bp, p)}
    b = Builder()
    f = b.add('theorem', name='FP_forward')
    back = b.add('theorem', name='FP_backward')
    r = b.add('hyp', formula=env['Reflection']) if local_reflection else b.add('theorem', name='Reflection')
    nf = b.add('nec', body=f)
    k1 = b.add('K', a=g, b=imp(bg, p))
    u = b.mp(k1, nf)  # BG -> Box(BG -> P)
    k2 = b.add('K', a=bg, b=p)
    four = b.add('four', a=g)
    h = b.add('hyp', formula=bg)
    boxed_arrow = b.mp(u, h)
    inner_arrow = b.mp(k2, boxed_arrow)
    bbg = b.mp(four, h)
    bp_proof = b.mp(inner_arrow, bbg)
    l = b.add('intro', hypothesis=h, body=bp_proof)  # BG -> BP
    h2 = b.add('hyp', formula=bg)
    bp2 = b.mp(l, h2)
    p2 = b.mp(r, bp2)
    hp = b.add('intro', hypothesis=h2, body=p2)  # BG -> P
    dg = b.mp(back, hp)
    dbg = b.add('nec', body=dg)  # disallowed when reflection is merely local
    b.mp(hp, dbg)
    return b.finish(p), env


def negative_cases() -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    import copy
    p, q = atom('P'), atom('Q')
    cert, env = loeb_certificate()
    cases = []
    cases.append(('missing_reflection_parameter', cert, {k:v for k,v in env.items() if k != 'Reflection'}))
    local, local_env = loeb_certificate(local_reflection=True)
    cases.append(('local_reflection_illegally_necessitated', local, local_env))
    b = Builder(); h = b.add('hyp', formula=p); b.add('nec', body=h)
    cases.append(('direct_open_necessitation', b.finish(box(p)), {}))
    b = Builder(); h = b.add('hyp', formula=p)
    cases.append(('undischarged_assumption', b.finish(p), {}))
    bad = copy.deepcopy(cert); bad['nodes'][3]['body'] = 3
    cases.append(('cyclic_reference', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][3]['body'] = 20
    cases.append(('forward_reference', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][5]['argument'] = True
    cases.append(('boolean_instead_of_reference', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][5]['argument'] = 1
    cases.append(('modus_ponens_wrong_argument', bad, env))
    bad = copy.deepcopy(cert); bad['conclusion'] = q
    cases.append(('forged_final_conclusion', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][2]['name'] = 'unlisted_axiom'
    cases.append(('unlisted_theorem', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][7]['a'] = ['box']
    cases.append(('malformed_formula', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][13]['hypothesis'] = 1
    cases.append(('discharge_theorem_as_local_hypothesis', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][3]['rule'] = 'trust_me'
    cases.append(('unimplemented_rule', bad, env))
    bad = copy.deepcopy(cert); bad['nodes'][2]['certified_by_hott'] = True
    cases.append(('unrecognized_certification_field', bad, env))
    return cases


def run_suite() -> dict[str, Any]:
    p = atom('P')
    positives: dict[str, Any] = {}
    certs: dict[str, Any] = {}
    for name, c in [('identity', identity_certificate(p)),
                    ('closed_necessitation', identity_certificate(p, True))]:
        positives[name] = replay(c, {})
        certs[name] = {'certificate': c, 'closed_theorem_parameters': {}}
    for name, target in [('conditional_loeb_P', p), ('conditional_loeb_BOTTOM', BOTTOM)]:
        c, env = loeb_certificate(target)
        positives[name] = replay(c, env)
        certs[name] = {'certificate': c, 'closed_theorem_parameters': env}
    negatives = []
    for name, c, env in negative_cases():
        try:
            replay(c, env)
        except Rejected as exc:
            negatives.append({'id': name, 'rejected': True, 'reason': str(exc)})
        else:
            raise AssertionError('negative certificate unexpectedly accepted: ' + name)
    return {'schema_version': 'r031-proof-certificate-replay/v1',
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'positive_certificates': positives, 'negative_cases': negatives,
            'certificates': certs,
            'limitations': ['No proof of Goedel coding or fixed-point lemma for full HoTT.',
                            'No validation of external closed-theorem parameter derivations.',
                            'No LEM in the checked rule set.',
                            'No full HoTT consistency or physical-runtime claim.',
                            'Finite replay checks a concrete derivation; general theorem is separate.']}


def native_status() -> dict[str, Any]:
    data = {}
    for command in ['agda', 'lean', 'coqc', 'rocq']:
        found = shutil.which(command)
        entry: dict[str, Any] = {'path': found, 'status': 'NOT_FOUND' if not found else 'FOUND'}
        if found:
            flag = '--version' if command in ('agda', 'lean') else '-v'
            try:
                p = subprocess.run([found, flag], text=True, capture_output=True, timeout=10)
                entry.update(exit_code=p.returncode, stdout=p.stdout, stderr=p.stderr)
            except Exception as exc:
                entry['version_probe_error'] = str(exc)
        data[command] = entry
    return {'tools': data, 'formal_file_status': 'NOT_RUN',
            'install_attempted': False, 'external_ai_started': False}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--native-status', type=Path)
    args = ap.parse_args()
    if args.out.exists() or (args.native_status and args.native_status.exists()):
        raise SystemExit('refusing to overwrite evidence')
    result = run_suite()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.native_status:
        args.native_status.write_text(json.dumps(native_status(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'positive_certificates':len(result['positive_certificates']),
                      'negative_cases_rejected':len(result['negative_cases']),
                      'conditional_loeb_nodes':result['positive_certificates']['conditional_loeb_BOTTOM']['nodes_checked'],
                      'hott_kernel_verification':False}, ensure_ascii=False))

if __name__ == '__main__':
    main()
