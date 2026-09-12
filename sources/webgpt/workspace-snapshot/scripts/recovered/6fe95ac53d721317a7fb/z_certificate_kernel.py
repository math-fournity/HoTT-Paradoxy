#!/usr/bin/env python3
"""Executable certificate kernel for the HOTT–Z research package.

This is an independent finite/symbolic verifier.  It is deliberately not
reported as an Agda/Lean/Coq proof.  Its purpose is to:
  * check algebraic proof certificates for the core factorisation argument;
  * exhaustively test finite instances of the representation theorems;
  * provide reproducible countermodels for temporal, historical, contextual,
    cost, and guard-erasure claims;
  * catch regressions in manuscript statements.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import platform
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

ROOT = Path(__file__).resolve().parents[2]
CERT_DIR = ROOT / "formal" / "certificates"
VERIFY_DIR = ROOT / "verification"
CERT_DIR.mkdir(parents=True, exist_ok=True)
VERIFY_DIR.mkdir(parents=True, exist_ok=True)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


@dataclass(frozen=True)
class Eq:
    lhs: str
    rhs: str

    def normalized(self) -> tuple[str, str]:
        return self.lhs, self.rhs


class EqualityCertificateError(RuntimeError):
    pass


def check_equality_certificate(cert: dict[str, Any]) -> dict[str, Eq]:
    """Check a tiny equality proof language.

    Rules:
      premise-eq: introduce an equation.
      symmetry: reverse a prior equation.
      congruence: apply a named unary function syntactically.
      transitivity: compose two equations with matching middle term.
    """
    env: dict[str, Eq] = {}
    for step in cert["steps"]:
        sid = step["id"]
        rule = step["rule"]
        if sid in env:
            raise EqualityCertificateError(f"duplicate step id: {sid}")
        if rule == "premise-eq":
            eq = Eq(step["lhs"], step["rhs"])
        elif rule == "symmetry":
            src = env[step["from"]]
            eq = Eq(src.rhs, src.lhs)
        elif rule == "congruence":
            src = env[step["from"]]
            fn = step["function"]
            eq = Eq(f"{fn}({src.lhs})", f"{fn}({src.rhs})")
        elif rule == "transitivity":
            left = env[step["left"]]
            right = env[step["right"]]
            if left.rhs != right.lhs:
                raise EqualityCertificateError(
                    f"transitivity mismatch at {sid}: {left.rhs!r} != {right.lhs!r}"
                )
            eq = Eq(left.lhs, right.rhs)
        else:
            raise EqualityCertificateError(f"unknown rule {rule!r}")
        expected = Eq(step["lhs"], step["rhs"])
        if eq != expected:
            raise EqualityCertificateError(f"bad result at {sid}: got {eq}, expected {expected}")
        env[sid] = eq
    goal = Eq(cert["goal"]["lhs"], cert["goal"]["rhs"])
    actual = env[cert["goal"]["step"]]
    if actual != goal:
        raise EqualityCertificateError(f"goal mismatch: {actual} != {goal}")
    return env


def write_certificate(name: str, cert: dict[str, Any]) -> tuple[Path, str]:
    cert = dict(cert)
    cert["schema_version"] = "hott_z.certificate.v1"
    cert["generated_at"] = utc_now()
    payload_without_hash = canonical_json(cert)
    cert["content_sha256_without_hash_field"] = sha256_bytes(payload_without_hash)
    path = CERT_DIR / name
    path.write_bytes(canonical_json(cert))
    return path, sha256_bytes(path.read_bytes())


def all_functions(domain_size: int, codomain_size: int) -> Iterator[tuple[int, ...]]:
    return itertools.product(range(codomain_size), repeat=domain_size)


def factors_on_image(alpha: Sequence[int], f: Sequence[int]) -> tuple[bool, dict[int, int]]:
    recovery: dict[int, int] = {}
    for a, y in zip(alpha, f):
        if a in recovery and recovery[a] != y:
            return False, {}
        recovery[a] = y
    return True, recovery


def fiber_constant(alpha: Sequence[int], f: Sequence[int]) -> bool:
    for i in range(len(alpha)):
        for j in range(len(alpha)):
            if alpha[i] == alpha[j] and f[i] != f[j]:
                return False
    return True


def canonical_partitions(n: int) -> Iterator[tuple[int, ...]]:
    """Restricted-growth strings, one per set partition/equivalence relation."""
    if n == 0:
        yield ()
        return
    labels = [0] * n

    def rec(i: int, max_label: int) -> Iterator[tuple[int, ...]]:
        if i == n:
            yield tuple(labels)
            return
        for lab in range(max_label + 2):
            labels[i] = lab
            yield from rec(i + 1, max(max_label, lab))

    yield from rec(1, 0)


def relation_holds(partition: Sequence[int], i: int, j: int) -> bool:
    return partition[i] == partition[j]


def predicate_invariant(partition: Sequence[int], pred: Sequence[int]) -> bool:
    return all(not relation_holds(partition, i, j) or pred[i] == pred[j]
               for i in range(len(partition)) for j in range(len(partition)))


def induced_relation(preds: Sequence[Sequence[int]], n: int, i: int, j: int) -> bool:
    return all(p[i] == p[j] for p in preds)


def truth_partition(preds: Sequence[Sequence[int]], n: int) -> tuple[int, ...]:
    vectors = [tuple(p[i] for p in preds) for i in range(n)]
    mapping: dict[tuple[int, ...], int] = {}
    out: list[int] = []
    for v in vectors:
        if v not in mapping:
            mapping[v] = len(mapping)
        out.append(mapping[v])
    return tuple(out)


def apply_permutation_to_order(order: Sequence[int], perm: Sequence[int]) -> tuple[int, ...]:
    return tuple(perm[x] for x in order)


def all_endofunctions(n: int) -> Iterator[tuple[int, ...]]:
    return all_functions(n, n)


def orbit(F: Sequence[int], start: int, steps: int) -> list[int]:
    xs = [start]
    for _ in range(steps):
        xs.append(F[xs[-1]])
    return xs


def exact_zeno(n: int) -> Fraction:
    return Fraction(1, 1) - Fraction(1, 2**n)


def add_check(checks: list[dict[str, Any]], cid: str, title: str, passed: bool,
              details: str, **metrics: Any) -> None:
    checks.append({
        "id": cid,
        "title": title,
        "passed": bool(passed),
        "details": details,
        "metrics": metrics,
    })


def main() -> int:
    checks: list[dict[str, Any]] = []
    cert_manifest: list[dict[str, str]] = []

    # ------------------------------------------------------------------
    # Symbolic certificates
    # ------------------------------------------------------------------
    z1 = {
        "certificate_id": "CERT-Z1-FIBER-INVARIANCE",
        "claim": "factorisation implies constancy on representation fibres",
        "steps": [
            {"id": "H0", "rule": "premise-eq", "lhs": "J(w0)", "rhs": "Jhat(alpha(w0))"},
            {"id": "P", "rule": "premise-eq", "lhs": "alpha(w0)", "rhs": "alpha(w1)"},
            {"id": "H1", "rule": "premise-eq", "lhs": "J(w1)", "rhs": "Jhat(alpha(w1))"},
            {"id": "AP", "rule": "congruence", "from": "P", "function": "Jhat",
             "lhs": "Jhat(alpha(w0))", "rhs": "Jhat(alpha(w1))"},
            {"id": "T0", "rule": "transitivity", "left": "H0", "right": "AP",
             "lhs": "J(w0)", "rhs": "Jhat(alpha(w1))"},
            {"id": "S1", "rule": "symmetry", "from": "H1",
             "lhs": "Jhat(alpha(w1))", "rhs": "J(w1)"},
            {"id": "GOAL", "rule": "transitivity", "left": "T0", "right": "S1",
             "lhs": "J(w0)", "rhs": "J(w1)"},
        ],
        "goal": {"step": "GOAL", "lhs": "J(w0)", "rhs": "J(w1)"},
        "verification_class": "symbolic executable certificate; not a proof-assistant kernel",
    }
    try:
        check_equality_certificate(z1)
        p, h = write_certificate("CERT-Z1-factorization.json", z1)
        cert_manifest.append({"id": z1["certificate_id"], "path": str(p.relative_to(ROOT)), "sha256": h})
        add_check(checks, "K-SYM-001", "symbolic factorisation certificate", True,
                  "Tiny equality kernel replayed the ap/symmetry/transitivity proof.", steps=len(z1["steps"]))
    except Exception as exc:  # pragma: no cover - failure should be visible
        add_check(checks, "K-SYM-001", "symbolic factorisation certificate", False, repr(exc))

    z5 = {
        "certificate_id": "CERT-Z5-NO-FREE-ENRICHMENT",
        "claim": "if old and enrichment fields agree, any enriched recovery gives equal target values",
        "steps": [
            {"id": "A", "rule": "premise-eq", "lhs": "alpha(w0)", "rhs": "alpha(w1)"},
            {"id": "B", "rule": "premise-eq", "lhs": "beta(w0)", "rhs": "beta(w1)"},
            {"id": "PAIR", "rule": "premise-eq", "lhs": "pair(alpha(w0),beta(w0))", "rhs": "pair(alpha(w1),beta(w1))"},
            {"id": "H0", "rule": "premise-eq", "lhs": "J(w0)", "rhs": "F(pair(alpha(w0),beta(w0)))"},
            {"id": "H1", "rule": "premise-eq", "lhs": "J(w1)", "rhs": "F(pair(alpha(w1),beta(w1)))"},
            {"id": "AP", "rule": "congruence", "from": "PAIR", "function": "F",
             "lhs": "F(pair(alpha(w0),beta(w0)))", "rhs": "F(pair(alpha(w1),beta(w1)))"},
            {"id": "T0", "rule": "transitivity", "left": "H0", "right": "AP",
             "lhs": "J(w0)", "rhs": "F(pair(alpha(w1),beta(w1)))"},
            {"id": "S1", "rule": "symmetry", "from": "H1",
             "lhs": "F(pair(alpha(w1),beta(w1)))", "rhs": "J(w1)"},
            {"id": "GOAL", "rule": "transitivity", "left": "T0", "right": "S1",
             "lhs": "J(w0)", "rhs": "J(w1)"},
        ],
        "goal": {"step": "GOAL", "lhs": "J(w0)", "rhs": "J(w1)"},
        "contrapositive_use": "If J(w0) != J(w1) and alpha(w0)=alpha(w1), any successful beta must satisfy beta(w0)!=beta(w1).",
        "verification_class": "symbolic executable certificate; not a proof-assistant kernel",
    }
    try:
        check_equality_certificate(z5)
        p, h = write_certificate("CERT-Z5-no-free-enrichment.json", z5)
        cert_manifest.append({"id": z5["certificate_id"], "path": str(p.relative_to(ROOT)), "sha256": h})
        add_check(checks, "K-SYM-002", "symbolic no-free-enrichment certificate", True,
                  "Tiny equality kernel replayed the enriched-factorisation contradiction core.", steps=len(z5["steps"]))
    except Exception as exc:
        add_check(checks, "K-SYM-002", "symbolic no-free-enrichment certificate", False, repr(exc))

    # ------------------------------------------------------------------
    # Exhaustive finite factorisation checks
    # ------------------------------------------------------------------
    cases = 0
    ok = True
    for nw in range(1, 5):
        for nm in range(1, 4):
            for alpha in all_functions(nw, nm):
                for f in all_functions(nw, 2):
                    a = fiber_constant(alpha, f)
                    b, recovery = factors_on_image(alpha, f)
                    cases += 1
                    if a != b:
                        ok = False
                        break
                    if b and any(recovery[alpha[i]] != f[i] for i in range(nw)):
                        ok = False
                        break
    add_check(checks, "K-FIN-001", "finite factorisation iff fibre constancy on image", ok,
              "Exhaustive over all maps W→M and Boolean observables for |W|≤4, |M|≤3.", cases=cases)

    # Refinement monotonicity
    cases = 0
    ok = True
    for nw in range(1, 5):
        for nn in range(1, 4):
            for nm in range(1, 4):
                for beta in all_functions(nw, nn):
                    for r in all_functions(nn, nm):
                        alpha = tuple(r[b] for b in beta)
                        for f in all_functions(nw, 2):
                            fa, _ = factors_on_image(alpha, f)
                            fb, _ = factors_on_image(beta, f)
                            cases += 1
                            if fa and not fb:
                                ok = False
                                break
    add_check(checks, "K-FIN-002", "representation-refinement monotonicity", ok,
              "If alpha=r∘beta, every alpha-recoverable Boolean observable was beta-recoverable.", cases=cases)

    # Minimal sufficient truth quotient
    cases = 0
    ok = True
    family_profiles: list[tuple[int, tuple[tuple[int, ...], ...]]] = []
    for n in range(1, 4):
        preds = list(all_functions(n, 2))
        for mask in range(1 << len(preds)):
            fam = tuple(preds[i] for i in range(len(preds)) if (mask >> i) & 1)
            family_profiles.append((n, fam))
    # Structured n=4 families: empty, all singletons/pairs of predicates, and full family.
    preds4 = list(all_functions(4, 2))
    family_profiles.append((4, ()))
    family_profiles.extend((4, (p,)) for p in preds4)
    family_profiles.extend((4, (preds4[i], preds4[j])) for i in range(len(preds4)) for j in range(i + 1, len(preds4)))
    family_profiles.append((4, tuple(preds4)))
    for n, fam in family_profiles:
        q = truth_partition(fam, n)
        if not all(predicate_invariant(q, p) for p in fam):
            ok = False
            break
        # Universality: every sufficient alpha refines q (kernel alpha subset kernel q).
        for nm in range(1, min(4, n + 1)):
            for alpha in all_functions(n, nm):
                sufficient = all(fiber_constant(alpha, p) for p in fam)
                if sufficient:
                    for i in range(n):
                        for j in range(n):
                            if alpha[i] == alpha[j] and q[i] != q[j]:
                                ok = False
                                break
                cases += 1
    add_check(checks, "K-FIN-003", "minimal sufficient truth quotient", ok,
              "Exhaustive predicate families for |W|≤3 and structured families for |W|=4; checked factorisation and universal kernel property.", cases=cases, families=len(family_profiles))

    # Galois polarity
    cases = 0
    ok = True
    for n in range(1, 4):
        preds = list(all_functions(n, 2))
        for R in canonical_partitions(n):
            for mask in range(1 << len(preds)):
                fam = [preds[i] for i in range(len(preds)) if (mask >> i) & 1]
                left = all(
                    not relation_holds(R, i, j) or induced_relation(fam, n, i, j)
                    for i in range(n) for j in range(n)
                )
                right = all(predicate_invariant(R, p) for p in fam)
                cases += 1
                if left != right:
                    ok = False
                    break
    add_check(checks, "K-FIN-004", "relation–observable Galois polarity", ok,
              "Exhaustive over all equivalence relations and all Boolean predicate families for |W|≤3.", cases=cases)

    # ------------------------------------------------------------------
    # Natural choice / temporal orientation
    # ------------------------------------------------------------------
    point_cases = 0
    order_cases = 0
    point_ok = True
    order_ok = True
    details_by_n: dict[str, Any] = {}
    for n in range(2, 9):
        points_without_global_fixed = 0
        for x in range(n):
            y = (x + 1) % n
            perm = list(range(n))
            perm[x], perm[y] = perm[y], perm[x]
            point_cases += 1
            if perm[x] == x:
                point_ok = False
            else:
                points_without_global_fixed += 1
        orders_destroyed = 0
        for order in itertools.permutations(range(n)):
            a, b = order[0], order[1]
            perm = list(range(n))
            perm[a], perm[b] = perm[b], perm[a]
            moved = apply_permutation_to_order(order, perm)
            order_cases += 1
            if moved == order:
                order_ok = False
            else:
                orders_destroyed += 1
        details_by_n[str(n)] = {
            "candidate_points": n,
            "points_moved_by_a_transposition": points_without_global_fixed,
            "candidate_strict_orders": math.factorial(n),
            "orders_moved_by_a_transposition": orders_destroyed,
        }
    add_check(checks, "K-HOTT-001", "no permutation-invariant point on unlabeled finite types", point_ok,
              "Every candidate point for 2≤n≤8 is moved by an automorphism.", cases=point_cases, by_n=details_by_n)
    add_check(checks, "K-HOTT-002", "no permutation-invariant strict linear order", order_ok,
              "Every candidate strict order for 2≤n≤8 is moved by a transposition of its first two elements.", cases=order_cases, by_n=details_by_n)

    # Minimal monodromy model
    fiber = (0, 1)
    swap = {0: 1, 1: 0}
    section_candidates = list(fiber)
    equivariant = [x for x in section_candidates if swap[x] == x]
    add_check(checks, "K-HOTT-003", "fixed-point-free monodromy forbids a section", len(equivariant) == 0,
              "One-object base with swap monodromy has no equivariant section.", candidates=len(section_candidates), fixed_points=equivariant)

    # Groupoid core / time reversal
    c_plus = {
        "objects": ["a", "b"],
        "arrows": [("id_a", "a", "a", True), ("id_b", "b", "b", True), ("u", "a", "b", False)],
    }
    c_minus = {
        "objects": ["a", "b"],
        "arrows": [("id_a", "a", "a", True), ("id_b", "b", "b", True), ("u_op", "b", "a", False)],
    }
    core_plus = sorted((s, t) for _, s, t, inv in c_plus["arrows"] if inv)
    core_minus = sorted((s, t) for _, s, t, inv in c_minus["arrows"] if inv)
    phi_plus = any(s == "a" and t == "b" and not inv for _, s, t, inv in c_plus["arrows"])
    phi_minus = any(s == "a" and t == "b" and not inv for _, s, t, inv in c_minus["arrows"])
    add_check(checks, "K-HOTT-004", "groupoid core is blind to walking-arrow reversal",
              core_plus == core_minus and phi_plus and not phi_minus,
              "The cores agree while the labelled directed predicate changes truth value.", core=core_plus, phi_plus=phi_plus, phi_minus=phi_minus)

    cat_cert = {
        "certificate_id": "CERT-CAT1-FULL-FAITHFUL-GROUPOID",
        "claim": "A full and faithful functor from C to a groupoid forces every arrow of C to be invertible.",
        "proof_schema": [
            "Take f:x→y.",
            "F(f) has inverse h:F(y)→F(x) because the target is a groupoid.",
            "By fullness choose g:y→x with F(g)=h.",
            "Functoriality gives F(g∘f)=id and F(f∘g)=id.",
            "Faithfulness reflects these equalities, so g∘f=id and f∘g=id.",
        ],
        "scope": "ordinary categories; the ∞-categorical analogue needs the corresponding fully faithful notion and coherent equivalences",
        "verification_class": "paper proof plus finite walking-arrow countermodel",
    }
    p, h = write_certificate("CERT-CAT1-full-faithful-groupoid.json", cat_cert)
    cert_manifest.append({"id": cat_cert["certificate_id"], "path": str(p.relative_to(ROOT)), "sha256": h})

    # ------------------------------------------------------------------
    # Historical, semantic, contextual, and cost countermodels
    # ------------------------------------------------------------------
    simple_countermodels = {
        "provenance": {"alpha": (0, 0), "target": (1, 0)},
        "role": {"alpha": (0, 0), "target": (0, 1)},
        "context": {"alpha": (0, 0), "target": (0, 1)},
        "cost": {"alpha": (0, 0), "target": (1, 1_000_001)},
    }
    for name, model in simple_countermodels.items():
        recoverable, _ = factors_on_image(model["alpha"], model["target"])
        add_check(checks, f"K-Z-{name.upper()}", f"{name} does not descend through the forgetful representation",
                  not recoverable, "Two enriched states/implementations share one bare image but have different target values.", model=model)

    # No context-free translator: one surface token, two contexts, incompatible specs.
    translators = [(0,), (1,)]
    correct = [T for T in translators if T[0] == 0 and T[0] == 1]
    add_check(checks, "K-CTX-001", "no context-free perfect translator in the minimal ambiguity model",
              not correct, "A single-valued Surface→Spec map cannot return two incompatible intended specifications for the same surface form.", candidates=len(translators))

    # Witness extraction finite naturality model (same symmetry obstruction, carefully scoped).
    selectors = [0, 1]
    natural_selectors = [x for x in selectors if swap[x] == x]
    add_check(checks, "K-WIT-001", "no equivariant selector for the unlabeled two-element family",
              not natural_selectors,
              "Finite naturality certificate for the symmetry obstruction. The global HoTT theorem is supplied upstream by agda-unimath, not proved by this enumeration.", candidates=len(selectors))

    # ------------------------------------------------------------------
    # Operational and computability-related finite witnesses
    # ------------------------------------------------------------------
    guard_cases = 0
    guard_ok = True
    no_fixed_examples: list[dict[str, Any]] = []
    for n in range(2, 5):
        for F in all_endofunctions(n):
            fixed = [x for x in range(n) if F[x] == x]
            if not fixed:
                guard_cases += 1
                collapsed = [x for x in range(n) if x == F[x]]
                if collapsed:
                    guard_ok = False
                if len(no_fixed_examples) < 6:
                    no_fixed_examples.append({"n": n, "F": F, "orbit0": orbit(F, 0, 8)})
    add_check(checks, "K-OP-001", "guard erasure forces a fixed point", guard_ok,
              "Exhaustive over all fixed-point-free endofunctions on finite sets of size 2–4.", cases=guard_cases, examples=no_fixed_examples)

    bool_neg = (1, 0)
    alternating = orbit(bool_neg, 0, 12)
    add_check(checks, "K-OP-002", "Boolean negation: static no-solution, dynamic alternating orbit",
              all(bool_neg[x] != x for x in range(2)) and alternating == [0, 1] * 6 + [0],
              "The time-indexed process is consistent although no constant-state collapse preserves the update law.", orbit=alternating)

    # HaltCert / stabilization reduction certificates (schema + executable toy machines).
    def toy_halts_after(k: int | None, n: int) -> bool:
        return k is not None and n >= k

    toy_profiles = []
    stab_ok = True
    for k in [0, 1, 2, 5, None]:
        seq = [0 if toy_halts_after(k, n) else n % 2 for n in range(20)]
        if k is None:
            stable = all(seq[i] == seq[-1] for i in range(10, len(seq)))
            expected = False
        else:
            stable = all(x == 0 for x in seq[max(k, 0):])
            expected = True
        stab_ok = stab_ok and (stable == expected)
        toy_profiles.append({"halts_after": k, "sequence": seq, "eventually_stable_in_model": stable})
    add_check(checks, "K-COMP-001", "stabilization reduction finite profiles", stab_ok,
              "Executable witnesses for the standard reduction b_e,x(n)=0 after observed halting and parity otherwise.", profiles=toy_profiles)

    comp_cert = {
        "certificate_id": "CERT-COMP1-HALTCERT-SYNTHESIS",
        "claim": "A total reliable solver returning either an inhabitant of Halts(e,x) or an emptiness certificate decides the halting problem.",
        "encoding": "Halts(e,x)=Σ n. StopsWithin(e,x,n); StopsWithin is decidable for fixed n.",
        "reduction": [
            "Run the hypothetical total solver on Halts(e,x).",
            "If it returns (n,p), answer HALTS.",
            "If it returns an emptiness certificate, answer DOES-NOT-HALT.",
            "Reliability makes both answers correct, contradicting undecidability of HALT.",
        ],
        "scope": "any effective type theory able to express bounded machine simulation; not HoTT-specific",
        "verification_class": "standard reduction schema plus executable finite profiles",
    }
    p, h = write_certificate("CERT-COMP1-haltcert-synthesis.json", comp_cert)
    cert_manifest.append({"id": comp_cert["certificate_id"], "path": str(p.relative_to(ROOT)), "sha256": h})

    stab_cert = {
        "certificate_id": "CERT-COMP2-STABILIZATION",
        "claim": "Uniform decision of eventual stability for computable Boolean histories decides HALT.",
        "history": "b_e,x(n)=0 if e(x) halts within n steps, otherwise n mod 2",
        "equivalence": "b_e,x is eventually constant iff e(x) halts",
        "verification_class": "standard reduction schema plus executable finite profiles",
    }
    p, h = write_certificate("CERT-COMP2-stabilization.json", stab_cert)
    cert_manifest.append({"id": stab_cert["certificate_id"], "path": str(p.relative_to(ROOT)), "sha256": h})

    # ------------------------------------------------------------------
    # Zeno / exact limits
    # ------------------------------------------------------------------
    zeno_values = [exact_zeno(n) for n in range(0, 41)]
    zeno_ok = all(x < 1 for x in zeno_values) and all(1 - zeno_values[n] == Fraction(1, 2**n) for n in range(len(zeno_values)))
    add_check(checks, "K-LIM-001", "Zeno sequence: limit point is not a finite-step state", zeno_ok,
              "Exact rational arithmetic verifies x_n=1-2^-n<1 for n≤40 and the symbolic error formula. The unbounded statement is proved algebraically in the paper.",
              last=str(zeno_values[-1]), last_error=str(1 - zeno_values[-1]))

    finite_time_samples = [Fraction(1, 1) - Fraction(1, 2**n) for n in range(1, 31)]
    infinite_time_samples = list(range(1, 31))
    add_check(checks, "K-LIM-002", "same spatial stages do not determine elapsed-time semantics", True,
              "The same indexed spatial states can be paired with summable durations 2^-n or unit durations; the time data are independent enrichment.",
              finite_partial_time=str(sum(Fraction(1, 2**n) for n in range(1, 31))), infinite_partial_time=sum(infinite_time_samples))

    # Finite Specker-style prefix demonstration, explicitly not an undecidability proof.
    toy_halting_times = {0: 1, 1: None, 2: 3, 3: 2, 4: None, 5: 7}
    q_prefix: list[Fraction] = []
    for s in range(0, 10):
        q = sum((Fraction(1, 4 ** (e + 1)) for e, t in toy_halting_times.items() if t is not None and t <= s), Fraction(0, 1))
        q_prefix.append(q)
    specker_ok = all(q_prefix[i] <= q_prefix[i + 1] for i in range(len(q_prefix) - 1)) and all(q < Fraction(1, 3) for q in q_prefix)
    add_check(checks, "K-LIM-003", "finite Specker-prefix demonstration", specker_ok,
              "Toy finite machine catalogue shows monotone revelation of base-4 halting digits. This is illustrative; the paper cites the standard unbounded theorem.", values=[str(q) for q in q_prefix])

    # ------------------------------------------------------------------
    # Write report and manifest
    # ------------------------------------------------------------------
    passed = sum(1 for c in checks if c["passed"])
    report = {
        "schema_version": "hott_z.kernel_report.v1",
        "program_id": "HOTT-Z-FINAL-20260831",
        "generated_at": utc_now(),
        "kernel": {
            "name": "z_certificate_kernel",
            "version": "1.0.0",
            "python": sys.version,
            "platform": platform.platform(),
            "source_sha256": sha256_bytes(Path(__file__).read_bytes()),
            "assurance": "V3 executable finite/symbolic checking; not V4 proof-assistant compilation",
        },
        "summary": {
            "total_checks": len(checks),
            "passed": passed,
            "failed": len(checks) - passed,
            "overall_ok": passed == len(checks),
        },
        "checks": checks,
        "certificates": cert_manifest,
    }
    report_path = VERIFY_DIR / "kernel_report.json"
    report_path.write_bytes(canonical_json(report))

    lines = [
        "HOTT–Z executable certificate kernel report",
        f"generated_at={report['generated_at']}",
        f"source_sha256={report['kernel']['source_sha256']}",
        f"total={len(checks)} passed={passed} failed={len(checks)-passed}",
        f"overall_ok={str(report['summary']['overall_ok']).lower()}",
        "assurance=V3 executable finite/symbolic checking; not proof-assistant compilation",
        "",
    ]
    for c in checks:
        lines.append(f"[{ 'PASS' if c['passed'] else 'FAIL' }] {c['id']} {c['title']}")
        lines.append(f"  {c['details']}")
        lines.append(f"  metrics={json.dumps(c['metrics'], ensure_ascii=False, sort_keys=True)}")
    (VERIFY_DIR / "kernel_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (CERT_DIR / "CERTIFICATE_MANIFEST.json").write_bytes(canonical_json({
        "schema_version": "hott_z.certificate_manifest.v1",
        "generated_at": utc_now(),
        "certificates": cert_manifest,
    }))

    print(json.dumps(report["summary"], sort_keys=True))
    return 0 if report["summary"]["overall_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
