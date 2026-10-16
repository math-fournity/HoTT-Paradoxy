from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

import coq_synthetic_incompleteness as replay  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
EVALUATION = (
    ROOT
    / "machine-overview/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001"
)
RECEIPT = EVALUATION / "BUILD-RECEIPT.json"


class CoqSyntheticIncompletenessReplayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.result = replay.verify(RECEIPT, False)

    def test_exact_source_image_and_two_clean_builds_verify(self) -> None:
        self.assertEqual(
            self.result["status"],
            "COQ_SYNTHETIC_INCOMPLETENESS_REPLAY_VALID",
        )
        self.assertEqual(self.result["source"]["files"], 807)
        self.assertEqual(
            self.result["source"]["commit"],
            "cd7d8490f8542bfe85658c465bcb26b2ed163f53",
        )
        comparison = self.result["builds"]["comparison"]
        self.assertTrue(comparison["stdout_exact"])
        self.assertTrue(comparison["stderr_exact"])
        self.assertTrue(comparison["stable_artifact_paths_and_hashes_exact"])
        self.assertTrue(comparison["target_exact"])
        self.assertEqual(self.result["builds"]["stable_artifacts"]["count"], 1284)

    def test_auxiliary_timing_files_are_excluded_from_stable_replay_claim(self) -> None:
        comparison = self.result["builds"]["comparison"]
        self.assertTrue(comparison["aux_artifact_path_sets_equal"])
        self.assertFalse(comparison["aux_artifact_hashes_exact"])
        self.assertEqual(comparison["aux_nondeterministic_count"], 319)

    def test_qualification_checks_the_expected_constants_and_assumption_output(self) -> None:
        qualification = self.result["qualification"]
        self.assertEqual(
            set(qualification["constants"]),
            {
                "self_halting_diverge",
                "recursively_separating_diverge",
                "insep_essential_incompleteness",
                "epf_mu_ctq",
                "Q_incomplete",
            },
        )
        self.assertEqual(qualification["closed_under_global_context_occurrences"], 3)
        text = (EVALUATION / "qualification.stdout.txt").read_text(encoding="utf-8")
        self.assertIn("CTQ ->", text)
        self.assertIn("~ Theories.tprv T Core.falsity", text)

    def test_changed_stable_manifest_summary_is_rejected(self) -> None:
        changed = copy.deepcopy(self.receipt)
        changed["build"]["first"]["stable_artifacts"]["manifest_sha256"] = "0" * 64
        with self.assertRaisesRegex(
            replay.VerificationError,
            "ARTIFACT_SUMMARY_CHANGED:first.stable:manifest_sha256",
        ):
            replay.verify_builds(changed)


if __name__ == "__main__":
    unittest.main()
