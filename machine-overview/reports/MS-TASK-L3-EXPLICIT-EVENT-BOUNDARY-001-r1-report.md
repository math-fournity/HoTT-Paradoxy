# Machine-overview symbolic exploration report: MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001

- generated_at_utc: 2026-09-13T18:29:46.989387+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001/case-revision-1.json` (revision 1, sha256 `02caf24733d0a06c943b3577ecf8662507a8819ebdf5e9d5e9e523ce756f1a60`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L3-M4-EVENT-001/RUN.json` (run `20260913-SEARCH-L3-M4-EVENT-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L3-CUBICAL-M4-TASKSET-v1`

## Symbolic search

- rules: 7; proof-depth bound: 4; rule-application checks: 59
- goal terms: 1; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['event_pack']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `event_boundary` | `(phase-start , (phase-finish , phase-apart))` | event_pack, stage_start, stage_finish, stage_apart | 4/2 | `450b7226e8ba0da8b670eecc1bd9b4053d080f6ab4fdce5416620ac5cb2c3b24` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "event_pack"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "start_pending",
      "finish_done",
      "endpoint_apart",
      "path_decoy"
    ],
    "reachable": [
      "endpoint_apart",
      "finish_done",
      "path_decoy",
      "start_pending"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L3-M4-EVENT-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `61c12e2fb60168088092dad0472ceab535fd2d25018983da77f210d5ef4ce6a4`
- source search: `20260913-SEARCH-L3-M4-EVENT-001` (sha256 `3e42aaf9344aab0fc12d22b25498dcb8af546035b092baa5322180e11ac9da3f`)
- proof AST: `450b7226e8ba0da8b670eecc1bd9b4053d080f6ab4fdce5416620ac5cb2c3b24`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001-r1-20260913-SEARCH-L3-M4-EVENT-001-WV-0001-450b7226`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001-r1-20260913-SEARCH-L3-M4-EVENT-001-WV-0001-450b7226.json`
- mechanism: The witness combines separately declared start, finish and apartness facts over an ordinary Stage carrier.  Exact completion remains an event-boundary observation and does not require treating Stage as the cubical dimension.
- task preservation: `PRESERVED_BY_EXPLICIT_EVENT_STRUCTURE`; reality correspondence: `MODEL_RELATIVE_EVENT_CONTROL`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
