# Machine-overview symbolic exploration report: MS-TASK-L3-INTERVAL-COMPLETION-001

- generated_at_utc: 2026-09-13T17:26:44.650337+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L3-INTERVAL-COMPLETION-001/case-revision-1.json` (revision 1, sha256 `827f4895c53792aa7dbb826978a05ff85c5e09c16896b89a073af9d917e48f77`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L3-SYMBOLIC-001/RUN.json` (run `20260913-SEARCH-L3-SYMBOLIC-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L3-CUBICAL-INTERVAL-MOTION-v1`

## Symbolic search

- rules: 4; proof-depth bound: 4; rule-application checks: 39
- goal terms: 2; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['interval_eta']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bottom` | `apart ((λ i → f i))` | apart_elim, interval_eta | 2/2 | `e538925469002b158d745a35162bfd75827055fc4f3a5bb9991b25ddcb3813eb` |
| WV-0002 | `bottom` | `apart (sym (sym ((λ i → f i))))` | apart_elim, path_sym_back, path_sym, interval_eta | 4/4 | `ba27008d95af0061a55319f7d98267a0d3fd5eae12594838a226d5b51b8e725b` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "interval_eta"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "endpoint_path"
    ],
    "reachable": [
      "endpoint_path"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L3-SYMBOLIC-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `c4ffd38ac5f40b25907f386345390dbe0d403511a290871fd570ef0c64524115`
- source search: `20260913-SEARCH-L3-SYMBOLIC-001` (sha256 `bec2b51b93ece2f0cd58d12b22dbbec210890389815ef0c46cc723f5d5bc66f4`)
- proof AST: `e538925469002b158d745a35162bfd75827055fc4f3a5bb9991b25ddcb3813eb`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L3-INTERVAL-COMPLETION-001-r1-20260913-SEARCH-L3-SYMBOLIC-001-WV-0001-e5389254`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L3-INTERVAL-COMPLETION-001-r1-20260913-SEARCH-L3-SYMBOLIC-001-WV-0001-e5389254.json`
- mechanism: The declared theoryization uses the cubical interval as the activity's time carrier. Any internal observable f : I → A supplies an endpoint Path λ i → f i; composing that Path with the task's declared endpoint apartness yields the searched obstruction.
- task preservation: `PRESERVED_ACROSS_DECLARED_ENDPOINT_OBSERVATION`; reality correspondence: `UNRESOLVED`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated Type₀ theorem target, controls, expected rejection, and replay.
- The activity-time interpretation is an explicit model under test. The run does not establish that standard HoTT identifies Path with physical time or that every temporal observable is continuous.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
