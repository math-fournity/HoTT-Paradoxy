#!/usr/bin/env python3
"""Register or refresh the three ZFC-actual-Q proof packages atomically.

The script is deliberately narrow: it adds only C-359/C-360/C-361 to the
append-only `later_packages` registry, verifies their captured identity before
writing, and recomputes the numeric later-claim count.  A final recapture may
replace only the registered primary run of an already registered package after
the same proof/claim/source identity is rechecked.  It does not mark runs
indexed or freeze matrix rows; those remain separate canonical steps.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_REL = Path("HoTT/verification/PROOF_VERSION_CLOSURE.json")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from proof_claim_ids import expand_claim_ids  # noqa: E402

PACKAGES = [
    {
        "proof_id": "MP-ZFC-ACTUAL-Q-POLICY-001",
        "claim_ids": "C-359",
        "source": "HoTT/formal/zfc-actual-q-policy/ZFC1IllusionPolicy.lean",
        "toolchain": "HoTT/formal/zfc-actual-q-policy/LEAN_CORE_TOOLCHAIN.json",
        "run": "HoTT/verification/runs/20261004-MP-ZFC-ACTUAL-Q-POLICY-001-06",
        "kind": "lean_core_zfc_one_policy_consequence_with_explicit_source_hypotheses",
        "verdict": "FORMAL_CHECKED_WITH_SCOPE: explicit ZFC-1 use-model, same-Q transport and HoTT-side B counterexample entail False; Q gap alone does not imply P.",
        "notes": "Lean core with no imports or axioms. This does not formalize bare ZFC, IEP, mathematical-community consensus, an actual same-Q mapping, or physical Zeno completion. The policy/source hypotheses remain explicit.",
    },
    {
        "proof_id": "MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001",
        "claim_ids": "C-360",
        "source": "HoTT/formal/zfc-actual-q-policy/HoTTCounterexample.agda",
        "toolchain": "HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json",
        "run": "HoTT/verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-06",
        "kind": "native_cubical_fixed_hott_q_counterexample_to_coarse_completion_promotion",
        "verdict": "FORMAL_CHECKED_WITH_SCOPE: the fixed stage-one completion of the set-truncated question cannot be promoted to finite halting of the original universe question.",
        "notes": "Safe Cubical Agda 2.8.0/cubical-0.9 with complete observed local import closure and a nothing != just 1 negative control. It does not decide task identity or formalize ZFC, IEP, source-owned policy, actual same-Q identity, HoTT inconsistency, or UR reality verdict.",
    },
    {
        "proof_id": "MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001",
        "claim_ids": "C-361",
        "source": "HoTT/formal/zfc-actual-q-policy/ZenoLimitControl.lean",
        "toolchain": "HoTT/formal/astra-real-geometry/TOOLCHAIN.json",
        "run": "HoTT/verification/runs/20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-07",
        "kind": "lean_mathlib_strict_limit_to_finite_stage_promotion_control_with_closed_time_positive_control",
        "verdict": "FORMAL_CHECKED_WITH_SCOPE / DECLARED_CLASSICAL_AXIOMS: for a fixed geometric sequence, formal limit completion does not imply a finite natural-stage endpoint; a closed continuous-time endpoint exists.",
        "notes": "Lean 4.34.0 plus pinned Mathlib; propext, Classical.choice and Quot.sound are retained in the receipt. It does not attribute the strict finite-stage condition to the Standard Solution, formalize ZFC, prove continuous motion lacks an endpoint, or supply actual same-Q/policy evidence.",
    },
]


def write_atomic(path: Path, data: bytes) -> None:
    temporary = path.with_name(f".{path.name}.tmp-{uuid.uuid4().hex}")
    try:
        with temporary.open("xb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        try:
            fd = os.open(path.parent, os.O_RDONLY)
            os.fsync(fd)
            os.close(fd)
        except OSError:
            pass
    finally:
        if temporary.exists():
            temporary.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="apply the exact registration or refresh")
    parser.add_argument(
        "--refresh-final-runs",
        action="store_true",
        help="replace only existing packages' primary runs after identity revalidation",
    )
    args = parser.parse_args()
    path = ROOT / REGISTRY_REL
    registry = json.loads(path.read_text(encoding="utf-8"))
    if registry.get("schema_version") != "hott-proof-version-closure/v2":
        raise SystemExit("REGISTRY_SCHEMA_INVALID")
    later = registry.get("later_packages")
    if not isinstance(later, list):
        raise SystemExit("LATER_PACKAGES_INVALID")
    known_rows = {row.get("proof_id"): row for row in later if isinstance(row, dict)}
    all_rows = list(registry.get("packages", [])) + list(later)
    for package in PACKAGES:
        existing = known_rows.get(package["proof_id"])
        if existing is not None and not args.refresh_final_runs:
            raise SystemExit(f"PACKAGE_ALREADY_REGISTERED:{package['proof_id']}")
        if existing is not None:
            for key in ("claim_ids", "source"):
                if existing.get(key) != package.get(key):
                    raise SystemExit(f"REFRESH_IDENTITY_MISMATCH:{package['proof_id']}:{key}")
            old_toolchain = existing.get("toolchain")
            new_toolchain = package.get("toolchain")
            if old_toolchain not in (None, new_toolchain):
                raise SystemExit(f"REFRESH_IDENTITY_MISMATCH:{package['proof_id']}:toolchain")
        claims = expand_claim_ids(package["claim_ids"])
        conflicting_claims = {
            claim
            for row in all_rows
            if isinstance(row, dict) and row.get("proof_id") != package["proof_id"]
            for claim in expand_claim_ids(row.get("claim_ids"))
        }
        if any(claim in conflicting_claims for claim in claims):
            raise SystemExit(f"CLAIM_ALREADY_REGISTERED:{package['proof_id']}")
        run_path = ROOT / package["run"] / "RUN.json"
        receipt = json.loads(run_path.read_text(encoding="utf-8"))
        if receipt.get("proof_id") != package["proof_id"] or receipt.get("claim_ids") != claims:
            raise SystemExit(f"RUN_IDENTITY_MISMATCH:{package['proof_id']}")
        if receipt.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or receipt.get("exit_code") != 0:
            raise SystemExit(f"RUN_NOT_ACCEPTED:{package['proof_id']}")
        if not (ROOT / package["source"]).is_file():
            raise SystemExit(f"SOURCE_MISSING:{package['proof_id']}")
        if "toolchain" in package and not (ROOT / package["toolchain"]).is_file():
            raise SystemExit(f"TOOLCHAIN_MISSING:{package['proof_id']}")
    proposed = dict(registry)
    packages_by_id = {package["proof_id"]: package for package in PACKAGES}
    proposed_later = []
    refreshed = []
    for row in later:
        if not isinstance(row, dict) or row.get("proof_id") not in packages_by_id:
            proposed_later.append(row)
            continue
        package = packages_by_id[row["proof_id"]]
        if args.refresh_final_runs:
            updated = dict(row)
            updated["run"] = package["run"]
            if package.get("toolchain"):
                updated["toolchain"] = package["toolchain"]
            proposed_later.append(updated)
            refreshed.append(package["proof_id"])
        else:
            proposed_later.append(row)
    for package in PACKAGES:
        if package["proof_id"] not in known_rows:
            proposed_later.append(dict(package))
    proposed["later_packages"] = proposed_later
    all_later_claims = {claim for row in proposed_later for claim in expand_claim_ids(row.get("claim_ids"))}
    proposed["later_machine_proved_claim_count"] = len([claim for claim in all_later_claims if claim.startswith("C-") and claim[2:].isdigit()])
    result = {
        "status": (
            "REFRESHED" if args.refresh_final_runs and args.write else
            "WOULD_REFRESH" if args.refresh_final_runs else
            "REGISTERED" if args.write else
            "WOULD_REGISTER"
        ),
        "proof_ids": [package["proof_id"] for package in PACKAGES],
        "later_packages_before": len(later),
        "later_packages_after": len(proposed_later),
        "later_machine_proved_claim_count": proposed["later_machine_proved_claim_count"],
        "refreshed_proof_ids": refreshed,
    }
    if args.write:
        write_atomic(path, (json.dumps(proposed, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
