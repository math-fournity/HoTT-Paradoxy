# Machine-overview calibration report: MS-TASK-GEN001-COMPLETION-PROCESS-001

- generated_at_utc: 2026-09-16T21:00:06.428085+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-GEN001-COMPLETION-PROCESS-001/case-revision-1.json` (revision 1, sha256 `c9cb476dc259cf6cea9097fa3e78a6bdab3357475e2811d7a40f9d144d42e3f1`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260916-SEARCH-GEN001-COMPLETION-PROCESS-001/RUN.json` (run `20260916-SEARCH-GEN001-COMPLETION-PROCESS-001`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.5.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-COMPLETION-PROCESS-v1` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-completion-process-v1.json` (sha256 `97e13dca450193494ab49b0e2dba3fc3ba9a7a7dc60acf879d75d8e1ac66819a`)
- delay atoms: 7; contexts planned: 460; contexts examined: 460
- pair-context checks: 5520 executed of 5520 planned
- separations seen: 1000; reduced distinct witnesses: 72
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

### `20260916-VERIFY-GEN001-COMPLETION-PROCESS-014` (witness WV-0014)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-COMPLETION-PROCESS-001` (sha256 `49d0e71753c4397678dc73219fb4cc6ddb27dd8cd700997b9221d019395077dc`)
- candidate AST sha256: `9098e2f65516b9bde5481d3bc57c133a5d108d4c11ad33f8915b3d26d17b2b00`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 0 false})
- target sha256: `6ad5bb172ece0b093edd036fd25e830d1097c52181712722105cc9fc735ac761`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-COMPLETION-PROCESS-021` (witness WV-0021)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-COMPLETION-PROCESS-001` (sha256 `49d0e71753c4397678dc73219fb4cc6ddb27dd8cd700997b9221d019395077dc`)
- candidate AST sha256: `431101ed8ab7a665cb112e3e5282e716c7a492c5c88033a18077207a77581c55`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under bind(□, λ{true↦ω; false↦ret 0 false}) → deadline(1, □)
- target sha256: `036eef3b4e16872d3ad3080f2a3e8e6e8198185c134b86e536b9b08b5676898b`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-COMPLETION-PROCESS-053` (witness WV-0053)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-COMPLETION-PROCESS-001` (sha256 `49d0e71753c4397678dc73219fb4cc6ddb27dd8cd700997b9221d019395077dc`)
- candidate AST sha256: `a29868676a71efdd47b1a67f9bea2433eff6ebf446afdeefbab7ad9f593f2a22`; target freeze: `FROZEN`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 0 true; false↦ret 2 false}) → deadline(1, □)
- target sha256: `697c3a673cf535fef7330c52ac137aa447add5200a32a56fbf38fe52b9eb4937`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-COMPLETION-PROCESS-070` (witness WV-0070)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-COMPLETION-PROCESS-001` (sha256 `49d0e71753c4397678dc73219fb4cc6ddb27dd8cd700997b9221d019395077dc`)
- candidate AST sha256: `b327b7d52acd6f5a02640ff27881dffc41173a418e4be8d77cdc7f093a7c7bec`; target freeze: `FROZEN`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 2 true; false↦ret 0 false}) → deadline(3, □)
- target sha256: `34e2eacd4657dc209a36ce149629a93dea05246d8f442032c1410155cc260817`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

## Correspondence review `RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0014-9098e2f6` (witness WV-0014)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0014-9098e2f6.json`
- mechanism: The declared race context makes one side diverge while the other returns; ≈ cannot see completion order, so it identifies the two result-equivalent inputs.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0021-431101ed` (witness WV-0021)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0021-431101ed.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0053-a2986867` (witness WV-0053)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0053-a2986867.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0070-b327b7d5` (witness WV-0070)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-COMPLETION-PROCESS-001-r1-20260916-SEARCH-GEN001-COMPLETION-PROCESS-001-WV-0070-b327b7d5.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package ([]); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); exploration receipts live under `machine-overview/runs/` and the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
