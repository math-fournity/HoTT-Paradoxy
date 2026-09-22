#!/usr/bin/env python3
"""Verify P36's local source/provenance classification without creating a theorem."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "P36-PROVENANCE-ORIGIN-COVERAGE-REPORT.md"
FREEZE = HERE / "P36-PROVENANCE-ORIGIN-SOURCE-FREEZE.json"
OUT = HERE / "P36-PROVENANCE-ORIGIN-COVERAGE-VERIFICATION.json"


def h(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text())
    report = REPORT.read_text()
    real_circle = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda").read_text()
    apartness = (ROOT / "HoTT/formal/agda-unimath/hott-z/PunctureApartness.agda").read_text()
    stereographic = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeStereographic.agda").read_text()
    rich = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda").read_text()
    source = (ROOT / "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda").read_text()
    runs = [
        json.loads((ROOT / "HoTT/verification/runs/20260920-MP-ASTRA-PUNCTURE-APARTNESS-001-01/RUN.json").read_text()),
        json.loads((ROOT / "HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-STEREOGRAPHIC-001-01/RUN.json").read_text()),
        json.loads((ROOT / "HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-INTERVAL-001-01/RUN.json").read_text()),
    ]
    mismatches = {rel: {"expected": digest, "actual": h(ROOT / rel)} for rel, digest in freeze["sha256"].items() if h(ROOT / rel) != digest}
    required_report = ["PARTIAL_REUSE", "ACTUAL_MRICH_IS_STRONG_REFINEMENT", "HISTORICAL_PROVENANCE_NOT_FORMALIZED", "P37", "NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM"]
    source_checks = {
        "weak_puncture": all(token in real_circle for token in ("puncturedSubtype p = neg-type-Prop (p ＝ east)", "PuncturedRealCircle")),
        "strong_refinement": all(token in apartness for token in ("StrongPuncture = Σ RealCircle Strong", "forgetStrong : StrongPuncture → PuncturedRealCircle", "Lift =")),
        "conditional_weak_to_strong": "weakCircleEquivStrong : Lift → PuncturedRealCircle ≃ StrongPuncture" in stereographic,
        "actual_source_strong": "mRich = StrongPuncture , mData" in rich,
        "source_is_supplied_not_event": all(token in source for token in ("Supplied source data", "no physical provenance oracle", "Input.source actualInput = mRich")),
    }
    missing = [token for token in required_report if token not in report]
    runs_ok = all(run["status"] == "KERNEL_ACCEPTED_WITH_SCOPE" and run["exit_code"] == 0 for run in runs)
    status = "PASS_WITH_SCOPE" if not mismatches and not missing and all(source_checks.values()) and runs_ok else "FAIL"
    out = {
        "schema_version": "p36-provenance-origin-coverage-verification/v1",
        "task_id": "P36-P1-PROVENANCE-ORIGIN-COVERAGE-001",
        "status": status,
        "verdict": "PARTIAL_REUSE / STATIC_FIXED_POINT_PUNCTURE_DEFINED / ACTUAL_MRICH_IS_STRONG_REFINEMENT / HISTORICAL_PROVENANCE_NOT_FORMALIZED / P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM",
        "report_sha256": h(REPORT),
        "freeze_sha256": h(FREEZE),
        "source_hash_mismatches": mismatches,
        "missing_report_tokens": missing,
        "source_checks": source_checks,
        "prior_kernel_receipts_ok": runs_ok,
        "scope": "Checks only the current local static puncture definition, strong refinement, and supplied-source boundary. It proves no historical event impossibility, HoTT defect, K, engine issue, or reality bridge.",
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
