#!/usr/bin/env python3
"""Freeze and classify the direct local consumers of the ABX circle symbols.

The denominator is intentionally narrow: project-local ``hott-z`` modules that
directly import one of the six ABX roots.  It is neither an agda-unimath-wide
semantic search nor a survey of the HoTT literature.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "HoTT/formal/agda-unimath/hott-z"
OUT = ROOT / "audit/abx-action-20260921/ABX-3-D2-DIRECT-CONSUMERS.json"
ROOTS = {
    "NativeOpenInterval",
    "NativeRichCurve",
    "NativeSourceContract",
    "NativeTaskIntegration",
    "PunctureApartness",
    "NativeCompletion",
}
IMPORT = re.compile(r"^open import hott-z\.([A-Za-z0-9-]+)", re.M)
CATEGORY = {
    "HomogeneousCircle.agda": "GEOMETRY_PREREQUISITE",
    "MarkovCountableChoice.agda": "EXPLICIT_PRINCIPLE_AND_DATA_SUPPLY",
    "NativeClosedMotionBase.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeClosedMotionContinuity.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeClosedMotionEndpoints.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeClosedMotionInterior.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeClosedSpatialBounds.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeClosedSpatialCoefficients.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeCompletion.agda": "CLOSED_DIAGRAM_MODEL",
    "NativeCompletionFibers.agda": "CLOSED_DIAGRAM_MODEL",
    "NativeCurveTask.agda": "TASK_SEPARATION_DEFENSE",
    "NativeCurveTaskControls.agda": "FULL_FIELD_TRANSPORT_DEFENSE",
    "NativeEndpointSeparation.agda": "CLOSED_MOTION_CONSTRUCTION",
    "NativeMotion.agda": "CURVE_CONSTRUCTION",
    "NativeMotionBridge.agda": "CURVE_CONSTRUCTION",
    "NativeMotionComplete.agda": "CONDITIONAL_WEAK_COVERAGE",
    "NativeMotionEmbedding.agda": "CURVE_CONSTRUCTION",
    "NativeMotionEndpoints.agda": "CURVE_CONSTRUCTION",
    "NativeOpenInterval.agda": "H_TOP_DEFINITION",
    "NativeRichCurve.agda": "R_ORIGIN_SURROGATE_AND_U_BOUNDARY",
    "NativeSourceContract.agda": "DONE_STRONG_DEFENSE",
    "NativeSpatialInequalities.agda": "GEOMETRY_PREREQUISITE",
    "NativeStereographic.agda": "GEOMETRY_EQUIVALENCE",
    "NativeTaskIntegration.agda": "OPERATION_CONTRACT_DEFENSE",
    "RealPrincipleBookScope.agda": "EXPLICIT_PRINCIPLE_ANALYSIS",
    "StereographicContinuity.agda": "GEOMETRY_EQUIVALENCE",
    "WeakCoverageMarkov.agda": "EXPLICIT_PRINCIPLE_ANALYSIS",
    "WeakLiftConsumer.agda": "CONDITIONAL_POINT_PRESERVING_REFINEMENT",
    "WeakLiftPrinciple.agda": "EXPLICIT_PRINCIPLE_ANALYSIS",
}
KEY_ANCHORS = {
    "NativeCurveTask.agda": ("bareSuccess", "noUniversalTraceLift"),
    "NativeCurveTaskControls.agda": ("fullTransportSuccess",),
    "NativeMotionComplete.agda": ("weakFinalCoverageIffLift", "weakChosenOutput"),
    "NativeRichCurve.agda": ("noAnyBarePathLift", "noUniformBareRecovery"),
    "NativeSourceContract.agda": ("plainNNotSatisfied", "bareCheckIsInsufficient"),
    "NativeTaskIntegration.agda": ("samePairDifferentOperations", "noCurveAmbientEquivalence"),
    "WeakLiftConsumer.agda": ("refinementPreservesPoint", "weakIntervalPathFromRealPrinciple"),
    "WeakCoverageMarkov.agda": ("fixedWeakCoverageImpliesBookMarkov",),
    "MarkovCountableChoice.agda": ("choiceMarkovGivesWeakCoverage", "No inhabitant"),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    rows = []
    for source in sorted(SOURCE_ROOT.glob("*.agda")):
        text = source.read_text()
        imports = [match.group(1) for match in IMPORT.finditer(text) if match.group(1) in ROOTS]
        if not imports:
            continue
        name = source.name
        if name not in CATEGORY:
            raise SystemExit(f"unclassified D_ABX_2 source: {name}")
        required = KEY_ANCHORS.get(name, ())
        missing = [anchor for anchor in required if anchor not in text]
        if missing:
            raise SystemExit(f"missing expected anchor in {name}: {missing}")
        rows.append({
            "path": source.relative_to(ROOT).as_posix(),
            "sha256": sha(source),
            "direct_abx_imports": imports,
            "classification": CATEGORY[name],
            "key_anchors": list(required),
            "is_actual_K": False,
        })
    if len(rows) != 29:
        raise SystemExit(f"D_ABX_2 denominator changed: expected 29, found {len(rows)}")
    if set(row["path"].split("/")[-1] for row in rows) != set(CATEGORY):
        raise SystemExit("D_ABX_2 category coverage mismatch")
    result = {
        "schema_version": "abx-d2-direct-consumers/v1",
        "status": "PASS_WITH_SCOPE",
        "denominator": {
            "root": "HoTT/formal/agda-unimath/hott-z",
            "selection": "all *.agda files directly importing at least one of NativeOpenInterval, NativeRichCurve, NativeSourceContract, NativeTaskIntegration, PunctureApartness, NativeCompletion",
            "expected_count": 29,
            "remainder": 0,
        },
        "records": rows,
        "verdict": "NO_K_WITHIN_D_ABX_2",
        "meaning": (
            "The declared direct-import denominator contains local geometry, conditional-principle, and explicit task-contract modules. "
            "Its closest consumers preserve source fields, require Lift/RealNonzeroApartness explicitly, or prove task contracts distinct. "
            "No module in this denominator treats a bare homeomorphism or U=Bare as completing Done_strong."
        ),
        "not_proved": [
            "no K exists in agda-unimath, Cubical, the HoTT Book, or other literature",
            "the classifications are a whole-library semantic proof",
            "any HoTT defect, inconsistency, or real-world restoration conclusion",
        ],
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    classes = {}
    for row in rows:
        classes[row["classification"]] = classes.get(row["classification"], 0) + 1
    print(json.dumps({
        "status": result["status"],
        "records": len(rows),
        "remainder": result["denominator"]["remainder"],
        "verdict": result["verdict"],
        "class_counts": classes,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
