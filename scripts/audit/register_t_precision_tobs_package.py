#!/usr/bin/env python3
"""Register the T-OBS abstract observation package in the later registry.

The proof-version registry is machine-managed. This narrow manager adds only
MP-T-PRECISION-TOBS-001 after validating its exact source, toolchain, run, and
claim identity. Indexing and row freezing remain separate canonical steps.
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


PACKAGE = {
    "proof_id": "MP-T-PRECISION-TOBS-001",
    "claim_ids": "C-367",
    "source": "HoTT/formal/t-precision-observation/ObservationPrecision.lean",
    "toolchain": "HoTT/formal/t-precision-observation/LEAN_CORE_TOOLCHAIN.json",
    "run": "HoTT/verification/runs/20261004-MP-T-PRECISION-TOBS-001-06",
    "kind": "lean_core_abstract_observation_factorisation_boundary",
    "verdict": "FORMAL_CHECKED_WITH_SCOPE: if a chosen observation map identifies x and y while a chosen Prop predicate differs, no decoder through that map decides the predicate globally; identity observation is a positive control.",
    "notes": "This is an abstract Lean-core function/Prop theorem plus a finite Bool/Unit control. It does not formalize quotient semantics, bare ZFC, HoTT-specific rules, a reality task, a Gödel diagonal, or any theorem that abstraction always causes paradox.",
}


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
    parser.add_argument("--write", action="store_true", help="apply the exact registration")
    parser.add_argument(
        "--refresh-primary-run",
        action="store_true",
        help="replace only the registered primary run after revalidating proof, claim, source, and toolchain identity",
    )
    args = parser.parse_args()
    registry_path = ROOT / REGISTRY_REL
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    if registry.get("schema_version") != "hott-proof-version-closure/v2":
        raise SystemExit("REGISTRY_SCHEMA_INVALID")
    later = registry.get("later_packages")
    frozen = registry.get("packages")
    if not isinstance(later, list) or not isinstance(frozen, list):
        raise SystemExit("REGISTRY_PACKAGES_INVALID")
    all_rows = [*frozen, *later]
    existing = next(
        (row for row in later if isinstance(row, dict) and row.get("proof_id") == PACKAGE["proof_id"]),
        None,
    )
    if existing is None and any(isinstance(row, dict) and row.get("proof_id") == PACKAGE["proof_id"] for row in frozen):
        raise SystemExit(f"FROZEN_PACKAGE_CONFLICT:{PACKAGE['proof_id']}")
    if existing is not None and not args.refresh_primary_run:
        raise SystemExit(f"PACKAGE_ALREADY_REGISTERED:{PACKAGE['proof_id']}")
    if existing is not None and any(existing.get(key) != PACKAGE[key] for key in ("proof_id", "claim_ids", "source", "toolchain")):
        raise SystemExit("REFRESH_IDENTITY_MISMATCH")

    claims = expand_claim_ids(PACKAGE["claim_ids"])
    claimed = {
        claim
        for row in all_rows
        if isinstance(row, dict) and row.get("proof_id") != PACKAGE["proof_id"]
        for claim in expand_claim_ids(row.get("claim_ids"))
    }
    if any(claim in claimed for claim in claims):
        raise SystemExit(f"CLAIM_ALREADY_REGISTERED:{PACKAGE['proof_id']}")

    source = ROOT / PACKAGE["source"]
    toolchain = ROOT / PACKAGE["toolchain"]
    run_path = ROOT / PACKAGE["run"] / "RUN.json"
    if not source.is_file() or not toolchain.is_file() or not run_path.is_file():
        raise SystemExit("PACKAGE_INPUT_MISSING")
    run = json.loads(run_path.read_text(encoding="utf-8"))
    if (
        run.get("proof_id") != PACKAGE["proof_id"]
        or run.get("claim_ids") != claims
        or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("exit_code") != 0
    ):
        raise SystemExit("PRIMARY_RUN_IDENTITY_INVALID")
    manifest = json.loads((run_path.parent / "source-manifest.json").read_text(encoding="utf-8"))
    paths = {row.get("path") for row in manifest.get("files", []) if isinstance(row, dict)}
    if PACKAGE["source"] not in paths:
        raise SystemExit("PRIMARY_SOURCE_NOT_IN_MANIFEST")

    proposed = dict(registry)
    proposed_later = [
        dict(PACKAGE) if isinstance(row, dict) and row.get("proof_id") == PACKAGE["proof_id"] else row
        for row in later
    ]
    if existing is None:
        proposed_later.append(dict(PACKAGE))
    proposed["later_packages"] = proposed_later
    later_claims = {
        claim
        for row in proposed_later
        for claim in expand_claim_ids(row.get("claim_ids"))
    }
    proposed["later_machine_proved_claim_count"] = len(
        [claim for claim in later_claims if claim.startswith("C-") and claim[2:].isdigit()]
    )
    result = {
        "status": (
            "REFRESHED" if args.refresh_primary_run and args.write else
            "WOULD_REFRESH" if args.refresh_primary_run else
            "REGISTERED" if args.write else
            "WOULD_REGISTER"
        ),
        "proof_id": PACKAGE["proof_id"],
        "run": PACKAGE["run"],
        "later_packages_before": len(later),
        "later_packages_after": len(proposed_later),
        "later_machine_proved_claim_count": proposed["later_machine_proved_claim_count"],
    }
    if args.write:
        write_atomic(registry_path, (json.dumps(proposed, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
