# Machine-overview calibration report: MS-TASK-L1-RACE-COMPLETION-001

- generated_at_utc: 2026-09-13T15:14:24.519105+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001/case-revision-3.json` (revision 3, sha256 `5524651182b74edc02882b0f108bac1f0ff6d415cc4d9b4fd780838cc527e733`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L1-003/RUN.json` (run `20260913-SEARCH-L1-003`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.1.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-PARTIALITY-RACE-DEADLINE-v1` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-v1.json` (sha256 `77b04fc6366555dbd1fc8a340c95c3c5a0f1d4a96a45b8bbce2956a8454ca986`)
- delay atoms: 7; contexts planned: 399; contexts examined: 399
- pair-context checks: 4788 executed of 4788 planned
- separations seen: 916; reduced distinct witnesses: 50
- complete-within-declared-grammar: `True`; truncated: `False` (checks budget `False`, context budget `False`, witness capture `False`)
- search answer-independence: order permutation set-equal = `True`; grammar mutation removes deadline kind = `False`
- known calibration benchmark present in the discovered set: `PRESENT` (['C-73', 'C-74'])

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

### `20260913-VERIFY-L1-POSTFIX-COMPLETION-001` (witness WV-0013)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_CALIBRATION_INSTANCE`; attempt: `1`
- source search run: `20260913-SEARCH-L1-003` (sha256 `d0e28a5c794ec45bb7300a1cf58bbfb1c97eb9316fbc672f9cc9914de5d70bd4`)
- candidate AST sha256: `e76eec9e97b7f1c2576dd0c955b808abcf528e893915494ab501bec5a42d62d2`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 0 true; false↦ω})
- target sha256: `103b4c9abfdd3b6dd977e98920d9b92741a0e3e9acf03e732a87914b91fe90ce`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

### `20260913-VERIFY-L1-POSTFIX-DEADLINE-001` (witness WV-0001)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_CALIBRATION_INSTANCE`; attempt: `1`
- source search run: `20260913-SEARCH-L1-003` (sha256 `d0e28a5c794ec45bb7300a1cf58bbfb1c97eb9316fbc672f9cc9914de5d70bd4`)
- candidate AST sha256: `9a92083e109d41ff259ce8cef960422f14a37d1733cdff674c232395ef72c8b0`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under deadline(0, □)
- target sha256: `87bb4895dede05f11e464d38b7cce85c43aa4c71419310959b293d151bcec548`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

### `20260913-VERIFY-L1-POSTFIX-VALUE-001` (witness WV-0002)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_CALIBRATION_INSTANCE`; attempt: `1`
- source search run: `20260913-SEARCH-L1-003` (sha256 `d0e28a5c794ec45bb7300a1cf58bbfb1c97eb9316fbc672f9cc9914de5d70bd4`)
- candidate AST sha256: `b8a1c20567d7b27debdfb414ce06c7348bbf8753520f85d322ba0920f90f7dfc`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true)
- target sha256: `e1ee1b9316fa720b2cd957ce56a5ed3e98ff0a1cd6167206b10fad3d962d5b49`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

## Correspondence review `RV-MS-TASK-L1-RACE-COMPLETION-001-r3-20260913-SEARCH-L1-003-WV-0001-9a92083e` (witness WV-0001)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-r3-20260913-SEARCH-L1-003-WV-0001-9a92083e.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `PRESERVED_AT_MODEL_LEVEL`; reality correspondence `UNRESOLVED`
- review checks: grammar_membership=PASS, case_search_binding=PASS, declared_observation_kind=PASS, declared_consumer_present=PASS, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-L1-RACE-COMPLETION-001-r3-20260913-SEARCH-L1-003-WV-0002-b8a1c205` (witness WV-0002)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-r3-20260913-SEARCH-L1-003-WV-0002-b8a1c205.json`
- mechanism: The declared context selects a different delivered Bool value on the two sides. Result equivalence ≈ identifies the input computations (same value and same convergence behaviour), so it cannot see which branch the context delivers.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `PRESERVED_AT_MODEL_LEVEL`; reality correspondence `UNRESOLVED`
- review checks: grammar_membership=PASS, case_search_binding=PASS, declared_observation_kind=PASS, declared_consumer_present=PASS, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-L1-RACE-COMPLETION-001-r3-20260913-SEARCH-L1-003-WV-0013-e76eec9e` (witness WV-0013)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-r3-20260913-SEARCH-L1-003-WV-0013-e76eec9e.json`
- mechanism: The declared race context reads completion order, and the declared business continuation turns the losing branch into divergence; ≈ identifies the two inputs because they have the same result behaviour before composition.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `PRESERVED_AT_MODEL_LEVEL`; reality correspondence `UNRESOLVED`
- review checks: grammar_membership=PASS, case_search_binding=PASS, declared_observation_kind=PASS, declared_consumer_present=PASS, compensation_classified=PASS

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package (['C-73', 'C-74', 'C-75', 'C-76']); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); exploration receipts live under `machine-overview/runs/` and the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
