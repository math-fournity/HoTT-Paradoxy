# Machine-overview symbolic exploration report: MS-TASK-L5-GIVEN-PROOF-CHECK-001

- generated_at_utc: 2026-09-13T20:14:40.259720+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L5-GIVEN-PROOF-CHECK-001/case-revision-1.json` (revision 1, sha256 `574f115920801f02ebbedd41bedb4e2678ab2e8165c2d40a3b93bd16018b2f3b`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L5-CHECK-001/RUN.json` (run `20260913-SEARCH-L5-CHECK-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L5-CONSUMER-QUALIFICATION-v1`

## Symbolic search

- rules: 4; proof-depth bound: 3; rule-application checks: 20
- goal terms: 1; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['check_supplied_derivation']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `accepted_derivation` | `L5.checkGivenProof (L5.givenK)` | check_supplied_derivation, supply_derivation | 2/2 | `034a4efdc3880504f6399285ad2c3fbd1097888ca01e72ed3f3ff95f90c19755` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "check_supplied_derivation"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "supplied_derivation"
    ],
    "reachable": [
      "searched_derivation",
      "supplied_derivation",
      "truth_decision"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L5-CHECK-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `d49c131ccb86e547a04517255be68ef4fd617515f9d4b0e6f50df9d6b5b04b12`
- source search: `20260913-SEARCH-L5-CHECK-001` (sha256 `4e7b6d044f15d0487a792b733faa1feb6a5fe66145af8bf07edcdfaf28d250ed`)
- proof AST: `034a4efdc3880504f6399285ad2c3fbd1097888ca01e72ed3f3ff95f90c19755`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L5-GIVEN-PROOF-CHECK-001-r1-20260913-SEARCH-L5-CHECK-001-WV-0001-034a4efd`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L5-GIVEN-PROOF-CHECK-001-r1-20260913-SEARCH-L5-CHECK-001-WV-0001-034a4efd.json`
- mechanism: The witness starts with one supplied derivation in the fixed ERCF-3 object syntax and passes that same derivation through the declared checker.  It performs no proof search, truth decision or self-reliability step.
- task preservation: `GIVEN_PROOF_TASK_EXACTLY_PRESERVED`; reality correspondence: `TASK_MODEL_EXACT`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded symbolic model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
