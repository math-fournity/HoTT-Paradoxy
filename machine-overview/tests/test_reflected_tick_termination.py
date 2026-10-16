from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import reflected_tick_termination  # noqa: E402
from machine_overview.util import json_bytes, sha256_bytes, sha256_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
EVALUATION = (
    ROOT
    / "machine-overview/evaluations/REFLECTED-TICK-REDUCTION-OBSERVER-001"
)
RUN = (
    EVALUATION
    / "runs/20260914-REFLECTED-TICK-REDUCTION-OBSERVER-001/RUN.json"
)
CURRENT_RUN = (
    EVALUATION
    / "runs/20260914-REFLECTED-TICK-REDUCTION-OBSERVER-005/RUN.json"
)


def load(name: str) -> dict:
    return json.loads((EVALUATION / name).read_text(encoding="utf-8"))


class ReflectedTickTerminationTest(unittest.TestCase):
    def test_freeze_pins_scope_evaluator_and_full_probe_roster(self) -> None:
        freeze = load("FREEZE.json")
        deterministic = freeze["deterministic"]
        self.assertTrue(deterministic["future_paths_absent"])
        self.assertEqual(len(deterministic["probe_plan"]), 10)
        self.assertEqual(
            sha256_bytes(json_bytes(deterministic)),
            freeze["deterministic_sha256"],
        )
        for key in ("evaluator", "scope"):
            row = deterministic[key]
            path = ROOT / row["path"]
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(sha256_file(path), row["sha256"])

    def test_decisions_cover_every_anchor_and_separate_source_roles(self) -> None:
        decisions = load("DECISIONS.json")["deterministic"]
        self.assertTrue(decisions["all_anchors_found"])
        self.assertEqual(len(decisions["anchor_checks"]), 23)
        self.assertTrue(all(row["found"] for row in decisions["anchor_checks"]))
        inventory = {
            row["tree_id"]: row
            for row in decisions["termination_annotation_inventory"]
        }
        self.assertEqual(inventory["RT-T1-CUBICAL-v0.9"]["matches"], 0)
        self.assertEqual(inventory["RT-T2-GUARDED-cf0c438"]["matches"], 0)
        self.assertEqual(inventory["RT-T3-PROJECT-HOTT-FORMAL"]["matches"], 0)
        self.assertEqual(inventory["RT-T4-AGDA-CHECKER-TESTS"]["matches"], 76)
        self.assertEqual(inventory["RT-T5-AGDA-CHECKER-EXAMPLES"]["matches"], 3)

    def test_historical_receipt_detects_later_formal_tree_evolution(self) -> None:
        with self.assertRaisesRegex(
            reflected_tick_termination.MachineOverviewError,
            "REFLECTED_TICK_TREE_CHANGED:RT-T3-PROJECT-HOTT-FORMAL",
        ):
            reflected_tick_termination.verify(RUN, False)

    def test_current_receipt_replays_after_formal_tree_refresh(self) -> None:
        result = reflected_tick_termination.verify(CURRENT_RUN, False)
        self.assertEqual(
            result["status"], "REFLECTED_TICK_REDUCTION_TERMINATION_VALID"
        )
        self.assertEqual(result["probe_count"], 10)
        self.assertEqual(result["hott_nonreality_status"], "NOT_ESTABLISHED")
        self.assertEqual(
            result["godel_status"], "GENERIC_SELF_REDUCTION_CALIBRATION_ONLY"
        )
        self.assertEqual(
            result["deterministic_sha256"],
            "69db8953ea10d57ca81bc0fca0eaca74d97c4063ed606cec94bead3f8667829b",
        )

    def test_current_revision_uses_a_frozen_formal_tree_inventory(self) -> None:
        snapshot = load("FORMAL-TREE-SNAPSHOT-REV5.json")
        self.assertEqual(snapshot["identity"]["file_count"], 99)
        self.assertEqual(snapshot["identity"]["total_bytes"], 384804)
        self.assertEqual(
            snapshot["identity"]["tree_sha256"],
            "925765a82a9f94abf73f0badcb0177bd36d60557a0a0c9ba45f15457576e1ad4",
        )
        self.assertEqual(snapshot["source_files_scanned"], 50)
        self.assertEqual(snapshot["annotation_matches"], [])
        scope = load("SCOPE-REV5.json")
        self.assertNotIn(
            "RT-T3-PROJECT-HOTT-FORMAL",
            {row["tree_id"] for row in scope["trees"]},
        )

    def test_all_native_probe_pairs_are_exact_replays(self) -> None:
        deterministic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"]
        probes = deterministic["probes"]
        self.assertEqual(len(probes), 10)
        self.assertTrue(all(row["expectation_met"] for row in probes))
        self.assertTrue(all(row["exact_replay"] for row in probes))
        classes = {row["probe_id"]: row["classification"] for row in probes}
        self.assertEqual(
            classes["P07-TERMINATION-OVERRIDE-FORCED-EQUALITY"],
            "EXPECTED_OBSERVATION_LIMIT",
        )
        self.assertEqual(
            classes["P10-REFLECTION-NORMALISES-RECURSIVE-TERM"],
            "EXPECTED_OBSERVATION_LIMIT",
        )
        self.assertEqual(
            classes["P09-GUARDED-INFINITE-NORMALISATION"], "KERNEL_ACCEPTED"
        )

    def test_trigger_cube_contains_three_distinct_causal_ablations(self) -> None:
        semantic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"][
            "semantic"
        ]
        cube = semantic["trigger_cube"]
        self.assertEqual(len(cube["full_conjunction"]), 3)
        self.assertEqual(cube["full_result"], "OBSERVATION_LIMIT_REACHED")
        self.assertEqual(
            {row["removed"] for row in cube["ablations"]},
            set(cube["full_conjunction"]),
        )
        self.assertEqual(
            {row["result"] for row in cube["ablations"]},
            {"COMPLETED", "TYPE_REJECTED"},
        )

    def test_reflection_observation_does_not_cross_object_path_boundary(self) -> None:
        semantic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"][
            "semantic"
        ]
        reflection = semantic["reflection"]
        self.assertTrue(reflection["call_site_syntax_split"])
        self.assertTrue(reflection["uniform_object_observer_preserves_path"])
        self.assertFalse(reflection["uniform_object_observer_retains_split"])
        self.assertEqual(
            reflection["path_indexed_reification"],
            "TYPE_REJECTED_TRUE_FALSE_BOUNDARY",
        )
        self.assertEqual(semantic["natural_usage_mismatches"], [])
        self.assertEqual(semantic["hott_godel_instances"], [])


if __name__ == "__main__":
    unittest.main()
