from __future__ import annotations

import hashlib
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ROOT = ROOT / "HoTT/verification/runs"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL = ROOT / "HoTT/formal/cubical-godel-infrastructure"
VERIFY = ROOT / "scripts/audit/verify_formal_proof_run.py"

PACKAGES = [
    (
        "20260914-CUBICAL-GODEL-PROOF-CHECKER-001",
        "PF-CUBICAL-GODEL-PROOF-CHECKER-001",
        [
            "MP-CGI-EQUALITY-001",
            "MP-CGI-CHECK-SOUND-001",
            "MP-CGI-CHECK-COMPLETE-001",
            "MP-CGI-TRUNCATED-PROVABILITY-001",
            "MP-CGI-CONTROLS-001",
        ],
    ),
    (
        "20260914-CUBICAL-GODEL-PROOF-SERIALIZATION-001",
        "PF-CUBICAL-GODEL-PROOF-SERIALIZATION-001",
        [
            "MP-CGI-SERIALIZE-ROUNDTRIP-001",
            "MP-CGI-SERIALIZED-CHECK-001",
            "MP-CGI-SERIALIZED-CONTROLS-001",
        ],
    ),
    (
        "20260914-CUBICAL-GODEL-FORMULA-BITCODE-001",
        "PF-CUBICAL-GODEL-FORMULA-BITCODE-001",
        [
            "MP-CGI-FML-BIT-LENGTH-001",
            "MP-CGI-FML-PARSER-001",
            "MP-CGI-FML-BIT-ROUNDTRIP-001",
        ],
    ),
    (
        "20260914-CUBICAL-GODEL-PROOF-BITCODE-001",
        "PF-CUBICAL-GODEL-PROOF-BITCODE-001",
        [
            "MP-CGI-TOKEN-BIT-ROUNDTRIP-001",
            "MP-CGI-PROOF-BIT-ROUNDTRIP-001",
            "MP-CGI-PROOF-BIT-CHECK-001",
            "MP-CGI-PROOF-BIT-CONTROLS-001",
        ],
    ),
    (
        "20260914-CUBICAL-GODEL-NAT-PROOF-CODE-001",
        "PF-CUBICAL-GODEL-NAT-PROOF-CODE-001",
        [
            "MP-CGI-PROOF-PREFIX-001",
            "MP-CGI-BIT-NAT-ROUNDTRIP-001",
            "MP-CGI-NAT-PROOF-ROUNDTRIP-001",
            "MP-CGI-NAT-PROOF-CHECK-001",
            "MP-CGI-NAT-PROOF-CONTROLS-001",
        ],
    ),
    (
        "20260914-CUBICAL-SYNTHETIC-INCOMPLETENESS-001",
        "PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001",
        [
            "MP-CSI-PARTIAL-BOOL-001",
            "MP-CSI-SEPARATOR-DIVERGENCE-001",
            "MP-CSI-EFFECTIVE-SYSTEM-001",
            "MP-CSI-INDEPENDENT-SENTENCE-001",
            "MP-CSI-ESSENTIAL-INCOMPLETENESS-001",
        ],
    ),
    (
        "20260914-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001",
        "PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001",
        [
            "MP-CGI-SEMANTIC-CONSISTENCY-001",
            "MP-CGI-PROOF-CORE-001",
            "MP-CGI-PROOF-CLASSIFIER-001",
            "MP-CGI-FORMAL-SYSTEM-INSTANCE-001",
        ],
    ),
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class CubicalGodelInfrastructureTest(unittest.TestCase):
    def test_every_stage_has_an_indexed_kernel_receipt_and_exact_rows(self) -> None:
        for run_id, proof_id, claim_ids in PACKAGES:
            with self.subTest(run_id=run_id):
                run_dir = RUN_ROOT / run_id
                run = load(run_dir / "RUN.json")
                rows = load(run_dir / "index-row-manifest.json")
                self.assertEqual(run["run_id"], run_id)
                self.assertEqual(run["proof_id"], proof_id)
                self.assertEqual(run["claim_ids"], claim_ids)
                self.assertEqual(run["status"], "KERNEL_ACCEPTED_WITH_SCOPE")
                self.assertEqual(run["index_status"], "INDEXED_IN_CLAIM_EVIDENCE_MATRIX")
                self.assertEqual(run["exit_code"], 0)
                self.assertEqual(run["stderr"]["bytes"], 0)
                self.assertEqual(rows["proof_id"], proof_id)
                self.assertEqual(rows["claim_ids"], claim_ids)
                self.assertEqual(len(rows["rows"]), len(claim_ids) + 1)
                self.assertEqual(rows["rows"][0]["id"], proof_id)
                self.assertEqual(
                    [row["id"] for row in rows["rows"][1:]], claim_ids
                )

    def test_frozen_row_hashes_still_identify_exact_matrix_lines(self) -> None:
        matrix_lines = MATRIX.read_text(encoding="utf-8").splitlines()
        matrix_hashes = {
            hashlib.sha256(line.encode("utf-8")).hexdigest() for line in matrix_lines
        }
        for run_id, _proof_id, _claim_ids in PACKAGES:
            rows = load(RUN_ROOT / run_id / "index-row-manifest.json")["rows"]
            for row in rows:
                with self.subTest(run_id=run_id, row=row["id"]):
                    self.assertIn(row["line_sha256"], matrix_hashes)

    def test_each_saved_package_verifies_without_native_reexecution(self) -> None:
        for run_id, _proof_id, _claim_ids in PACKAGES:
            with self.subTest(run_id=run_id):
                completed = subprocess.run(
                    [
                        "python3",
                        str(VERIFY),
                        "--project-root",
                        str(ROOT),
                        "--run-dir",
                        str(Path("HoTT/verification/runs") / run_id),
                    ],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                result = json.loads(completed.stdout)
                self.assertEqual(result["status"], "PASS_WITH_SCOPE")
                self.assertIn(
                    result["index_validation"],
                    {
                        "EXACT_INDEX_SNAPSHOT_MATCH",
                        "ROW_STABLE_AFTER_INDEX_EVOLUTION",
                    },
                )

    def test_nat_stage_accumulates_the_actual_coding_sources(self) -> None:
        run = load(
            RUN_ROOT
            / "20260914-CUBICAL-GODEL-NAT-PROOF-CODE-001/source-manifest.json"
        )
        paths = {row["path"] for row in run["files"]}
        expected = {
            "HoTT/formal/cubical-godel-infrastructure/MiniProofChecker.agda",
            "HoTT/formal/cubical-godel-infrastructure/ProofSerialization.agda",
            "HoTT/formal/cubical-godel-infrastructure/FormulaBitCode.agda",
            "HoTT/formal/cubical-godel-infrastructure/ProofBitCode.agda",
            "HoTT/formal/cubical-godel-infrastructure/NatProofCode.agda",
            "HoTT/formal/cubical-godel-infrastructure/NAT_PROOF_CODE_CLAIM.md",
        }
        self.assertTrue(expected.issubset(paths))

    def test_nat_source_exposes_total_checker_without_assumed_declarations(self) -> None:
        source = (FORMAL / "NatProofCode.agda").read_text(encoding="utf-8")
        for forbidden in ("postulate", "{-# TERMINATING #-}", "{-# NON_TERMINATING #-}"):
            self.assertNotIn(forbidden, source)
        for theorem in (
            "decodeProofNat",
            "codeProof-roundtrip",
            "codeProof-injective",
            "checkProofNat-code",
            "natChecked-sound",
            "derives→natChecked",
        ):
            self.assertIn(theorem, source)

    def test_classifier_run_records_both_cross_package_include_directories(self) -> None:
        run_dir = RUN_ROOT / "20260914-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001"
        run = load(run_dir / "RUN.json")
        manifest = load(run_dir / "source-manifest.json")
        expected = [
            "HoTT/formal/cubical-godel-infrastructure",
            "HoTT/formal/cubical-synthetic-incompleteness",
        ]
        self.assertEqual(run["include_dirs"], expected)
        self.assertEqual(manifest["include_dirs"], expected)
        argv = run["command_argv"]
        include_values = [argv[index + 1] for index, value in enumerate(argv) if value == "-i"]
        self.assertEqual(
            include_values,
            [str(ROOT / relative) for relative in expected],
        )


if __name__ == "__main__":
    unittest.main()
