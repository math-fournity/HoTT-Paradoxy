from __future__ import annotations

import hashlib
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "HoTT/formal/cubical-candidate-coverage"
RUN_DIR = ROOT / "HoTT/verification/runs/20260914-CUBICAL-CANDIDATE-COVERAGE-001"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
VERIFY = ROOT / "scripts/audit/verify_formal_proof_run.py"
CLAIMS = [
    "MP-CCC-RAW-ENUMERATION-001",
    "MP-CCC-NORMALIZATION-SEMANTICS-001",
    "MP-CCC-TASK-PRESERVATION-001",
    "MP-CCC-REDUCED-COVERAGE-001",
    "MP-CCC-CONTROLS-001",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class CubicalCandidateCoverageTest(unittest.TestCase):
    def test_source_contains_coverage_and_preservation_without_assumptions(self) -> None:
        source = (FORMAL / "CandidateCoverage.agda").read_text(encoding="utf-8")
        for forbidden in ("postulate", "{-# TERMINATING #-}", "{-# NON_TERMINATING #-}"):
            self.assertNotIn(forbidden, source)
        for theorem in (
            "allRaw-complete",
            "normalization-preserves-convergence",
            "normalization-preserves-deadline",
            "horizon-preserved",
            "expected-preserved",
            "observation-preserved",
            "reduced-space-complete",
        ):
            self.assertIn(theorem, source)

    def test_run_binds_exact_sources_claims_and_include_directories(self) -> None:
        run = load(RUN_DIR / "RUN.json")
        manifest = load(RUN_DIR / "source-manifest.json")
        self.assertEqual(run["proof_id"], "PF-CUBICAL-CANDIDATE-COVERAGE-001")
        self.assertEqual(run["claim_ids"], CLAIMS)
        self.assertEqual(run["status"], "KERNEL_ACCEPTED_WITH_SCOPE")
        self.assertEqual(run["index_status"], "INDEXED_IN_CLAIM_EVIDENCE_MATRIX")
        self.assertEqual(run["exit_code"], 0)
        self.assertEqual(run["stderr"]["bytes"], 0)
        self.assertEqual(
            run["include_dirs"],
            [
                "HoTT/formal/cubical-candidate-coverage",
                "HoTT/formal/partiality-race-timeout",
            ],
        )
        paths = {row["path"] for row in manifest["files"]}
        self.assertIn(
            "HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda",
            paths,
        )
        self.assertIn("HoTT/formal/cubical-candidate-coverage/CLAIM.md", paths)

    def test_frozen_rows_survive_matrix_evolution(self) -> None:
        frozen = load(RUN_DIR / "index-row-manifest.json")
        self.assertEqual(frozen["claim_ids"], CLAIMS)
        self.assertEqual(len(frozen["rows"]), 6)
        hashes = {
            hashlib.sha256(line.encode("utf-8")).hexdigest()
            for line in MATRIX.read_text(encoding="utf-8").splitlines()
        }
        for row in frozen["rows"]:
            self.assertIn(row["line_sha256"], hashes)

    def test_saved_run_verifies_and_retains_exact_scope_limits(self) -> None:
        completed = subprocess.run(
            [
                "python3",
                str(VERIFY),
                "--project-root",
                str(ROOT),
                "--run-dir",
                "HoTT/verification/runs/20260914-CUBICAL-CANDIDATE-COVERAGE-001",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "PASS_WITH_SCOPE")
        joined = " ".join(result["non_goals"])
        self.assertIn("No coverage of all HoTT terms", joined)
        self.assertIn("UnsupportedIndexedMatch", joined)
        stdout = (RUN_DIR / "stdout.txt").read_text(encoding="utf-8")
        self.assertIn("UnsupportedIndexedMatch", stdout)


if __name__ == "__main__":
    unittest.main()

