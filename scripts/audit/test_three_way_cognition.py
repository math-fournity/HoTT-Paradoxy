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
            "schema_version": "cognition-load-set/v4",
            "always_full_documents": ["核心认知.md", "方向追踪.md", "全景视野.md", "扩展认知.md"],
            "document_order": ["核心认知.md", "方向追踪.md", "全景视野.md", "扩展认知.md"],
        }
        state = {"revision": 1, "current_core": {"generation": "core-cognition-generation-4"}}
        core_manifest = {"schema_version": "core-cognition/v2", "generation": "core-cognition-generation-4", "units": [{"id": "KC-000001", "author_class": "USER_OWNED_DIRECT", "themes": ["THEME_A"]}]}
        self.write(".codex/cognition/LOAD_SET.json", load_set)
        self.write(".codex/research/hott/STATE.json", state)
        self.write("核心认知.manifest.json", core_manifest)
        self.write("核心认知.md", "# core\n")
        self.write(
            "方向追踪.md",
            """<!-- integrated-direction-portfolio:v1\nsource_state_revision: 1\n-->\n| direction_id | 方向 | 来源 | 状态 | 核心关联 | 结果 | 下一步 | 证据 |\n|---|---|---|---|---|---|---|---|\n| `DIR-A` | a | test | `ACTIVE` | `THEME_A` | `OUT-A` | next | evidence |\n""",
        )
        self.write(
            "全景视野.md",
            """<!-- integrated-outcome-panorama:v1\nsource_state_revision: 1\n-->\n| result_id | 结果 | 方向 |\n|---|---|---|\n| `OUT-A` | a | `DIR-A` |\n""",
        )
        self.write(
            "扩展认知.md",
            """<!-- essay-role:v1\nlogical_id: CORE-ESSAY\nrole: AI_EXPOSITION_LAYER\n-->\n# essay fixture\n""",
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

    def shard_the_panorama(self) -> None:
        shard = self.root / "全景视野" / "001 - 结果总览.md"
        self.write(
            "全景视野/001 - 结果总览.md",
            "<!-- governance-shard:v2\nlogical_id: PANORAMA\nshard_id: 001\nindex: ../全景视野.md\n-->\n\n"
            "# 结果总览\n\n| result_id | 结果 | 方向 |\n|---|---|---|\n| `OUT-A` | a | `DIR-A` |\n",
        )
        self.write(
            "全景视野.md",
            "<!-- governance-shard-index:v2\nlogical_id: PANORAMA\nmode: topical\nshard_root: 全景视野\n"
            "last_shard: 全景视野/001 - 结果总览.md\nappend_target: -\nsoft_line_target: 300\n-->\n\n"
            "<!-- integrated-outcome-panorama:v1\nsource_state_revision: 1\n-->\n\n"
            "<!-- governance-shard-table:start -->\n| Shard | 文件 | 语义范围 | 状态 |\n|---|---|---|---|\n"
            "| 001 | [结果总览](<全景视野/001 - 结果总览.md>) | 全部结果 | current |\n"
            "<!-- governance-shard-table:end -->\n",
        )
        self.shard_path = shard

    def test_sharded_projection_reads_through_the_index(self) -> None:
        self.shard_the_panorama()
        result = MODULE.validate(self.root)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["outcome_count"], 1)

    def test_missing_projection_shard_fails_closed(self) -> None:
        self.shard_the_panorama()
        self.shard_path.unlink()
        with self.assertRaisesRegex(MODULE.ThreeWayError, "PROJECTION_SHARD_UNREADABLE"):
            MODULE.validate(self.root)

    def test_wrong_fixed_order_rejected(self) -> None:
        path = self.root / ".codex/cognition/LOAD_SET.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["always_full_documents"] = [
            "方向追踪.md",
            "核心认知.md",
            "全景视野.md",
            "扩展认知.md",
        ]
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
        with self.assertRaisesRegex(MODULE.ThreeWayError, "FIXED_ORDER"):
            MODULE.validate(self.root)

    def test_orphan_outcome_rejected(self) -> None:
        path = self.root / "全景视野.md"
        path.write_text(path.read_text(encoding="utf-8").replace("DIR-A", "DIR-MISSING"), encoding="utf-8")
        with self.assertRaisesRegex(MODULE.ThreeWayError, "ORPHAN"):
            MODULE.validate(self.root)

    def test_obsolete_core_theme_rejected(self) -> None:
        path = self.root / "方向追踪.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`THEME_A`", "`OBSOLETE_THEME`"), encoding="utf-8")
        with self.assertRaisesRegex(MODULE.ThreeWayError, "CORE_THEME_NOT_IN_CURRENT_MANIFEST"):
            MODULE.validate(self.root)


if __name__ == "__main__":
    unittest.main()
