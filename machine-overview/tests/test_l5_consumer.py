from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import l5_consumer_audit  # noqa: E402
from machine_overview.util import sha256_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
EVALUATION = ROOT / "machine-overview/evaluations/L5-CONSUMER-QUALIFICATION-001"


class L5ConsumerQualificationTest(unittest.TestCase):
    def test_adapter_freeze_still_matches_every_pinned_source(self) -> None:
        freeze = json.loads((EVALUATION / "ADAPTER-FREEZE.json").read_text(encoding="utf-8"))
        self.assertTrue(freeze["future_inputs_absent_at_freeze"])
        self.assertEqual(freeze["source_artifact_count"], 9)
        for row in freeze["adapter_sources"]:
            path = ROOT / row["path"]
            self.assertEqual(path.stat().st_size, row["bytes"], row["path"])
            self.assertEqual(sha256_file(path), row["sha256"], row["path"])

    def test_consumer_matrix_replays_and_has_no_qualified_hit(self) -> None:
        run = EVALUATION / "runs/20260913-L5-CONSUMER-AUDIT-001/RUN.json"
        result = l5_consumer_audit.verify(ROOT, run)
        self.assertEqual(result["status"], "L5_CONSUMER_AUDIT_VALID")
        self.assertEqual(result["verdict"], "NO_QUALIFIED_CONSUMER_IN_FROZEN_SET")
        self.assertEqual(result["source_count"], 5)
        self.assertEqual(result["qualified_hits"], [])

    def test_four_capabilities_remain_distinct(self) -> None:
        run = json.loads(
            (EVALUATION / "runs/20260913-L5-CONSUMER-AUDIT-001/RUN.json").read_text(encoding="utf-8")
        )["deterministic"]
        self.assertEqual(run["strongest_near_hit"], "L5-S2-METAROCQ-9.1")
        capabilities = [
            "given_proof_check",
            "bounded_proof_search",
            "finite_truth_decision",
            "same_layer_total_self_reliability",
        ]
        self.assertEqual(set(run["capability_counts"]), set(capabilities))
        self.assertGreater(
            run["capability_counts"]["given_proof_check"]["CLAIMED_WITH_SCOPE"]
            + run["capability_counts"]["given_proof_check"]["INFRASTRUCTURE_PRIMITIVE"],
            0,
        )
        self.assertEqual(
            run["capability_counts"]["same_layer_total_self_reliability"]["CLAIMED_WITH_SCOPE"],
            0,
        )

    def test_four_native_runs_have_exact_positive_negative_and_replay_chain(self) -> None:
        run_ids = [
            "20260913-VERIFY-L5-CHECK-001",
            "20260913-VERIFY-L5-BOUNDED-001",
            "20260913-VERIFY-L5-TRUTH-001",
            "20260913-VERIFY-L5-LOB-001",
        ]
        for run_id in run_ids:
            with self.subTest(run_id=run_id):
                payload = json.loads(
                    (ROOT / "machine-overview/runs" / run_id / "RUN.json").read_text(encoding="utf-8")
                )
                self.assertEqual(payload["status"], "NATIVE_CHECKED_EXPLORATION_CANDIDATE")
                kernels = {row["label"]: row for row in payload["kernel_runs"]}
                self.assertEqual(kernels["verify"]["exit_code"], 0)
                self.assertEqual(kernels["controls"]["exit_code"], 0)
                self.assertEqual(kernels["negative-control"]["exit_code"], 42)
                self.assertTrue(kernels["negative-control"]["expectation_met"])
                self.assertEqual(kernels["verify-replay"]["exit_code"], 0)
                self.assertEqual(payload["replay"]["classification"], "EXACT_EXIT_STDOUT_STDERR_MATCH")


if __name__ == "__main__":
    unittest.main()
