#!/usr/bin/env python3
"""Generate the general second coherence (the permutohedron P4) of the
semi-simplicial identities as an Agda type (Claude, session 7f138325,
2026-09-26; goal CG-003, gate G1; claim CG001-C-68).

Why this exists.  CLAIM-C66.md reduced the second coherence to the condition
Deg3 on the degenerate structure `flat` by a hand argument (p4_faces.py only
checked the combinatorics).  Terra's question T-040 asks whether that
reduction is right.  This script removes the hand step: it writes the
general coherence Coh3 as an Agda type, from the rewriting graph of four
face maps, so that the kernel itself can evaluate it on `flat`.

What the script does, and what it checks before writing anything.
  1. Words are four face maps d_{a1} d_{a2} d_{a3} d_{a4} applied to x, with
     letters written as  fsuc^f (weaken^w v)  for v in {i, j, k, l}.  The rule
     (a, fsuc b) -> (b, weaken a), for a <= b, is the semi-simplicial identity
     `sid`.  From  d_i d_{j+1} d_{k+2} d_{l+3}  it reaches 24 words by 36
     rewrites (the 1-skeleton of P4) and ends at  d_l d_k d_j d_i.
  2. Faces: 6 squares (rewrites at positions 0 and 2 commute; naturality of
     a homotopy, `homotopyNatural`), 4 "bottom" hexagons (positions 0, 1; the
     level-m hexagon of the WildSST2 datum), 4 "top" hexagons (positions 1, 2;
     the level-(m+1) hexagon pushed along the outer face map).
  3. Routes are maximal chains (reduced words of the longest permutation, 16
     of them); a move replaces two or three consecutive edges of a route by
     the other side of one face.  The script searches for two sequences of
     moves from the lexicographically least route to the greatest one whose
     faces together are all 14 faces of P4, each exactly once (they turn out
     to have 6 and 8 moves).  The two composites are the two hemispheres of
     the boundary sphere; Coh3 says they are equal.
  4. It writes WildSSTP4.agda (definitions and Coh3), WildSSTP4Flat.agda
     (the proofs that Coh3 fails for the surf filling on `flat` and holds for
     the trivial one; the per-move steps are mechanical, the lemmas are fixed
     text) and P4_STRUCTURE.txt (every word, route, move and face, and the
     checks).

Usage: python3 -B gen_p4.py        (writes the two files next to itself)
The output is deterministic.
"""
from __future__ import annotations

import itertools
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
VARS = "ijkl"

# ---------------------------------------------------------------------------
# Words and rewrites

def letter_str(let):
    v, f, w = let
    s = v
    for _ in range(w):
        s = f"weaken ({s})" if " " in s or "(" in s else f"weaken {s}"
    for _ in range(f):
        s = f"fsuc ({s})" if " " in s or "(" in s else f"fsuc {s}"
    return s


def paren(s):
    return s if (" " not in s) else f"({s})"


START = (("i", 0, 0), ("j", 1, 0), ("k", 2, 0), ("l", 3, 0))


def can_rewrite(word, p):
    a, b = word[p], word[p + 1]
    return VARS.index(a[0]) < VARS.index(b[0])


def rewrite(word, p):
    a, b = word[p], word[p + 1]
    assert can_rewrite(word, p)
    assert b[1] >= 1, (word, p)
    b2 = (b[0], b[1] - 1, b[2])
    a2 = (a[0], a[1], a[2] + 1)
    return word[:p] + (b2, a2) + word[p + 2:]


def strip(let, n=1):
    v, f, w = let
    assert f >= n
    return (v, f - n, w)


def graph():
    seen, edges, todo = {START}, [], [START]
    while todo:
        w = todo.pop()
        for p in range(3):
            if can_rewrite(w, p):
                v = rewrite(w, p)
                edges.append((w, p, v))
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
    return seen, edges


# ---------------------------------------------------------------------------
# Order proofs (irrelevant in Agda, but they must type-check)

def base_proof(u, v):
    table = {
        ("i", "j"): "p", ("j", "k"): "q", ("k", "l"): "s",
        ("i", "k"): "≤F-trans i j k p q", ("j", "l"): "≤F-trans j k l q s",
        ("i", "l"): "≤F-trans i k l (≤F-trans i j k p q) s",
    }
    return table[(u, v)]


def le_proof(a, b):
    """A proof of  a ≤F b  for letters a, b of the same Fin size, with var(a)
    before var(b).  After stripping f(a) common fsucs (definitional), the goal
    is  weaken^{w(a)} va ≤F fsuc^g (weaken^{w(b)} vb)  with g = f(b) - f(a)."""
    va, fa, wa = a
    vb, fb, wb = b
    g = fb - fa
    assert g >= 0 and wa - wb == g, (a, b)
    inner = f"weaken≤N {wb} {va} {vb} ({base_proof(va, vb)})"
    return f"wk≤fs {g} (weakenN {wb} {va}) (weakenN {wb} {vb}) ({inner})"


# ---------------------------------------------------------------------------
# Agda terms for edges

def lvl(n):
    """the Agda level m + n"""
    s = "m"
    for _ in range(n):
        s = f"suc ({s})" if " " in s else f"suc {s}"
    return s


def inner_word(word, frm):
    """d (m+frm) A_frm ( ... (d (m+3) A4 x))  for letters frm..3 (0-based)"""
    s = "x"
    for t in range(3, frm - 1, -1):
        s = f"d {paren(lvl(t))} {paren(letter_str(word[t]))} {paren(s)}"
    return s


def edge_term(word, p):
    a, b = word[p], word[p + 1]
    bb = strip(b)
    pr = le_proof(a, bb)
    if p == 0:
        return (f"sid m {paren(letter_str(a))} {paren(letter_str(bb))} ({pr}) "
                f"{paren(inner_word(word, 2))}")
    if p == 1:
        return (f"cong (d m {paren(letter_str(word[0]))}) "
                f"(sid {paren(lvl(1))} {paren(letter_str(a))} {paren(letter_str(bb))} ({pr}) "
                f"{paren(inner_word(word, 3))})")
    return (f"cong (λ z → d m {paren(letter_str(word[0]))} (d {paren(lvl(1))} {paren(letter_str(word[1]))} z)) "
            f"(sid {paren(lvl(2))} {paren(letter_str(a))} {paren(letter_str(bb))} ({pr}) x)")


# ---------------------------------------------------------------------------
# Routes, faces, moves

def routes_from(word):
    """all maximal chains from word, as tuples of positions"""
    nxt = [p for p in range(3) if can_rewrite(word, p)]
    if not nxt:
        return [()]
    out = []
    for p in nxt:
        for rest in routes_from(rewrite(word, p)):
            out.append((p,) + rest)
    return out


def route_words(ps):
    ws = [START]
    for p in ps:
        ws.append(rewrite(ws[-1], p))
    return ws


PATTERNS = {
    (0, 2): ("square", (2, 0)), (2, 0): ("square", (0, 2)),
    (1, 0, 1): ("bottom", (0, 1, 0)), (0, 1, 0): ("bottom", (1, 0, 1)),
    (2, 1, 2): ("top", (1, 2, 1)), (1, 2, 1): ("top", (2, 1, 2)),
}


def moves_of(ps):
    ws = route_words(ps)
    out = []
    for t in range(len(ps)):
        for ln in (2, 3):
            seg = tuple(ps[t:t + ln])
            if len(seg) == ln and seg in PATTERNS:
                kind, repl = PATTERNS[seg]
                new = ps[:t] + repl + ps[t + ln:]
                top = ws[t]
                face = (kind, top)
                out.append((t, ln, seg, kind, face, new))
    return out


def all_faces():
    faces = set()
    vertices, _ = graph()
    for w in vertices:
        if can_rewrite(w, 0) and can_rewrite(w, 2):
            faces.add(("square", w))
        # a hexagon's top word has its three letters in the original order
        if can_rewrite(w, 0) and can_rewrite(w, 1) and can_rewrite(rewrite(w, 1), 0) \
                and VARS.index(w[0][0]) < VARS.index(w[2][0]):
            faces.add(("bottom", w))
        if can_rewrite(w, 1) and can_rewrite(w, 2) and VARS.index(w[1][0]) < VARS.index(w[3][0]):
            faces.add(("top", w))
    return faces


def face_words(face):
    kind, top = face
    if kind == "square":
        a = rewrite(top, 0)
        b = rewrite(top, 2)
        return {top, a, b, rewrite(a, 2)}
    ps = (1, 0, 1) if kind == "bottom" else (2, 1, 2)
    qs = (0, 1, 0) if kind == "bottom" else (1, 2, 1)
    ws = {top}
    for seq in (ps, qs):
        w = top
        for p in seq:
            w = rewrite(w, p)
            ws.add(w)
    return ws


def find_hemispheres(routes, faces):
    rmin, rmax = min(routes), max(routes)
    # all move-paths of length <= 8 from rmin to rmax without repeating a face
    paths = []
    todo = deque([(rmin, (), frozenset())])
    while todo:
        r, mv, used = todo.popleft()
        if r == rmax and mv:
            paths.append((mv, used))
            continue
        if len(mv) >= 8:
            continue
        for (t, ln, seg, kind, face, new) in moves_of(r):
            if face in used:
                continue
            todo.append((new, mv + ((r, t, ln, seg, kind, face, new),), used | {face}))
    for (m1, u1), (m2, u2) in itertools.combinations(sorted(paths, key=lambda x: [str(y) for y in x[0]]), 2):
        if len(u1 & u2) == 0 and (u1 | u2) == faces:
            return rmin, rmax, m1, m2
    raise SystemExit("NO_HEMISPHERE_PAIR")


# ---------------------------------------------------------------------------
# Face terms

def hexagon_indices(top, kind):
    if kind == "bottom":
        u, v, w = top[0], strip(top[1]), strip(top[2], 2)
    else:
        u, v, w = top[1], strip(top[2]), strip(top[3], 2)
    return u, v, w


def face_term(kind, top, seg):
    if kind == "square":
        a1, a2 = top[0], top[1]
        b = rewrite(top, 0)
        b1, b2 = b[0], b[1]
        H = (f"(λ y → sid m {paren(letter_str(a1))} {paren(letter_str(strip(a2)))} "
             f"({le_proof(a1, strip(a2))}) y)")
        P = (f"(sid {paren(lvl(2))} {paren(letter_str(top[2]))} {paren(letter_str(strip(top[3])))} "
             f"({le_proof(top[2], strip(top[3]))}) x)")
        f = f"(λ y → d m {paren(letter_str(a1))} (d {paren(lvl(1))} {paren(letter_str(a2))} y))"
        g = f"(λ y → d m {paren(letter_str(b1))} (d {paren(lvl(1))} {paren(letter_str(b2))} y))"
        nat = f"homotopyNatural {{f = {f}}} {{g = {g}}} {H} {P}"
        return nat if seg == (0, 2) else f"sym ({nat})"
    u, v, w = hexagon_indices(top, kind)
    pu, pv = le_proof(u, v), le_proof(v, w)
    if kind == "bottom":
        hx = (f"hexagon m {paren(letter_str(u))} {paren(letter_str(v))} {paren(letter_str(w))} "
              f"({pu}) ({pv}) {paren(inner_word(top, 3))}")
        return hx if seg == (1, 0, 1) else f"sym ({hx})"
    fsym = f"(d m {paren(letter_str(top[0]))})"
    args = (f"{paren(lvl(1))} {paren(letter_str(u))} {paren(letter_str(v))} {paren(letter_str(w))} "
            f"({pu}) ({pv}) x")
    hx = f"topFace {fsym} (hexagon {args})"
    return hx if seg == (2, 1, 2) else f"sym ({hx})"


# ---------------------------------------------------------------------------
# Emit Agda

HEADER = r'''{-# OPTIONS --safe --cubical --guardedness #-}
{-
  GENERATED by gen_p4.py -- do not edit by hand.
  (Claude, session 7f138325, 2026-09-26; goal CG-003, gate G1)

  proof id : MP-CG001-WILD-SST-P4-001
  claim    : CG001-C-68 (full statement in CLAIM.md)

  The general second coherence Coh₃ (the permutohedron P₄) of the
  semi-simplicial identities.  Its value on the degenerate structure flat of
  CG001-C-66 is established in WildSSTP4Flat.agda (generated by the same
  script).

  WildSSTᵢ is the definition of CG001-C-64 (WildSST.agda, same Fin, weaken,
  order, face maps and identities) with one change: the order hypothesis
  i ≤F j of the identities is an irrelevant argument.  ≤F is a proposition,
  so this only identifies proof terms that are equal anyway; it lets the
  same edge of P₄, reached through different faces, be the same term.
  toIrr turns every WildSST of CG001-C-64 into a WildSSTᵢ.

  The structure of P₄ used below (words, routes, moves, faces, and the check
  that the two hemispheres use every face exactly once) is listed in
  P4_STRUCTURE.txt, written by the same script.
-}
module WildSSTP4 where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc ; congFunct)
open import Cubical.Foundations.Function using (homotopyNatural)
open import Cubical.Data.Nat using (ℕ ; zero ; suc ; _+_)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Sum using (inl ; inr)
open import Cubical.Data.Int using (ℤ ; pos ; negsuc)
open import Cubical.Data.Int.Properties using (negsucNotpos)
open import Cubical.HITs.S1.Base using (S¹ ; base ; winding)
open import Cubical.HITs.S2.Base using (S²) renaming (base to north)
open import Cubical.Relation.Nullary using (¬_)

open import WildSST using (Fin ; fzero ; fsuc ; weaken ; _≤F_ ; ≤F-trans ; weaken≤ ; weaken≤suc ; WildSST)
open import WildSST2 using (Hopf ; carry ; r ; σr)

------------------------------------------------------------------------
-- Order lemmas used to build the (irrelevant) proofs.

weakenN : (g : ℕ) {s : ℕ} → Fin s → Fin (g + s)
weakenN zero a = a
weakenN (suc g) a = weaken (weakenN g a)

fsucN : (g : ℕ) {s : ℕ} → Fin s → Fin (g + s)
fsucN zero a = a
fsucN (suc g) a = fsuc (fsucN g a)

weaken≤N : (g : ℕ) {s : ℕ} (a b : Fin s) → a ≤F b → weakenN g a ≤F weakenN g b
weaken≤N zero a b h = h
weaken≤N (suc g) a b h = weaken≤ (weakenN g a) (weakenN g b) (weaken≤N g a b h)

wk≤fs : (g : ℕ) {s : ℕ} (a b : Fin s) → a ≤F b → weakenN g a ≤F fsucN g b
wk≤fs zero a b h = h
wk≤fs (suc g) a b h = weaken≤suc (weakenN g a) (fsucN g b) (wk≤fs g a b h)

------------------------------------------------------------------------
-- The definition of CG001-C-64 with an irrelevant order hypothesis.

record WildSSTᵢ : Type₁ where
  field
    X   : ℕ → Type
    d   : (n : ℕ) → Fin (suc (suc n)) → X (suc n) → X n
    sid : (n : ℕ) (i j : Fin (suc (suc n))) → .(i ≤F j) → (x : X (suc (suc n)))
        → d n i (d (suc n) (fsuc j) x) ≡ d n j (d (suc n) (weaken i) x)

toIrr : WildSST → WildSSTᵢ
WildSSTᵢ.X (toIrr S) = WildSST.X S
WildSSTᵢ.d (toIrr S) = WildSST.d S
WildSSTᵢ.sid (toIrr S) n i j h x = WildSST.sid S n i j (recompute i j h) x
  where
  recompute : {n : ℕ} (a b : Fin n) → .(a ≤F b) → a ≤F b
  recompute {suc n} (inl _) b _ = tt
  recompute {suc n} (inr a) (inl _) ()
  recompute {suc n} (inr a) (inr b) h = recompute a b h

module Routesᵢ (S : WildSSTᵢ) where
  open WildSSTᵢ S

  routeA : (m : ℕ) (i j k : Fin (suc (suc m))) .(p : i ≤F j) .(q : j ≤F k)
    (x : X (suc (suc (suc m))))
    → d m i (d (suc m) (fsuc j) (d (suc (suc m)) (fsuc (fsuc k)) x))
      ≡ d m k (d (suc m) (weaken j) (d (suc (suc m)) (weaken (weaken i)) x))
  routeA m i j k p q x =
      cong (d m i) (sid (suc m) (fsuc j) (fsuc k) q x)
    ∙ sid m i k (≤F-trans i j k p q) (d (suc (suc m)) (weaken (fsuc j)) x)
    ∙ cong (d m k) (sid (suc m) (weaken i) (weaken j) (weaken≤ i j p) x)

  routeB : (m : ℕ) (i j k : Fin (suc (suc m))) .(p : i ≤F j) .(q : j ≤F k)
    (x : X (suc (suc (suc m))))
    → d m i (d (suc m) (fsuc j) (d (suc (suc m)) (fsuc (fsuc k)) x))
      ≡ d m k (d (suc m) (weaken j) (d (suc (suc m)) (weaken (weaken i)) x))
  routeB m i j k p q x =
      sid m i j p (d (suc (suc m)) (fsuc (fsuc k)) x)
    ∙ cong (d m j) (sid (suc m) (weaken i) (fsuc k)
                      (weaken≤suc i k (≤F-trans i j k p q)) x)
    ∙ sid m j k q (d (suc (suc m)) (weaken (weaken i)) x)

open Routesᵢ

Coh₂ᵢ : WildSSTᵢ → Type
Coh₂ᵢ S = (m : ℕ) (i j k : Fin (suc (suc m))) .(p : i ≤F j) .(q : j ≤F k)
  (x : WildSSTᵢ.X S (suc (suc (suc m))))
  → routeA S m i j k p q x ≡ routeB S m i j k p q x

record WildSSTᵢ₂ : Type₁ where
  field
    underlying : WildSSTᵢ
    hexagon    : Coh₂ᵢ underlying

------------------------------------------------------------------------
-- Path algebra: replacing a segment of a composite, and pushing a hexagon
-- along a map.

module _ {ℓ : Level} {A : Type ℓ} where
  seg2 : {w x x' z v : A} {a : w ≡ x} {b : x ≡ z} {a' : w ≡ x'} {b' : x' ≡ z}
       → a ∙ b ≡ a' ∙ b' → (T : z ≡ v) → a ∙ b ∙ T ≡ a' ∙ b' ∙ T
  seg2 {a = a} {b} {a' = a'} {b'} Q T = assoc a b T ∙ cong (_∙ T) Q ∙ sym (assoc a' b' T)

  seg3 : {w x y x' y' z v : A} {a : w ≡ x} {b : x ≡ y} {c : y ≡ z}
         {a' : w ≡ x'} {b' : x' ≡ y'} {c' : y' ≡ z}
       → a ∙ b ∙ c ≡ a' ∙ b' ∙ c' → (T : z ≡ v) → a ∙ b ∙ c ∙ T ≡ a' ∙ b' ∙ c' ∙ T
  seg3 {a = a} {b} {c} {a' = a'} {b'} {c'} H T =
      (cong (a ∙_) (assoc b c T) ∙ assoc a (b ∙ c) T)
    ∙ cong (_∙ T) H
    ∙ sym (cong (a' ∙_) (assoc b' c' T) ∙ assoc a' (b' ∙ c') T)

module _ {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'} where
  congFunct₃ : (f : A → B) {w x y z : A} (a : w ≡ x) (b : x ≡ y) (c : y ≡ z)
             → cong f (a ∙ b ∙ c) ≡ cong f a ∙ cong f b ∙ cong f c
  congFunct₃ f a b c = congFunct f a (b ∙ c) ∙ cong (cong f a ∙_) (congFunct f b c)

  topFace : (f : A → B) {w x y x' y' z : A} {a : w ≡ x} {b : x ≡ y} {c : y ≡ z}
            {a' : w ≡ x'} {b' : x' ≡ y'} {c' : y' ≡ z}
          → a ∙ b ∙ c ≡ a' ∙ b' ∙ c'
          → cong f a ∙ cong f b ∙ cong f c ≡ cong f a' ∙ cong f b' ∙ cong f c'
  topFace f {a = a} {b} {c} {a' = a'} {b'} {c'} H =
    sym (congFunct₃ f a b c) ∙ cong (cong f) H ∙ congFunct₃ f a' b' c'
'''


def main() -> int:
    vertices, edges = graph()
    assert len(vertices) == 24 and len(edges) == 36
    end = (("l", 0, 0), ("k", 0, 1), ("j", 0, 2), ("i", 0, 3))
    assert end in vertices and not any(can_rewrite(end, p) for p in range(3))
    faces = all_faces()
    kinds = sorted(k for k, _ in faces)
    assert len(faces) == 14 and kinds.count("square") == 6 and kinds.count("bottom") == 4 \
        and kinds.count("top") == 4, kinds
    # every edge lies on exactly two faces
    edge_faces = {}
    for fc in faces:
        ws = face_words(fc)
        for (w, p, v) in edges:
            if w in ws and v in ws:
                edge_faces.setdefault((w, p), []).append(fc)
    assert len(edge_faces) == 36 and all(len(v) == 2 for v in edge_faces.values())
    routes = sorted(routes_from(START))
    assert len(routes) == 16
    rmin, rmax, h1, h2 = find_hemispheres(routes, faces)
    used1 = [m[5] for m in h1]
    used2 = [m[5] for m in h2]
    assert len(set(used1) | set(used2)) == 14 and not (set(used1) & set(used2))

    # ---- Agda ----
    out = [HEADER]
    out.append(r'''
------------------------------------------------------------------------
-- The two hemispheres of P₄ and the coherence Coh₃.

module P4 (S : WildSSTᵢ₂) where
  open WildSSTᵢ₂ S
  open WildSSTᵢ underlying

  module _ (m : ℕ) (i j k l : Fin (suc (suc m)))
           .(p : i ≤F j) .(q : j ≤F k) .(s : k ≤F l)
           (x : X (suc (suc (suc (suc m))))) where
''')
    edge_names = {}

    def ename(word, p):
        key = (word, p)
        if key not in edge_names:
            edge_names[key] = f"e{len(edge_names)}"
        return edge_names[key]

    # collect all routes used
    used_routes = [rmin]
    for mv in list(h1) + list(h2):
        if mv[6] not in used_routes:
            used_routes.append(mv[6])
    for rt in used_routes:
        ws = route_words(rt)
        for t, p in enumerate(rt):
            ename(ws[t], p)
    for (word, p), nm in sorted(edge_names.items(), key=lambda kv: int(kv[1][1:])):
        out.append(f"    {nm} : _\n    {nm} = {edge_term(word, p)}\n")

    def route_edges(rt):
        ws = route_words(rt)
        return [ename(ws[t], p) for t, p in enumerate(rt)]

    def comp(names):
        s = "refl"
        for nm in reversed(names):
            s = f"{nm} ∙ {s}" if s == "refl" else f"{nm} ∙ ({s})" if " " in s else f"{nm} ∙ {s}"
        return s

    def comp_str(names):
        # right-nested, trailing refl: e1 ∙ e2 ∙ ... ∙ e6 ∙ refl (∙ is infixr)
        return " ∙ ".join(names + ["refl"])

    def move_term(mv):
        r, t, ln, seg, kind, face, new = mv
        es = route_edges(r)
        prefix = es[:t]
        tail = es[t + ln:]
        F = face_term(kind, face[1], seg)
        segf = "seg2" if ln == 2 else "seg3"
        body = f"{segf} ({F}) ({comp_str(tail)})"
        if prefix:
            lam = " ∙ ".join(prefix + ["z"])
            body = f"cong (λ z → {lam}) ({body})"
        return body

    for hname, hem in (("hem₁", h1), ("hem₂", h2)):
        names = []
        for idx, mv in enumerate(hem):
            nm = f"{hname}-{idx + 1}"
            names.append(nm)
            out.append(f"    {nm} : _\n    {nm} = {move_term(mv)}\n")
        out.append(f"    {hname} : _\n    {hname} = " + " ∙ ".join(names) + "\n")

    out.append(r'''
Coh₃ : WildSSTᵢ₂ → Type
Coh₃ S = (m : ℕ) (i j k l : Fin (suc (suc m)))
  .(p : i ≤F j) .(q : j ≤F k) .(s : k ≤F l)
  (x : WildSSTᵢ.X (WildSSTᵢ₂.underlying S) (suc (suc (suc (suc m)))))
  → P4.hem₁ S m i j k l p q s x ≡ P4.hem₂ S m i j k l p q s x
''')
    (HERE / "WildSSTP4.agda").write_text("".join(out), encoding="utf-8")

    # ---- structure listing ----
    lines = []
    lines.append("P4 structure used by WildSSTP4.agda (generated by gen_p4.py)\n")
    lines.append(f"words: {len(vertices)}; rewrites: {len(edges)}; faces: 14 "
                 f"(squares {kinds.count('square')}, bottom hexagons {kinds.count('bottom')}, "
                 f"top hexagons {kinds.count('top')}); routes (maximal chains): {len(routes)}\n")
    lines.append("every rewrite lies on exactly two faces: OK\n")
    lines.append(f"least route (positions): {rmin}\ngreatest route: {rmax}\n")
    for hname, hem, used in (("hem1", h1, used1), ("hem2", h2, used2)):
        lines.append(f"\n{hname}: {len(hem)} moves\n")
        for mv in hem:
            r, t, ln, seg, kind, face, new = mv
            lines.append(f"  route {r} --[{kind} at edges {t}..{t + ln - 1}, {seg} -> "
                         f"{PATTERNS[seg][1]}; top word {tuple(letter_str(x) for x in face[1])}]--> {new}\n")
    lines.append("\nfaces used by hem1 and hem2 are disjoint and together are all 14 faces: OK\n")
    lines.append("\nall faces (kind, top word):\n")
    for fc in sorted(faces, key=lambda f: (f[0], str(f[1]))):
        who = "hem1" if fc in used1 else "hem2"
        lines.append(f"  {fc[0]:7s} {tuple(letter_str(x) for x in fc[1])}  in {who}\n")
    (HERE / "P4_STRUCTURE.txt").write_text("".join(lines), encoding="utf-8")

    emit_flat(h1, h2)
    print("WROTE WildSSTP4.agda, WildSSTP4Flat.agda and P4_STRUCTURE.txt; ALL_CHECKS_OK")
    return 0


# ---------------------------------------------------------------------------
# The flat computation (second generated file)

FLAT_HEADER = r'''{-# OPTIONS --safe --cubical --guardedness #-}
{-
  GENERATED by gen_p4.py -- do not edit by hand.
  (Claude, session 7f138325, 2026-09-26; goal CG-003, gate G1)

  proof id : MP-CG001-WILD-SST-P4-001 (together with WildSSTP4.agda)
  claim    : CG001-C-68 (full statement in CLAIM-C68.md)

  The general second coherence Coh₃ of WildSSTP4.agda, evaluated on the
  degenerate structure flat of CG001-C-66 (points of S² in dimension 0,
  Unit above, every identity refl), with the two hexagon data of C-66:

  (a) notCoh₃   : ¬ Coh₃ flatSurfᵢ   (level-0 hexagon filler σr at (0,0,0))
  (b) coh₃Trivial : Coh₃ flatTrivialᵢ (every hexagon filler refl)

  This replaces the hand step of CLAIM-C66.md ("P₄ reduces to Deg₃ on
  flat"): the violation is now read off the general coherence itself.

  How the proof goes.  On flat at level 0 every edge of P₄ is refl, so every
  route is the same composite of refl's and every move is a loop.  Each move
  is  cong P (seg₂/₃ F T)  for a prefix P, a tail T and a face F; a move whose
  face is refl (after computation), topFace f refl, or homotopyNatural on
  constant maps is refl (natConst, seg-refl, topFace-refl).  At the instance
  m = 0, (i, j, k, l) = (0, 0, 0, 1) exactly one face carries a non-trivial
  filler: the level-0 hexagon at (i, j, k) = (0, 0, 0), in the first move of
  hem₁, which is  seg₃ (sym σr) T.  So Coh₃ gives  seg₃ (sym σr) T ≡ refl, and
  seg₃ is injective in its face (seg3-inj), hence σr ≡ refl, which C-66
  refutes (σr≢refl).
-}
module WildSSTP4Flat where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit ; rUnit ; lCancel ; rCancel ; assoc)
open import Cubical.Foundations.Function using (homotopyNatural)
open import Cubical.Foundations.Path using (compPathr-isEquiv)
open import Cubical.Functions.Embedding using (isEquiv→isEmbedding ; isEmbedding→Inj)
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Unit.Properties using (isOfHLevelUnit)
open import Cubical.Data.Sum using (inl ; inr)
open import Cubical.HITs.S2.Base using (S²) renaming (base to north)
open import Cubical.Relation.Nullary using (¬_)

open import WildSST using (Fin ; fzero ; fsuc ; _≤F_)
open import WildSST2 using (σr ; σr≢refl)
open import WildSSTP4

------------------------------------------------------------------------
-- Lemmas: trivial faces give trivial moves; seg₃ is injective in its face.

natConst : ∀ {ℓ ℓ'} {A : Type ℓ} {B : Type ℓ'} (b : B) {x y : A} (p : x ≡ y)
  → homotopyNatural {f = λ _ → b} {g = λ _ → b} (λ _ → refl) p ≡ refl
natConst b p t i j =
  hcomp (λ k → λ { (i = i0) → compPath-filler (refl {x = b}) refl k j
                 ; (i = i1) → compPath-filler' (refl {x = b}) refl k j
                 ; (j = i0) → b
                 ; (j = i1) → b
                 ; (t = i1) → compPath-filler (refl {x = b}) refl k j })
        b

module _ {ℓ : Level} {A : Type ℓ} where
  conj-triv : {u v : A} {Y : u ≡ u} (α : v ≡ u) → α ∙ Y ∙ sym α ≡ refl → Y ≡ refl
  conj-triv {Y = Y} α h =
    Y                                  ≡⟨ lUnit Y ⟩
    refl ∙ Y                           ≡⟨ cong (_∙ Y) (sym (lCancel α)) ⟩
    (sym α ∙ α) ∙ Y                    ≡⟨ sym (assoc (sym α) α Y) ⟩
    sym α ∙ α ∙ Y                      ≡⟨ cong (λ Z → sym α ∙ α ∙ Z) (rUnit Y) ⟩
    sym α ∙ α ∙ Y ∙ refl               ≡⟨ cong (λ Z → sym α ∙ α ∙ Y ∙ Z) (sym (lCancel α)) ⟩
    sym α ∙ α ∙ Y ∙ sym α ∙ α          ≡⟨ cong (λ Z → sym α ∙ α ∙ Z) (assoc Y (sym α) α) ⟩
    sym α ∙ α ∙ (Y ∙ sym α) ∙ α        ≡⟨ cong (sym α ∙_) (assoc α (Y ∙ sym α) α) ⟩
    sym α ∙ (α ∙ Y ∙ sym α) ∙ α        ≡⟨ cong (λ Z → sym α ∙ Z ∙ α) h ⟩
    sym α ∙ refl ∙ α                   ≡⟨ cong (sym α ∙_) (sym (lUnit α)) ⟩
    sym α ∙ α                          ≡⟨ lCancel α ⟩
    refl                               ∎


module _ {ℓ : Level} {A : Type ℓ} where
  seg2-refl : {w x z v : A} {a : w ≡ x} {b : x ≡ z} (T : z ≡ v)
            → seg2 {a = a} {b} {a' = a} {b' = b} refl T ≡ refl
  seg2-refl {a = a} {b} T =
    cong (assoc a b T ∙_) (sym (lUnit (sym (assoc a b T)))) ∙ rCancel (assoc a b T)

  seg3-refl : {w x y z v : A} {a : w ≡ x} {b : x ≡ y} {c : y ≡ z} (T : z ≡ v)
            → seg3 {a = a} {b} {c} {a' = a} {b' = b} {c' = c} refl T ≡ refl
  seg3-refl {a = a} {b} {c} T = cong (α ∙_) (sym (lUnit (sym α))) ∙ rCancel α
    where
    α = cong (a ∙_) (assoc b c T) ∙ assoc a (b ∙ c) T

  seg3-inj : {w x y z v : A} {a : w ≡ x} {b : x ≡ y} {c : y ≡ z} (T : z ≡ v)
             (F : a ∙ b ∙ c ≡ a ∙ b ∙ c) → seg3 F T ≡ refl → F ≡ refl
  seg3-inj {a = a} {b} {c} T F h =
    isEmbedding→Inj
      (isEquiv→isEmbedding (isEquiv→isEmbedding (compPathr-isEquiv T) (a ∙ b ∙ c) (a ∙ b ∙ c)))
      F refl (conj-triv α h)
    where
    α = cong (a ∙_) (assoc b c T) ∙ assoc a (b ∙ c) T

  ∙-triv : {u : A} {p q : u ≡ u} → p ≡ refl → q ≡ refl → p ∙ q ≡ refl
  ∙-triv ep eq = cong₂ _∙_ ep eq ∙ sym (rUnit refl)

module _ {ℓ ℓ' : Level} {A : Type ℓ} {C : Type ℓ'} where
  mv2-triv : {w x z v : A} {a : w ≡ x} {b : x ≡ z} (P : (w ≡ v) → C) (T : z ≡ v)
             {F : a ∙ b ≡ a ∙ b} → F ≡ refl → cong P (seg2 F T) ≡ refl
  mv2-triv P T e = cong (λ Y → cong P (seg2 Y T)) e ∙ cong (cong P) (seg2-refl T)

  mv3-triv : {w x y z v : A} {a : w ≡ x} {b : x ≡ y} {c : y ≡ z} (P : (w ≡ v) → C) (T : z ≡ v)
             {F : a ∙ b ∙ c ≡ a ∙ b ∙ c} → F ≡ refl → cong P (seg3 F T) ≡ refl
  mv3-triv P T e = cong (λ Y → cong P (seg3 Y T)) e ∙ cong (cong P) (seg3-refl T)

module _ {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'} where
  topFace-refl : (f : A → B) {w x y z : A} {a : w ≡ x} {b : x ≡ y} {c : y ≡ z}
    → topFace f {a = a} {b} {c} {a' = a} {b' = b} {c' = c} refl ≡ refl
  topFace-refl f {a = a} {b} {c} = cong (sym C ∙_) (sym (lUnit C)) ∙ lCancel C
    where
    C = congFunct₃ f a b c

------------------------------------------------------------------------
-- flat (the same clauses as WildSST2.flat) and its two hexagon data.

flatᵢ : WildSSTᵢ
WildSSTᵢ.X flatᵢ zero = S²
WildSSTᵢ.X flatᵢ (suc n) = Unit
WildSSTᵢ.d flatᵢ zero _ _ = north
WildSSTᵢ.d flatᵢ (suc n) _ _ = tt
WildSSTᵢ.sid flatᵢ zero _ _ _ _ = refl
WildSSTᵢ.sid flatᵢ (suc n) _ _ _ _ = refl

cohTrivialᵢ : Coh₂ᵢ flatᵢ
cohTrivialᵢ zero i j k _ _ x = refl
cohTrivialᵢ (suc m) i j k _ _ x = refl

cohSurfᵢ : Coh₂ᵢ flatᵢ
cohSurfᵢ zero (inl _) (inl _) (inl _) _ _ x = σr
cohSurfᵢ zero i j k _ _ x = refl
cohSurfᵢ (suc m) i j k _ _ x = refl

flatTrivialᵢ flatSurfᵢ : WildSSTᵢ₂
flatTrivialᵢ = record { underlying = flatᵢ ; hexagon = cohTrivialᵢ }
flatSurfᵢ    = record { underlying = flatᵢ ; hexagon = cohSurfᵢ }
'''


def emit_flat(h1, h2):
    val = {"i": 0, "j": 0, "k": 0, "l": 1}

    def letter_val(let):
        return val[let[0]] + let[1]

    def refls(n):
        return " ∙ ".join(["refl"] * n) if n else ""

    def prefix_lam(t):
        if t == 0:
            return "(λ (z : north ≡ north) → z)"
        return f"(λ (z : north ≡ north) → {refls(t)} ∙ z)"

    def tail_term(n):
        # n edges (each refl at the instance) followed by the trailing refl
        return "(" + " ∙ ".join(["refl {x = north}"] + ["refl"] * n) + ")"

    def face_triv(kind, seg):
        if kind == "bottom":
            return "refl"
        if kind == "top":
            tf = "topFace-refl (λ (_ : Unit) → north) {a = refl} {b = refl} {c = refl}"
            return f"({tf})" if seg == (2, 1, 2) else f"(cong sym ({tf}))"
        nc = "natConst north {x = tt} {y = tt} refl"
        return f"({nc})" if seg == (0, 2) else f"(cong sym ({nc}))"

    def is_sigma(mv):
        r, t, ln, seg, kind, face, new = mv
        if kind != "bottom":
            return False
        u, v, w = hexagon_indices(face[1], "bottom")
        return all(letter_val(x) == 0 for x in (u, v, w))

    def triv_term(mv):
        r, t, ln, seg, kind, face, new = mv
        tail_n = 6 - t - ln
        f = "mv2-triv" if ln == 2 else "mv3-triv"
        return f"{f} {prefix_lam(t)} {tail_term(tail_n)} {face_triv(kind, seg)}"

    out = [FLAT_HEADER]
    inst = "zero fzero fzero fzero (fsuc fzero) tt tt tt tt"
    sigma = [(h, idx) for h, hem in (("hem₁", h1), ("hem₂", h2)) for idx, mv in enumerate(hem) if is_sigma(mv)]
    assert sigma == [("hem₁", 0)], sigma
    out.append("\n------------------------------------------------------------------------\n"
               "-- (a) The instance m = 0, (i, j, k, l) = (0, 0, 0, 1) on flatSurfᵢ.\n\n"
               "module AtSurf where\n")
    for hname, hem in (("hem₁", h1), ("hem₂", h2)):
        for idx, mv in enumerate(hem):
            if hname == "hem₁" and idx == 0:
                continue
            nm = f"triv-{hname}-{idx + 1}"
            out.append(f"  {nm} : P4.{hname}-{idx + 1} flatSurfᵢ {inst} ≡ refl\n"
                       f"  {nm} = {triv_term(mv)}\n")

    def fold(names):
        s = names[-1]
        for nm in reversed(names[:-1]):
            s = f"∙-triv {nm} ({s})"
        return s

    rest1 = [f"triv-hem₁-{i + 1}" for i in range(1, len(h1))]
    all2 = [f"triv-hem₂-{i + 1}" for i in range(len(h2))]
    first = h1[0]
    tail_n = 6 - first[1] - first[2]
    out.append(f"""
  rest₁ : _
  rest₁ = {fold(rest1)}

  all₂ : P4.hem₂ flatSurfᵢ {inst} ≡ refl
  all₂ = {fold(all2)}

notCoh₃ : ¬ Coh₃ flatSurfᵢ
notCoh₃ h = σr≢refl (cong sym (seg3-inj {tail_term(tail_n)} (sym σr) key))
  where
  open AtSurf
  key : P4.hem₁-1 flatSurfᵢ {inst} ≡ refl
  key = rUnit _ ∙ cong (P4.hem₁-1 flatSurfᵢ {inst} ∙_) (sym rest₁)
      ∙ h zero fzero fzero fzero (fsuc fzero) tt tt tt tt ∙ all₂
""")
    # (b) positive control
    out.append("\n------------------------------------------------------------------------\n"
               "-- (b) flatTrivialᵢ satisfies Coh₃: at level 0 every move is refl (for all\n"
               "-- indices); above level 0 the simplices form Unit, a groupoid.\n\n"
               "module AtTrivial (i j k l : Fin 2) .(p : i ≤F j) .(q : j ≤F k) .(s : k ≤F l) (x : Unit) where\n")
    instT = "zero i j k l p q s x"
    for hname, hem in (("hem₁", h1), ("hem₂", h2)):
        for idx, mv in enumerate(hem):
            nm = f"triv-{hname}-{idx + 1}"
            out.append(f"  {nm} : P4.{hname}-{idx + 1} flatTrivialᵢ {instT} ≡ refl\n"
                       f"  {nm} = {triv_term(mv)}\n")
    all1T = [f"triv-hem₁-{i + 1}" for i in range(len(h1))]
    out.append(f"""
  all₁ : P4.hem₁ flatTrivialᵢ {instT} ≡ refl
  all₁ = {fold(all1T)}

  all₂ : P4.hem₂ flatTrivialᵢ {instT} ≡ refl
  all₂ = {fold(all2)}

coh₃Trivial : Coh₃ flatTrivialᵢ
coh₃Trivial zero i j k l p q s x = AtTrivial.all₁ i j k l p q s x ∙ sym (AtTrivial.all₂ i j k l p q s x)
coh₃Trivial (suc m) i j k l p q s x = isOfHLevelUnit 3 _ _ _ _ _ _
""")
    (HERE / "WildSSTP4Flat.agda").write_text("".join(out), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
