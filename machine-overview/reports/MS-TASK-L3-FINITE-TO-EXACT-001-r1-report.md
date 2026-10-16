# Machine-overview symbolic exploration report: MS-TASK-L3-FINITE-TO-EXACT-001

- generated_at_utc: 2026-09-13T18:29:50.031385+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L3-FINITE-TO-EXACT-001/case-revision-1.json` (revision 1, sha256 `eca5a02dfc26a9767597c33daf6430e53ca5c619b9408cf16052e84d2ae82b9b`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L3-M4-EXACT-001/RUN.json` (run `20260913-SEARCH-L3-M4-EXACT-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L3-CUBICAL-M4-TASKSET-v1`

## Symbolic search

- rules: 6; proof-depth bound: 4; rule-application checks: 59
- goal terms: 4; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['finite_to_exact_candidate']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `exact_arrival` | `finiteToExactCandidate (finite)` | finite_to_exact_candidate, finite_observation | 2/2 | `bdc25fd93a061e96ddffd725fbcf4682fd88411450bba178d9625c0f70eb7ad5` |
| WV-0002 | `exact_arrival` | `finiteToExactCandidate (finite)` | exact_identity_decoy, finite_to_exact_candidate, finite_observation | 3/3 | `cae734e8568e9bb28e0a032126e90c362bf220c5c14dd1fa1cfd47b61072332c` |
| WV-0003 | `exact_arrival` | `finiteToExactCandidate (forgetRefinement (refineFinite (finite)))` | finite_to_exact_candidate, refined_forget_decoy, finite_refine_decoy, finite_observation | 4/4 | `f871461bf25ac7dab365554f6da7785dbd42c7bb24ec4d8a67ca098f491f3040` |
| WV-0004 | `exact_arrival` | `finiteToExactCandidate (finite)` | exact_identity_decoy, exact_identity_decoy, finite_to_exact_candidate, finite_observation | 4/4 | `5867c2476bef1a86e2cca707eb0e9947d339409a0f8f437f941bb0b1824cef1e` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "finite_to_exact_candidate"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "finite_approximation",
      "path_decoy"
    ],
    "reachable": [
      "finite_approximation",
      "path_decoy"
    ]
  }
}
```

## Native Cubical verification

- no accepted native run yet
## Native candidate rejections

### `20260913-VERIFY-L3-M4-EXACT-001` (witness WV-0001)

- status: `NATIVE_CHECK_FAILED`; receipt: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-VERIFY-L3-M4-EXACT-001/RUN.json`
- target sha256: `72dd6b6b79b08891a2a923e9553b621be7d6d522ce5f13a5fba41bb369fb0fb1`; source search: `20260913-SEARCH-L3-M4-EXACT-001`
- kernel `verify`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`

## Correspondence review `RV-MS-TASK-L3-FINITE-TO-EXACT-001-r1-20260913-SEARCH-L3-M4-EXACT-001-WV-0001-bdc25fd9`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L3-FINITE-TO-EXACT-001-r1-20260913-SEARCH-L3-M4-EXACT-001-WV-0001-bdc25fd9.json`
- mechanism: The symbolic witness applies the declared speculative finite-to-exact rule to finite approximation evidence.  Symbolic typing alone does not establish that the rule has a native Cubical inhabitant.
- task preservation: `TASK_INPUT_PRESERVED_CANDIDATE_REQUIRES_NATIVE_DECISION`; reality correspondence: `BOUNDED_CONTROL_ONLY`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
