from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import natural_consumer_audit as audit
from machine_overview.util import MachineOverviewError


class NaturalConsumerInventoryTest(unittest.TestCase):
    def test_page_and_keyword_locations_are_deterministic(self) -> None:
        lines = [
            "===== PDF_PAGE 3 =====",
            "A clock tick records one time step.",
            "Paths express equality, not an arrival event.",
        ]
        result = audit._hits_from_lines(lines)
        self.assertEqual(result["counts"]["clock"], 1)
        self.assertEqual(result["counts"]["tick"], 1)
        self.assertEqual(result["counts"]["time"], 1)
        self.assertEqual(result["counts"]["path"], 1)
        self.assertEqual(result["counts"]["arrival"], 1)
        self.assertEqual(result["captured_hits"]["clock"][0]["pdf_page"], 3)

    def test_tree_scan_records_relative_source_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.agda").write_text("clock tick\npath interval\n", encoding="utf-8")
            result = audit._scan_tree(root)
            self.assertEqual(result["scanned_files"], 1)
            self.assertEqual(result["counts"]["clock"], 1)
            self.assertEqual(result["captured_hits"]["path"][0]["source_path"], "sample.agda")

    def test_external_artifact_must_stay_in_declared_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            cache = Path(directory) / "cache"
            cache.mkdir()
            outside = Path(directory) / "outside.txt"
            outside.write_text("time", encoding="utf-8")
            with self.assertRaisesRegex(MachineOverviewError, "PATH_OUTSIDE_DECLARED_ROOT"):
                audit._under(outside, cache, "test")


if __name__ == "__main__":
    unittest.main()
