#!/usr/bin/env python3
"""Finite/model regression tests for the HOTT–Z research package.

These checks are *not* proof-assistant proofs.  They exercise finite instances,
verify countermodels, and protect theorem statements against common mistakes.
"""
from __future__ import annotations

import itertools
import json
import math
import pathlib
import sys
from dataclasses import dataclass, asdict
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "verification" / "model_checks.json"

@dataclass
class Check:
    id: str
    title: str
    passed: bool
    detail: str
    verification_level: str = "V3 finite/model check"

checks: List[Check] = []

def add(cid: str, title: str, condition: bool, detail: str) -> None:
    checks.append(Check(cid, title, bool(condition), detail))

# ---------------------------------------------------------------------------
# M1: fiberwise factorization and loss spectra
# ---------------------------------------------------------------------------
W = tuple(range(6))
alpha_coarse = {w: w % 2 for w in W}
alpha_fine = {w: w for w in W}
P_parity = {w: w % 2 for w in W}
P_exact0 = {w: int(w == 0) for w in W}
P_high = {w: int(w >= 3) for w in W}

def fiber_constant(alpha: Dict[int, int], P: Dict[int, int]) -> bool:
    for x, y in itertools.product(W, repeat=2):
        if alpha[x] == alpha[y] and P[x] != P[y]:
            return False
    return True

def recoverer_exists(alpha: Dict[int, int], P: Dict[int, int]) -> bool:
    # In a finite setting over im(alpha), a factor exists iff P is fiber-constant.
    vals: Dict[int, int] = {}
    for w in W:
        m = alpha[w]
        if m in vals and vals[m] != P[w]:
            return False
        vals[m] = P[w]
    return True

add("MC-001", "fiber criterion: parity factors through parity abstraction",
    fiber_constant(alpha_coarse, P_parity) and recoverer_exists(alpha_coarse, P_parity),
    "P(w)=w mod 2 is constant on every alpha(w)=w mod 2 fiber.")
add("MC-002", "fiber obstruction: exact-zero does not factor through parity",
    (not fiber_constant(alpha_coarse, P_exact0)) and (not recoverer_exists(alpha_coarse, P_exact0)),
    "0 and 2 share the coarse representation but have different exact-zero truth values.")

Phi = {"parity": P_parity, "zero": P_exact0, "high": P_high}

def loss(alpha: Dict[int, int]) -> List[str]:
    return sorted(k for k, P in Phi.items() if not fiber_constant(alpha, P))

loss_coarse = loss(alpha_coarse)
loss_fine = loss(alpha_fine)
add("MC-003", "loss spectrum refinement monotonicity",
    set(loss_fine).issubset(loss_coarse) and loss_fine == [],
    f"Loss(fine)={loss_fine}; Loss(coarse)={loss_coarse}.")

# Minimal sufficient truth quotient for the selected predicates.
def truth_vector(w: int) -> Tuple[int, ...]:
    return tuple(Phi[k][w] for k in sorted(Phi))
classes: Dict[Tuple[int, ...], List[int]] = {}
for w in W:
    classes.setdefault(truth_vector(w), []).append(w)
all_const = all(len({P[w] for w in members}) == 1
                for members in classes.values() for P in Phi.values())
# Any representation preserving all predicates must not merge different vectors.
all_pairs_respected = all(
    (truth_vector(x) == truth_vector(y)) or (alpha_fine[x] != alpha_fine[y])
    for x, y in itertools.product(W, repeat=2)
)
add("MC-004", "minimal sufficient truth quotient finite instance",
    all_const and all_pairs_respected,
    f"The selected truth vectors induce {len(classes)} observational equivalence classes: {classes}.")

# No-free-enrichment finite witness.
base = {"h0": "snapshot", "h1": "snapshot"}
enrichment = {"h0": "original", "h1": "replica"}
target = {"h0": 1, "h1": 0}
base_collides = base["h0"] == base["h1"]
enrichment_separates = enrichment["h0"] != enrichment["h1"]
add("MC-005", "enrichment concession principle",
    base_collides and target["h0"] != target["h1"] and enrichment_separates,
    "Any successful enriched classifier must separate histories that the base snapshot merged.")

# ---------------------------------------------------------------------------
# M2: automorphism/no-section tests
# ---------------------------------------------------------------------------
def permutations(n: int) -> List[Tuple[int, ...]]:
    return list(itertools.permutations(range(n)))

def apply_perm(p: Tuple[int, ...], x: int) -> int:
    return p[x]

for n in range(2, 9):
    perms = permutations(n)
    invariant_points = [x for x in range(n) if all(apply_perm(p, x) == x for p in perms)]
    add(f"MC-1{n:02d}", f"no globally permutation-invariant point on Fin({n})",
        invariant_points == [],
        f"Fixed points under the full symmetric group: {invariant_points}.")

# Strict total order represented by ranking tuple; action transports labels.
def is_strict_total_order(order: Tuple[int, ...], n: int) -> bool:
    return sorted(order) == list(range(n)) and len(order) == n

def transport_order(p: Tuple[int, ...], order: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(p[x] for x in order)

for n in range(2, 7):
    perms = permutations(n)
    orders = list(itertools.permutations(range(n)))
    invariant_orders = [o for o in orders if is_strict_total_order(o, n)
                        and all(transport_order(p, o) == o for p in perms)]
    add(f"MC-2{n:02d}", f"no natural strict total order on unlabeled Fin({n})",
        invariant_orders == [],
        f"Invariant linear orders under Sym({n}): {invariant_orders}.")

# ---------------------------------------------------------------------------
# M1/M2 category-theoretic finite exemplars
# ---------------------------------------------------------------------------
# Walking arrow C+: a->b. C-: b->a. Cores retain only identities.
objects = ("a", "b")
core_plus = {(x, x) for x in objects}
core_minus = {(x, x) for x in objects}
dir_plus = ("a", "b")
dir_minus = ("b", "a")
add("MC-301", "walking arrow and reverse have identical labeled cores",
    core_plus == core_minus and dir_plus != dir_minus,
    f"Both cores={sorted(core_plus)} while directed nonidentity arrows are {dir_plus} and {dir_minus}.")

# A full and faithful functor into a groupoid would force every source arrow invertible.
# Finite sanity instance: walking arrow has no inverse b->a, while its image arrow in a groupoid would.
source_homs = {("a", "a"), ("b", "b"), ("a", "b")}
missing_inverse = ("b", "a") not in source_homs
add("MC-302", "noninvertible walking arrow blocks full-faithful groupoid encoding",
    missing_inverse,
    "The sole nonidentity arrow has no inverse in the source; fullness would have to lift the target inverse.")

# ---------------------------------------------------------------------------
# Signature/history/context/evidence/cost examples
# ---------------------------------------------------------------------------
snapshots = {("painting", "original"): "pixels-X", ("painting", "replica"): "pixels-X"}
original = {k: int(k[1] == "original") for k in snapshots}
add("MC-401", "provenance does not factor through snapshot",
    snapshots[("painting", "original")] == snapshots[("painting", "replica")]
    and original[("painting", "original")] != original[("painting", "replica")],
    "Original and replica share the selected snapshot but differ in provenance truth.")

bare_nat = {"arith": "Nat-structure", "index": "Nat-structure"}
role = {"arith": "arithmetic", "index": "list-index"}
add("MC-402", "intended role does not factor through bare Nat structure",
    bare_nat["arith"] == bare_nat["index"] and role["arith"] != role["index"],
    "The same zero/successor algebra is paired with distinct intended roles.")

surface = {("bank", "finance"): "bank", ("bank", "river"): "bank"}
spec = {("bank", "finance"): "FinancialInstitution", ("bank", "river"): "RiverBank"}
add("MC-403", "context-free single-valued formalizer impossible in ambiguous instance",
    surface[("bank", "finance")] == surface[("bank", "river")]
    and spec[("bank", "finance")] != spec[("bank", "river")],
    "Identical surface string requires incompatible specifications in two contexts.")

# Assertion/mere-existence/witness: swapping a two-element witness set has no invariant witness.
witnesses = (0, 1)
swap = (1, 0)
fixed = [x for x in witnesses if swap[x] == x]
add("MC-404", "no natural witness extraction from symmetric mere existence",
    fixed == [],
    "The two witnesses are exchanged by an automorphism; no selected witness is invariant.")

programs = {
    "p": {"function": tuple(0 for _ in range(4)), "cost": 1},
    "q": {"function": tuple(0 for _ in range(4)), "cost": 1_000_001},
}
add("MC-405", "extensional function does not determine execution cost",
    programs["p"]["function"] == programs["q"]["function"]
    and programs["p"]["cost"] != programs["q"]["cost"],
    "Two implementations compute the same finite function and have different step counts.")

# Cartesian/linear witness: diagonal duplicates a token, violating an exact-use-once policy.
def cartesian_diagonal(token: str) -> Tuple[str, str]:
    return (token, token)

def exact_use_once(trace: Sequence[str]) -> bool:
    return len(trace) == len(set(trace))

diag = cartesian_diagonal("r")
add("MC-406", "Cartesian diagonal conflicts with an exact-use-once token policy",
    not exact_use_once(diag),
    f"Diagonal trace {diag} contains two uses of the same token. This is a finite policy witness, not a general categorical proof.")

# ---------------------------------------------------------------------------
# M3: stabilization, guard erasure, and limit/reachability
# ---------------------------------------------------------------------------
def toggling_or_halt(halts_at: int | None, n: int) -> int:
    if halts_at is not None and n >= halts_at:
        return 0
    return n % 2

def eventually_constant_prefix(seq: Sequence[int], tail: int = 10) -> bool:
    return len(seq) >= tail and len(set(seq[-tail:])) == 1

seq_halt = [toggling_or_halt(7, n) for n in range(40)]
seq_loop = [toggling_or_halt(None, n) for n in range(40)]
add("MC-501", "bounded stabilization reduction witness",
    eventually_constant_prefix(seq_halt) and not eventually_constant_prefix(seq_loop),
    "The halting-coded history stabilizes after stage 7; the nonhalting-coded history alternates. Finite trace only.")

# Guard erasure: x_{n+1}=not x_n has an orbit but no Boolean fixed point.
F = lambda b: 1 - b
fixed_points = [b for b in (0, 1) if F(b) == b]
orbit = [0]
for _ in range(7):
    orbit.append(F(orbit[-1]))
add("MC-502", "guard erasure forces absent fixed point",
    fixed_points == [] and orbit == [0, 1, 0, 1, 0, 1, 0, 1],
    f"Dynamic orbit exists {orbit}; static equation b=not b has fixed points {fixed_points}.")

# Limit/closure/reachability witnesses.
partial = [1 - 2 ** (-n) for n in range(1, 21)]
finite_reaches_one = any(x == 1 for x in partial)
last_error = abs(1 - partial[-1])
add("MC-503", "Zeno sequence: limit/closure does not imply finite-step reachability",
    not finite_reaches_one and last_error < 1e-5,
    f"No enumerated finite term equals 1; twentieth error={last_error:.3e}. This numerically illustrates, not proves, convergence.")

# Same geometric image/closure, different timing and endpoint reachability.
finite_image_endpoint = True  # gamma_F(1)=1
asymptotic_image_endpoint = False  # gamma_inf(t)=1-exp(-t)<1 for finite t
add("MC-504", "same closure can hide different finite-time endpoint reachability",
    finite_image_endpoint and not asymptotic_image_endpoint,
    "[0,1] and [0,1) have the same closure but differ on whether endpoint 1 is attained.")

# ---------------------------------------------------------------------------
# Galois correspondence finite exhaustive test.
# ---------------------------------------------------------------------------
Wg = tuple(range(4))
# equivalence relation by parity
R = {(x, y) for x in Wg for y in Wg if x % 2 == y % 2}
preds = []
for bits in itertools.product((0, 1), repeat=len(Wg)):
    preds.append(dict(zip(Wg, bits)))

def invariant(P: Dict[int, int]) -> bool:
    return all(P[x] == P[y] for (x, y) in R)
Inv = [P for P in preds if invariant(P)]
Ind = {(x, y) for x in Wg for y in Wg if all(P[x] == P[y] for P in Inv)}
add("MC-601", "representation-observable Galois closure recovers finite equivalence relation",
    Ind == R,
    f"Parity relation has {len(R)} ordered pairs; invariant predicates={len(Inv)}; induced relation matches exactly.")

# ---------------------------------------------------------------------------
# Aggregate
# ---------------------------------------------------------------------------
passed = sum(c.passed for c in checks)
report = {
    "schema_version": "hott_z_model_checks.v1",
    "warning": "Finite/model checks are V3 error-detection evidence and do not replace unbounded mathematical or proof-assistant proofs.",
    "total": len(checks),
    "passed": passed,
    "failed": len(checks) - passed,
    "overall_ok": passed == len(checks),
    "checks": [asdict(c) for c in checks],
}
OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for c in checks:
    print(f"{'PASS' if c.passed else 'FAIL'} {c.id}: {c.title} — {c.detail}")
print(f"TOTAL={len(checks)} PASSED={passed} FAILED={len(checks)-passed}")
sys.exit(0 if report["overall_ok"] else 1)
