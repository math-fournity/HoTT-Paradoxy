# Machine-overview symbolic exploration report: MS-TASK-L4-SIP-OBSERVATION-001

- generated_at_utc: 2026-09-13T19:28:39.641652+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L4-SIP-OBSERVATION-001/case-revision-1.json` (revision 1, sha256 `da4b30228e7629bfcefad148042727dd080d630a8c2298dbd957f5e77c9da962`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L4-M3-SIP-001/RUN.json` (run `20260913-SEARCH-L4-M3-SIP-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `M3-CUBICAL-BREADTH-v1`

## Symbolic search

- rules: 7; proof-depth bound: 4; rule-application checks: 50
- goal terms: 1; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['sip_identification']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bottom` | `SIP.C-125-obs-differs (sym (hs) ∙ cong f (SIP.C-124-identification) ∙ ht)` | bool_apart, chain_observation, left_specification, map_observer, sip_identification, right_specification | 6/4 | `f7e15a7fa1967ae7810f646bba6a39b6d49192b2c4f6866da2c6bff77a21ab4c` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "sip_identification"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "structure_path",
      "left_spec",
      "right_spec"
    ],
    "reachable": [
      "left_spec",
      "right_spec",
      "structure_path"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L4-M3-SIP-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `2e2cc8cb1f2fe6c31c92fc519ffe8d553a4717fe75dc2681798e334b20b3ae8f`
- source search: `20260913-SEARCH-L4-M3-SIP-001` (sha256 `2ab6b60b66f3de097b66a4a35f98da7b99c6da3047bb62df3f87340dbf4a7350`)
- proof AST: `f7e15a7fa1967ae7810f646bba6a39b6d49192b2c4f6866da2c6bff77a21ab4c`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L4-SIP-OBSERVATION-001-r1-20260913-SEARCH-L4-M3-SIP-001-WV-0001-f7e15a7f`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L4-SIP-OBSERVATION-001-r1-20260913-SEARCH-L4-M3-SIP-001-WV-0001-f7e15a7f.json`
- mechanism: The witness maps the pinned SIP/ua identification through a proposed Bool observer and combines it with the observer's two endpoint specifications, forcing true ≡ false.
- task preservation: `SIP_TASK_AND_OUTSIDE_OBSERVATION_PRESERVED`; reality correspondence: `FIXED_FORMAL_PRESENTATIONS`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
