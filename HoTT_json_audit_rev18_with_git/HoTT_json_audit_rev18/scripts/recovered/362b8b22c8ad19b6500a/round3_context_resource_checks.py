#!/usr/bin/env python3
"""Finite sanity checks for HOTT-Z round 3.

These checks illustrate minimal countermodels and registry invariants. They are not
proof-assistant verification and must not be described as unbounded formal proofs.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def role_erasure_check() -> dict[str, Any]:
    # One bare object has two enriched interpretations.
    bare = "successor-algebra"
    enriched = [(bare, "Arith"), (bare, "Index")]

    # Any deterministic predictor from the singleton bare domain chooses one role.
    predictors = [dict(value=v) for v in ("Arith", "Index")]
    failures = []
    for predictor in predictors:
        value = predictor["value"]
        bad = [e for e in enriched if e[1] != value]
        failures.append({"predictor": value, "misclassified": bad})

    return {
        "bare_images_equal": enriched[0][0] == enriched[1][0],
        "roles_different": enriched[0][1] != enriched[1][1],
        "predictor_count": len(predictors),
        "every_predictor_fails": all(item["misclassified"] for item in failures),
        "details": failures,
    }


def swap_equivariance_check() -> dict[str, Any]:
    # A two-element symmetric carrier; a canonical choice must be fixed by swap.
    carrier = (0, 1)
    swap = {0: 1, 1: 0}
    fixed = [x for x in carrier if swap[x] == x]
    return {
        "carrier": carrier,
        "swap": swap,
        "fixed_points": fixed,
        "equivariant_global_choice_exists": bool(fixed),
    }


def cartesian_structure_check() -> dict[str, Any]:
    # Finite-set illustration: every element is duplicated by the diagonal and
    # every element is discarded by the unique map to the singleton.
    A = ("token0", "token1")
    diagonal = {a: (a, a) for a in A}
    discard = {a: "*" for a in A}
    return {
        "object": A,
        "diagonal": diagonal,
        "discard": discard,
        "all_elements_duplicated": all(diagonal[a] == (a, a) for a in A),
        "all_elements_discarded": all(discard[a] == "*" for a in A),
        "interpretation": "Finite cartesian semantics automatically supplies copy/delete; a non-copyable resource needs extra structure or a different regime.",
    }


def registry_check() -> dict[str, Any]:
    reg = json.loads((ROOT / "HOTT_Z_SOURCE_REGISTRY.json").read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in reg["sources"]}
    duplicate_pairs = []
    all_match = True
    for source in reg["sources"]:
        dup = source.get("duplicate_of")
        if not dup:
            continue
        target = by_id[dup]
        same = source["sha256"] == target["sha256"]
        duplicate_pairs.append({"source": source["id"], "target": dup, "same_sha256": same})
        all_match = all_match and same
    return {
        "source_count": len(reg["sources"]),
        "duplicate_pairs": duplicate_pairs,
        "all_declared_byte_duplicates_match": all_match,
    }


def main() -> None:
    result = {
        "schema_version": "hott_z_round3_checks.v1",
        "scope_warning": "Finite sanity checks only; not proof-assistant verification or an unbounded proof.",
        "role_erasure": role_erasure_check(),
        "swap_equivariance": swap_equivariance_check(),
        "cartesian_copy_delete": cartesian_structure_check(),
        "source_registry": registry_check(),
    }
    out_json = ROOT / "verification" / "round3_context_resource_checks.json"
    out_txt = ROOT / "verification" / "round3_context_resource_checks.txt"
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "HOTT-Z round 3 finite sanity checks",
        "WARNING: finite checks only; not a proof-assistant verification or unbounded proof.",
        "",
        f"role erasure: every bare-only predictor fails = {result['role_erasure']['every_predictor_fails']}",
        f"two-point swap: equivariant choice exists = {result['swap_equivariance']['equivariant_global_choice_exists']}",
        f"cartesian copy/delete present = {result['cartesian_copy_delete']['all_elements_duplicated'] and result['cartesian_copy_delete']['all_elements_discarded']}",
        f"declared byte duplicates match = {result['source_registry']['all_declared_byte_duplicates_match']}",
    ]
    out_txt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_txt.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
