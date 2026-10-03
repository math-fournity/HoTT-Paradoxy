#!/usr/bin/env python3
"""Capture the bare-Lean run for MP-ZFC-META-OBSERVATION-CONSISTENCY-001."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261003-MP-ZFC-META-OBSERVATION-CONSISTENCY-001-01"
PROOF_ID = "MP-ZFC-META-OBSERVATION-CONSISTENCY-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/MetaObservationConsistency.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/MetaObservationConsistency-CLAIM.md")
LEAN = Path("/Users/aurolafly/.elan/bin/lean")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def source_row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith("20261003-MP-ZFC-META-OBSERVATION-CONSISTENCY-001-"):
        raise SystemExit("RUN_ID_INVALID")
    source = ROOT / SOURCE
    claim = ROOT / CLAIM
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not source.is_file() or not claim.is_file() or not LEAN.is_file():
        raise SystemExit("REQUIRED_INPUT_MISSING")
    argv = [str(LEAN), str(source)]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    completed = dt.datetime.now(dt.timezone.utc)
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [source_row(source), source_row(claim), source_row(Path(__file__))],
        "external_dependencies": [],
        "policy": "Bare Lean core meta-policy theorem; no formalization of ZFC, community consensus, or the actual HoTT candidate."
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["ZFC-META-OBS-001", "ZFC-META-OBS-002", "ZFC-META-OBS-003", "ZFC-META-OBS-004", "ZFC-META-OBS-005", "ZFC-META-OBS-006"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 core meta-policy model; not a formalization of ZFC, HoTT, physics, or community judgment.",
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Conditional O1–O5/QProfile policy inconsistency under same full profile and opposite original-resolution/bridge-required judgments; explicit O1/O2-without-O3–O5 fixture included.",
        "non_goals": [
            "No theorem that ZFC has an object-language inconsistency.",
            "No assertion that actual Zeno and HoTT cases share the same full QProfile.",
            "No claim that a revised completion contract is false or that all continuous models fail."
        ],
        "index_status": "CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"
    }
    run.mkdir(parents=True)
    environment = (
        f"platform={platform.platform()}\nlean={version}\n"
        "imports=none\naxioms=printed-in-stdout\n"
    ).encode()
    for name, data in [
        ("stdout.txt", result.stdout),
        ("stderr.txt", result.stderr),
        ("environment.txt", environment),
        ("source-manifest.json", json_bytes(manifest)),
    ]:
        write_new(run / name, data)
        receipt[name.removesuffix(".txt").replace("-", "_")] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode, "duration_seconds": receipt["duration_seconds"], "stdout_sha256": sha(result.stdout), "stderr_sha256": sha(result.stderr)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
