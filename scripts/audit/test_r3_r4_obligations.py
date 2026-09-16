#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/audit/build_r3_r4_obligations.py"
SPEC = importlib.util.spec_from_file_location("r3_r4", SCRIPT)
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class R3R4ObligationTests(unittest.TestCase):
    def test_exact_denominator_and_statuses(self) -> None:
        matrix, _ = M.build_core()
        self.assertEqual(len(matrix["obligations"]), 12)
        self.assertEqual(len({row["id"] for row in matrix["obligations"]}), 12)
        self.assertEqual(matrix["input_remainder"], 0)
        self.assertEqual(matrix["counts"]["by_status"]["PRESENT_MACHINE_PROVED"], 2)
        self.assertEqual(matrix["counts"]["by_status"]["ABSENT_BY_DEFINITION"], 3)
        self.assertEqual(matrix["counts"]["by_status"]["OPEN"], 7)

    def test_host_features_do_not_fill_object_calculus(self) -> None:
        matrix, _ = M.build_core()
        rows = {row["id"]: row for row in matrix["obligations"]}
        self.assertEqual(rows["H-ID/PATH"]["status"], "ABSENT_BY_DEFINITION")
        self.assertEqual(rows["H-UNIVALENCE/HIT"]["status"], "ABSENT_BY_DEFINITION")
        self.assertEqual(rows["H-PROOF-CODE"]["status"], "OPEN")
        self.assertEqual(matrix["hott_essentiality"], "NOT_ESTABLISHED")

    def test_r3_does_not_auto_promote_r4(self) -> None:
        matrix, _ = M.build_core()
        self.assertEqual(matrix["source_theory"]["claims"], ["C-244", "C-245", "C-246", "C-247", "C-248", "C-249"])
        self.assertEqual(matrix["r4_readiness"], "NOT_READY")
        self.assertIn("H-INDEPENDENCE", matrix["blocking_obligations"])

    def test_deleting_known_obligation_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="r3-r4-negative-") as name:
            temp = Path(name)
            for filename in ("R3-R4-OBLIGATIONS.json", "REPORT.md", "RECEIPT.json"):
                shutil.copyfile(ROOT / "audit/r3-r4-godel" / filename, temp / filename)
            path = temp / "R3-R4-OBLIGATIONS.json"
            matrix = json.loads(path.read_text(encoding="utf-8"))
            matrix["obligations"] = [row for row in matrix["obligations"] if row["id"] != "H-NAT"]
            path.write_bytes(M.json_bytes(matrix))
            with self.assertRaisesRegex(ValueError, "OBLIGATION_DENOMINATOR_MISMATCH"):
                M.validate(temp)

    def test_bundle_is_deterministic_and_current_output_valid(self) -> None:
        self.assertEqual(M.bundle(), M.bundle())
        result = M.validate(ROOT / "audit/r3-r4-godel")
        self.assertIn(result["status"], {"VALID", "VALID_WITH_SOURCE_EVOLUTION"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
