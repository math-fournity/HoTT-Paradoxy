#!/usr/bin/env python3
"""Verify P31's static source audit and preserve its proof-boundary limits."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-REPORT.md"
FREEZE = HERE / "P31-TT-PROVABILITY-SOURCE-FREEZE.json"
RUN = HERE / "runs/20260921-P31-TT-PROVABILITY-SOURCE-01"
OUT = HERE / "P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-VERIFICATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    receipt = json.loads((RUN / "RUN.json").read_text())
    manifest = json.loads((RUN / "source-manifest.json").read_text())
    required = [
        "O1", "O2", "O3", "O4", "O5", "O6", "Löb", "⋆⋆TODO⋆⋆",
        "NOT_HOTT", "P32-HOTT-SPECIFIC", "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [token for token in required if token not in REPORT.read_text()]
    mismatches = {
        path: {"expected": expected, "actual": manifest.get(path)}
        for path, expected in freeze["external_files_sha256"].items()
        if manifest.get(path) != expected
    }
    payload = {
        "schema_version": "p31-tt-provability-verification/v1",
        "task_id": "P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-001",
        "status": "PASS_WITH_SCOPE" if not missing and not mismatches and receipt["commit"] == freeze["remote"]["commit"] else "FAIL",
        "verdict": freeze["verdict"],
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing,
        "external_source_hash_mismatches": mismatches,
        "run_status": receipt["status"],
        "kernel_replay": receipt["kernel_replay"],
        "required_anchors": {
          "lob": bool(receipt["anchors"]["typed_lob_constructor"]),
          "universal_todo": bool(receipt["anchors"]["universal_todo_axiom"]),
          "positivity_disabled": bool(receipt["anchors"]["positivity_disabled"]),
          "termination_disabled": bool(receipt["anchors"]["termination_disabled"]),
          "semantic_hole": bool(receipt["anchors"]["semantic_hole"]),
        },
        "scope": "Verifies P31's fixed source identity and static report. It does not run Agda and proves no theorem about the repository, HoTT, or a reality task.",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if payload["status"] != "PASS_WITH_SCOPE":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
