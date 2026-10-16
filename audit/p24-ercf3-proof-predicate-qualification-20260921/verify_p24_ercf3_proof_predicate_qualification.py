#!/usr/bin/env python3
"""Verify the bounded P24 ERCF-3 bridge qualification record."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-REPORT.md"
FREEZE = OUT / "P24-ERCF3-SOURCE-FREEZE.json"
RESULT = OUT / "P24-ERCF3-PROOF-PREDICATE-QUALIFICATION-VERIFICATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    required_report_tokens = [
        "OBJECT_LEVEL_PROVABILITY_BRIDGE_NOT_ESTABLISHED",
        "NATURAL_SELF_VERIFICATION_CONSUMER_NOT_ESTABLISHED_WITHIN_P24_DENOMINATOR",
        "KNOWN_ANALOGUE_AND_SPECIFICATION_CONTROL",
        "P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-001",
        "NO_NEW_HOTT_DEFECT_CLAIM",
        "ASSUMED_SCHEMA_NOT_REPRESENTABILITY_THEOREM",
        "NAMED_UNINHABITED_OBLIGATION",
    ]
    missing_report_tokens = [token for token in required_report_tokens if token not in report]
    hash_mismatches = []
    for relative, expected in freeze["local_sources"].items():
        path = ROOT / relative
        actual = sha256(path) if path.is_file() else None
        if actual != expected:
            hash_mismatches.append({"path": relative, "expected": expected, "actual": actual})

    object_syntax = (ROOT / "HoTT/formal/ercf3-t3/ObjectSyntax.agda").read_text(encoding="utf-8")
    representability = (ROOT / "HoTT/formal/ercf3-t3/ProvRepresentability.agda").read_text(encoding="utf-8")
    reflection = (ROOT / "HoTT/formal/ercf3-t3/ReflectionSketch.agda").read_text(encoding="utf-8")
    repaired = (ROOT / "HoTT/formal/ercf3-t3/RepairedSyntax.agda").read_text(encoding="utf-8")
    semantic_anchors = {
        "prov_is_derivability_interface": "Prov φ = ⊢ φ" in object_syntax,
        "repr_is_constructor_schema": "repr : (φ : FmlP)" in representability,
        "repr_all_is_direct_application": "reprAll φ = repr φ" in representability,
        "reflect_is_named_type": "Reflect : Set" in reflection,
        "reflect_alias_does_not_inhabit": "reflectIsNamedObligation = Reflect" in reflection,
        "repaired_syntax_has_formula_substitution_agreement": "substCodeF-agrees" in repaired,
        "repaired_syntax_has_diagonal_code_relation": "diagonalize'-code" in repaired,
    }
    external = freeze["external_source_observations"]
    external_pin_ok = (
        external["hottlean"]["remote_head"] == "31133dd5b25226ea897f8aa5e2e43b61392459eb"
        and external["coquand_agda_godel_tree"]["remote_head"] == "5475628ea4b648f956dce4baee7d0273ba257730"
    )
    status = "PASS_WITH_SCOPE" if not missing_report_tokens and not hash_mismatches and all(semantic_anchors.values()) and external_pin_ok else "FAIL"
    result = {
        "schema_version": "p24-ercf3-proof-predicate-qualification-verification/v1",
        "task_id": freeze["task_id"],
        "status": status,
        "verdict": freeze["verdict"],
        "report_sha256": sha256(REPORT),
        "freeze_sha256": sha256(FREEZE),
        "missing_report_tokens": missing_report_tokens,
        "source_hash_mismatches": hash_mismatches,
        "semantic_anchors": semantic_anchors,
        "external_pin_ok": external_pin_ok,
        "scope": "Checks the frozen P24 report, local source identities, and source-level bridge anchors. It does not prove a Gödel theorem, a HoTT theorem, a HoTT defect, or source-level behavior of the external projects.",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if status == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
