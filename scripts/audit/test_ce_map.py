#!/usr/bin/env python3
"""Meaningful regression and negative controls for CE-MAP v1."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/audit/build_ce_map.py"
SPEC = importlib.util.spec_from_file_location("build_ce_map", SCRIPT)
assert SPEC and SPEC.loader
ce_map = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ce_map)


class CEMapTests(unittest.TestCase):
    def test_frozen_machine_import_is_self_contained_and_valid(self) -> None:
        manifest, catalog = ce_map.validate_import()
        self.assertEqual(manifest["counts"]["documents"], 169)
        self.assertEqual(len(catalog["tasks"]), 14)
        self.assertEqual(len(catalog["cases"]), 13)
        self.assertEqual(len(catalog["evaluations"]), 15)
        self.assertEqual(len(catalog["runs"]), 48)
        self.assertEqual(len(catalog["reviews"]), 18)
        for key in ("tasks", "cases", "runs", "reviews"):
            ids = [row["source_id"] for row in catalog[key]]
            self.assertNotIn(None, ids)
            self.assertEqual(len(ids), len(set(ids)))

    def test_denominator_axes_and_order_are_complete(self) -> None:
        validation = ce_map.validate_bundle(ROOT / "audit/ce-map")
        mapping = json.loads((ROOT / "audit/ce-map/CE-MAP.json").read_text(encoding="utf-8"))
        current_revision = json.loads((ROOT / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))["revision"]
        if current_revision == 149:
            first = ce_map.bundle_bytes()
            second = ce_map.bundle_bytes()
            self.assertEqual(first, second)
            self.assertTrue(validation["exact_rebuild"])
        else:
            self.assertEqual(validation["status"], "VALID_WITH_SOURCE_EVOLUTION")
            self.assertFalse(validation["exact_rebuild"])
        self.assertEqual(mapping["status"], "CE_MAP_V1_COMPLETE_WITH_SCOPE")
        self.assertEqual(mapping["input_denominator"]["total"], 478)
        self.assertEqual(mapping["integrity"]["input_remainder"], 0)
        self.assertEqual(mapping["integrity"]["axis_cell_remainder"], 0)
        self.assertEqual(len(mapping["items"]), 478)
        self.assertEqual(len({item["id"] for item in mapping["items"]}), 478)
        for item in mapping["items"]:
            self.assertEqual(set(item["axes"]), set(ce_map.AXES))
            self.assertTrue(all(item["axes"][axis] for axis in ce_map.AXES))

    def test_internalisation_is_one_pattern_without_swallowing_other_frontiers(self) -> None:
        mapping = json.loads((ROOT / "audit/ce-map/CE-MAP.json").read_text(encoding="utf-8"))
        classes = {row["id"]: row for row in mapping["classes"]}
        pattern = classes["CE-CLASS-UNQUALIFIED-INTERNALISATION-001"]
        self.assertEqual(pattern["reduction_status"], "PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE")
        self.assertEqual(len(pattern["members"]), 6)
        self.assertIn("proof_claim:C-234", pattern["members"])
        self.assertNotIn("state_record:A-G-HOTT-SYNTAX-001", pattern["members"])
        self.assertNotIn("machine_task:MS-TASK-L3-INTERVAL-COMPLETION-001", pattern["members"])
        self.assertEqual(mapping["selected_successor"]["task"], "R3_R4_GODEL_RETURN_001")

    def test_deleting_one_known_input_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ce-map-negative-") as name:
            temp = Path(name)
            for filename in ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md", "RECEIPT.json"):
                shutil.copyfile(ROOT / "audit/ce-map" / filename, temp / filename)
            path = temp / "CE-MAP.json"
            mapping = json.loads(path.read_text(encoding="utf-8"))
            mapping["items"] = [item for item in mapping["items"] if item["id"] != "proof_claim:C-234"]
            path.write_bytes(ce_map.json_bytes(mapping))
            with self.assertRaisesRegex(ValueError, "INPUT_DENOMINATOR_COUNT"):
                ce_map.validate_bundle(temp)

    def test_removing_one_axis_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ce-map-axis-negative-") as name:
            temp = Path(name)
            for filename in ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md", "RECEIPT.json"):
                shutil.copyfile(ROOT / "audit/ce-map" / filename, temp / filename)
            path = temp / "CE-MAP.json"
            mapping = json.loads(path.read_text(encoding="utf-8"))
            del mapping["items"][0]["axes"]["Oracle"]
            path.write_bytes(ce_map.json_bytes(mapping))
            with self.assertRaisesRegex(ValueError, "AXIS_CELL_MISSING"):
                ce_map.validate_bundle(temp)

    def test_cli_query_and_validation(self) -> None:
        validate = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "validate"],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)
        query = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "query", "--id", "proof_claim:C-234"],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(query.returncode, 0, query.stdout + query.stderr)
        result = json.loads(query.stdout)
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["items"][0]["axes"]["CompletionProperty"], "INTERVAL_COLLAPSE")

        listing = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "list-unclassified"],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(listing.returncode, 0, listing.stdout + listing.stderr)
        remainder = json.loads(listing.stdout)
        self.assertEqual(remainder["count"], len(remainder["entries"]))
        self.assertGreater(remainder["count"], 0)

    def test_separate_process_rebuild_is_byte_identical(self) -> None:
        current_revision = json.loads((ROOT / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))["revision"]
        if current_revision != 149:
            validation = ce_map.validate_bundle(ROOT / "audit/ce-map")
            self.assertEqual(validation["status"], "VALID_WITH_SOURCE_EVOLUTION")
            self.assertFalse(validation["exact_rebuild"])
            return
        names = ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md", "RECEIPT.json")
        before = {name: (ROOT / "audit/ce-map" / name).read_bytes() for name in names}
        for _ in range(2):
            run = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), "build", "--write"],
                cwd=ROOT,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        after = {name: (ROOT / "audit/ce-map" / name).read_bytes() for name in names}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
