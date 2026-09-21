#!/usr/bin/env python3
"""Verify P13's scoped reuse and operation-class distinction."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / "P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-REPORT.md"
FREEZE = OUT / "P13-AMBIENT-PAIR-EVIDENCE-FREEZE.json"
RECEIPT = OUT / "P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-VERIFICATION.json"
RUNS = {
    "ambient": "HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02/RUN.json",
    "curve": "HoTT/verification/runs/20260920-MP-ASTRA-CURVE-DEFORMATION-001-02/RUN.json",
    "structured": "HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/RUN.json",
}
EXPECTED_RUNS = {
    "ambient": ("MP-ASTRA-AMBIENT-CIRCLE-001", ["C-266", "C-267", "C-268"]),
    "curve": ("MP-ASTRA-CURVE-DEFORMATION-001", ["C-269", "C-270"]),
    "structured": ("MP-ASTRA-STRUCTURED-CURVE-001", ["C-275", "C-276", "C-277"]),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def manifest_hashes(rel: str) -> dict[str, str]:
    data = json.loads(read(rel))
    return {row["path"]: row["sha256"] for row in data["files"] if "path" in row and "sha256" in row}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = REPORT.read_text(encoding="utf-8")
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    required = [
        "R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE", "OPERATION_CLASS_SPLIT_REQUIRED",
        "H_intrinsic", "Done_ambient^fin", "Done_curve", "C-266", "C-267", "C-268",
        "C-269", "C-270", "P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-001",
        "NO_ACTUAL_K", "NO_NEW_HOTT_DEFECT_CLAIM",
    ]
    missing = [item for item in required if item not in report]
    sources = {entry["path"]: entry["sha256"] for entry in freeze["sources"]}
    current = {path: sha(ROOT / path) for path in sources}
    run_details = {}
    for key, rel in RUNS.items():
        data = json.loads(read(rel))
        proof_id, claim_ids = EXPECTED_RUNS[key]
        ok = data.get("status") == "KERNEL_ACCEPTED_WITH_SCOPE" and data.get("proof_id") == proof_id and data.get("claim_ids") == claim_ids
        if not ok:
            raise SystemExit(f"RUN_IDENTITY_MISMATCH:{rel}")
        run_details[key] = {"path": rel, "sha256": sha(ROOT / rel), "git_status": data.get("git_status")}
    manifests = {
        "ambient": manifest_hashes("HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02/source-manifest.json"),
        "curve": manifest_hashes("HoTT/verification/runs/20260920-MP-ASTRA-CURVE-DEFORMATION-001-02/source-manifest.json"),
        "structured": manifest_hashes("HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/source-manifest.json"),
    }
    manifest_checks = {
        "AmbientCircle.lean": manifests["ambient"].get("HoTT/formal/astra-real-geometry/AmbientCircle.lean") == current["HoTT/formal/astra-real-geometry/AmbientCircle.lean"],
        "DeformationCircle.lean": manifests["curve"].get("HoTT/formal/astra-real-geometry/DeformationCircle.lean") == current["HoTT/formal/astra-real-geometry/DeformationCircle.lean"],
        "StructuredCurve.lean": manifests["structured"].get("HoTT/formal/astra-real-geometry/StructuredCurve.lean") == current["HoTT/formal/astra-real-geometry/StructuredCurve.lean"],
    }
    if not all(manifest_checks.values()):
        raise SystemExit("SOURCE_MANIFEST_MISMATCH")
    source_markers = {
        "ambient": ["embeddedIntrinsicHomeomorph", "runAmbient", "no_finite_ambient_reconstruction"],
        "curve": ["exists_curve_deformation", "deformation_initial_image", "deformation_final_image"],
        "structured": ["PresentationEquivalence", "no_concrete_structure_equivalence", "no_bare_coincidence_transport"],
    }
    source_paths = {
        "ambient": "HoTT/formal/astra-real-geometry/AmbientCircle.lean",
        "curve": "HoTT/formal/astra-real-geometry/DeformationCircle.lean",
        "structured": "HoTT/formal/astra-real-geometry/StructuredCurve.lean",
    }
    source_markers_ok = {key: all(token in read(source_paths[key]) for token in tokens) for key, tokens in source_markers.items()}
    if not all(source_markers_ok.values()):
        raise SystemExit("SOURCE_MARKER_MISSING")
    result = {
        "schema_version": "p13-ambient-pair-rmin-requalification-verification/v1",
        "task_id": "P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-001",
        "status": "PASS_WITH_SCOPE" if not missing and current == sources else "FAIL",
        "verdict": "R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE / OPERATION_CLASS_SPLIT_REQUIRED / P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY_NEXT / NO_ACTUAL_K / NO_NEW_HOTT_DEFECT_CLAIM",
        "scope": "Checks declared existing-source identities, preserved kernel-receipt identities, and the report's operation-class distinction. It does not rerun Lean, prove a general isotopy-extension theorem, formalize native HoTT, find K, or prove a HoTT defect.",
        "sources": {str(REPORT.relative_to(ROOT)): sha(REPORT), str(FREEZE.relative_to(ROOT)): sha(FREEZE), **current},
        "missing_required_tokens": missing,
        "run_details": run_details,
        "manifest_checks": manifest_checks,
        "source_markers_ok": source_markers_ok,
        "external_sources_checked": [
            "https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rolfsen.pdf",
            "https://mathworld.wolfram.com/AmbientIsotopy.html",
        ],
    }
    if args.write:
        RECEIPT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "PASS_WITH_SCOPE" else 1)


if __name__ == "__main__":
    main()
