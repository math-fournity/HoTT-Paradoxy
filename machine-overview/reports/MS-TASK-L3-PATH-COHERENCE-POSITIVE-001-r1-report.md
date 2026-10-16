# Machine-overview symbolic exploration report: MS-TASK-L3-PATH-COHERENCE-POSITIVE-001

- generated_at_utc: 2026-09-13T18:29:44.035269+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L3-PATH-COHERENCE-POSITIVE-001/case-revision-1.json` (revision 1, sha256 `fa5560856427b65a86e94b5b5f7dec5f717dfe479c392c2db62901432300b772`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L3-M4-PATH-001/RUN.json` (run `20260913-SEARCH-L3-M4-PATH-001`, COMPLETED_WITHIN_BUDGET)
- backend: `symbolic-horn-v1`; profile: `L3-CUBICAL-M4-TASKSET-v1`

## Symbolic search

- rules: 5; proof-depth bound: 4; rule-application checks: 76
- goal terms: 7; complete within declared grammar: `True`; truncated: `False`
- order permutation set-equal: `True`
- ablation: `remove symbolic rules ['interval_eta']`; goal remains: `False`

| witness | goal | synthesized term | rules | nodes/depth | AST sha256 |
|---|---|---|---|---|---|
| WV-0001 | `endpoint_path` | `(λ i → f i)` | interval_eta | 1/1 | `7e96a14d76183e976ee8081dab44ce1a67c03e29ea8fdde52499f06339f1921d` |
| WV-0002 | `endpoint_path` | `(λ i → f i)` | path_identity_decoy, interval_eta | 2/2 | `a6905c41623fd46b9d154281c6c1657584fdb863353fef1711e23934b4be7e60` |
| WV-0003 | `endpoint_path` | `(λ i → f i)` | path_identity_decoy, path_identity_decoy, interval_eta | 3/3 | `b32a67949633b06da0a527d38f8dc5b6e2117fef6985149c93e7718dac9304c6` |
| WV-0004 | `endpoint_path` | `sym (sym ((λ i → f i)))` | path_sym_back, path_sym, interval_eta | 3/3 | `c3cbd64d2bb61771a46dc8cc7c2c795838b49e1a214c6c823c59f187c31c4171` |
| WV-0005 | `endpoint_path` | `(λ i → f i)` | path_identity_decoy, path_identity_decoy, path_identity_decoy, interval_eta | 4/4 | `96090d7d3ae6c37797f7e9f682c92d620f819f9734775a6fa14a855a3dbb00a1` |
| WV-0006 | `endpoint_path` | `sym (sym ((λ i → f i)))` | path_sym_back, path_sym, path_identity_decoy, interval_eta | 4/4 | `d3e2ac6676afff39b8ac47e3f48717f52979feb4e1a9b0af8d8ce28d36547428` |
| WV-0007 | `endpoint_path` | `sym (sym ((λ i → f i)))` | path_identity_decoy, path_sym_back, path_sym, interval_eta | 4/4 | `da8c9f1111f2a44ad39255201347664f7fb6750ae906f9cba5b127a9bc426dce` |

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
      "endpoint_path",
      "event_decoy"
    ],
    "reachable": [
      "endpoint_path",
      "event_decoy"
    ]
  }
}
```

## Native Cubical verification

### `20260913-VERIFY-L3-M4-PATH-001` (witness WV-0001)

- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; target sha256: `cc363a17f23d2d8b28d88235ead86e7930a42fe6c361283eeb02aa77410384f7`
- source search: `20260913-SEARCH-L3-M4-PATH-001` (sha256 `eefffb515b272c8a0e4bf4b2c03cf56529edd3a3cbdd4d09b714fbb6889bd23a`)
- proof AST: `7e96a14d76183e976ee8081dab44ce1a67c03e29ea8fdde52499f06339f1921d`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`

## Correspondence review `RV-MS-TASK-L3-PATH-COHERENCE-POSITIVE-001-r1-20260913-SEARCH-L3-M4-PATH-001-WV-0001-7e96a14d`

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L3-PATH-COHERENCE-POSITIVE-001-r1-20260913-SEARCH-L3-M4-PATH-001-WV-0001-7e96a14d.json`
- mechanism: The task asks for endpoint Path coherence from an internal f : I → A. The witness uses the declared interval-abstraction rule, so the generated Path is the requested output rather than an added completion obligation.
- task preservation: `PATH_TASK_PRESERVED_BY_PATH_REPRESENTATION`; reality correspondence: `NOT_APPLICABLE_FORMAL_POSITIVE_CONTROL`

## Evidence boundaries

- The symbolic search composes declared typed rules; native Cubical Agda checks the generated target, controls, expected rejection, and replay.
- The task is one bounded M4-lite model. Its native result checks that model only; physical time, natural-use adoption, novelty and general search effectiveness remain separate questions.
- This is an exploration receipt, not a registered mathematical claim. It does not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
