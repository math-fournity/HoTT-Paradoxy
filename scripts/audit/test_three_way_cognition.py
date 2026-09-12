#!/usr/bin/env python3
"""Positive and negative tests for verify_three_way_cognition.py."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("verify_three_way_cognition.py")
SPEC = importlib.util.spec_from_file_location("verify_three_way_cognition", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ThreeWayTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / ".codex/cognition").mkdir(parents=True)
        (self.root / ".codex/research/hott").mkdir(parents=True)
        load_set = {
            "schema_version": "cognition-load-set/v2",
            "fixed_full_text": ["核心认知.md", "方向追踪.md", "全景视野.md"],
            "three_way_order": ["核心认知.md", "方向追踪.md", "全景视野.md"],
        }
        state = {"revision": 1}
        core_manifest = {"schema_version": "core-cognition/v1", "units": [{"id": "KC-000001"}]}
        self.write(".codex/cognition/LOAD_SET.json", load_set)
        self.write(".codex/research/hott/STATE.json", state)
        self.write("核心认知.manifest.json", core_manifest)
        self.write("核心认知.md", "# core\n")
        self.write(
            "方向追踪.md",
            """<!-- integrated-direction-portfolio:v1\nsource_state_revision: 1\n-->\n| direction_id | 方向 | 结果 |\n|---|---|---|\n| `DIR-A` | a | `OUT-A` |\n""",
        )
        self.write(
            "全景视野.md",
            """<!-- integrated-outcome-panorama:v1\nsource_state_revision: 1\n-->\n| result_id | 结果 | 方向 |\n|---|---|---|\n| `OUT-A` | a | `DIR-A` |\n""",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, rel: str, value: object) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, str):
            path.write_text(value, encoding="utf-8")
        else:
            path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def test_valid_three_way_projection(self) -> None:
        self.assertEqual(MODULE.validate(self.root)["status"], "PASS")

    def test_wrong_fixed_order_rejected(self) -> None:
        path = self.root / ".codex/cognition/LOAD_SET.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["fixed_full_text"] = ["方向追踪.md", "核心认知.md", "全景视野.md"]
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
        with self.assertRaisesRegex(MODULE.ThreeWayError, "FIXED_ORDER"):
            MODULE.validate(self.root)

    def test_orphan_outcome_rejected(self) -> None:
        path = self.root / "全景视野.md"
        path.write_text(path.read_text(encoding="utf-8").replace("DIR-A", "DIR-MISSING"), encoding="utf-8")
        with self.assertRaisesRegex(MODULE.ThreeWayError, "ORPHAN"):
            MODULE.validate(self.root)


if __name__ == "__main__":
    unittest.main()
