# Machine-overview calibration report: MS-TASK-GEN001-IDENTITY-OBSERVATION-001

- generated_at_utc: 2026-09-16T21:49:28.375102+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-GEN001-IDENTITY-OBSERVATION-001/case-revision-1.json` (revision 1, sha256 `a30a0df962edc47abab7f3b150b3fd82dcb7c311da993567337c3fdc501cb93e`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001/RUN.json` (run `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.5.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-IDENTITY-OBSERVATION-v1` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-identity-observation-v1.json` (sha256 `6da102ec3c1a46725a585a12c3083588b1c4bb22a81cb6970fa384666f48b6a6`)
- delay atoms: 7; contexts planned: 440; contexts examined: 440
- pair-context checks: 5280 executed of 5280 planned
- separations seen: 956; reduced distinct witnesses: 70
- complete-within-declared-grammar: `True`; truncated: `False` (checks budget `False`, context budget `False`, witness capture `False`)
- search answer-independence: order permutation set-equal = `True`; grammar mutation removes deadline kind = `False`
- known calibration benchmark present in the discovered set: `NOT_DECLARED` (None)

## Candidates (reduced, in discovery order)

| witness | pair | context | separated observation | kind | ast sha256 |
|---|---|---|---|---|---|
| WV-0001 | (ret 0 false, ret 1 false) | deadline(0, □) | some false ≠ none | deadline_observation | `9a92083e109d…` |
| WV-0002 | (ret 0 false, ret 1 false) | race(□, ret 0 true) | ret 0 false ≠ ret 0 true | value_mismatch | `b8a1c20567d7…` |
| WV-0003 | (ret 0 true, ret 1 true) | deadline(0, □) | some true ≠ none | deadline_observation | `c054c6ab96ce…` |
| WV-0004 | (ret 0 true, ret 1 true) | race(□, ret 0 false) | ret 0 true ≠ ret 0 false | value_mismatch | `66edcd36dd91…` |
| WV-0005 | (ret 1 false, ret 0 false) | deadline(0, □) | none ≠ some false | deadline_observation | `d772f01224e0…` |
| WV-0006 | (ret 1 false, ret 0 false) | race(□, ret 0 true) | ret 0 true ≠ ret 0 false | value_mismatch | `149db19973fa…` |
| WV-0007 | (ret 1 true, ret 0 true) | deadline(0, □) | none ≠ some true | deadline_observation | `822aa3d772b0…` |
| WV-0008 | (ret 1 true, ret 0 true) | race(□, ret 0 false) | ret 0 false ≠ ret 0 true | value_mismatch | `19b1f50f2f5b…` |
| WV-0009 | (ret 0 false, ret 1 false) | race(ret 1 true, □) | ret 0 false ≠ ret 1 true | value_mismatch | `f69a2806560b…` |
| WV-0010 | (ret 0 true, ret 1 true) | race(ret 1 false, □) | ret 0 true ≠ ret 1 false | value_mismatch | `b66fb5974cfd…` |
| WV-0011 | (ret 1 false, ret 0 false) | race(ret 1 true, □) | ret 1 true ≠ ret 0 false | value_mismatch | `dbe9b10ae3cf…` |
| WV-0012 | (ret 1 true, ret 0 true) | race(ret 1 false, □) | ret 1 false ≠ ret 0 true | value_mismatch | `94d256e7ec82…` |

## Controls

- positive control (`bind_preserves_result_equivalence`, claim ref C-71): preserved = `True`
- negative control (`declared_deadline_does_not_separate_this_pair`): separated = `False`, expectation met = `True`

## Native kernel verification (accepted runs)

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0014` (witness WV-0014)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001` (sha256 `f6ec56733a7e449e65b9c03435200213b8029cc7823dfccaa3fe907ba4c541e9`)
- candidate AST sha256: `f3eca18f2b03dee3987ad00f2b904d1d5d869b9ec84d7d6fc57370d69475cbbe`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 0 true})
- target sha256: `b9f7e07487cb6d83d7fb55b0707158bfd253d38c48e6d2df6c3bbcd12dfce8fb`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0023` (witness WV-0023)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001` (sha256 `f6ec56733a7e449e65b9c03435200213b8029cc7823dfccaa3fe907ba4c541e9`)
- candidate AST sha256: `d7c591b46459094c812a58fc38e8279080781611315407a99a1aed0e567a1d63`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 0 true; false↦ret 1 false})
- target sha256: `b58b72ddab518733bb32a55b9b89a82a3c4931b85ef44b3fcf757bb32e67c03a`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0044` (witness WV-0044)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001` (sha256 `f6ec56733a7e449e65b9c03435200213b8029cc7823dfccaa3fe907ba4c541e9`)
- candidate AST sha256: `c4db2f86b7041bfeb798e1a24a5393ed49d8c37ecc5fb6b7f2de6cb3d73938d6`; target freeze: `FROZEN`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 0 true; false↦ret 1 false}) → deadline(1, □)
- target sha256: `e7aeb754176bb677fbcedbf9aa9edd5380aaa327398fb0805ee411ee69cca61f`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0067` (witness WV-0067)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001` (sha256 `f6ec56733a7e449e65b9c03435200213b8029cc7823dfccaa3fe907ba4c541e9`)
- candidate AST sha256: `d81521fa38c97d5e34366275f1a89552e7a61965484d745a1c3b4d8c35d19c48`; target freeze: `FROZEN`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 1 true; false↦ret 2 false}) → deadline(2, □)
- target sha256: `476c80c37cb44d011174e8ed0f4e4ab0556cfd87ff7ce7739341a7ab2aefd9ca`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

## Correspondence review `RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0014-f3eca18f` (witness WV-0014)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0014-f3eca18f.json`
- mechanism: The declared race context makes one side diverge while the other returns; ≈ cannot see completion order, so it identifies the two result-equivalent inputs.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0023-d7c591b4` (witness WV-0023)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0023-d7c591b4.json`
- mechanism: The declared context selects a different delivered Bool value on the two sides. Result equivalence ≈ identifies the input computations (same value and same convergence behaviour), so it cannot see which branch the context delivers.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0044-c4db2f86` (witness WV-0044)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0044-c4db2f86.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0067-d81521fa` (witness WV-0067)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-IDENTITY-OBSERVATION-001-r1-20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001-WV-0067-d81521fa.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package ([]); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); exploration receipts live under `machine-overview/runs/` and the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
