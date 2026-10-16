from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import hott_quotation_bridge  # noqa: E402
import force_consumer_inventory  # noqa: E402
from machine_overview.util import sha256_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
EVALUATION = ROOT / "machine-overview/evaluations/HOTT-QUOTATION-BRIDGE-001"
RUN = EVALUATION / "runs/20260913-HOTT-QUOTATION-BRIDGE-001/RUN.json"


class HoTTQuotationBridgeTest(unittest.TestCase):
    def test_freeze_pins_evaluator_and_scope(self) -> None:
        freeze = json.loads((EVALUATION / "BRIDGE-FREEZE.json").read_text(encoding="utf-8"))
        self.assertTrue(freeze["future_paths_absent"])
        for key in ("evaluator", "scope"):
            row = freeze[key]
            path = ROOT / row["path"]
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(sha256_file(path), row["sha256"])

    def test_bridge_receipt_replays_without_executing_kernel(self) -> None:
        result = hott_quotation_bridge._verify(ROOT, RUN, False)
        self.assertEqual(result["status"], "HOTT_QUOTATION_BRIDGE_VALID")
        self.assertEqual(result["verdict"], "GUARDED_FORCE_ERASURE_CONDITIONAL_COLLAPSE_WITH_DEFENSE")
        self.assertEqual(result["hott_bug_status"], "NOT_ESTABLISHED")
        self.assertEqual(result["source_count"], 6)
        self.assertEqual(result["probe_count"], 10)

    def test_role_inventory_and_consumer_boundary(self) -> None:
        deterministic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"]
        self.assertEqual(deterministic["roles"], ["HOST_TC", "SYNTAX_QUOTATION", "TEMPORAL_LATER"])
        self.assertEqual(deterministic["guard_erasure_consumers"], [])
        self.assertTrue(deterministic["all_anchors_found"])
        self.assertEqual(deterministic["reflection_inventory"]["quoteTC"]["occurrences"], 12)
        self.assertEqual(deterministic["reflection_inventory"]["unquoteTC"]["occurrences"], 0)
        self.assertEqual(deterministic["reflection_inventory"]["guarded_tick_option"]["occurrences"], 0)
        self.assertEqual(deterministic["reflection_inventory"]["tick_binder"]["occurrences"], 0)
        self.assertTrue(all(row["answers"]["H6"]["status"] == "FAIL" for row in deterministic["source_decisions"]))

    def test_native_positive_negative_and_toolchain_controls(self) -> None:
        probes = {
            row["probe_id"]: row
            for row in json.loads(RUN.read_text(encoding="utf-8"))["deterministic"]["probes"]
        }
        self.assertTrue(all(row["accepted"] for row in probes.values()))
        self.assertEqual(probes["P06-GUARDED-FORCE-COLLAPSE"]["first"]["exit_code"], 0)
        self.assertEqual(
            probes["P07-BAD-FIXED-FORCE"]["first"]["classification"],
            "EXPECTED_TYPE_REJECTION",
        )
        self.assertEqual(
            probes["P09-BAD-LOCAL-FROM-GLOBAL"]["first"]["classification"],
            "EXPECTED_TYPE_REJECTION",
        )
        self.assertEqual(
            probes["P10-FORCING-TICKS-TOOLCHAIN"]["first"]["classification"],
            "EXPECTED_TOOLCHAIN_VERSION_MISMATCH",
        )
        self.assertTrue(all(row["replay_classification"] == "EXACT_EXIT_STDOUT_STDERR_MATCH" for row in probes.values()))

    def test_force_consumer_inventory_is_complete_for_fixed_tree(self) -> None:
        inventory = EVALUATION / "FORCE-CONSUMER-INVENTORY.json"
        result = force_consumer_inventory.verify(ROOT, inventory)
        self.assertEqual(result["status"], "FORCE_CONSUMER_INVENTORY_VALID")
        self.assertEqual(result["matching_lines"], 9)
        self.assertEqual(result["files_with_matches"], 2)
        rows = json.loads(inventory.read_text(encoding="utf-8"))["deterministic"]["matches"]
        self.assertEqual({row["path"] for row in rows}, {"Clocked/Primitives.agda", "Clocked/Lift.agda"})
        lift_rows = [row for row in rows if row["path"] == "Clocked/Lift.agda"]
        self.assertEqual(len(lift_rows), 1)
        self.assertIn("force (\\ k → \\ α →", lift_rows[0]["text"])


if __name__ == "__main__":
    unittest.main()
