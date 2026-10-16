#!/usr/bin/env python3
"""Verify the bounded P15 published-source K_app audit."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-REPORT.md"
FREEZE = OUT / "P15-PRIETO-CUBIDES-SOURCE-FREEZE.json"
RECEIPT = OUT / "P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-VERIFICATION.json"
P14 = ROOT / "audit/p14-ambient-operation-k-successor-discovery-20260921/P14-PRIETO-CUBIDES-CANDIDATE-FREEZE.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = REPORT.read_text(encoding="utf-8")
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    p14 = json.loads(P14.read_text(encoding="utf-8"))
    required = [
        "NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES", "DEFENSE_EXPLICIT_MAP_FACE_WALK_SPHERICAL_DATA",
        "TASK_DIFFERENT_FROM_P13_MN_DONE", "P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT",
        "K-input", "K-output", "K-claim", "K-forgetting", "K-version",
        "Map G", "Face G M", "M-is-spherical", "spherical-equiv", "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [token for token in required if token not in report]
    version = freeze["version"]
    p7 = freeze["p7_assessment"]
    identity_ok = (
        version["page_version"] == "Sunday, January 22, 2023, 10:42 PM"
        and version["agda_version"] == "2.6.2.2-442c76b"
        and version["source_commit_short"] == "57c278b4"
        and len(freeze["pages"]) == 6
        and p14["candidate_id"] == freeze["candidate_id"]
    )
    p7_ok = p7 == {
        "K_input": "FAILS_BARE_H_INPUT",
        "K_output": "NOT_P13_DONE_AMBIENT_OR_CURVE",
        "K_claim": "NO_P13_COMPLETION_CLAIM_FOUND_WITHIN_FIXED_PAGES",
        "K_forgetting": "NO_BARE_H_TO_DONE_BRIDGE_FOUND_WITHIN_FIXED_PAGES",
        "K_version": "VERSION_PINNED_SOURCE_INSPECTED_WITH_SCOPE",
    }
    result = {
        "schema_version": "p15-prieto-cubides-spherical-maps-agda-corpus-verification/v1",
        "task_id": "P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-001",
        "status": "PASS_WITH_SCOPE" if not missing and identity_ok and p7_ok else "FAIL",
        "verdict": "NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES / DEFENSE_EXPLICIT_MAP_FACE_WALK_SPHERICAL_DATA / TASK_DIFFERENT_FROM_P13_MN_DONE / P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM",
        "scope": "Checks the fixed P15 report, frozen page identity, and P7 classification. It does not fetch pages, replay Agda, prove a global absence, or establish a HoTT theorem.",
        "sources": {str(REPORT.relative_to(ROOT)): sha(REPORT), str(FREEZE.relative_to(ROOT)): sha(FREEZE), str(P14.relative_to(ROOT)): sha(P14)},
        "missing_required_tokens": missing,
        "source_identity_ok": identity_ok,
        "p7_classification_ok": p7_ok,
        "pages": freeze["pages"],
    }
    if args.write:
        RECEIPT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
