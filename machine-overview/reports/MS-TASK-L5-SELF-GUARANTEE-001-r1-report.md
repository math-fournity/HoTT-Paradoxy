# Machine-overview symbolic exploration report: MS-TASK-L5-SELF-GUARANTEE-001

- generated_at_utc: 2026-09-13T19:28:44.156225+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L5-SELF-GUARANTEE-001/case-revision-1.json` (revision 1, sha256 `13d8aae5e3b4a5658c40b76d59258f711d136d04bf62b3461440c629373862d2`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L5-M3-SELF-001/RUN.json` (run `20260913-SEARCH-L5-M3-SELF-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `M3-CUBICAL-BREADTH-v1`

## Symbolic search

- rules: 5; proof-depth bound: 4; rule-application checks: 44
- goal terms: 2; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['section_at_liar']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bottom` | `notNoFixed (encode self self) (cong (λ h → h self) (section liar))` | boolean_no_fixed, evaluate_at_self, section_at_liar | 3/3 | `2ae6a0d6679ca7071c580d6690536b693fca05f05ffa1199be1118a71e3d6243` |
| WV-0002 | `bottom` | `notNoFixed (encode self self) (sym (sym (cong (λ h → h self) (section liar))))` | boolean_no_fixed, fixed_double_sym_decoy, evaluate_at_self, section_at_liar | 4/4 | `c8d59c31d2743d76b2a392b228567f315cd6963a693e90b9a06a65f4ef71fec7` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "section_at_liar"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "section_path",
      "checked_proof"
    ],
    "reachable": [
      "checked_proof",
      "section_path"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L5-M3-SELF-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `72ba4a9a1d69e074fea695ef3fce549614857d70f3e3814add33b90fd1b0cffb`
- source search: `20260913-SEARCH-L5-M3-SELF-001` (sha256 `965a1ea38f4c56084d0d1f345a8d2b7c0c38b817896234fd8a300d501e1daade`)
- proof AST: `2ae6a0d6679ca7071c580d6690536b693fca05f05ffa1199be1118a71e3d6243`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L5-SELF-GUARANTEE-001-r1-20260913-SEARCH-L5-M3-SELF-001-WV-0001-2ae6a0d6`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L5-SELF-GUARANTEE-001-r1-20260913-SEARCH-L5-M3-SELF-001-WV-0001-2ae6a0d6.json`
- mechanism: The witness instantiates the proposed exact self-coding section at its diagonal predicate, evaluates the resulting function path at the decoded self, and obtains a Boolean fixed point of negation.
- task preservation: `EXACT_SECTION_TARGET_PRESERVED`; reality correspondence: `TASK_STRENGTH_MISMATCH_IDENTIFIED`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
