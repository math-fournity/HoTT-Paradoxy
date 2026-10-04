#!/usr/bin/env python3
"""Register the M1-A ZFC-H0 final-closure proof package atomically.

The proof-version registry is machine-managed.  This narrow manager adds only
the C-365 primary package after checking its run identity; indexing the run and
verifying its row remain separate canonical operations.
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


TRACE_PACKAGE = {
    "proof_id": "MP-ZFC-H0-TRACE-001",
    "claim_ids": "C-365",
    "source": "HoTT/formal/zfc-h0-final-closure/H0TraceObservation.agda",
    "toolchain": "HoTT/formal/zfc-h0-final-closure/TOOLCHAIN.json",
    "run": "HoTT/verification/runs/20261004-MP-ZFC-H0-TRACE-001-07",
    "kind": "native_cubical_fixed_h0_delay_finite_observation_trace_fragment",
    "verdict": "FORMAL_CHECKED_WITH_SCOPE: fixed H0's Delay/runFor output maps to a set-valued all-nothing finite trace for every universe Judge.",
    "notes": "This is H0_OPERATIONAL_FRAGMENT_ONLY. It does not construct a complete CCHM/ZFC semantics or establish H0Map, C_accept, AdequacyLift, SameFullQ, P/Q, or bare-ZFC attribution.",
}

PROCESS_REPRESENTATION_PACKAGE = {
    "proof_id": "MP-ZFC-H0-PROCESS-REPRESENTATION-001",
    "claim_ids": "C-366",
    "source": "HoTT/formal/zfc-h0-final-closure/H0ProcessRepresentation.lean",
    "toolchain": "HoTT/formal/zfc-h0-final-closure/H0ProcessRepresentation-TOOLCHAIN.json",
    "run": "HoTT/verification/runs/20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-001-05",
    "kind": "external_foundation_lean_zermelo_sequence_representability_positive_control",
    "verdict": "FORMAL_CHECKED_WITH_SCOPE: the pinned Foundation Zermelo-model interface represents ordinal-indexed sequence graphs and unique stage values.",
    "notes": "This is M3_PROCESS_REPRESENTABILITY_ONLY. It rejects only the language-absence route; it does not establish bare ZFC syntax/model theory, H0Map, C_accept, AdequacyLift, SameFullQ, P/Q, or bare-ZFC attribution.",
}

PROVISIONAL_REPLAY_RUN = "HoTT/verification/runs/20261004-MP-ZFC-H0-TRACE-001-03"


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
    parser.add_argument("--write", action="store_true", help="apply the exact primary-package registration")
    parser.add_argument("--refresh-primary-run", action="store_true", help="replace this package's primary run after identity revalidation")
    parser.add_argument("--register-process-representation", action="store_true", help="select the C-366 external Foundation representability package")
    parser.add_argument("--refresh-process-representation", action="store_true", help="refresh C-366 after revalidating its primary run")
    parser.add_argument("--retire-provisional-replay", action="store_true", help="remove only the known pre-closure replay relation while preserving its run files")
    args = parser.parse_args()
    if args.refresh_process_representation:
        args.register_process_representation = True
    package = PROCESS_REPRESENTATION_PACKAGE if args.register_process_representation else TRACE_PACKAGE
    refresh = args.refresh_primary_run or args.refresh_process_representation
    if args.retire_provisional_replay and (refresh or args.register_process_representation):
        raise SystemExit("RETIRE_AND_REFRESH_CONFLICT")

    registry_path = ROOT / REGISTRY_REL
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    if registry.get("schema_version") != "hott-proof-version-closure/v2":
        raise SystemExit("REGISTRY_SCHEMA_INVALID")
    if args.retire_provisional_replay:
        replay = registry.get("replay_runs")
        if not isinstance(replay, dict) or not isinstance(replay.get("entries"), list):
            raise SystemExit("REPLAY_REGISTRY_INVALID")
        matched = [entry for entry in replay["entries"] if isinstance(entry, dict) and entry.get("run") == PROVISIONAL_REPLAY_RUN]
        if not matched:
            print(json.dumps({"status": "ALREADY_RETIRED", "run": PROVISIONAL_REPLAY_RUN}, ensure_ascii=False))
            return 0
        if len(matched) != 1 or matched[0].get("proof_id") != TRACE_PACKAGE["proof_id"]:
            raise SystemExit("PROVISIONAL_REPLAY_IDENTITY_INVALID")
        run_path = ROOT / PROVISIONAL_REPLAY_RUN / "RUN.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        if run.get("proof_id") != TRACE_PACKAGE["proof_id"] or run.get("index", {}).get("relation") != "REGISTERED_REPLAY":
            raise SystemExit("PROVISIONAL_RUN_IDENTITY_INVALID")
        proposed = dict(registry)
        proposed_replay = dict(replay)
        proposed_replay["entries"] = [entry for entry in replay["entries"] if entry is not matched[0]]
        proposed["replay_runs"] = proposed_replay
        run.pop("index", None)
        run["index_status"] = "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE"
        result = {"status": "RETIRED" if args.write else "WOULD_RETIRE", "run": PROVISIONAL_REPLAY_RUN}
        if args.write:
            write_atomic(registry_path, (json.dumps(proposed, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())
            write_atomic(run_path, (json.dumps(run, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())
        print(json.dumps(result, ensure_ascii=False))
        return 0
    later = registry.get("later_packages")
    all_packages = list(registry.get("packages", [])) + list(later or [])
    if not isinstance(later, list) or any(not isinstance(row, dict) for row in all_packages):
        raise SystemExit("REGISTRY_PACKAGES_INVALID")
    existing = next((row for row in later if row.get("proof_id") == package["proof_id"]), None)
    if existing is None and any(row.get("proof_id") == package["proof_id"] for row in registry.get("packages", [])):
        raise SystemExit(f"FROZEN_PACKAGE_CONFLICT:{package['proof_id']}")
    if existing is not None and not refresh:
        raise SystemExit(f"PACKAGE_ALREADY_REGISTERED:{package['proof_id']}")
    if existing is not None and any(existing.get(key) != package[key] for key in ("proof_id", "claim_ids", "source", "toolchain")):
        raise SystemExit("REFRESH_IDENTITY_MISMATCH")

    claims = expand_claim_ids(package["claim_ids"])
    registered_claims = {
        claim
        for row in all_packages
        if row.get("proof_id") != package["proof_id"]
        for claim in expand_claim_ids(row.get("claim_ids"))
    }
    if any(claim in registered_claims for claim in claims):
        raise SystemExit("CLAIM_ALREADY_REGISTERED")

    source = ROOT / package["source"]
    toolchain = ROOT / package["toolchain"]
    run_path = ROOT / package["run"] / "RUN.json"
    if not source.is_file() or not toolchain.is_file() or not run_path.is_file():
        raise SystemExit("PACKAGE_INPUT_MISSING")
    run = json.loads(run_path.read_text(encoding="utf-8"))
    if (
        run.get("proof_id") != package["proof_id"]
        or run.get("claim_ids") != claims
        or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
        or run.get("exit_code") != 0
    ):
        raise SystemExit("PRIMARY_RUN_IDENTITY_INVALID")
    manifest = json.loads((run_path.parent / "source-manifest.json").read_text(encoding="utf-8"))
    paths = {row.get("path") for row in manifest.get("files", []) if isinstance(row, dict)}
    if package["source"] not in paths:
        raise SystemExit("PRIMARY_SOURCE_NOT_IN_MANIFEST")

    proposed = dict(registry)
    proposed_later = [dict(package) if row.get("proof_id") == package["proof_id"] else row for row in later]
    if existing is None:
        proposed_later.append(dict(package))
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
        "status": ("REFRESHED" if refresh else "REGISTERED") if args.write else ("WOULD_REFRESH" if refresh else "WOULD_REGISTER"),
        "proof_id": package["proof_id"],
        "run": package["run"],
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
