#!/usr/bin/env python3
"""Verify P30's fixed-source crosswalk without claiming a HoTT theorem."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md"
FREEZE = HERE / "P30-HOTT-REFLECTION-CROSSWALK-SOURCE-FREEZE.json"
OUT = HERE / "P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-VERIFICATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    required = [
        "O1", "O2", "O3", "O4", "O5", "O6", "P24 ERCF3", "P25 HoTTLean",
        "P26 TTasQIIRT", "P28 CFTT", "P29 Climber", "P31-TT-PROVABILITY",
        "NO_NEW_HOTT_DEFECT_CLAIM", "SWITCH_BRANCH",
    ]
    text = REPORT.read_text()
    missing = [token for token in required if token not in text]
    mismatches = {}
    for relative, expected in freeze["local_source_sha256"].items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            mismatches[relative] = {"expected": expected, "actual": actual}
    payload = {
        "schema_version": "p30-hott-reflection-crosswalk-verification/v1",
        "task_id": "P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-001",
        "status": "PASS_WITH_SCOPE" if not missing and not mismatches else "FAIL",
        "verdict": "CLOSE_WITH_SCOPE / SIX_OBLIGATION_CROSSWALK_COMPLETED / NO_FIXED_HOTT_RELATED_ASSET_ESTABLISHES_THE_FULL_STRONG_REFLECTION_CHAIN / P31_TT_PROVABILITY_SOURCE_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM",
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing,
        "local_source_hash_mismatches": mismatches,
        "candidate_scope": "P31 is a version-pinned public Agda source candidate only; it is not asserted to be HoTT or a same-task consumer.",
        "scope": "Checks the P30 report and P24-P29 source references. It proves no HoTT theorem, defect, or global absence claim.",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if payload["status"] != "PASS_WITH_SCOPE":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
