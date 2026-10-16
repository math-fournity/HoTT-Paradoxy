# Machine-overview symbolic exploration report: MS-TASK-L6-COMPENSATION-COHERENCE-001

- generated_at_utc: 2026-09-13T19:28:48.630551+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L6-COMPENSATION-COHERENCE-001/case-revision-1.json` (revision 1, sha256 `491143ceb24d11f952b66ecf8c0442c56f2d112bd8e609fd6bde54503104c593`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L6-M3-COMP-001/RUN.json` (run `20260913-SEARCH-L6-M3-COMP-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `M3-CUBICAL-BREADTH-v1`

## Symbolic search

- rules: 5; proof-depth bound: 4; rule-application checks: 90
- goal terms: 4; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['path_compensation']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bottom` | `apart (path)` | apart_compensation, path_compensation | 2/2 | `b2776ba84685650a08e7184b4bce5f8f2573f89691216d1583eb3163338b0ae3` |
| WV-0002 | `bottom` | `apart (path)` | apart_compensation, path_identity_decoy, path_compensation | 3/3 | `9bfdd8d4e9c711afcebf46af4b93c3a78062519d2a87f4462bc875f05c804074` |
| WV-0003 | `bottom` | `apart (path)` | apart_compensation, path_identity_decoy, path_identity_decoy, path_compensation | 4/4 | `20c1576fcd7d85075ba061923edc0766b01d477b66ed8d6b03ad65fe6d144ce4` |
| WV-0004 | `bottom` | `apart (sym (sym (path)))` | apart_compensation, path_sym_back_decoy, path_sym_decoy, path_compensation | 4/4 | `fa5f2b74c78aa0ae623d8f4c2752ba1aec520c51d8224150d06d540ae68f9fe7` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "path_compensation"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "path_evidence"
    ],
    "reachable": [
      "path_evidence"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L6-M3-COMP-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `12aea003aaeb547564f9f317b63aa1056dcd25e3f74fd50812ce1cc2258c8309`
- source search: `20260913-SEARCH-L6-M3-COMP-001` (sha256 `fb2b4f9509c18ac6be2ffd3ddc8cd89f7d62a8416c742eea92c006dff6867d45`)
- proof AST: `b2776ba84685650a08e7184b4bce5f8f2573f89691216d1583eb3163338b0ae3`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L6-COMPENSATION-COHERENCE-001-r1-20260913-SEARCH-L6-M3-COMP-001-WV-0001-b2776ba8`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L6-COMPENSATION-COHERENCE-001-r1-20260913-SEARCH-L6-M3-COMP-001-WV-0001-b2776ba8.json`
- mechanism: The witness applies the declared endpoint-apartness compensation to the declared Path compensation for the same endpoints.  Their individual outputs have incompatible joint coherence requirements.
- task preservation: `JOINT_COMPENSATION_TASK_PRESERVED`; reality correspondence: `MODEL_RELATIVE_KNOWN_MECHANISM`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
