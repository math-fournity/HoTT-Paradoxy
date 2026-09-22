#!/usr/bin/env python3
"""Verify P35's fixed-source coverage decision without creating a new proof claim."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P35-FIBERWISE-TRACE-COVERAGE-REPORT.md"
FREEZE = HERE / "P35-FIBERWISE-TRACE-SOURCE-FREEZE.json"
OUT = HERE / "P35-FIBERWISE-TRACE-COVERAGE-VERIFICATION.json"


def h(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    report = REPORT.read_text()
    task = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda").read_text()
    rich = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda").read_text()
    source = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda").read_text()
    curve_task = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeCurveTask.agda").read_text()
    p34_run = json.loads((ROOT / "HoTT/verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01/RUN.json").read_text())
    p21_run = json.loads((ROOT / "HoTT/verification/runs/20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01/RUN.json").read_text())
    mismatches = {rel: {"expected": digest, "actual": h(ROOT / rel)} for rel, digest in freeze["sha256"].items() if h(ROOT / rel) != digest}
    report_required = ["EXACT_COVERAGE_WITH_SCOPE", "NO_NEW_WRAPPER_OR_KERNEL_CLAIM", "P36", "NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM"]
    source_required = {
        "curve_fields": all(token in task for token in ("record CurveRun", "jointlyContinuous", "agreesInterior", "slice", "initial", "final", "spaceBound")),
        "actual_run": "actualCurveRun : CurveRun nRich mRich" in task,
        "target_transport": "fullTransportPath : mRich ＝ transportedRich" in rich,
        "source_contract_separate": all(token in source for token in ("Satisfies", "Done", "bareCheckIsInsufficient")),
        "ambient_contract_separate": all(token in curve_task for token in ("Success", "noSuccessNtoM", "noUniversalTraceLift")),
    }
    missing = [token for token in report_required if token not in report]
    run_ok = p34_run["status"] == "KERNEL_ACCEPTED_WITH_SCOPE" and p34_run["exit_code"] == 0 and p21_run["exit_code"] == 0
    status = "PASS_WITH_SCOPE" if not mismatches and not missing and all(source_required.values()) and run_ok else "FAIL"
    out = {
        "schema_version": "p35-fiberwise-trace-coverage-verification/v1",
        "task_id": "P35-P1-FIBERWISE-TRACE-COVERAGE-001",
        "status": status,
        "verdict": "EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_PROVENANCE_ORIGIN_COVERAGE_GATE_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM",
        "report_sha256": h(REPORT),
        "freeze_sha256": h(FREEZE),
        "source_hash_mismatches": mismatches,
        "missing_report_tokens": missing,
        "source_field_checks": source_required,
        "prior_kernel_receipts_ok": run_ok,
        "scope": "Verifies only that existing P34/P21 local sources jointly cover the declared P35 contract. It proves no new fiberwise term, wrapper record, general R_origin theory, K, HoTT defect, or reality claim.",
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
