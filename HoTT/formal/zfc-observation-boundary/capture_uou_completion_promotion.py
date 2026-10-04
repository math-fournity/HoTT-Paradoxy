#!/usr/bin/env python3
"""Capture the bare-Lean UOU source-card classification run.

The external PDF stays on the approved external volume. This script records
its URL, byte identity and SHA-256 in the run manifest without copying the
source text or credentials into the repository.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "20261004-MP-UOU-COMPLETION-PROMOTION-SOURCE-001-"
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else PREFIX + "01"
PROOF_ID = "MP-UOU-COMPLETION-PROMOTION-SOURCE-001"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/UouCompletionPromotion.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/UouCompletionPromotion-CLAIM.md")
CARD = Path("audit/20261004-P-DAG-ZFC-QP-104-PROMPT.md")
LEAN = Path("/Users/aurolafly/.elan/bin/lean")
EXTERNAL_PDF = Path("/Volumes/D/HoTT-ZFC-sources/20261004-UOU-Real-Analysis/MT-N-201-real-analysis.pdf")
EXTERNAL_PDF_SHA256 = "e8c3e3bb4867b3547f3174f5623d75ea401362ca6f338d195e3723874f4b833b"
EXTERNAL_URL = "https://uou.ac.in/sites/default/files/slm/MT%28N%29-201.pdf"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith(PREFIX):
        raise SystemExit("RUN_ID_INVALID")
    source, claim, card = ROOT / SOURCE, ROOT / CLAIM, ROOT / CARD
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    if not all(path.is_file() for path in (source, claim, card, LEAN, EXTERNAL_PDF)):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    if sha(EXTERNAL_PDF.read_bytes()) != EXTERNAL_PDF_SHA256:
        raise SystemExit("EXTERNAL_PDF_SHA256_MISMATCH")

    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run([str(LEAN), str(source)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    completed = dt.datetime.now(dt.timezone.utc)
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()

    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(source), row(claim), row(card), row(Path(__file__))],
        "external_sources": [{
            "kind": "downloaded-public-pdf",
            "url": EXTERNAL_URL,
            "path": str(EXTERNAL_PDF),
            "bytes": EXTERNAL_PDF.stat().st_size,
            "sha256": EXTERNAL_PDF_SHA256,
            "locator": "MT(N)-201 §5.1, physical PDF page 75",
        }],
        "policy": "Checks a frozen UOU source-card classification only; not UOU truth, ZFC, topology, or physical completion.",
    }
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["UOU-P-SOURCE-001", "UOU-P-SOURCE-002", "UOU-P-SOURCE-003"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": "Lean 4 core frozen-source-card classification; no formalization of UOU prose, ZFC, real topology, or physical motion.",
        "command_argv": [str(LEAN), str(source)],
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Frozen UOU card states finite-sum/limit F, named Achilles catch-up/resolution D, F-to-D promotion, no supplied task-preserving bridge, and no supplied stronger-Done distinction/equivalence.",
        "non_goals": [
            "No proof UOU is true.",
            "No theorem that limits fail to represent continuous endpoints.",
            "No actual ZFC conclusion.",
            "No P-to-HoTT-B provenance.",
        ],
        "index_status": "CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    environment = (
        f"platform={platform.platform()}\nlean={version}\nimports=none\n"
        "axioms=printed-in-stdout\n"
    ).encode()
    for name, data in [
        ("stdout.txt", result.stdout),
        ("stderr.txt", result.stderr),
        ("environment.txt", environment),
        ("source-manifest.json", (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()),
    ]:
        write_new(run / name, data)
        receipt[name.removesuffix(".txt").replace("-", "_")] = {
            "path": name, "bytes": len(data), "sha256": sha(data)
        }
    write_new(run / "RUN.json", (json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode, "duration_seconds": receipt["duration_seconds"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
