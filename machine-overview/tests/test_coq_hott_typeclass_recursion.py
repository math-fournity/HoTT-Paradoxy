from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import coq_hott_typeclass_recursion  # noqa: E402
from machine_overview.util import json_bytes, sha256_bytes, sha256_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
EVALUATION = (
    ROOT
    / "machine-overview/evaluations/COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001"
)
RUN = (
    EVALUATION
    / "runs/20260914-COQ-HOTT-TYPECLASS-RECURSION-001/RUN.json"
)


def load(name: str) -> dict:
    return json.loads((EVALUATION / name).read_text(encoding="utf-8"))


class CoqHoTTTypeclassRecursionTest(unittest.TestCase):
    def test_freeze_precedes_and_pins_all_formal_probes(self) -> None:
        freeze = load("FREEZE.json")
        deterministic = freeze["deterministic"]
        self.assertTrue(deterministic["future_paths_absent"])
        self.assertEqual(len(deterministic["probe_plan"]), 8)
        self.assertEqual(
            sha256_bytes(json_bytes(deterministic)),
            freeze["deterministic_sha256"],
        )
        for key in ("evaluator", "scope"):
            row = deterministic[key]
            path = ROOT / row["path"]
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(sha256_file(path), row["sha256"])

    def test_source_decision_has_complete_anchors_and_no_active_registration(self) -> None:
        decisions = load("DECISIONS.json")["deterministic"]
        self.assertTrue(decisions["all_anchors_found"])
        self.assertEqual(len(decisions["anchor_checks"]), 18)
        self.assertTrue(all(row["found"] for row in decisions["anchor_checks"]))
        inventory = decisions["registration_inventory"]
        self.assertEqual(inventory["active_registration_count"], 0)
        self.assertEqual(inventory["active_isequiv_O_inverts_registrations"], [])
        self.assertEqual(inventory["documented_boundary_count"], 5)

    def test_receipt_replays_without_native_execution(self) -> None:
        result = coq_hott_typeclass_recursion.verify(RUN, False)
        self.assertEqual(result["status"], "COQ_HOTT_TYPECLASS_RECURSION_VALID")
        self.assertEqual(result["probe_count"], 8)
        self.assertEqual(
            result["candidate_scope"],
            "COMMUNITY_HOTT_AUTOMATION_RECURSION_BOUNDARY",
        )
        self.assertEqual(result["hott_nonreality_status"], "NOT_ESTABLISHED")
        self.assertEqual(result["hott_bug_status"], "NOT_ESTABLISHED")
        self.assertEqual(
            result["godel_status"],
            "NO_OBJECT_LANGUAGE_OR_PROVABILITY_PREDICATE",
        )
        self.assertEqual(
            result["deterministic_sha256"],
            "c42ddc1b878c64d9cd926e56daba1cfa338da2e723e5f32d548ea7c794ee5bd2",
        )

    def test_probe_matrix_separates_default_bounded_known_and_generic_cases(self) -> None:
        probes = {
            row["probe_id"]: row
            for row in json.loads(RUN.read_text(encoding="utf-8"))["deterministic"][
                "probes"
            ]
        }
        self.assertEqual(len(probes), 8)
        self.assertTrue(all(row["expectation_met"] for row in probes.values()))
        self.assertTrue(all(row["exact_replay"] for row in probes.values()))
        self.assertEqual(
            probes["P01-DEFAULT-NO-REGISTRATION"]["classification"],
            "EXPECTED_PROOF_SEARCH_FAILURE",
        )
        self.assertEqual(
            probes["P02-COMMENTED-HINT-IMMEDIATE"]["classification"],
            "EXPECTED_PROOF_SEARCH_FAILURE",
        )
        self.assertEqual(
            probes["P03-EXISTING-INSTANCE"]["classification"],
            "EXPECTED_OBSERVATION_LIMIT",
        )
        self.assertEqual(
            probes["P04-HINT-RESOLVE"]["classification"],
            "EXPECTED_OBSERVATION_LIMIT",
        )
        self.assertEqual(
            probes["P05-BOUNDED-SEARCH-DEPTH"]["classification"],
            "EXPECTED_SEARCH_DEPTH_LIMIT",
        )
        self.assertEqual(
            probes["P06-KNOWN-EQUIVALENCE"]["classification"],
            "KERNEL_ACCEPTED",
        )
        self.assertEqual(
            probes["P07-GENERIC-TYPECLASS-RECURSION"]["classification"],
            "EXPECTED_OBSERVATION_LIMIT",
        )

    def test_bounded_trace_exhibits_nested_O_functor_obligations(self) -> None:
        semantic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"][
            "semantic"
        ]
        trace = semantic["causal_controls"]["bounded_trace"]
        self.assertEqual(trace["line_count"], 206)
        self.assertEqual(trace["isequiv_O_inverts_steps"], 8)
        self.assertEqual(trace["O_functor_occurrences"], 34)
        self.assertTrue(trace["contains_first_nested_obligation"])
        self.assertTrue(trace["contains_second_nested_obligation"])

    def test_qualification_does_not_promote_automation_to_hott_or_godel(self) -> None:
        semantic = json.loads(RUN.read_text(encoding="utf-8"))["deterministic"][
            "semantic"
        ]
        qualification = semantic["qualification"]
        self.assertEqual(qualification["N0_OBSERVATION_LIMIT"], "PASS")
        self.assertEqual(qualification["N1_CAUSAL_CONTROLS"], "PASS")
        self.assertTrue(qualification["N2_ORDINARY_CONFIGURATION"].startswith("FAIL_"))
        self.assertTrue(qualification["N3_HOTT_ESSENTIALITY"].startswith("FAIL_"))
        self.assertTrue(qualification["N4_NATURAL_CONSUMER"].startswith("PARTIAL_"))
        self.assertEqual(semantic["natural_enabled_consumers"], [])
        self.assertEqual(
            semantic["direction_b_status"],
            "ASK_LIKE_DESIGN_GUARD_PRESENT_NOT_BYPASSED",
        )


if __name__ == "__main__":
    unittest.main()
