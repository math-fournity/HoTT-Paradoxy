#!/usr/bin/env python3
"""Enumerate the rewriting graph of four face maps (the permutohedron P4) and
list which index triples its hexagons carry (Claude, session 7f138325,
2026-09-26; supporting computation for CG001-C-66, not a proof).

Why this exists: CLAIM-C66.md reduces the second coherence of the
semi-simplicial identities, on the degenerate structure `flat`, to the
condition Deg3 of WildSST2.agda.  The reduction uses three combinatorial
facts about the rewriting of a word d_{a1} d_{a2} d_{a3} d_{a4}:
  1. starting from d_i d_{j+1} d_{k+2} d_{l+3} (i <= j <= k <= l), the words
     reachable by the rule  d_a d_b -> d_{b-1} d_a  (a < b)  form a
     permutohedron: 24 words, 36 rewrites, 6 squares and 8 hexagons, ending
     at d_l d_k d_j d_i;
  2. the 4 hexagons on the leftmost three letters ("bottom", level-0 cells)
     start at d_x d_{y+1} d_{z+2} with (x, y, z) running over
     (i, j, k), (i, j, l), (i, k, l), (j, k, l), one each;
  3. the other 4 hexagons act on the rightmost three letters (level-1 cells,
     which live in Unit on `flat`), and the 6 squares act on disjoint pairs.
This script checks the three facts for every i <= j <= k <= l in a range and
prints the bottom triples.  Letters are face indices, leftmost = applied last.

Usage: python3 -B p4_faces.py [max_index]   (default 2; deterministic output)
"""
from __future__ import annotations

import sys
from itertools import combinations_with_replacement


def rewrites(word: tuple[int, ...]) -> list[tuple[int, tuple[int, ...]]]:
    out = []
    for p in range(len(word) - 1):
        a, b = word[p], word[p + 1]
        if a < b:
            new = word[:p] + (b - 1, a) + word[p + 2:]
            out.append((p, new))
    return out


def graph(start: tuple[int, ...]):
    seen, edges, todo = {start}, [], [start]
    while todo:
        w = todo.pop()
        for p, v in rewrites(w):
            edges.append((w, p, v))
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen, edges


def components(vertices, edges, positions):
    parent = {v: v for v in vertices}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for w, p, v in edges:
        if p in positions:
            parent[find(w)] = find(v)
    comps: dict = {}
    for v in vertices:
        comps.setdefault(find(v), []).append(v)
    return [sorted(c) for c in comps.values()]


def source(comp, edges, positions):
    targets = {v for w, p, v in edges if p in positions and w in comp}
    sources = [v for v in comp if v not in targets]
    assert len(sources) == 1, sources
    return sources[0]


def main() -> int:
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    ok = True
    for i, j, k, l in combinations_with_replacement(range(top + 1), 4):
        start = (i, j + 1, k + 2, l + 3)
        vertices, edges = graph(start)
        end = (l, k, j, i)
        squares = components(vertices, edges, {0, 2})
        bottom = components(vertices, edges, {0, 1})
        upper = components(vertices, edges, {1, 2})
        facts_1 = (len(vertices) == 24 and len(edges) == 36 and end in vertices
                   and not rewrites(end) and all(len(c) == 4 for c in squares)
                   and len(squares) == 6 and all(len(c) == 6 for c in bottom + upper)
                   and len(bottom) == 4 and len(upper) == 4)
        triples = []
        for comp in bottom:
            x, y, z, _ = source(comp, edges, {0, 1})
            triples.append((x, y - 1, z - 2))
        triples.sort()
        expected = sorted([(i, j, k), (i, j, l), (i, k, l), (j, k, l)])
        fact_2 = triples == expected and all(a <= b <= c for a, b, c in triples)
        ok = ok and facts_1 and fact_2
        count000 = triples.count((0, 0, 0))
        print(f"(i,j,k,l)=({i},{j},{k},{l})  P4:{'ok' if facts_1 else 'FAIL'}  "
              f"bottom triples={triples}  match:{'ok' if fact_2 else 'FAIL'}  "
              f"copies of (0,0,0)={count000}")
    print("ALL_OK" if ok else "SOME_FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
