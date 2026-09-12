#!/usr/bin/env python3
"""Exact finite successor descent and certificate transport, NOT a HoTT kernel.

Imports the unchanged R036 transition model. Generic HoTT/Acc and infinite
countdown results are PAPER proofs; finite examples below do not certify them.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import argparse
import hashlib
import json
from typing import Any
from r036_transition_abstraction import System, Abstraction, specimen, nat


class DescentError(ValueError):
    """The proposed exact quotient lacks a current-state continuation."""


def row(a: Abstraction, state: int) -> frozenset[int]:
    if not nat(state) or state >= a.source.size:
        raise ValueError('invalid concrete state')
    return frozenset(a.alpha[t] for t in a.source.successors(state))


def uniform_failures(a: Abstraction) -> tuple[dict, ...]:
    return tuple({'left': s, 'right': t,
                  'left_row': sorted(row(a, s)), 'right_row': sorted(row(a, t))}
                 for s in range(a.source.size) for t in range(s + 1, a.source.size)
                 if a.alpha[s] == a.alpha[t] and row(a, s) != row(a, t))


@dataclass(frozen=True)
class LiftEntry:
    current: int
    target_label: int
    successor: int


def check_lift_table(a: Abstraction, entries: tuple[LiftEntry, ...]) -> bool:
    if type(entries) is not tuple:
        return False
    expected = {(s, v) for s in range(a.source.size)
                for v in a.target.successors(a.alpha[s])}
    found = set()
    for e in entries:
        if type(e) is not LiftEntry or not all(nat(x) for x in (e.current, e.target_label, e.successor)):
            return False
        key = (e.current, e.target_label)
        if key in found or key not in expected or (e.current, e.successor) not in a.source.edges:
            return False
        if a.alpha[e.successor] != e.target_label:
            return False
        found.add(key)
    return found == expected


def make_lift_table(a: Abstraction) -> tuple[LiftEntry, ...]:
    """Explicit finite enumeration, not a choice principle for general types."""
    entries = []
    for s in range(a.source.size):
        for v in a.target.successors(a.alpha[s]):
            candidates = [t for t in a.source.successors(s) if a.alpha[t] == v]
            if not candidates:
                raise DescentError(f'no current lift: state={s}, target_label={v}')
            entries.append(LiftEntry(s, v, candidates[0]))
    table = tuple(entries)
    assert check_lift_table(a, table)
    return table


def lift_path(a: Abstraction, table: tuple[LiftEntry, ...], start: int,
              abstract_path: tuple[int, ...]) -> tuple[int, ...]:
    if not check_lift_table(a, table):
        raise DescentError('invalid or incomplete continuation evidence')
    if not nat(start) or start >= a.source.size:
        raise ValueError('bad concrete start')
    if type(abstract_path) is not tuple or not abstract_path:
        raise ValueError('nonempty finite path required')
    if any(not nat(x) or x >= a.target.size for x in abstract_path):
        raise ValueError('invalid abstract state')
    if a.alpha[start] != abstract_path[0]:
        raise ValueError('initial representative mismatch')
    if any((u, v) not in a.target.edges for u, v in zip(abstract_path, abstract_path[1:])):
        raise ValueError('invalid abstract edge')
    lookup = {(e.current, e.target_label): e.successor for e in table}
    path = [start]
    for v in abstract_path[1:]:
        path.append(lookup[(path[-1], v)])
    return tuple(path)


@dataclass(frozen=True)
class AccNode:
    state: int
    children: tuple[tuple[int, 'AccNode'], ...]


def check_acc(system: System, proof: AccNode) -> bool:
    """Verify a finite, all-successors DAG/tree; a cycle or missing branch fails."""
    grey: set[int] = set()
    done: set[int] = set()
    def go(node: AccNode) -> bool:
        if type(node) is not AccNode or not nat(node.state) or node.state >= system.size:
            return False
        if id(node) in grey:
            return False
        if id(node) in done:
            return True
        if type(node.children) is not tuple:
            return False
        grey.add(id(node))
        labels = []
        for item in node.children:
            if type(item) is not tuple or len(item) != 2:
                return False
            t, sub = item
            if not nat(t) or type(sub) is not AccNode or sub.state != t:
                return False
            labels.append(t)
            if not go(sub):
                return False
        if len(labels) != len(set(labels)) or set(labels) != set(system.successors(node.state)):
            return False
        grey.remove(id(node)); done.add(id(node))
        return True
    return go(proof)


def make_acc(system: System, start: int) -> AccNode:
    if not nat(start) or start >= system.size:
        raise ValueError('invalid start')
    active: set[int] = set(); cache: dict[int, AccNode] = {}
    def go(s: int) -> AccNode:
        if s in active:
            raise ValueError('reachable cycle: no finite Acc tree')
        if s in cache:
            return cache[s]
        active.add(s)
        out = AccNode(s, tuple((t, go(t)) for t in system.successors(s)))
        active.remove(s); cache[s] = out
        return out
    out = go(start)
    assert check_acc(system, out)
    return out


def migrate_acc(a: Abstraction, table: tuple[LiftEntry, ...], proof: AccNode) -> AccNode:
    """Finite counterpart of the paper accessibility-induction construction.

    This implementation uses an explicit finite table. The paper generalization
    eliminates propositional existence into isProp(Acc); Python does not do that.
    """
    if not check_lift_table(a, table):
        raise DescentError('cannot transport via missing current-state lifts')
    if not check_acc(a.source, proof):
        raise ValueError('invalid source termination certificate')
    lookup = {(e.current, e.target_label): e.successor for e in table}
    def go(p: AccNode) -> AccNode:
        children = dict(p.children)
        u = a.alpha[p.state]
        return AccNode(u, tuple((v, go(children[lookup[(p.state, v)]]))
                                for v in a.target.successors(u)))
    out = go(proof)
    assert check_acc(a.target, out)
    return out


def as_json(p: AccNode) -> dict:
    return {'state': p.state, 'children': [{'label': t, 'proof': as_json(q)} for t, q in p.children]}


def safe_branching() -> Abstraction:
    return Abstraction(System(4, frozenset({(0, 1), (0, 2), (1, 3), (2, 3)}), 0,
                              frozenset({3})), (0, 1, 1, 2))


def nonuniform_terminating() -> Abstraction:
    return Abstraction(System(4, frozenset({(0, 3), (1, 2), (2, 3)}), 1,
                              frozenset({3})), (0, 0, 1, 2))


def countdown_edge(s: Any, t: Any) -> bool:
    if s == 'root':
        return nat(t)
    return nat(s) and s > 0 and nat(t) and t == s - 1


def countdown_label(s: Any) -> str:
    if s == 'root':
        return 'Start'
    if not nat(s):
        raise ValueError('invalid countdown state')
    return 'Done' if s == 0 else 'Work'


def countdown_prefix(edges: int) -> tuple[Any, ...]:
    if not nat(edges):
        raise ValueError('finite nonnegative horizon required')
    # This witness changes its first concrete choice as the horizon changes.
    return ('root',) + tuple(range(edges, 0, -1))


def committed_countdown(n: int) -> tuple[Any, ...]:
    if not nat(n):
        raise ValueError('finite natural choice required')
    return ('root',) + tuple(range(n, -1, -1))


def report() -> dict:
    bad = specimen(); good = safe_branching(); weak = nonuniform_terminating()
    table = make_lift_table(good)
    source_cert = make_acc(good.source, good.source.initial)
    target_cert = migrate_acc(good, table, source_cert)
    horizons = []
    for n in range(17):
        path = countdown_prefix(n)
        assert all(countdown_edge(s, t) for s, t in zip(path, path[1:]))
        assert tuple(map(countdown_label, path)) == ('Start',) + ('Work',) * n
        commit = committed_countdown(n)
        assert countdown_label(commit[-1]) == 'Done'
        horizons.append({'horizon_edges': n, 'finite_prefix_lift': path,
                         'committed_run': commit, 'committed_done_at': len(commit) - 1})
    return {
        'kind': 'FINITE_CERTIFICATE_AND_INTERFACE_CHECK_NOT_HOTT_KERNEL',
        'bad_R036': {'uniform_failures': uniform_failures(bad),
                     'current_lift_failures': bad.backward_failures(),
                     'may_edges': sorted(bad.target.edges),
                     'source_terminates': bad.source.all_runs_complete(),
                     'target_terminates': bad.target.all_runs_complete()},
        'good_branching': {'table': [vars(e) for e in table],
                           'lift': lift_path(good, table, 0, (0, 1, 2)),
                           'source_certificate': as_json(source_cert),
                           'target_certificate': as_json(target_cert),
                           'target_certificate_checked': check_acc(good.target, target_cert)},
        'not_necessary_for_termination': {'uniform': not uniform_failures(weak),
                                        'source_terminates': weak.source.all_runs_complete(),
                                        'target_terminates': weak.target.all_runs_complete()},
        'countdown_horizons': horizons,
        'bounds': {'horizon_checks': len(horizons), 'general_theorems': 'PAPER_ONLY',
                   'infinite_branch_counterexample': 'EXACT_SYMBOLIC_PROOF_IN_PROOF_NOTE',
                   'isPropAcc': 'SOURCE_REVIEWED_NOT_LOCALLY_COMPILED',
                   'dependent_choice_used_in_paper_transfer': False,
                   'claims_HoTT_core_error': False}}


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    result = report(); result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'horizons': 17,
                      'bad_lifts': result['bad_R036']['current_lift_failures'],
                      'certificate_checked': result['good_branching']['target_certificate_checked']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
