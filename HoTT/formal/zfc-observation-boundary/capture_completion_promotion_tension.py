#!/usr/bin/env python3
"""Capture positive and negative Lean evidence for completion-promotion tension."""
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
PREFIX = "20261004-MP-ZFC-COMPLETION-PROMOTION-TENSION-"
POSITIVE_RUN_ID = sys.argv[1] if len(sys.argv) > 1 else f"{PREFIX}001-01"
NEGATIVE_RUN_ID = sys.argv[2] if len(sys.argv) > 2 else f"{PREFIX}NEG-001-01"
POSITIVE_PROOF_ID = "MP-ZFC-COMPLETION-PROMOTION-TENSION-001"
NEGATIVE_PROOF_ID = "MP-ZFC-COMPLETION-PROMOTION-TENSION-NEG-001"
META_SOURCE = Path("HoTT/formal/zfc-observation-boundary/MetaSubtheoryAudit.lean")
SOURCE = Path("HoTT/formal/zfc-observation-boundary/CompletionPromotionTension.lean")
WRONG = Path("HoTT/formal/zfc-observation-boundary/WrongCompletionPromotionTension.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/CompletionPromotionTension-CLAIM.md")
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
    negative_matches = result.returncode == 1 and expected_error in (result.stdout + result.stderr)
    status = "KERNEL_REJECTED" if expected_negative else ("KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED")
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": proof_id,
        "run_id": run_id,
        "files": [source_row(path) for path in manifest_files],
        "external_dependencies": [],
        "policy": "Lean 4 core policy/semantic completion-promotion calculus; not an encoding of actual ZFC, a community, a physical process, or an actual source policy.",
    }
    receipt: dict[str, object] = {
        "schema_version": "formal-proof-run/v1",
        "run_id": run_id,
        "proof_id": proof_id,
        "claim_ids": [
            "ZFC-COMPLETION-PROMOTION-001",
            "ZFC-COMPLETION-PROMOTION-002",
            "ZFC-COMPLETION-PROMOTION-003",
            "ZFC-COMPLETION-PROMOTION-004",
            "ZFC-COMPLETION-PROMOTION-005",
            "ZFC-COMPLETION-PROMOTION-006",
        ],
        "proof_assistant": "Lean",
        "proof_assistant_version": subprocess.check_output([str(LEAN), "--version"], text=True).strip(),
        "theory_variant": "Lean 4 core policy/semantic completion-promotion calculus; not actual ZFC, real analysis, HoTT, a physical process, or the mathematical community.",
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": status,
        "scope": "An adopted inference rule promoting formal completion to origin completion is sound only with a statewise completion bridge; a Q-missing coarse fixture plus adopted P, formal A and origin countertrace B is unsound; the same Q-missing fixture need not adopt P; a bridge-paid positive control is sound.",
        "non_goals": [
            "No theorem that actual ZFC is inconsistent, lacks Q, or adopts P.",
            "No theorem that standard real analysis fails a specified physical task.",
            "No theorem that a real HoTT task and a Zeno task are identical.",
            "No source-level proof of P-to-B provenance in actual mathematical practice.",
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
        "imports=Lean core plus temporary local .olean dependencies\n"
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
    meta = ROOT / META_SOURCE
    source = ROOT / SOURCE
    wrong = ROOT / WRONG
    claim = ROOT / CLAIM
    script = Path(__file__)
    if not all(path.is_file() for path in (meta, source, wrong, claim, script, LEAN)):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    with tempfile.TemporaryDirectory(prefix="zfc-completion-promotion-lean-") as temporary:
        temporary_root = Path(temporary)
        meta_olean = temporary_root / "MetaSubtheoryAudit.olean"
        source_olean = temporary_root / "CompletionPromotionTension.olean"
        meta_build = subprocess.run([str(LEAN), "-o", str(meta_olean), str(meta)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if meta_build.returncode != 0:
            raise RuntimeError("META_DEPENDENCY_BUILD_FAILED")
        started = dt.datetime.now(dt.timezone.utc)
        positive = subprocess.run([str(LEAN), "-o", str(source_olean), str(source)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env={**os.environ, "LEAN_PATH": str(temporary_root)})
        completed = dt.datetime.now(dt.timezone.utc)
        positive_summary = write_run(
            run_id=POSITIVE_RUN_ID,
            proof_id=POSITIVE_PROOF_ID,
            argv=[str(LEAN), str(source)],
            result=positive,
            started=started,
            completed=completed,
            manifest_files=[meta, source, claim, script],
            expected_negative=False,
        )
        negative_started = dt.datetime.now(dt.timezone.utc)
        negative = subprocess.run([str(LEAN), str(wrong)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env={**os.environ, "LEAN_PATH": str(temporary_root)})
        negative_completed = dt.datetime.now(dt.timezone.utc)
        negative_summary = write_run(
            run_id=NEGATIVE_RUN_ID,
            proof_id=NEGATIVE_PROOF_ID,
            argv=[str(LEAN), str(wrong)],
            result=negative,
            started=negative_started,
            completed=negative_completed,
            manifest_files=[meta, source, wrong, claim, script],
            expected_negative=True,
        )
    print(json.dumps({"positive": positive_summary, "negative": negative_summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
