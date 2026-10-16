# Machine-overview symbolic exploration report: MS-TASK-L2-TRUNCATED-LIMIT-001

- generated_at_utc: 2026-09-13T19:28:35.158167+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L2-TRUNCATED-LIMIT-001/case-revision-1.json` (revision 1, sha256 `1a4b2fda50638b758379a810f84ba1b0d54ee2bd5b0eb69fed0fd299557eb234`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L2-M3-LIMIT-001/RUN.json` (run `20260913-SEARCH-L2-M3-LIMIT-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `M3-CUBICAL-BREADTH-v1`

## Symbolic search

- rules: 5; proof-depth bound: 4; rule-application checks: 62
- goal terms: 2; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['hypothetical_recovery']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `bottom` | `TL.C-114-LimA-empty (recover (TL.C-115-limTrunc))` | exact_limit_empty, hypothetical_recovery, stagewise_mere_limit | 3/3 | `562c3e9090c7d4823f9198304a0365f318904908e42a0c589a16270b3ba8d414` |
| WV-0002 | `bottom` | `TL.C-114-LimA-empty (recover (TL.C-115-limTrunc))` | exact_limit_empty, hypothetical_recovery, truncated_identity_decoy, stagewise_mere_limit | 4/4 | `f7d7d449c44ffb3b4967357c196cd296b6955e246dca2d79e3a0472e278d3af4` |

## Declared controls

```json
{
  "negative": {
    "control": "ablation_removes_goal_proof",
    "expectation_met": true,
    "goal_terms_after_ablation": 0,
    "removed_rules": [
      "hypothetical_recovery"
    ]
  },
  "positive": {
    "control": "declared_zero-premise_rules_reach_control_goals",
    "expectation_met": true,
    "goals": [
      "truncated_limit",
      "decoy_limit"
    ],
    "reachable": [
      "decoy_limit",
      "truncated_limit"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L2-M3-LIMIT-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `cb8a8ebd9a38da7817afd022ef080747f5cd849fc5b77aba027faacf441692e2`
- source search: `20260913-SEARCH-L2-M3-LIMIT-001` (sha256 `8fedb9dde9547515dab197c34dd56240d7c65131c542cdfa6d478133b915caa7`)
- proof AST: `562c3e9090c7d4823f9198304a0365f318904908e42a0c589a16270b3ba8d414`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L2-TRUNCATED-LIMIT-001-r1-20260913-SEARCH-L2-M3-LIMIT-001-WV-0001-562c3e90`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L2-TRUNCATED-LIMIT-001-r1-20260913-SEARCH-L2-M3-LIMIT-001-WV-0001-562c3e90.json`
- mechanism: The witness starts from the declared stagewise truncated limit, applies the hypothetical recovery to obtain one compatible exact limit, and eliminates that result with the pinned exact-limit emptiness proof.
- task preservation: `FIXED_TOWER_AND_RECOVERY_TASK_PRESERVED`; reality correspondence: `FORMAL_TOWER_ONLY`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
