from __future__ import annotations

import unittest
from pathlib import Path

import m4_eval
from machine_overview.case import symbolic_renderer_id
from machine_overview.search import compute_search_semantics
from machine_overview.util import MachineOverviewError, read_json
from machine_overview.verify import render_controls, render_falsify, render_proof, render_target, render_verify


ROOT = Path(__file__).resolve().parents[2]


def grammar(renderer: str, observation: str, goal: str = "goal") -> dict:
    return {
        "backend": "symbolic-horn-v1",
        "propositions": ["seed", goal],
        "goal": goal,
        "observation_kind": observation,
        "max_proof_depth": 3,
        "rules": [
            {"id": "seed", "premises": [], "conclusion": "seed", "term_template": "seed-term"},
            {"id": "lift", "premises": ["seed"], "conclusion": goal, "term_template": "lift-term {0}"},
        ],
        "mechanism_rules": ["seed", "lift"],
        "positive_control_goals": ["seed"],
        "ablation": {"remove_rules": ["lift"]},
        "native_contract": {"renderer": renderer, "target_scope": "test scope"},
    }


class SymbolicNativeRendererTest(unittest.TestCase):
    def test_existing_l3_target_remains_byte_identical(self) -> None:
        case = read_json(ROOT / "machine-overview/cases/MS-TASK-L3-INTERVAL-COMPLETION-001/case-revision-1.json")
        search = read_json(ROOT / "machine-overview/runs/20260913-SEARCH-L3-SYMBOLIC-001/RUN.json")
        old_grammar = read_json(ROOT / "machine-overview/grammars/l3-symbolic-v1.json")
        rendered = render_target(case, search["witnesses"][0], old_grammar)
        frozen = (ROOT / "machine-overview/runs/20260913-VERIFY-L3-SYMBOLIC-001/generated/Target.agda").read_text()
        self.assertEqual(rendered, frozen)

    def test_renderer_observation_pair_is_fail_closed(self) -> None:
        bad = grammar("l3_path_coherence_positive_v1", "finite_to_exact_candidate")
        with self.assertRaisesRegex(MachineOverviewError, "SYMBOLIC_RENDERER_OBSERVATION_MISMATCH"):
            symbolic_renderer_id(bad)

    def test_all_new_renderers_emit_bound_modules(self) -> None:
        cases = [
            ("l3_path_coherence_positive_v1", "path_coherence_positive", "PathCarrierCoherence"),
            ("l3_event_boundary_v1", "explicit_event_boundary", "ExactEventBoundary"),
            ("l3_finite_to_exact_candidate_v1", "finite_to_exact_candidate", "FiniteToExact"),
        ]
        witness = {"witness_id": "WV-0001", "ast_sha256": "a" * 64, "proof_term": "lift-term seed-term"}
        case = {"case_id": "TEST"}
        for renderer, observation, target_name in cases:
            with self.subTest(renderer=renderer):
                current = grammar(renderer, observation)
                self.assertIn(target_name, render_target(case, witness, current))
                self.assertIn(f"Target.{target_name}", render_proof(case, witness, current))
                self.assertIn(target_name, render_verify(witness, current))
                self.assertIn("module Controls where", render_controls(witness, current))
                self.assertIn("module Falsify where", render_falsify(witness, current))


class M4ModeEvaluationTest(unittest.TestCase):
    def test_native_feedback_removes_rejected_speculative_rule(self) -> None:
        current = grammar("l3_finite_to_exact_candidate_v1", "finite_to_exact_candidate")
        budget = {"max_witnesses": 100, "max_checks": 1000, "max_contexts": 3}
        semantics = compute_search_semantics(current, budget, 7)
        first = semantics["witnesses"][0]
        task = {
            "expected_native_outcome": "REJECT",
            "mode_rules": {
                "hybrid_feedback": {
                    "initial_rules": ["seed", "lift"],
                    "remove_after_native_rejection": ["lift"],
                }
            },
        }
        mode = {"mode_id": "hybrid_feedback", "strategy": "native_feedback"}
        verify_run = {"candidate_ast_sha256": first["ast_sha256"], "status": "NATIVE_CHECK_FAILED"}
        result = m4_eval.evaluate_mode(task, current, verify_run, mode, budget, 7)
        self.assertTrue(result["feedback_applied"])
        self.assertIsNone(result["stages"][-1]["first_witness"])
        self.assertTrue(result["expectation_met"])
        self.assertFalse(result["false_promotion"])

    def test_rule_selection_rejects_unknown_rule(self) -> None:
        current = grammar("l3_path_coherence_positive_v1", "path_coherence_positive")
        with self.assertRaisesRegex(MachineOverviewError, "M4_MODE_RULE_SELECTION_INVALID"):
            m4_eval.filtered_grammar(current, ["missing"])


if __name__ == "__main__":
    unittest.main()
