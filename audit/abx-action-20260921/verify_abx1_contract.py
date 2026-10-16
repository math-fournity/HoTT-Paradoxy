#!/usr/bin/env python3
"""Qualify the existing formal controls used by the first ABX task contract.

This is deliberately a source/run qualification, not a fresh kernel replay.
It verifies that the retained runs still bind the named sources and claim rows,
then records the small source denominator used for the first K-consumer scan.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "ABX-1-FORMAL-QUALIFICATION.json"
VERIFY = ROOT / "scripts/audit/verify_formal_proof_run.py"
RUNS = (
    ("20260919-MP-ASTRA-RESTORE-CRITERION-01", "MP-ASTRA-RESTORE-CRITERION-001", ("C-261", "C-262")),
    ("20260919-MP-ASTRA-QCIRCLE-RESTORE-01", "MP-ASTRA-QCIRCLE-RESTORE-001", ("C-263",)),
    ("20260919-MP-ASTRA-HIT-RESTORE-CONTROL-02", "MP-ASTRA-HIT-RESTORE-CONTROL-001", ("C-264",)),
    ("20260920-MP-ASTRA-PUNCTURE-APARTNESS-001-01", "MP-ASTRA-PUNCTURE-APARTNESS-001", ("C-283", "C-284")),
    ("20260920-MP-ASTRA-NATIVE-STEREOGRAPHIC-001-01", "MP-ASTRA-NATIVE-STEREOGRAPHIC-001", ("C-285", "C-286")),
    ("20260920-MP-ASTRA-NATIVE-INTERVAL-001-01", "MP-ASTRA-NATIVE-INTERVAL-001", ("C-289", "C-290")),
    ("20260920-MP-ASTRA-NATIVE-COMPLETION-001-01", "MP-ASTRA-NATIVE-COMPLETION-001", ("C-291", "C-292")),
    ("20260920-MP-ASTRA-NATIVE-RICH-TASK-001-02", "MP-ASTRA-NATIVE-RICH-TASK-001", ("C-293", "C-294")),
    ("20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01", "MP-ASTRA-NATIVE-SOURCE-CONTRACT-001", ("C-295", "C-296")),
    ("20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01", "MP-ASTRA-NATIVE-TASK-INTEGRATION-001", ("C-320",)),
)
NATIVE = "HoTT/formal/agda-unimath/hott-z"
UNIMATH = Path("/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d")
CUBICAL = Path("/Volumes/D/HoTT-toolchain-cache/cubical-v0.9/cubical")
ANCHORS = {
    f"{NATIVE}/NativeRealCircleQualification.agda": ("RealCircle", "east north", "PuncturedRealCircle", "OpenRealInterval"),
    f"{NATIVE}/PunctureApartness.agda": ("Weak", "StrongPuncture", "forgetStrong", "Lift"),
    f"{NATIVE}/NativeOpenInterval.agda": ("strongCircleUnitHomeomorphism", "weakCircleUnitHomeomorphism", "strongIntervalTypePath"),
    f"{NATIVE}/NativeCompletion.agda": ("mCompletion", "nCompletion", "mInterior"),
    f"{NATIVE}/NativeRichCurve.agda": ("RichCurve", "Bare", "noAnyBarePathLift", "noUniformBareRecovery"),
    f"{NATIVE}/NativeSourceContract.agda": ("Input", "Denotes", "Satisfies", "plainNDoesNotDenote", "bareCheckIsInsufficient"),
    f"{NATIVE}/NativeTaskIntegration.agda": ("CurveRun", "samePairDifferentOperations", "noCurveAmbientEquivalence"),
    "HoTT/formal/astra-breakpoint-check/PointRestoration.agda": ("SplitRestore", "PointDecidable", "restorationEquiv"),
    "HoTT/formal/astra-breakpoint-check/RationalRestoration.agda": ("restoreQCircle", "specifiedPointPreserved"),
    "HoTT/formal/astra-breakpoint-check/HomotopyRestorationControl.agda": ("noHomotopySplit", "noPointDecision"),
}
K_DENOMINATOR = {
    "agda_unimath_commit": "7b81411d9f60afec359d29ed1e4edf43f4711c8a",
    "files": (
        "src/metric-spaces/uniform-homeomorphisms-metric-spaces.lagda.md",
        "src/metric-spaces/totally-bounded-metric-spaces.lagda.md",
        "src/real-numbers/uniform-homeomorphism-unit-interval-proper-closed-interval-real-numbers.lagda.md",
    ),
    "local_controls": (
        f"{NATIVE}/NativeSourceContract.agda",
        f"{NATIVE}/NativeTaskIntegration.agda",
    ),
    "cubical_literal_tree": str(CUBICAL),
    "query": "homeomorphism|Homeomorphism",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_verifier(run_id: str, proof_id: str, claims: tuple[str, ...]) -> dict:
    result = subprocess.run(
        [sys.executable, "-B", str(VERIFY), "--run-dir", f"HoTT/verification/runs/{run_id}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"formal-run verifier failed for {run_id}: {result.stderr}")
    row = json.loads(result.stdout)
    if row.get("status") != "PASS_WITH_SCOPE":
        raise SystemExit(f"unexpected status for {run_id}: {row.get('status')}")
    if row.get("proof_id") != proof_id or tuple(row.get("claim_ids", ())) != claims:
        raise SystemExit(f"identity mismatch for {run_id}")
    if row.get("kernel_status") != "KERNEL_ACCEPTED_WITH_SCOPE":
        raise SystemExit(f"kernel status mismatch for {run_id}")
    if row.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit(f"index status mismatch for {run_id}")
    if row.get("replay") != "NOT_RUN":
        raise SystemExit(f"unexpected replay state for {run_id}")
    return row


def text_file(rel: str) -> Path:
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f"missing source: {rel}")
    return path


def main() -> None:
    checked_runs = [run_verifier(*row) for row in RUNS]
    anchor_receipts = {}
    for rel, required in ANCHORS.items():
        path = text_file(rel)
        body = path.read_text()
        missing = [value for value in required if value not in body]
        if missing:
            raise SystemExit(f"anchor mismatch in {rel}: {missing}")
        anchor_receipts[rel] = {"sha256": digest(path), "required_anchors": list(required)}

    unimath_files = []
    for rel in K_DENOMINATOR["files"][:3]:
        path = UNIMATH / rel
        if not path.is_file():
            raise SystemExit(f"missing pinned agda-unimath source: {path}")
        unimath_files.append({"path": str(path), "sha256": digest(path)})

    local_control_files = []
    for rel in K_DENOMINATOR["local_controls"]:
        path = text_file(rel)
        local_control_files.append({"path": rel, "sha256": digest(path)})

    cubical_scan = subprocess.run(
        ["rg", "-l", "--glob", "*.agda", K_DENOMINATOR["query"], str(CUBICAL)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if cubical_scan.returncode not in (0, 1):
        raise SystemExit(f"Cubical literal scan failed: {cubical_scan.stderr}")
    cubical_matches = [line for line in cubical_scan.stdout.splitlines() if line]

    result = {
        "schema_version": "abx-1-formal-qualification/v1",
        "status": "PASS_WITH_SCOPE",
        "scope": "Existing proof runs and source anchors for the ABX-1 task contract; no proof command was replayed.",
        "formal_runs": checked_runs,
        "source_anchors": anchor_receipts,
        "candidate_contract": {
            "C": "NativeRealCircleQualification.RealCircle",
            "p": "NativeRealCircleQualification.east",
            "M_weak": "PuncturedRealCircle = Σ RealCircle (λ q → q ≠ east)",
            "M_strong": "StrongPuncture = Σ RealCircle Strong",
            "N": "OpenRealInterval",
            "H_top": "strongCircleUnitHomeomorphism / strongIntervalTypePath; weak version requires Lift",
            "R_origin_surrogate": "RichCurve's parametrization, realization, continuous closed diagram, and interior agreement",
            "U": "NativeRichCurve.Bare",
            "Done_weak": "Bare r = Input.targetCarrier actualInput",
            "Done_strong": "Satisfies actualInput r = carrier match × Denotes exact closed diagram",
        },
        "K_denominator_D_ABX_1": {
            **K_DENOMINATOR,
            "pinned_source_files": unimath_files,
            "local_control_files": local_control_files,
            "cubical_literal_match_count": len(cubical_matches),
            "cubical_literal_matches": cubical_matches,
            "verdict": "NO_K_WITHIN_DECLARED_DENOMINATOR",
            "meaning": (
                "The inspected uniform-homeomorphism consumers transport metric properties of their declared input spaces; "
                "the two local consumers preserve or distinguish the rich contract; the literal Cubical scan has no "
                "homeomorphism-named file. This is not a semantic search of all Cubical/HoTT code or an absence theorem."
            ),
        },
        "not_proved": [
            "an unrestricted geometric or physical restoration impossibility",
            "a full R_origin/provenance theorem beyond the declared RichCurve surrogate",
            "an actual HoTT consumer that mistakes Done_weak for Done_strong",
            "a HoTT inconsistency, defect, or global safety theorem",
        ],
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "qualified_runs": len(checked_runs),
        "cubical_literal_match_count": len(cubical_matches),
        "K_verdict": result["K_denominator_D_ABX_1"]["verdict"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
