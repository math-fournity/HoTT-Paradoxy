#!/usr/bin/env python3
"""Unit tests for the reader-banner policy on shard indexes (audit layer)."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import logical_document as LD  # noqa: E402

MARKER = "<!-- governance-shard-index:v2\nlogical_id: T\nmode: topical\nshard_root: T\n" \
         "last_shard: T/001 - x.md\nappend_target: -\nsoft_line_target: 300\n-->\n"
BANNER = ("> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 1 个分片；缺一片即未完成，按表顺序读取。\n")


class BannerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="banner-test-")
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, text: str) -> None:
        (self.root / "T.md").write_text(text, encoding="utf-8")

    def test_banner_present_passes(self) -> None:
        self.write(MARKER + "\n" + BANNER + "\nbody\n")
        self.assertEqual(LD.canonical_indexes(self.root), ["T.md"])
        self.assertEqual(LD.banner_issues(self.root), [])

    def test_missing_banner_flagged(self) -> None:
        self.write(MARKER + "\n# T\n\nbody\n")
        self.assertEqual(LD.banner_issues(self.root), ["MISSING_READER_BANNER:T.md"])

    def test_incomplete_banner_flagged(self) -> None:
        self.write(MARKER + "\n> ⚠️ 逻辑文档索引：只是索引。\n\nbody\n")
        self.assertEqual(LD.banner_issues(self.root), ["INCOMPLETE_READER_BANNER:T.md"])

    def test_banner_outside_window_flagged(self) -> None:
        filler = "".join(f"line {n}\n" for n in range(LD.READER_BANNER_WINDOW + 2))
        self.write(MARKER + filler + BANNER)
        self.assertEqual(LD.banner_issues(self.root), ["MISSING_READER_BANNER:T.md"])

    def test_checkpoint_copies_are_excluded(self) -> None:
        path = self.root / ".codex/cognition/checkpoints/S1/after/T.md"
        path.parent.mkdir(parents=True)
        path.write_text(MARKER + "# T\n", encoding="utf-8")
        self.assertEqual(LD.canonical_indexes(self.root), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
