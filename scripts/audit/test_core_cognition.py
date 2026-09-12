#!/usr/bin/env python3
"""Deterministic and negative tests for generation-3 core curation."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDER_PATH = Path(__file__).with_name("build_core_cognition.py")
SPEC = importlib.util.spec_from_file_location("core_builder_test", BUILDER_PATH)
assert SPEC and SPEC.loader
B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(B)


class CoreCognitionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.curation = json.loads((ROOT / B.DEFAULT_CURATION).read_text(encoding="utf-8"))

    def temp_root(self, curation: dict | None = None) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory(prefix="core-cognition-v3-")
        root = Path(temp.name)
        for source in self.curation["sources"]:
            target = root / source["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / source["path"]).read_bytes())
        target = root / B.DEFAULT_CURATION
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(curation or self.curation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return temp, root

    def test_actual_generation_has_complete_small_denominator(self) -> None:
        manifest, core, manifest_bytes, units = B.build(ROOT)
        self.assertEqual(manifest["generation"], "core-cognition-generation-3")
        self.assertEqual(manifest["counts"]["messages_parsed"], 88)
        self.assertEqual(manifest["counts"]["messages_included"], 23)
        self.assertEqual(manifest["counts"]["core_units"], 27)
        self.assertEqual(manifest["counts"]["units_by_platform"], {"Gemini": 13, "LocalGPT": 6, "WebGPT": 8})
        self.assertLess(len(core.encode("utf-8")), 100_000)
        self.assertEqual(B.json_bytes(manifest), manifest_bytes)
        self.assertEqual(len(units), 27)

    def test_output_is_deterministic_and_chronological(self) -> None:
        first = B.build(ROOT)
        second = B.build(ROOT)
        self.assertEqual(first[:3], second[:3])
        rows = first[0]["units"]
        self.assertEqual([row["id"] for row in rows], [f"KC-{i:06d}" for i in range(1, 28)])
        self.assertEqual([row["timestamp_utc"] for row in rows], sorted(row["timestamp_utc"] for row in rows))

    def test_every_payload_is_direct_user_text(self) -> None:
        _, core, _, units = B.build(ROOT)
        self.assertNotIn("# Response annotations:", core)
        self.assertNotIn("AI回答：", core)
        self.assertNotIn("致 OUT-", core)
        for row in units:
            self.assertEqual(row["author_class"], "USER_OWNED_DIRECT")

    def test_missing_message_decision_fails_closed(self) -> None:
        altered = copy.deepcopy(self.curation)
        altered["message_decisions"].pop()
        temp, root = self.temp_root(altered)
        try:
            with self.assertRaisesRegex(B.CoreBuildError, "DENOMINATOR_MISMATCH"):
                B.build(root)
        finally:
            temp.cleanup()

    def test_source_hash_drift_fails_closed(self) -> None:
        temp, root = self.temp_root()
        try:
            source = root / self.curation["sources"][0]["path"]
            source.write_text(source.read_text(encoding="utf-8") + "DRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(B.CoreBuildError, "SOURCE_HASH_MISMATCH"):
                B.build(root)
        finally:
            temp.cleanup()

    def test_relayed_ai_selector_fails_closed(self) -> None:
        altered = copy.deepcopy(self.curation)
        altered["units"][0] = {
            "source_message_id": "GEMINI-M-013",
            "semantic_label": "negative fixture",
            "source_lines": [580, 590]
        }
        temp, root = self.temp_root(altered)
        try:
            with self.assertRaisesRegex(B.CoreBuildError, "RELAYED_CONTEXT"):
                B.build(root)
        finally:
            temp.cleanup()

    def test_generation_transition_covers_all_913_old_ids(self) -> None:
        manifest, _, _, units = B.build(ROOT)
        transition = B.build_transition(ROOT, "governance-v2.1.0", manifest, units)
        self.assertEqual(transition["mapping_count"], 913)
        self.assertEqual(transition["mapping_remainder"], 0)
        self.assertEqual(len({row["old_id"] for row in transition["mappings"]}), 913)
        self.assertTrue({"CURATED_EXACT_SUBRANGE", "EXCLUDED_NON_PRIMARY_INPUT"} <= set(transition["relation_counts"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
