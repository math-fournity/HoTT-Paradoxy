#!/usr/bin/env python3
"""Check P38's fixed six-file source identity and positive declarations.

This script does not certify semantic absence of a source-event bridge.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P38-REAL-ORIGIN-EVENT-BRIDGE-REPORT.md"
FREEZE = HERE / "P38-REAL-ORIGIN-EVENT-BRIDGE-SOURCE-FREEZE.json"
OUT = HERE / "P38-REAL-ORIGIN-EVENT-BRIDGE-VERIFICATION.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    text = REPORT.read_text()
    mismatches = {
        relative: {"expected": expected, "actual": digest(ROOT / relative)}
        for relative, expected in freeze["sha256"].items()
        if digest(ROOT / relative) != expected
    }
    base = ROOT / "HoTT/formal/agda-unimath/hott-z"
    circle = (base / "NativeRealCircleQualification.agda").read_text()
    rich = (base / "NativeRichCurve.agda").read_text()
    source = (base / "NativeSourceContract.agda").read_text()
    process = (base / "NativeTaskIntegration.agda").read_text()
    finite = (ROOT / "HoTT/formal/astra-breakpoint-check/OriginDirectedDiagram.agda").read_text()
    checks = {
        "static_puncture_defined": "puncturedSubtype p = neg-type-Prop (p ＝ east)" in circle,
        "strong_source_selected": "mRich = StrongPuncture , mData" in rich,
        "source_supplied": "Input.source actualInput = mRich" in source,
        "curve_process_present": "record CurveRun" in process,
        "finite_label_control": "OriginDirectedDiagram = Σ[ static ∈ RichDiagram ]" in finite,
        "report_names_scope": all(
            phrase in text
            for phrase in (
                "NO_EXPLICIT_HISTORICAL_EVENT_BRIDGE_IN_SIX_CHECKED_MODULES",
                "P39_ONE_BOUNDED_CONTRACT_GATE",
                "Goal-3 §3 的逐项反思",
                "Goal-3 §3.1 的波次定位",
                "Goal-3 §3.2–3.3 的 successor 与航向复核",
            )
        ),
    }
    status = "PASS_WITH_SCOPE" if not mismatches and all(checks.values()) else "FAIL"
    result = {
        "schema_version": "p38-real-origin-event-bridge-verification/v2",
        "task_id": freeze["task_id"],
        "status": status,
        "verdict": freeze["verdict"],
        "report_sha256": digest(REPORT),
        "freeze_sha256": digest(FREEZE),
        "source_hash_mismatches": mismatches,
        "positive_checks": checks,
        "semantic_absence_not_machine_certified": True,
        "scope": "Only six frozen model modules were inspected. The checker verifies source identity and positive anchors; it does not establish a repository-wide negative, an impossibility theorem, a HoTT defect, or an actual K.",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
