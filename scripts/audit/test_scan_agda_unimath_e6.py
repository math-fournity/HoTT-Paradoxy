#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("scan_agda_unimath_e6.py")
SPEC = importlib.util.spec_from_file_location("scan_agda_unimath_e6", SCRIPT)
assert SPEC and SPEC.loader
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)


class ScanTests(unittest.TestCase):
    def test_literate_parser_counts_only_agda_code(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "sample.lagda.md"
            path.write_text(
                "postulate proseOnly\n\n```text\npostulate textFence\n```\n\n"
                "```agda\npostulate\n  realAxiom : Set\nprimitive\n  primThing : Set\n```\n",
                encoding="utf-8",
            )
            self.assertEqual(
                [(row["kind"], row["line"]) for row in S.declarations(path)],
                [("postulate", 8), ("primitive", 10)],
            )

    def test_source_anchor_requires_every_pattern(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw); path = root / "x.lagda.md"
            path.write_text("alpha\nbeta\n", encoding="utf-8")
            result = S.source_anchor(root, "x.lagda.md", [r"alpha", r"beta"])
            self.assertEqual([row["line"] for row in result["hits"]], [1, 2])
            with self.assertRaisesRegex(S.ScanError, "REQUIRED_ANCHOR_MISSING"):
                S.source_anchor(root, "x.lagda.md", [r"gamma"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
