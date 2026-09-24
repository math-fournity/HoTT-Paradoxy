#!/usr/bin/env python3
"""Finite R05 completion-triggered graph changes with explicit specification IDs.

Arithmetic projection of StageStep/fsuc on six observed stages, not a native
SeqColim evaluator, proof of infinite execution, or natural HoTT consumer.
"""
import argparse, hashlib, json
from pathlib import Path


def graph(n):
    return {"stage": n, "nodes": list(range(n + 1)),
            "edges": [[x, x - 1] for x in range(1, n + 1)]}


def identity(g):
    return hashlib.sha256(json.dumps(g, sort_keys=True).encode()).hexdigest()


def finished(g, node):
    assert node in g["nodes"]
    return not any(x == node for x, _ in g["edges"])


def observe(policy, rounds, n=0, node=0):
    records = []
    for k in range(rounds):
        before = graph(n)
        certificate = {"spec": identity(before), "node": node, "done": finished(before, node)}
        if certificate["done"] and policy == "grow-on-done":
            n, node = n + 1, node + 1
            action = "extend-stage-and-apply-fsuc-projection"
        else:
            action = "keep-stage-and-node"
        after = graph(n)
        current_done = finished(after, node)
        scoped_accept = certificate["spec"] == identity(after) and certificate["node"] == node and certificate["done"]
        preserved_edges = all([x + 1, y + 1] in after["edges"] for x, y in before["edges"]) if action.startswith("extend") else before == after
        walk = [node]
        while not finished(after, node):
            targets = [y for x, y in after["edges"] if x == node]
            assert len(targets) == 1
            node = targets[0]; walk.append(node)
        records.append({"round": k, "before": before, "certificate": certificate,
                        "trigger_read": certificate["done"], "action": action, "after": after,
                        "after_node_before_walk": walk[0], "old_boolean_accepts": certificate["done"],
                        "scoped_certificate_accepts": scoped_accept, "actual_current_done_before_walk": current_done,
                        "old_edges_preserved_in_this_instance": preserved_edges, "fresh_walk": walk,
                        "fresh_done": finished(after, node)})
    return records


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); args = ap.parse_args()
    results = {policy: observe(policy, 6) for policy in ['grow-on-done', 'frozen']}
    # Independent expectations about these named observations, not every possible
    # graph or controller. The nonterminal control checks the branch predicate.
    growing = results['grow-on-done']; frozen = results['frozen']
    nonterminal = observe('grow-on-done', 1, n=2, node=1)[0]
    checks = {
        'six_growth_events': all(r['after']['stage'] == i + 1 for i, r in enumerate(growing)),
        'growth_changes_done_scope': all(r['old_boolean_accepts'] and not r['scoped_certificate_accepts'] and not r['actual_current_done_before_walk'] for r in growing),
        'growth_fresh_walks': all(r['fresh_walk'] == [1, 0] and r['fresh_done'] for r in growing),
        'frozen_keeps_same_done': all(r['scoped_certificate_accepts'] and r['actual_current_done_before_walk'] and r['fresh_walk'] == [0] for r in frozen),
        'finite_edge_preservation': all(r['old_edges_preserved_in_this_instance'] for rows in results.values() for r in rows),
        'nonterminal_control_no_growth': not nonterminal['trigger_read'] and nonterminal['action'] == 'keep-stage-and-node' and nonterminal['after'] == graph(2) and nonterminal['fresh_walk'] == [1, 0],
    }
    result = {'scope': __doc__, 'rounds_per_policy': 6, 'policies': results,
              'nonterminal_control': nonterminal,
              'checks': checks, 'all_expected': all(checks.values()), 'native_proof': False,
              'infinite_execution_proved': False,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    with Path(args.out).open('x') as f: json.dump(result, f, ensure_ascii=False, indent=2); f.write('\n')
    print(json.dumps({'checks': checks, 'all_expected': result['all_expected']}, ensure_ascii=False))
    return 0 if result['all_expected'] else 1


if __name__ == '__main__': main()
