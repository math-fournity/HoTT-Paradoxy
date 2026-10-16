#!/usr/bin/env python3
"""The hexagon of three face maps has exactly two sides (Claude, session
7f138325, 2026-09-26; goal CG-003, gate G2; supporting check for CG001-C-69,
not a proof).

Terra's question T-039 asks whether routeA and routeB in WildSST.agda are
the right two routes.  This script checks, symbolically in i <= j <= k:
  1. from d_i d_{j+1} d_{k+2} the rule (a, fsuc b) -> (b, weaken a) reaches
     6 words by 6 rewrites (the hexagon P3) and ends at d_k d_j d_i;
  2. there are exactly two maximal chains, with rewrite positions (1, 0, 1)
     and (0, 1, 0);
  3. each rewrite is determined by its source word and position: the
     identity used is sid at that level with index pair (a, b), where the
     source letters are (a, fsuc b);
  4. the index pairs along the two chains are exactly those used by routeA
     and routeB in WildSST.agda (letters compared in the canonical form
     fsuc^f (weaken^w v), where weaken (fsuc v) = fsuc (weaken v) holds by
     computation).
So Coh2 = (routeA == routeB) is the unique 2-cell of the rewriting of three
face maps; there is no other choice of routes to compare.

Usage: python3 -B p3_routes.py   (deterministic output)
"""
from __future__ import annotations

VARS = "ijk"
START = (("i", 0, 0), ("j", 1, 0), ("k", 2, 0))


def show(let):
    v, f, w = let
    s = v
    for _ in range(w):
        s = f"weaken ({s})" if " " in s else f"weaken {s}"
    for _ in range(f):
        s = f"fsuc ({s})" if " " in s else f"fsuc {s}"
    return s


def can(word, p):
    return VARS.index(word[p][0]) < VARS.index(word[p + 1][0])


def step(word, p):
    a, b = word[p], word[p + 1]
    assert b[1] >= 1
    b2 = (b[0], b[1] - 1, b[2])       # b = fsuc b2
    a2 = (a[0], a[1], a[2] + 1)       # weaken a
    return word[:p] + (b2, a2) + word[p + 2:], (show(a), show(b2))


def chains(word):
    moves = [p for p in range(2) if can(word, p)]
    if not moves:
        return [((), (), (word,))]
    out = []
    for p in moves:
        nxt, pair = step(word, p)
        for ps, pairs, ws in chains(nxt):
            out.append(((p,) + ps, (pair,) + pairs, (word,) + ws))
    return out


def main() -> int:
    cs = sorted(chains(START))
    words = {w for _, _, ws in cs for w in ws}
    edges = {(ws[t], ps[t]) for ps, _, ws in cs for t in range(len(ps))}
    end = cs[0][2][-1]
    ok1 = len(words) == 6 and len(edges) == 6 and all(c[2][-1] == end for c in cs) \
        and end == (("k", 0, 0), ("j", 0, 1), ("i", 0, 2))
    ok2 = [c[0] for c in cs] == [(0, 1, 0), (1, 0, 1)]
    # routeA = positions (1,0,1), routeB = (0,1,0), index pairs as in WildSST.agda
    expected = {
        (1, 0, 1): (("fsuc j", "fsuc k"), ("i", "k"), ("weaken i", "weaken j")),
        (0, 1, 0): (("i", "j"), ("weaken i", "fsuc k"), ("j", "k")),
    }
    ok4 = all(expected[ps] == pairs for ps, pairs, _ in cs)
    print(f"words={len(words)} rewrites={len(edges)} end={tuple(show(x) for x in end)}  P3:{'ok' if ok1 else 'FAIL'}")
    for ps, pairs, ws in cs:
        name = "routeA" if ps == (1, 0, 1) else "routeB"
        print(f"{name}: positions {ps}; sid index pairs {pairs}")
    print(f"exactly two maximal chains: {'ok' if ok2 else 'FAIL'}")
    print(f"index pairs agree with WildSST.agda: {'ok' if ok4 else 'FAIL'}")
    ok = ok1 and ok2 and ok4
    print("ALL_OK" if ok else "SOME_FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
