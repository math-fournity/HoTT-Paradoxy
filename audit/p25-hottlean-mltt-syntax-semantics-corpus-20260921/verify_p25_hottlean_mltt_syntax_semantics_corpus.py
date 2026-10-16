#!/usr/bin/env python3
"""Verify the fixed-source P25 HoTTLean consumer audit record."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-REPORT.md"
FREEZE = OUT / "P25-HOTTLEAN-SOURCE-FREEZE.json"
RESULT = OUT / "P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-VERIFICATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    required = [
        "ACTUAL_SYNTACTIC_MODEL_CONSUMER_CONFIRMED",
        "NOT_A_SAME_LAYER_GLOBAL_SELF_VALIDATION_CONSUMER_WITHIN_FIXED_COMMIT",
        "DEFENSE_BY_EXPLICIT_HOST_OBJECT_STRATIFICATION_AND_SCOPE",
        "P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-001",
        "NO_NEW_HOTT_DEFECT_CLAIM",
        "NO_NAMED_P24_PROOF_PREDICATE_WITHIN_LITERAL_DENOMINATOR",
    ]
    missing = [item for item in required if item not in report]
    external_checkout = Path("/tmp/hottlean-p25-31133dd5")
    source_hashes = freeze["external_files_sha256"]
    mismatches = []
    for relative, expected in source_hashes.items():
        source = external_checkout / relative
        actual = sha256(source) if source.is_file() else None
        if actual != expected:
            mismatches.append({"path": relative, "expected": expected, "actual": actual})
    anchors = {}
    if not mismatches:
        basic = (external_checkout / "HoTTLean/Syntax/Basic.lean").read_text(encoding="utf-8")
        typing = (external_checkout / "HoTTLean/Syntax/Typing.lean").read_text(encoding="utf-8")
        checked = (external_checkout / "HoTTLean/Frontend/Checked.lean").read_text(encoding="utf-8")
        commands = (external_checkout / "HoTTLean/Frontend/Commands.lean").read_text(encoding="utf-8")
        synth = (external_checkout / "HoTTLean/Typechecker/Synth.lean").read_text(encoding="utf-8")
        interpretation = (external_checkout / "HoTTLean/Model/Unstructured/Interpretation.lean").read_text(encoding="utf-8")
        anchors = {
            "external_expr_inductive": "inductive Expr where" in basic,
            "object_code_is_type_code": "Code from a type" in basic and "Type from a code" in basic,
            "typing_judgments_are_lean_prop": "inductive WfTm" in typing and "→ Prop" in typing,
            "checked_definition_carries_host_proof": "wf_val : E ∣ [] ⊢[l] val : tp" in checked,
            "frontend_uses_host_metam": "MetaM Unit" in commands and "translateAsTm" in commands,
            "typechecker_is_partial_host_program": "partial def checkTm" in synth and "Lean.MetaM" in synth,
            "soundness_is_host_theorem": "theorem ofType_ofTerm_sound" in interpretation,
        }
    remote_ok = freeze["remote"]["commit"] == "31133dd5b25226ea897f8aa5e2e43b61392459eb"
    qiirt_pin_ok = freeze["public_source_observations"]["qiirt_cpp_2026"]["remote_head_observed"] == "8db08306287333067b2749f95f8ad3ba7a0e14d1"
    status = "PASS_WITH_SCOPE" if not missing and not mismatches and all(anchors.values()) and remote_ok and qiirt_pin_ok else "FAIL"
    result = {
        "schema_version": "p25-hottlean-mltt-syntax-semantics-verification/v1",
        "task_id": freeze["task_id"],
        "status": status,
        "verdict": freeze["verdict"],
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing,
        "external_source_hash_mismatches": mismatches,
        "source_anchors": anchors,
        "remote_pin_ok": remote_ok,
        "qiirt_successor_pin_ok": qiirt_pin_ok,
        "scope": "Verifies fixed checkout source identity and the source-level P25 classification. It does not build HoTTLean, prove external program behavior, or prove a HoTT theorem or defect.",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
