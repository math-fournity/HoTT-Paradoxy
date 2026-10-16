from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import tick_irrelevance_gap  # noqa: E402
from machine_overview.util import sha256_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
EVALUATION = ROOT / "machine-overview/evaluations/TICK-IRRELEVANCE-OPERATIONAL-GAP-001"
RUN = EVALUATION / "runs/20260913-TICK-IRRELEVANCE-OPERATIONAL-GAP-001/RUN.json"


class TickIrrelevanceOperationalGapTest(unittest.TestCase):
    def test_freeze_pins_evaluator_scope_and_probe_plan(self) -> None:
        freeze = json.loads((EVALUATION / "FREEZE.json").read_text(encoding="utf-8"))
        self.assertTrue(freeze["future_paths_absent"])
        self.assertEqual(len(freeze["probe_plan"]), 9)
        for key in ("evaluator", "scope"):
            row = freeze[key]
            path = ROOT / row["path"]
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(sha256_file(path), row["sha256"])

    def test_complete_search_finds_only_the_three_edge_collision(self) -> None:
        scope = json.loads((EVALUATION / "SCOPE.json").read_text(encoding="utf-8"))
        result = tick_irrelevance_gap.equality_search(scope)
        self.assertEqual(result["target_paths"], 1)
        self.assertEqual(result["minimal_edge_count"], 3)
        self.assertTrue(result["order_independent"])
        self.assertTrue(all(row["target_paths"] == 0 for row in result["ablations"]))

    def test_source_signature_covers_both_path_and_reducer_sides(self) -> None:
        deterministic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"]
        signature = deterministic["candidate_signature"]
        self.assertTrue(signature["complete"])
        self.assertEqual(len(signature["requirements"]), 6)
        values = {row["id"]: row["actual"] for row in signature["requirements"]}
        self.assertEqual(values["PATH_FORCE_DELAY"], 2)
        self.assertEqual(values["PATH_TICK_IRRELEVANCE"], 6)
        self.assertEqual(values["CHECKER_DIAMOND_BRANCH"], 1)
        self.assertEqual(values["CHECKER_PFIX_GUARD"], 2)

    def test_receipt_replays_without_running_kernels(self) -> None:
        result = tick_irrelevance_gap._verify(ROOT, RUN, False)
        self.assertEqual(result["status"], "TICK_IRRELEVANCE_OPERATIONAL_GAP_VALID")
        self.assertEqual(result["verdict"], "EXTENSIONAL_TICK_IRRELEVANCE_WITH_METALEVEL_OPERATIONAL_SPLIT")
        self.assertEqual(result["candidate_scope"], "REPRESENTATION_BOUNDARY")
        self.assertEqual(result["hott_bug_status"], "NOT_ESTABLISHED")
        self.assertEqual(result["natural_usage_mismatches"], 0)

    def test_native_controls_keep_path_and_judgemental_equality_distinct(self) -> None:
        probes = {
            row["probe_id"]: row
            for row in json.loads(RUN.read_text(encoding="utf-8"))["deterministic"]["probes"]
        }
        self.assertEqual(len(probes), 9)
        self.assertTrue(all(row["accepted"] for row in probes.values()))
        self.assertEqual(probes["P05-DIAMOND-JUDGEMENTAL-UNFOLD"]["first"]["exit_code"], 0)
        self.assertEqual(probes["P06-ORDINARY-TICK-PATH"]["first"]["exit_code"], 0)
        self.assertEqual(probes["P07-BAD-ORDINARY-JUDGEMENTAL-UNFOLD"]["first"]["exit_code"], 42)
        self.assertEqual(probes["P08-FORCE-DELAY-PATH"]["first"]["exit_code"], 0)
        self.assertEqual(probes["P09-BAD-FORCE-DELAY-AS-REFL"]["first"]["exit_code"], 42)
        self.assertTrue(all(row["replay_classification"] == "EXACT_EXIT_STDOUT_STDERR_MATCH" for row in probes.values()))

    def test_fixed_consumers_do_not_promote_path_to_current_reduction(self) -> None:
        deterministic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"]
        rows = deterministic["consumer_promotions"]
        self.assertEqual(len(rows), 4)
        self.assertEqual(deterministic["natural_usage_mismatches"], [])
        self.assertNotIn("OPERATIONAL_PROMOTION", {row["classification"] for row in rows})


if __name__ == "__main__":
    unittest.main()
