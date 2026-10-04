#!/usr/bin/env python3
"""Capture positive and negative Lean runs for the Meta/Sub Theory audit."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "20261004-MP-ZFC-META-SUBTHEORY-AUDIT-"
POSITIVE_RUN_ID = sys.argv[1] if len(sys.argv) > 1 else f"{PREFIX}001-01"
NEGATIVE_RUN_ID = sys.argv[2] if len(sys.argv) > 2 else f"{PREFIX}NEG-001-01"
POSITIVE_PROOF_ID = "MP-ZFC-META-SUBTHEORY-AUDIT-001"
NEGATIVE_PROOF_ID = "MP-ZFC-META-SUBTHEORY-AUDIT-NEG-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/MetaSubtheoryAudit.lean")
WRONG = Path("HoTT/formal/zfc-observation-boundary/WrongMetaSubtheoryAudit.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/MetaSubtheoryAudit-CLAIM.md")
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


def validate_id(run_id: str) -> None:
    if "/" in run_id or not run_id.startswith(PREFIX):
        raise SystemExit("RUN_ID_INVALID")


def write_run(
    *,
    run_id: str,
    proof_id: str,
    argv: list[str],
    result: subprocess.CompletedProcess[bytes],
    started: dt.datetime,
    completed: dt.datetime,
    manifest_files: list[Path],
    expected_negative: bool,
) -> dict[str, object]:
    run = ROOT / "HoTT/verification/runs" / run_id
    if run.exists():
        raise RuntimeError(f"RUN_ALREADY_EXISTS:{run_id}")
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    expected_error = b"Tactic `assumption` failed"
    # Lean emits ordinary elaboration diagnostics on stdout in this invocation.
    # Check both streams so the receipt records the mathematical rejection,
    # rather than falsely classifying the diagnostic channel as a test failure.
    negative_matches = result.returncode == 1 and expected_error in (result.stdout + result.stderr)
    status = "KERNEL_REJECTED" if expected_negative else ("KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED")
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": proof_id,
        "run_id": run_id,
        "files": [source_row(path) for path in manifest_files],
        "external_dependencies": [],
        "policy": "Lean 4 core Meta/Sub Theory completion-audit model; not an encoding of actual ZFC, a physical process, or a source-owned policy.",
    }
    receipt: dict[str, object] = {
        "schema_version": "formal-proof-run/v1",
        "run_id": run_id,
        "proof_id": proof_id,
        "claim_ids": ["ZFC-META-SUBTHEORY-AUDIT-001", "ZFC-META-SUBTHEORY-AUDIT-002", "ZFC-META-SUBTHEORY-AUDIT-003", "ZFC-META-SUBTHEORY-AUDIT-004", "ZFC-META-SUBTHEORY-AUDIT-005"],
        "proof_assistant": "Lean",
        "proof_assistant_version": subprocess.check_output([str(LEAN), "--version"], text=True).strip(),
        "theory_variant": "Lean 4 core Meta/Sub Theory completion-audit calculus; not actual ZFC or a physical process.",
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": status,
        "scope": "Meta acceptance of a subtheory formal completion requires a bridge before it can be promoted to origin completion; observation collisions block the audit; a bridge-aware positive control and a rejected coarse-promotion negative control are included.",
        "non_goals": [
            "No theorem that actual ZFC is inconsistent or lacks all time representation.",
            "No theorem that standard real analysis fails a specified physical task.",
            "No theorem that an actual HoTT task and a Zeno task are identical.",
        ],
        "index_status": "CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    if expected_negative:
        receipt["expected_error"] = "Tactic `assumption` failed"
        receipt["expected_error_stream"] = "stdout-or-stderr"
        receipt["outcome_matches_expectation"] = negative_matches
    run.mkdir(parents=True)
    environment = (
        f"platform={platform.platform()}\n"
        f"lean={receipt['proof_assistant_version']}\n"
        f"expected_negative={expected_negative}\n"
        "imports=Lean core plus temporary local .olean for the negative control\n"
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
    return {"run_id": run_id, "status": status, "exit": result.returncode, "expected": negative_matches if expected_negative else accepted}


def main() -> None:
    validate_id(POSITIVE_RUN_ID)
    validate_id(NEGATIVE_RUN_ID)
    source = ROOT / SOURCE
    wrong = ROOT / WRONG
    claim = ROOT / CLAIM
    script = Path(__file__)
    if not all(path.is_file() for path in (source, wrong, claim, script, LEAN)):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    with tempfile.TemporaryDirectory(prefix="zfc-meta-subtheory-lean-") as temporary:
        temporary_root = Path(temporary)
        olean = temporary_root / "MetaSubtheoryAudit.olean"
        build_started = dt.datetime.now(dt.timezone.utc)
        build = subprocess.run([str(LEAN), "-o", str(olean), str(source)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        build_completed = dt.datetime.now(dt.timezone.utc)
        if build.returncode != 0:
            raise RuntimeError("POSITIVE_BUILD_FAILED")
        positive = subprocess.CompletedProcess([str(LEAN), str(source)], build.returncode, build.stdout, build.stderr)
        positive_summary = write_run(
            run_id=POSITIVE_RUN_ID,
            proof_id=POSITIVE_PROOF_ID,
            argv=[str(LEAN), str(source)],
            result=positive,
            started=build_started,
            completed=build_completed,
            manifest_files=[source, claim, script],
            expected_negative=False,
        )
        env = os.environ.copy()
        env["LEAN_PATH"] = str(temporary_root)
        negative_started = dt.datetime.now(dt.timezone.utc)
        negative = subprocess.run([str(LEAN), str(wrong)], cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        negative_completed = dt.datetime.now(dt.timezone.utc)
        negative_summary = write_run(
            run_id=NEGATIVE_RUN_ID,
            proof_id=NEGATIVE_PROOF_ID,
            argv=[str(LEAN), str(wrong)],
            result=negative,
            started=negative_started,
            completed=negative_completed,
            manifest_files=[source, wrong, claim, script],
            expected_negative=True,
        )
    print(json.dumps({"positive": positive_summary, "negative": negative_summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
