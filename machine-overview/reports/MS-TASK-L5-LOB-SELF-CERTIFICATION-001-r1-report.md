# Machine-overview symbolic exploration report: MS-TASK-L5-LOB-SELF-CERTIFICATION-001

- generated_at_utc: 2026-09-13T20:14:57.898495+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L5-LOB-SELF-CERTIFICATION-001/case-revision-1.json` (revision 1, sha256 `f18529042a4771fd98325571ac9f5a665fbea9eb9e407b09901369ae7740047f`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L5-LOB-001/RUN.json` (run `20260913-SEARCH-L5-LOB-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L5-CONSUMER-QUALIFICATION-v1`

## Symbolic search

- rules: 5; proof-depth bound: 4; rule-application checks: 33
- goal terms: 1; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['certify_reflection']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bottom` | `reflect ⊥ (lob ⊥ (certify ⊥))` | reflect_bottom, lob_at_bottom, certify_reflection | 3/3 | `f3e60d5a935069305cdf2a8f75d9c9dafa76abe46349337b4fb80521b8d2330c` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "certify_reflection"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": false,
    "goals": [
      "certified_reflection_at_bottom",
      "boxed_bottom",
      "given_check",
      "finite_truth"
    ],
    "reachable": [
      "certified_reflection_at_bottom",
      "finite_truth",
      "given_check"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L5-LOB-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `a3b2ddb3687fdd6ce339aece5e7b4d8f5bee33c298b0ec35deb27e390c10f23d`
- source search: `20260913-SEARCH-L5-LOB-001` (sha256 `39c4178a45d4c5c035b2aef06431d676a418c5d8540aca619f380ae07470c3b7`)
- proof AST: `f3e60d5a935069305cdf2a8f75d9c9dafa76abe46349337b4fb80521b8d2330c`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L5-LOB-SELF-CERTIFICATION-001-r1-20260913-SEARCH-L5-LOB-001-WV-0001-f3e60d5a`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L5-LOB-SELF-CERTIFICATION-001-r1-20260913-SEARCH-L5-LOB-001-WV-0001-f3e60d5a.json`
- mechanism: The witness instantiates the internally certified reflection principle at bottom, uses the declared Löb rule to obtain boxed bottom, and applies reflection.
- task preservation: `CONDITIONAL_INTERFACE_EXACTLY_PRESERVED`; reality correspondence: `CONSUMER_QUALIFICATION_REQUIRED`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded symbolic model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
