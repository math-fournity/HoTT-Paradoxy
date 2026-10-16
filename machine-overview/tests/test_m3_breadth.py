from __future__ import annotations

import sys
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import m4_replay_closure  # noqa: E402
from machine_overview.case import symbolic_renderer_id  # noqa: E402
from machine_overview.verify import (  # noqa: E402
    render_controls,
    render_falsify,
    render_proof,
    render_target,
    render_verify,
)


ROOT = Path(__file__).resolve().parents[2]


class M3BreadthRendererTest(unittest.TestCase):
    def test_four_line_renderers_bind_distinct_native_targets(self) -> None:
        rows = [
            (
                "m3_l2_truncated_limit_v1",
                "local_to_global_completion_boundary",
                "NoTruncatedLimitRecovery",
                "TL.C-114-LimA-empty (recover TL.C-115-limTrunc)",
            ),
            (
                "m3_l4_sip_observation_v1",
                "identity_observation_boundary",
                "NoOutsideObservationRecovery",
                "SIP.C-125-obs-differs (sym hs ∙ cong f SIP.C-124-identification ∙ ht)",
            ),
            (
                "m3_l5_self_guarantee_v1",
                "self_guarantee_diagonal_boundary",
                "NoExactSelfCoding",
                "notNoFixed (encode self self) (cong (λ h → h self) (section liar))",
            ),
            (
                "m3_l6_compensation_conflict_v1",
                "compensation_coherence_conflict",
                "NoJointPathAndApart",
                "apart path",
            ),
        ]
        case = {"case_id": "M3-TEST"}
        for renderer, observation, target_name, term in rows:
            with self.subTest(renderer=renderer):
                grammar = {
                    "backend": "symbolic-horn-v1",
                    "observation_kind": observation,
                    "native_contract": {"renderer": renderer},
                }
                witness = {"witness_id": "WV-0001", "ast_sha256": "a" * 64, "proof_term": term}
                self.assertEqual(symbolic_renderer_id(grammar), renderer)
                self.assertIn(target_name, render_target(case, witness, grammar))
                self.assertIn(f"Target.{target_name}", render_proof(case, witness, grammar))
                self.assertIn(target_name, render_verify(witness, grammar))
                self.assertIn("module Controls where", render_controls(witness, grammar))
                self.assertIn("module Falsify where", render_falsify(witness, grammar))

    def test_m4_v2_replay_survives_live_adapter_evolution(self) -> None:
        run = ROOT / (
            "machine-overview/evaluations/M4-LITE-L3-001/runs/"
            "20260913-M4-LITE-L3-REPLAY-V2/RUN.json"
        )
        result = m4_replay_closure.verify_replay(ROOT, run)
        self.assertEqual(result["status"], "M4_LITE_REPLAY_V2_VALID")
        self.assertEqual(result["tasks"], 3)


if __name__ == "__main__":
    unittest.main()
