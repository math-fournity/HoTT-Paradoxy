# Machine-overview symbolic exploration report: MS-TASK-L5-BOUNDED-PROOF-SEARCH-001

- generated_at_utc: 2026-09-13T20:14:46.120465+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L5-BOUNDED-PROOF-SEARCH-001/case-revision-1.json` (revision 1, sha256 `ca1485b39007d9e5e5d3d1191027bca7cafb10f40d9ddbe375d723e8c51faa95`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L5-BOUNDED-001/RUN.json` (run `20260913-SEARCH-L5-BOUNDED-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L5-CONSUMER-QUALIFICATION-v1`

## Symbolic search

- rules: 4; proof-depth bound: 4; rule-application checks: 26
- goal terms: 1; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['execute_search']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bounded_result` | `Target.bounded (L5.searchAtOne) (L5.searchSoundAtOne (L5.searchAtOne))` | package_search_result, execute_search, validate_found_result, execute_search | 4/3 | `5b10f679ea9a299ec255b64581f034f757000b6b21eb895240161486ffcb103b` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "execute_search"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": false,
    "goals": [
      "search_success",
      "checked_found_proof"
    ],
    "reachable": [
      "search_success",
      "unbounded_result"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L5-BOUNDED-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `3c010d690b04b74d0ebeb42bc1a8f51e98e3557e88baef2a97aabeac5dc2963d`
- source search: `20260913-SEARCH-L5-BOUNDED-001` (sha256 `4639d59f2fdfabd41d48d61a9b99d8dc22236ba174a472c03e65990a3c88aa70`)
- proof AST: `5b10f679ea9a299ec255b64581f034f757000b6b21eb895240161486ffcb103b`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L5-BOUNDED-PROOF-SEARCH-001-r1-20260913-SEARCH-L5-BOUNDED-001-WV-0001-5b10f679`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L5-BOUNDED-PROOF-SEARCH-001-r1-20260913-SEARCH-L5-BOUNDED-001-WV-0001-5b10f679.json`
- mechanism: The witness executes the declared one-fuel search, checks its successful Boolean result, and packages the result with a derivation of the fixed K-formula.
- task preservation: `BOUNDED_SEARCH_TASK_EXACTLY_PRESERVED`; reality correspondence: `TASK_MODEL_EXACT_WITH_FUEL`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded symbolic model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
