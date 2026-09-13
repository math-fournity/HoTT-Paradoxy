"""Unit and negative-control tests for the machine-overview coordinator."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

from machine_overview.case import validate_workspace  # noqa: E402
from machine_overview.index import build_index  # noqa: E402
from machine_overview.model import (  # noqa: E402
    bind_value,
    deadline_value,
    delay_equivalent,
    race_value,
    ret,
)
from machine_overview.search import enumerate_contexts, run_search  # noqa: E402
from machine_overview.util import MachineOverviewError, find_repo_root, read_json  # noqa: E402
from machine_overview.verify import (  # noqa: E402
    check_proof_hygiene,
    render_proof,
    render_target,
    verify_witness,
)


def load_json(relative: str) -> dict:
    repo_root = find_repo_root()
    return read_json(repo_root / relative)


class ModelSemanticsTest(unittest.TestCase):
    def test_result_equivalence_forgets_round_index(self) -> None:
        self.assertTrue(delay_equivalent(ret(0, True), ret(2, True)))
        self.assertFalse(delay_equivalent(ret(0, True), ret(0, False)))

    def test_race_and_deadline_read_the_round_index(self) -> None:
        p0, p2, q1 = ret(0, True), ret(2, True), ret(1, False)
        self.assertEqual(race_value(p0, q1), ret(0, True))
        self.assertEqual(race_value(p2, q1), ret(1, False))
        self.assertFalse(delay_equivalent(race_value(p0, q1), race_value(p2, q1)))
        self.assertEqual(deadline_value(1, p0), ("some", True))
        self.assertEqual(deadline_value(1, p2), ("none",))

    def test_business_continuation_turns_the_losing_branch_into_divergence(self) -> None:
        deliver = {True: ret(0, True), False: ("omega",)}
        p0, p2, q1 = ret(0, True), ret(2, True), ret(1, False)
        self.assertEqual(bind_value(race_value(p0, q1), deliver), ret(1, True))
        self.assertEqual(bind_value(race_value(p2, q1), deliver), ("omega",))


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = find_repo_root()
        cls.grammar = load_json("machine-overview/grammars/l1-v0.json")
        cls.case = load_json("machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001/case-revision-1.json") \
            if (cls.repo_root / "machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001/case-revision-1.json").is_file() \
            else None

    def test_search_is_answer_independent_and_covers_the_benchmark(self) -> None:
        profile_report = {
            "profile_id": "L1-PARTIALITY-RACE-DEADLINE-v0",
            "status": "PROFILE_QUALIFIED",
            "toolchain_ref": "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json",
        }
        case = self.case or {
            "case_id": "UNIT-TEST-CASE",
            "revision": 1,
            "grammar": {"path": "machine-overview/grammars/l1-v0.json", "sha256": "unit"},
            "task": {"path": "machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json", "sha256": "unit"},
            "claim_refs": ["C-73", "C-74", "C-75"],
        }
        receipt = run_search(
            self.repo_root,
            run_id="unit-test-search",
            case_path=self.repo_root / "machine-overview/grammars/l1-v0.json",
            case=case,
            grammar=self.grammar,
            profile_report=profile_report,
            registry={"coordinator_version": "test", "registry_id": "test"},
            limits={"max_witnesses": 50000, "max_checks": 5000000},
        )
        self.assertTrue(receipt["order_independence_check"]["order_independent_set_equal"])
        self.assertEqual(receipt["calibration_match"]["status"], "PRESENT")
        self.assertFalse(receipt["grammar_sensitivity_check"]["mutated_contains_deadline_kind"])
        kinds = {item["separation_kind"] for item in receipt["witnesses"]}
        self.assertIn("deadline_observation", kinds)
        self.assertTrue(kinds & {"completion_divergence", "value_mismatch"})
        self.assertGreater(receipt["statistics"]["pair_context_checks"], 1000)
        self.assertTrue(receipt["controls"]["positive"]["preserved"])
        self.assertTrue(receipt["controls"]["negative"]["expectation_met"])

    def test_contexts_follow_the_declared_depth(self) -> None:
        contexts = enumerate_contexts(self.grammar)
        self.assertTrue(all(len(context) <= self.grammar["context_depth_max"] for context in contexts))
        self.assertGreater(len(contexts), 100)


class ProofHygieneTest(unittest.TestCase):
    def test_forbidden_declaration_is_rejected(self) -> None:
        text = "module Proof where\nopen import Target\npostulate cheat : Target.gap\n"
        with self.assertRaises(MachineOverviewError):
            check_proof_hygiene(text, "unit-test")

    def test_missing_target_reference_is_rejected(self) -> None:
        with self.assertRaises(MachineOverviewError):
            check_proof_hygiene("module Proof where\n", "unit-test")

    def test_target_generation_is_deterministic(self) -> None:
        grammar = load_json("machine-overview/grammars/l1-v0.json")
        profile_report = {"profile_id": "x", "status": "PROFILE_QUALIFIED",
                          "toolchain_ref": "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"}
        receipt = run_search(
            find_repo_root(),
            run_id="unit-test-target",
            case_path=find_repo_root() / "machine-overview/grammars/l1-v0.json",
            case={"case_id": "UNIT-TEST-CASE", "revision": 1,
                  "grammar": {"path": "x", "sha256": "x"}, "task": {"path": "x", "sha256": "x"},
                  "claim_refs": []},
            grammar=grammar,
            profile_report=profile_report,
            registry={"coordinator_version": "test", "registry_id": "test"},
            limits={"max_witnesses": 20, "max_checks": 1000000},
        )
        witness = receipt["witnesses"][0]
        first = render_target({"case_id": "UNIT-TEST-CASE", "revision": 1}, witness)
        second = render_target({"case_id": "UNIT-TEST-CASE", "revision": 1}, witness)
        self.assertEqual(first, second)
        self.assertIn("module Target where", first)

    def test_value_mismatch_lemma_orientation(self) -> None:
        """`⇔-fwd (h a) refl : c ≡ a` needs the lemma refuting c ≡ a."""
        witness = {
            "witness_id": "UNIT",
            "pair": {"left": {"kind": "ret", "n": 0, "value": False},
                     "right": {"kind": "ret", "n": 1, "value": False}},
            "ops": [{"kind": "race_left", "partner": {"kind": "ret", "n": 0, "value": True}}],
            "observation_mode": "delay",
            "left_observation": {"kind": "ret", "n": 0, "value": False},
            "right_observation": {"kind": "ret", "n": 0, "value": True},
            "separation_kind": "value_mismatch",
            "size": {"context_ops": 1, "index_sum": 0},
        }
        proof = render_proof({"case_id": "UNIT", "revision": 1}, witness)
        self.assertIn("gap h = true≢false (⇔-fwd (h false) refl)", proof)


class WorkspaceTest(unittest.TestCase):
    def test_workspace_validates(self) -> None:
        report = validate_workspace(find_repo_root())
        self.assertEqual(report["status"], "VALID", report["errors"])

    def test_index_rebuild_is_stable(self) -> None:
        repo_root = find_repo_root()
        root = repo_root / "machine-overview"
        first = build_index(root)
        second = build_index(root)
        self.assertEqual(
            [entry["path"] for entry in first["entries"]],
            [entry["path"] for entry in second["entries"]],
        )


class FailClosedTest(unittest.TestCase):
    def test_target_tamper_is_rejected_before_side_effects(self) -> None:
        repo_root = find_repo_root()
        grammar = load_json("machine-overview/grammars/l1-v0.json")
        search = run_search(
            repo_root,
            run_id="unit-test-tamper",
            case_path=repo_root / "machine-overview/grammars/l1-v0.json",
            case={"case_id": "UNIT-TEST-CASE", "revision": 1,
                  "grammar": {"path": "x", "sha256": "x"}, "task": {"path": "x", "sha256": "x"},
                  "claim_refs": []},
            grammar=grammar,
            profile_report={"profile_id": "x", "status": "PROFILE_QUALIFIED",
                            "toolchain_ref": "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"},
            registry={"coordinator_version": "test", "registry_id": "test"},
            limits={"max_witnesses": 5, "max_checks": 1000000},
        )
        case = {"case_id": "UNIT-TEST-CASE", "revision": 1, "target_text_hash": "0" * 64}
        run_dir = repo_root / "machine-overview/runs/unit-test-tamper"
        with self.assertRaises(MachineOverviewError) as ctx:
            verify_witness(
                repo_root,
                run_id="unit-test-tamper",
                case_path=repo_root / "machine-overview/grammars/l1-v0.json",
                case=case,
                witness=search["witnesses"][0],
                profile_report={"profile_id": "x", "status": "PROFILE_QUALIFIED",
                                "toolchain_ref": "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"},
                toolchain=load_json("HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"),
                registry={"coordinator_version": "test", "registry_id": "test"},
                run_dir=run_dir,
            )
        self.assertEqual(str(ctx.exception), "TARGET_CHANGED")
        self.assertFalse(run_dir.exists())


if __name__ == "__main__":
    unittest.main()
