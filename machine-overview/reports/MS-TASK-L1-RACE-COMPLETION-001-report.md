# Machine-overview calibration report: MS-TASK-L1-RACE-COMPLETION-001

- generated_at_utc: 2026-09-13T14:28:56.918141+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001/case-revision-2.json` (sha256 `b4a7892e0febd9b3d9f7862edf6d8668b96e8104b53428dd66a2100e9fd24985`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260913-SEARCH-L1-002/RUN.json` (run `20260913-SEARCH-L1-002`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.1.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-PARTIALITY-RACE-DEADLINE-v0` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-v1.json` (sha256 `77b04fc6366555dbd1fc8a340c95c3c5a0f1d4a96a45b8bbce2956a8454ca986`)
- delay atoms: 7; contexts: 399; pair-context checks: 4788
- separations seen in the declared space: 916; reduced distinct witnesses: 50
- search answer-independence: order permutation set-equal = `True`; grammar mutation removes deadline kind = `False`
- known calibration benchmark present in the discovered set: `PRESENT` (['C-73', 'C-74'])

## Candidates (reduced, in discovery order)

| witness | pair | context | separated observation | kind |
|---|---|---|---|---|
| WV-0001 | (ret 0 false, ret 1 false) | deadline(0, □) | some false ≠ none | deadline_observation |
| WV-0002 | (ret 0 false, ret 1 false) | race(□, ret 0 true) | ret 0 false ≠ ret 0 true | value_mismatch |
| WV-0003 | (ret 0 true, ret 1 true) | deadline(0, □) | some true ≠ none | deadline_observation |
| WV-0004 | (ret 0 true, ret 1 true) | race(□, ret 0 false) | ret 0 true ≠ ret 0 false | value_mismatch |
| WV-0005 | (ret 1 false, ret 0 false) | deadline(0, □) | none ≠ some false | deadline_observation |
| WV-0006 | (ret 1 false, ret 0 false) | race(□, ret 0 true) | ret 0 true ≠ ret 0 false | value_mismatch |
| WV-0007 | (ret 1 true, ret 0 true) | deadline(0, □) | none ≠ some true | deadline_observation |
| WV-0008 | (ret 1 true, ret 0 true) | race(□, ret 0 false) | ret 0 false ≠ ret 0 true | value_mismatch |
| WV-0009 | (ret 0 false, ret 1 false) | race(ret 1 true, □) | ret 0 false ≠ ret 1 true | value_mismatch |
| WV-0010 | (ret 0 true, ret 1 true) | race(ret 1 false, □) | ret 0 true ≠ ret 1 false | value_mismatch |
| WV-0011 | (ret 1 false, ret 0 false) | race(ret 1 true, □) | ret 1 true ≠ ret 0 false | value_mismatch |
| WV-0012 | (ret 1 true, ret 0 true) | race(ret 1 false, □) | ret 1 false ≠ ret 0 true | value_mismatch |

## Controls

- positive control (`bind_preserves_result_equivalence`, claim ref C-71): preserved = `True`
- negative control (`declared_deadline_does_not_separate_this_pair`): separated = `False`, expectation met = `True`

## Native kernel verification

### `20260913-VERIFY-L1-COMPLETION-001` (witness WV-0013)

- proof origin: `coordinator_template`; status: `NATIVE_CHECK_FAILED`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 0 true; false↦ω})
- target sha256: `103b4c9abfdd3b6dd977e98920d9b92741a0e3e9acf03e732a87914b91fe90ce`
- kernel `verify`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`
- kernel `controls`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`, replay match `True`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

### `20260913-VERIFY-L1-COMPLETION-002` (witness WV-0013)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_CALIBRATION_INSTANCE`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 0 true; false↦ω})
- target sha256: `103b4c9abfdd3b6dd977e98920d9b92741a0e3e9acf03e732a87914b91fe90ce`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, replay match `True`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

### `20260913-VERIFY-L1-DEADLINE-001` (witness WV-0001)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_CALIBRATION_INSTANCE`
- statement: (ret 0 false, ret 1 false) under deadline(0, □)
- target sha256: `87bb4895dede05f11e464d38b7cce85c43aa4c71419310959b293d151bcec548`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, replay match `True`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

### `20260913-VERIFY-L1-VALUE-001` (witness WV-0002)

- proof origin: `coordinator_template`; status: `NATIVE_CHECK_FAILED`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true)
- target sha256: `e1ee1b9316fa720b2cd957ce56a5ed3e98ff0a1cd6167206b10fad3d962d5b49`
- kernel `verify`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`
- kernel `controls`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 42, status `KERNEL_REJECTED_UNEXPECTED`, expectation met `False`, replay match `True`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

### `20260913-VERIFY-L1-VALUE-002` (witness WV-0002)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_CALIBRATION_INSTANCE`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true)
- target sha256: `e1ee1b9316fa720b2cd957ce56a5ed3e98ff0a1cd6167206b10fad3d962d5b49`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, replay match `True`
- related existing claims: ['C-73', 'C-74', 'C-75', 'C-76']
- registers new claim: `False`

## Correspondence review `RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0001` (witness WV-0001)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0001.json`
- mechanism: the result-equivalence class forgets the round index; the deadline consumer reads it
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `PRESERVED_AT_MODEL_LEVEL`; reality correspondence `UNRESOLVED`

- original activity and completion criterion are declared before search: `DECLARED`
- the theoryization step is an operation of the pinned model: `SUPPORTED`
- the separating observation is declared in the task, not an oracle added later: `DECLARED`
- compensation class of the consumer: `RECOVERY_FROM_ORIGINAL_REPRESENTATION`
- quantifier scope of the claim: `FINITE_DECLARED_GRAMMAR_ONLY`
- reality bridge: `NOT_CLOSED_IN_M1`

## Correspondence review `RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0002` (witness WV-0002)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0002.json`
- mechanism: race reads completion order; the composed business continuation turns the losing branch into divergence
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `PRESERVED_AT_MODEL_LEVEL`; reality correspondence `UNRESOLVED`

- original activity and completion criterion are declared before search: `DECLARED`
- the theoryization step is an operation of the pinned model: `SUPPORTED`
- the separating observation is declared in the task, not an oracle added later: `DECLARED`
- compensation class of the consumer: `PRE_KEPT_BY_TASK_DECLARATION`
- quantifier scope of the claim: `FINITE_DECLARED_GRAMMAR_ONLY`
- reality bridge: `NOT_CLOSED_IN_M1`

## Correspondence review `RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0013` (witness WV-0013)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0013.json`
- mechanism: race reads completion order; the composed business continuation turns the losing branch into divergence
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `PRESERVED_AT_MODEL_LEVEL`; reality correspondence `UNRESOLVED`

- original activity and completion criterion are declared before search: `DECLARED`
- the theoryization step is an operation of the pinned model: `SUPPORTED`
- the separating observation is declared in the task, not an oracle added later: `DECLARED`
- compensation class of the consumer: `PRE_KEPT_BY_TASK_DECLARATION`
- quantifier scope of the claim: `FINITE_DECLARED_GRAMMAR_ONLY`
- reality bridge: `NOT_CLOSED_IN_M1`

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package (['C-73', 'C-74', 'C-75', 'C-76']); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Exploration receipts live under `machine-overview/runs/`; the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
