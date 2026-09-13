#!/usr/bin/env python3
"""Bind a captured proof run to the exact claim-matrix snapshot that indexes it.

Capture scripts write `index_status = PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`.
After the proof row and all claim rows exist in `HoTT/CLAIM_EVIDENCE_MATRIX.md`,
this helper records the matrix path and SHA-256 inside RUN.json and flips the
status to `INDEXED_IN_CLAIM_EVIDENCE_MATRIX` — the precondition checked by
`freeze_proof_index_rows.py`. No mathematical content is changed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
RUN_ROOT = Path("HoTT/verification/runs")
INDEX_PATH = "HoTT/CLAIM_EVIDENCE_MATRIX.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def unique_row(lines: list[str], identity: str, prefix: str) -> str:
    matches = [line for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise SystemExit(f"INDEX_ROW_COUNT:{identity}:{len(matches)}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    run_relative = safe_relative(args.run_dir)
    try:
        run_relative.relative_to(RUN_ROOT)
    except ValueError:
        raise SystemExit("RUN_OUTSIDE_AUTHORITATIVE_ROOT")
    run_dir = root / run_relative
    run_path = run_dir / "RUN.json"
    run = json.loads(run_path.read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE":
        raise SystemExit("RUN_NOT_KERNEL_ACCEPTED")
    if run.get("index_status") != "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE":
        raise SystemExit(f"UNEXPECTED_INDEX_STATUS:{run.get('index_status')}")
    proof_id = run.get("proof_id")
    claim_ids = run.get("claim_ids")
    if not isinstance(proof_id, str) or not isinstance(claim_ids, list) or not claim_ids:
        raise SystemExit("RUN_IDENTITIES_INVALID")
    index_data = (root / INDEX_PATH).read_bytes()
    lines = index_data.decode("utf-8").splitlines()
    unique_row(lines, proof_id, f"| `{proof_id}` |")
    for claim_id in claim_ids:
        unique_row(lines, str(claim_id), f"| {claim_id} |")
    run["index"] = {"path": INDEX_PATH, "sha256": sha(index_data)}
    run["index_status"] = "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
    tmp_path = run_path.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(run, handle, ensure_ascii=False, sort_keys=True, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp_path, run_path)
    print(json.dumps({
        "status": "INDEXED",
        "run_id": run.get("run_id"),
        "index_sha256": run["index"]["sha256"],
        "claims": len(claim_ids),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
