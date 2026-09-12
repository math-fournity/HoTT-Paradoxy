"""Finite groupoid actions for R033, not a HoTT kernel.

All tables are explicit finite data.  Acceptance means naturality in THIS model;
it does not mean the table is an elaborated dependent type-theory term.
"""
from __future__ import annotations
import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

class ModelError(ValueError):
    pass

@dataclass(frozen=True)
class Arrow:
    source: str
    target: str
    twist: int

    def __post_init__(self):
        if not isinstance(self.source, str) or not isinstance(self.target, str):
            raise ModelError('objects must be strings')
        if type(self.twist) is not int or self.twist not in (0, 1):
            raise ModelError('twist must be an integer 0 or 1')

    def then(self, other: Arrow) -> Arrow:
        if self.target != other.source:
            raise ModelError('non-composable arrows')
        return Arrow(self.source, other.target, self.twist ^ other.twist)

    def inverse(self) -> Arrow:
        return Arrow(self.target, self.source, self.twist)

class Action:
    """A checked functor from the connected finite C2 groupoid to finite sets."""
    def __init__(self, fibres: Mapping[str, tuple[str, ...]],
                 tables: Mapping[Arrow, tuple[str, ...]]):
        self.fibres = {k: tuple(v) for k, v in fibres.items()}
        self.tables = {k: tuple(v) for k, v in tables.items()}
        if not self.fibres:
            raise ModelError('empty object list not used in this model')
        for key, vals in self.fibres.items():
            if not isinstance(key, str) or any(not isinstance(v, str) for v in vals):
                raise ModelError('objects and fibre elements must be strings')
            if len(vals) != len(set(vals)):
                raise ModelError('duplicate fibre elements')
        self.arrows = tuple(Arrow(x, y, t) for x in self.fibres
                            for y in self.fibres for t in (0, 1))
        if set(self.tables) != set(self.arrows):
            raise ModelError('missing or extra arrow action')
        for p in self.arrows:
            vals = self.tables[p]
            if len(vals) != len(self.fibres[p.source]) or set(vals) != set(self.fibres[p.target]):
                raise ModelError('arrow action must be a bijection')
            if len(vals) != len(set(vals)):
                raise ModelError('arrow action not injective')
        for x, vals in self.fibres.items():
            if self.tables[Arrow(x, x, 0)] != vals:
                raise ModelError('identity law failed')
        for p in self.arrows:
            for q in self.arrows:
                if p.target == q.source:
                    for b in self.fibres[p.source]:
                        if self.apply(p.then(q), b) != self.apply(q, self.apply(p, b)):
                            raise ModelError('composition law failed')

    def apply(self, p: Arrow, b: str) -> str:
        if p not in self.tables or b not in self.fibres[p.source]:
            raise ModelError('ill-typed transport')
        return self.tables[p][self.fibres[p.source].index(b)]

    def pair_path(self, p: Arrow, b: str, target_value: str) -> tuple:
        if target_value not in self.fibres[p.target]:
            raise ModelError('target value outside target fibre')
        actual = self.apply(p, b)
        if actual != target_value:
            raise ModelError('missing second-component equality')
        return (p, b, target_value)

    def parallel_actions_agree(self) -> bool:
        return all(self.apply(Arrow(x, y, 0), b) == self.apply(Arrow(x, y, 1), b)
                   for x in self.fibres for y in self.fibres for b in self.fibres[x])

    def all_loop_actions_trivial(self) -> bool:
        return all(self.apply(Arrow(x, x, t), b) == b
                   for x in self.fibres for t in (0, 1) for b in self.fibres[x])

    def endpoint_table(self) -> dict:
        if not self.parallel_actions_agree():
            raise ModelError('path erasure loses action')
        return {(x, y): self.tables[Arrow(x, y, 0)] for x in self.fibres for y in self.fibres}


def c2_family(*, swapped: bool, objects=('base',)) -> Action:
    if type(swapped) is not bool:
        raise ModelError('swapped must be bool')
    fibres = {x: ('0', '1') for x in objects}
    tables = {Arrow(x, y, t): (('1', '0') if swapped and t else ('0', '1'))
              for x in objects for y in objects for t in (0, 1)}
    return Action(fibres, tables)


def naturality(source: Action, target: Action, maps: Mapping[str, tuple[str, ...]]) -> dict:
    """Base map is identity; return a witnessed failure, not just False."""
    if set(source.fibres) != set(target.fibres) or set(maps) != set(source.fibres):
        raise ModelError('incompatible object domains')
    for x, vals in source.fibres.items():
        if len(maps[x]) != len(vals) or any(v not in target.fibres[x] for v in maps[x]):
            raise ModelError('fibre map ill-typed')
    def phi(x, b):
        return maps[x][source.fibres[x].index(b)]
    count = 0
    for p in source.arrows:
        for b in source.fibres[p.source]:
            count += 1
            left = target.apply(p, phi(p.source, b))
            right = phi(p.target, source.apply(p, b))
            if left != right:
                return {'natural': False, 'checks': count,
                        'witness': {'source': p.source, 'target': p.target, 'twist': p.twist,
                                    'input': b, 'target_after_map': left,
                                    'map_after_source': right}}
    return {'natural': True, 'checks': count}


def all_local_maps(source: Action, target: Action):
    objects = tuple(source.fibres)
    choices = [tuple(itertools.product(target.fibres[x], repeat=len(source.fibres[x]))) for x in objects]
    for tables in itertools.product(*choices):
        yield dict(zip(objects, tables))


def perm_then(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    n = len(p)
    if any(type(x) is not int for x in p + q) or len(q) != n or set(p) != set(range(n)) or set(q) != set(range(n)):
        raise ModelError('invalid permutation')
    return tuple(q[p[i]] for i in range(n))


def evidence() -> dict:
    swap = c2_family(swapped=True)
    trivial = c2_family(swapped=False)
    maps = list(all_local_maps(swap, swap))
    same = [{'table': m['base'], **naturality(swap, swap, m)} for m in maps]
    different = [{'table': m['base'], **naturality(trivial, swap, m)} for m in maps]
    two = c2_family(swapped=True, objects=('left', 'right'))
    two_maps = list(all_local_maps(two, two))
    alpha, beta = (1, 0, 2), (0, 2, 1)
    involutions = []
    for n in range(5):
        elems = tuple(map(str, range(n)))
        for perm in itertools.permutations(range(n)):
            if any(perm[perm[i]] != i for i in range(n)):
                continue
            model = Action({'x': elems}, {Arrow('x', 'x', 0): elems,
                            Arrow('x', 'x', 1): tuple(elems[i] for i in perm)})
            lhs, rhs = model.parallel_actions_agree(), model.all_loop_actions_trivial()
            if lhs != rhs:
                raise AssertionError('finite criterion disagreement')
            involutions.append({'size': n, 'permutation': perm, 'erasable': lhs})
    return {
        'schema': 'r033-finite-actions/v1',
        'scope': 'Finite C2-groupoid set-action diagnostics; not a HoTT kernel or proof of univalence',
        'same_swap_family': same,
        'trivial_to_swap': different,
        'two_objects': {'local_tables': len(two_maps),
                        'natural_tables': sum(naturality(two, two, m)['natural'] for m in two_maps)},
        'pair_path': {'source': '0', 'via_identity': swap.apply(Arrow('base','base',0), '0'),
                      'via_swap': swap.apply(Arrow('base','base',1), '0')},
        'order': {'alpha_then_beta': perm_then(alpha,beta), 'beta_then_alpha': perm_then(beta,alpha),
                  'on_0_first_order': perm_then(alpha,beta)[0], 'on_0_reverse_order': perm_then(beta,alpha)[0]},
        'loop_action_criterion_checks': involutions,
        'general_theorems': 'Paper proofs separate; no extrapolation from enumeration',
        'native_formal_status': 'NOT_RUN'
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('refusing to overwrite result')
    data = evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status':'PASS', 'same_fibre_maps':len(data['same_swap_family']),
                      'same_natural':sum(x['natural'] for x in data['same_swap_family']),
                      'trivial_to_swap_natural':sum(x['natural'] for x in data['trivial_to_swap']),
                      'two_objects':data['two_objects'],
                      'involutions_checked':len(data['loop_action_criterion_checks']),
                      'output':str(args.output)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
