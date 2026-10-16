# Machine-overview symbolic exploration report: MS-TASK-L5-FINITE-TRUTH-DECISION-001

- generated_at_utc: 2026-09-13T20:14:52.079886+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L5-FINITE-TRUTH-DECISION-001/case-revision-1.json` (revision 1, sha256 `f3f36408bb99874e816fe19462a1c84e453a8a3acdab50a8adcd00ccfc02b900`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L5-TRUTH-001/RUN.json` (run `20260913-SEARCH-L5-TRUTH-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L5-CONSUMER-QUALIFICATION-v1`

## Symbolic search

- rules: 2; proof-depth bound: 2; rule-application checks: 6
- goal terms: 1; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['finite_truth_certificate']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `finite_truth_certificate` | `L5.truthDecision` | finite_truth_certificate | 1/1 | `5c75d8265ee1c2f1c0b3ca4c0d64591e01636343fa77183ec6f38eb40d19ad04` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "finite_truth_certificate"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "finite_truth_certificate"
    ],
    "reachable": [
      "finite_truth_certificate",
      "general_truth_oracle"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L5-TRUTH-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `3508ea9d9fcf8fed159a7927a5a5b5e3526527066aa522b11842e83171a92340`
- source search: `20260913-SEARCH-L5-TRUTH-001` (sha256 `9ad43e53700dbb0e97aa8553cb6f3080efe36c5457e1712bfd92a20e401ad635`)
- proof AST: `5c75d8265ee1c2f1c0b3ca4c0d64591e01636343fa77183ec6f38eb40d19ad04`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L5-FINITE-TRUTH-DECISION-001-r1-20260913-SEARCH-L5-TRUTH-001-WV-0001-5c75d826`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L5-FINITE-TRUTH-DECISION-001-r1-20260913-SEARCH-L5-TRUTH-001-WV-0001-5c75d826.json`
- mechanism: The witness evaluates one closed formula in the explicitly finite Boolean fragment and supplies the resulting equality certificate.
- task preservation: `FINITE_TRUTH_TASK_EXACTLY_PRESERVED`; reality correspondence: `TASK_MODEL_EXACT`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded symbolic model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
