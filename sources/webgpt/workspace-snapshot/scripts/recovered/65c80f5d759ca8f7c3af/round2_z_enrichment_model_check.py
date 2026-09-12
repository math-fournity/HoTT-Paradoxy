#!/usr/bin/env python3
"""Finite sanity checks for the second-round HoTT–Z reconstruction.

This program checks only small finite witnesses used to catch mistakes in the
paper arguments.  It is NOT a proof-assistant formalization and does not replace
any unbounded mathematical proof.

Checked patterns:
1. provenance cannot factor through a current-snapshot projection;
2. a finer representation recovers every observable recoverable by a coarser one;
3. opposite event orders cannot factor through an unordered support;
4. duration cannot factor through an unparameterized trace;
5. endpoint reachability cannot factor through closure alone;
6. the target-truth signature is sufficient for exactly the chosen observables;
7. a non-injective abstraction has no exact reconstruction left inverse.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from itertools import product
import json
from pathlib import Path
from typing import Any, Callable, Dict, Hashable, Iterable, Mapping, Sequence, Tuple

ROOT = Path(__file__).resolve().parent
OUT_JSON = ROOT / "round2_z_enrichment_model_check.json"


def all_functions(domain: Sequence[Hashable], codomain: Sequence[Any]):
    """Enumerate all functions from a finite domain to a finite codomain."""
    for values in product(codomain, repeat=len(domain)):
        yield dict(zip(domain, values))


def factors_through(
    worlds: Sequence[Hashable],
    abstraction: Mapping[Hashable, Hashable],
    observable: Mapping[Hashable, Any],
) -> bool:
    """Finite fiber-constancy criterion for factorization."""
    seen: Dict[Hashable, Any] = {}
    for world in worlds:
        abstract = abstraction[world]
        value = observable[world]
        if abstract in seen and seen[abstract] != value:
            return False
        seen[abstract] = value
    return True


def exact_left_inverse_exists(
    worlds: Sequence[Hashable],
    abstract_values: Sequence[Hashable],
    abstraction: Mapping[Hashable, Hashable],
) -> bool:
    """Exhaustively test for beta with beta(alpha(w)) = w for every world."""
    for candidate in all_functions(abstract_values, worlds):
        if all(candidate[abstraction[w]] == w for w in worlds):
            return True
    return False


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str


def main() -> None:
    checks = []

    # 1. Snapshot/provenance.
    histories = (
        ("same-current-structure", "original"),
        ("same-current-structure", "replica"),
    )
    snapshot = {h: h[0] for h in histories}
    enriched = {h: h for h in histories}
    is_original = {h: h[1] == "original" for h in histories}

    coarse_provenance = factors_through(histories, snapshot, is_original)
    fine_provenance = factors_through(histories, enriched, is_original)
    checks.append(Check(
        "provenance_nonfactorization",
        (not coarse_provenance) and fine_provenance,
        "IsOriginal varies inside one snapshot fiber, but factors through the enriched history.",
    ))

    # 2. Refinement monotonicity on a finite observable family.
    current_structure = {h: h[0] == "same-current-structure" for h in histories}
    observables = {
        "current_structure": current_structure,
        "is_original": is_original,
    }
    coarse_recoverable = {
        name for name, obs in observables.items() if factors_through(histories, snapshot, obs)
    }
    fine_recoverable = {
        name for name, obs in observables.items() if factors_through(histories, enriched, obs)
    }
    checks.append(Check(
        "refinement_monotonicity",
        coarse_recoverable <= fine_recoverable and coarse_recoverable < fine_recoverable,
        f"coarse={sorted(coarse_recoverable)}, fine={sorted(fine_recoverable)}",
    ))

    # 3. Direction vs unordered event support.
    ordered_histories = ("a-before-b", "b-before-a")
    unordered_support = {h: frozenset(("a", "b")) for h in ordered_histories}
    a_before_b = {
        "a-before-b": True,
        "b-before-a": False,
    }
    checks.append(Check(
        "direction_nonfactorization",
        not factors_through(ordered_histories, unordered_support, a_before_b),
        "Opposite orders have the same unordered support but opposite truth values.",
    ))

    # 4. Duration vs unparameterized trace.
    timed_paths = ("unit-speed", "half-speed")
    geometric_trace = {h: "oriented-unit-interval-trace" for h in timed_paths}
    duration = {"unit-speed": 1, "half-speed": 2}
    checks.append(Check(
        "duration_nonfactorization",
        not factors_through(timed_paths, geometric_trace, duration),
        "The same unparameterized trace supports different durations.",
    ))

    # 5. Closure vs actual endpoint reachability.
    processes = ("closed-domain-reaches", "open-ended-asymptotic")
    closure = {p: "closed-unit-interval" for p in processes}
    reaches_endpoint = {
        "closed-domain-reaches": True,
        "open-ended-asymptotic": False,
    }
    checks.append(Check(
        "closure_reachability_nonfactorization",
        not factors_through(processes, closure, reaches_endpoint),
        "Equal image closures do not determine whether the endpoint is attained.",
    ))

    # 6. Minimal sufficient truth signature for selected observables.
    worlds = ("a-before-b", "b-before-a", "simultaneous")
    target_observables = {
        "a_before_b": {
            "a-before-b": True,
            "b-before-a": False,
            "simultaneous": False,
        },
        "b_before_a": {
            "a-before-b": False,
            "b-before-a": True,
            "simultaneous": False,
        },
    }
    truth_signature = {
        w: tuple(target_observables[name][w] for name in sorted(target_observables))
        for w in worlds
    }
    signature_sufficient = all(
        factors_through(worlds, truth_signature, obs)
        for obs in target_observables.values()
    )
    collapsed = {w: "one-state" for w in worlds}
    collapsed_sufficient = all(
        factors_through(worlds, collapsed, obs)
        for obs in target_observables.values()
    )
    checks.append(Check(
        "truth_signature_sufficiency",
        signature_sufficient and not collapsed_sufficient,
        f"signatures={truth_signature}",
    ))

    # 7. No exact left inverse for a non-injective abstraction.
    abstract_values = tuple(sorted(set(snapshot.values())))
    no_left_inverse = not exact_left_inverse_exists(histories, abstract_values, snapshot)
    checks.append(Check(
        "no_free_exact_reconstruction",
        no_left_inverse,
        "A non-injective snapshot projection has no beta with beta∘alpha=id.",
    ))

    payload = {
        "scope": "finite_sanity_check_only",
        "not_a_proof_assistant_formalization": True,
        "checks": [asdict(c) for c in checks],
        "all_passed": all(c.passed for c in checks),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Second-round HoTT–Z finite model sanity checks")
    print("NOTE: finite checks only; not an unbounded formal proof.\n")
    for c in checks:
        print(f"[{'PASS' if c.passed else 'FAIL'}] {c.name}: {c.detail}")
    print(f"\nall_passed={payload['all_passed']}")
    print(f"json={OUT_JSON}")

    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
