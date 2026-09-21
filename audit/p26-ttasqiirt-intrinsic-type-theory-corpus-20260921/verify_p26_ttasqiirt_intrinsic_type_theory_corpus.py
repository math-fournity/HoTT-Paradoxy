#!/usr/bin/env python3
"""Verify the P26 fixed-source report and its external Agda run receipt."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md"
FREEZE = OUT / "P26-TTASQIIRT-SOURCE-FREEZE.json"
RUN = OUT / "runs/20260921-P26-TTASQIIRT-INDEX-01/RUN.json"
RESULT = OUT / "P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-VERIFICATION.json"
EXTERNAL = Path("/tmp/ttasqiirt-p26-8db08306")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    needed = [
        "NATIVE_INTRINSIC_SYNTAX_AND_METATHEORY_ENTRYPOINT_ACCEPTED_WITH_SCOPE",
        "INTRINSIC_SYNTAX_NOT_GLOBAL_SELF_VALIDATION",
        "EXPLICIT_UIP_AND_TERMINATION_TRUST_BOUNDARIES",
        "P27-REFLECTION-CONSUMER-DISCOVERY-2026-001",
        "NO_NEW_HOTT_DEFECT_CLAIM",
        "NO_NAMED_OBJECT_PROVABILITY_CHAIN_WITHIN_LITERAL_DENOMINATOR",
    ]
    missing = [item for item in needed if item not in report]
    mismatches = []
    for relative, expected in freeze["external_files_sha256"].items():
        path = EXTERNAL / relative
        actual = sha256(path) if path.is_file() else None
        if actual != expected:
            mismatches.append({"path": relative, "expected": expected, "actual": actual})
    run = json.loads(RUN.read_text(encoding="utf-8"))
    anchors = {}
    if not mismatches:
        syntax = (EXTERNAL / "src/Theory/SC/QIIRT-tyOf/Syntax.agda").read_text(encoding="utf-8")
        index = (EXTERNAL / "src/index.agda").read_text(encoding="utf-8")
        rec = (EXTERNAL / "src/Theory/SC/QIIRT-tyOf/Rec.agda").read_text(encoding="utf-8")
        set_model = (EXTERNAL / "src/Theory/SC/QIIRT-tyOf/Model/Set.agda").read_text(encoding="utf-8")
        reflection = (EXTERNAL / "src/Cubical/Reflection/StrictEquiv.agda").read_text(encoding="utf-8")
        anchors = {
            "intrinsic_ctx_ty_tm_tyof": all(token in syntax for token in ("data Ctx", "data Ty", "data Tm", "tyOf")),
            "index_excludes_incomplete_advanced_modules": "The following files are not complete" in index and "Canonicity" in index and "LogPred" in index,
            "termination_pragma_in_imported_recursion": "{-# TERMINATING #-}" in rec,
            "uip_postulate_in_standard_model": "postulate" in set_model and "UIP" in set_model,
            "reflection_is_agda_builtin_reflection": "Agda.Builtin.Reflection" in reflection,
        }
    run_ok = (
        run.get("external_commit") == "8db08306287333067b2749f95f8ad3ba7a0e14d1"
        and run.get("status") == "DEFAULT_ENTRYPOINT_ACCEPTED_SAFE_CONFIGURATION_REJECTED_WITH_SCOPE"
        and run.get("default_ignore_interfaces", {}).get("exit_code") == 0
        and run.get("safe_ignore_interfaces", {}).get("exit_code") == 42
    )
    status = "PASS_WITH_SCOPE" if not missing and not mismatches and all(anchors.values()) and run_ok else "FAIL"
    result = {
        "schema_version": "p26-ttasqiirt-intrinsic-type-theory-verification/v1",
        "task_id": freeze["task_id"],
        "status": status,
        "verdict": freeze["verdict"],
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing,
        "external_source_hash_mismatches": mismatches,
        "source_anchors": anchors,
        "run_ok": run_ok,
        "scope": "Checks P26 source identity, source-level boundary anchors and saved external run receipt. It does not prove a HoTT theorem, global self-validation, no-glue execution, or a defect.",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
