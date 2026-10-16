# Machine-overview calibration report: MS-TASK-GEN001-WITNESS-RECOVERY-001

- generated_at_utc: 2026-09-16T19:53:14.073111+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-GEN001-WITNESS-RECOVERY-001/case-revision-1.json` (revision 1, sha256 `8ac64f3778667091653bc044d5b97a7675369eb12e6206e38ff473a01a975603`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260916-SEARCH-GEN001-WITNESS-RECOVERY-001/RUN.json` (run `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.5.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-WITNESS-RECOVERY-v1` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-witness-recovery-v1.json` (sha256 `84c932a4aa522ca85be5df748ccc7de2bf97b78293e60c22dbaef2f33e34c3b0`)
- delay atoms: 9; contexts planned: 598; contexts examined: 598
- pair-context checks: 14352 executed of 14352 planned
- separations seen: 2736; reduced distinct witnesses: 52
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

### `20260916-VERIFY-GEN001-WITNESS-RECOVERY-040` (witness WV-0040)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001` (sha256 `6c35e9ee71741134ea51fc1effab3a0add1f770cfa77a5d231063fcb262d55a9`)
- candidate AST sha256: `82fa19e6598ebe6eba71e7f8a56b323d440b848383b067cbc2ad3cf3fb8948df`; target freeze: `FROZEN`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 1 true; false↦ω}) → deadline(2, □)
- target sha256: `828edc8103d3b3e39dc28cba13413fecc0967bbed0b6e3641fe3570c5f9da44a`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-WITNESS-RECOVERY-041B` (witness WV-0041)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001` (sha256 `6c35e9ee71741134ea51fc1effab3a0add1f770cfa77a5d231063fcb262d55a9`)
- candidate AST sha256: `36be28716883c36be899a2294bc04d20f418118dd4eeeb6a5fb178e8c50125ca`; target freeze: `REUSED`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 1 true; false↦ω}) → race(□, ret 2 false)
- target sha256: `b1a106015f4cc6d515a0d7a6eb7c04149faf1d8989fc106dcf27d8c582e31d3b`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `20260916-VERIFY-GEN001-WITNESS-RECOVERY-049` (witness WV-0049)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001` (sha256 `6c35e9ee71741134ea51fc1effab3a0add1f770cfa77a5d231063fcb262d55a9`)
- candidate AST sha256: `d9ca673449410daf8171ba20cb174eddc3bd353fd8e13c9160f2ded426936a51`; target freeze: `FROZEN`
- statement: (ret 0 true, ret 1 true) under bind(□, λ{true↦ret 1 true; false↦ω}) → race(ret 3 false, □)
- target sha256: `de35e347694be301ff5e65a208f6c87a3d092f79bf163ac669eceb97a1359678`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

## Correspondence review `RV-MS-TASK-GEN001-WITNESS-RECOVERY-001-r1-20260916-SEARCH-GEN001-WITNESS-RECOVERY-001-WV-0001-9a92083e` (witness WV-0001)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-WITNESS-RECOVERY-001-r1-20260916-SEARCH-GEN001-WITNESS-RECOVERY-001-WV-0001-9a92083e.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package ([]); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); exploration receipts live under `machine-overview/runs/` and the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
