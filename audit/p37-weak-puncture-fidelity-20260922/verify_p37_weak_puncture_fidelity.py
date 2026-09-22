#!/usr/bin/env python3
"""Verify P37's source/domain requalification using existing kernel receipts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P37-WEAK-PUNCTURE-FIDELITY-REPORT.md"
FREEZE = HERE / "P37-WEAK-PUNCTURE-FIDELITY-SOURCE-FREEZE.json"
OUT = HERE / "P37-WEAK-PUNCTURE-FIDELITY-VERIFICATION.json"


def h(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    report = REPORT.read_text()
    circle = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda").read_text()
    puncture = (ROOT / "HoTT/formal/agda-unimath/hott-z/PunctureApartness.agda").read_text()
    stereographic = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeStereographic.agda").read_text()
    weak_consumer = (ROOT / "HoTT/formal/agda-unimath/hott-z/WeakLiftConsumer.agda").read_text()
    motion = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeMotionComplete.agda").read_text()
    rich = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda").read_text()
    user = (ROOT / "Astra继续尝试/断点与证明机制系统检查/对话原文/007 - 归档交付与指定缺口的新问题.md").read_text()
    runs = [
        json.loads((ROOT / rel).read_text()) for rel in (
            "HoTT/verification/runs/20260920-MP-ASTRA-PUNCTURE-APARTNESS-001-01/RUN.json",
            "HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-STEREOGRAPHIC-001-01/RUN.json",
            "HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-INTERVAL-001-01/RUN.json",
            "HoTT/verification/runs/20260920-MP-ASTRA-WEAK-LIFT-PRINCIPLE-001-01/RUN.json",
        )
    ]
    mismatches = {rel: {"expected": digest, "actual": h(ROOT / rel)} for rel, digest in freeze["sha256"].items() if h(ROOT / rel) != digest}
    report_required = ["EXACT_COVERAGE_BY_EXISTING_C283_C290_C307_C308", "ORIGINAL_WEAK_M_NOT_UNCONDITIONALLY_MODELED_BY_STRONG_SOURCE", "P38", "NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM"]
    source_checks = {
        "ordinary_weak_puncture": "puncturedSubtype p = neg-type-Prop (p ＝ east)" in circle,
        "strong_refinement_and_forget": all(token in puncture for token in ("StrongPuncture = Σ RealCircle Strong", "forgetStrong : StrongPuncture → PuncturedRealCircle", "Lift =")),
        "strong_result_and_conditional_weak_result": all(token in stereographic for token in ("strongCircleEquivReal", "weakCircleEquivStrong : Lift → PuncturedRealCircle ≃ StrongPuncture", "weakCircleEquivReal : Lift")),
        "weak_consumer_condition_explicit": all(token in weak_consumer for token in ("weakIntervalHomeomorphismFromRealPrinciple", "PuncturedRealCircle ＝ OpenRealInterval")),
        "weak_final_coverage_condition": "weakFinalCoverageIffLift : WeakFinalCoverage ↔ Lift" in motion,
        "actual_source_strong": "mRich = StrongPuncture , mData" in rich,
        "user_source_operation_phrase": "圆上拿掉一点" in user,
    }
    missing = [token for token in report_required if token not in report]
    runs_ok = all(run["status"] == "KERNEL_ACCEPTED_WITH_SCOPE" and run["exit_code"] == 0 for run in runs)
    status = "PASS_WITH_SCOPE" if not mismatches and not missing and all(source_checks.values()) and runs_ok else "FAIL"
    out = {
        "schema_version": "p37-weak-puncture-fidelity-verification/v1",
        "task_id": "P37-P1-WEAK-PUNCTURE-FIDELITY-REQUALIFICATION-001",
        "status": status,
        "verdict": "EXACT_COVERAGE_BY_EXISTING_C283_C290_C307_C308 / ORIGINAL_WEAK_M_NOT_UNCONDITIONALLY_MODELED_BY_STRONG_SOURCE / SPEC_REFINEMENT_NOT_JUSTIFIED_BY_ORIGINAL_TEXT / P38_REAL_ORIGIN_EVENT_BRIDGE_DISCOVERY_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM",
        "report_sha256": h(REPORT),
        "freeze_sha256": h(FREEZE),
        "source_hash_mismatches": mismatches,
        "missing_report_tokens": missing,
        "source_checks": source_checks,
        "prior_kernel_receipts_ok": runs_ok,
        "scope": "Verifies the conditional weak/strong relationship and the actual source declaration in fixed local files. It does not prove impossibility of every weak equivalence, a reality judgment about Lift, a HoTT defect, K, or an engine issue.",
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
