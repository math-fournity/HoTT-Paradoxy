# Machine-overview calibration report: CASE-GEN001-EXISTENCE-001

- generated_at_utc: 2026-09-16T23:46:34.876644+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/CASE-GEN001-EXISTENCE-001/case-revision-1.json` (revision 1, sha256 `1b1268980dea02480182fc15265d32d72cd7817c55f597c65ba387a886b51d36`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/SEARCH-GEN001-EXISTENCE-001/RUN.json` (run `SEARCH-GEN001-EXISTENCE-001`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.5.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-EXISTENCE-v1` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-existence-v1.json` (sha256 `c2cc645ea7b23937f1d5c5f26d0388628c4c44dfbf0cf95b82c342cdf2572a0e`)
- delay atoms: 7; contexts planned: 440; contexts examined: 440
- pair-context checks: 5280 executed of 5280 planned
- separations seen: 916; reduced distinct witnesses: 58
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

### `VERIFY-GEN001-EXISTENCE-WV-0017` (witness WV-0017)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-EXISTENCE-001` (sha256 `f0385061819584fca86c615f21ebc6385ca942564429c2f832290ed38421fd1d`)
- candidate AST sha256: `4fd50538000942399655de85f9d06bdfc3a843c92fd56339d7ce426a23eee4b1`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 1 false; false↦ω})
- target sha256: `cd6910737e41d1d118f5bdcf1b2ab4d0fb7569900123170e187ed1199ef41d53`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-EXISTENCE-WV-0018` (witness WV-0018)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-EXISTENCE-001` (sha256 `f0385061819584fca86c615f21ebc6385ca942564429c2f832290ed38421fd1d`)
- candidate AST sha256: `5c5fa7779adfbf6f1f53fbb15e1652e8c2c764d21fbf9054dbe37492e44a2304`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 1 false})
- target sha256: `9ae7679d70a7ab38ebd21d2f3baa942cd07dde7b9d34299b7c69cbffcddc4f8a`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-EXISTENCE-WV-0043` (witness WV-0043)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-EXISTENCE-001` (sha256 `f0385061819584fca86c615f21ebc6385ca942564429c2f832290ed38421fd1d`)
- candidate AST sha256: `268de616f37ff40c9184f05780d4ee6ae3f6d762f1ff1e29b246ac4b8e46bcc6`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under bind(□, λ{true↦ω; false↦ret 1 false}) → deadline(2, □)
- target sha256: `b0422ca954f3eff398cc08e7433b645dd78fb7c3b8628b02d34ba1ab6d92c95c`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-EXISTENCE-WV-0051` (witness WV-0051)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-EXISTENCE-001` (sha256 `f0385061819584fca86c615f21ebc6385ca942564429c2f832290ed38421fd1d`)
- candidate AST sha256: `4dae7ad01a2317adce1366c435d614b54895fb27c2879c349266cf0f7893250b`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 2 true; false↦ret 2 false})
- target sha256: `c907901583538f86f0cb62634ca177fe34ac78a4d871578658e0f2cd2921e8e7`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

## Correspondence review `RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0017-4fd50538` (witness WV-0017)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0017-4fd50538.json`
- mechanism: The declared race context makes one side diverge while the other returns; ≈ cannot see completion order, so it identifies the two result-equivalent inputs.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0018-5c5fa777` (witness WV-0018)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0018-5c5fa777.json`
- mechanism: The declared race context makes one side diverge while the other returns; ≈ cannot see completion order, so it identifies the two result-equivalent inputs.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0043-268de616` (witness WV-0043)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0043-268de616.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0051-4dae7ad0` (witness WV-0051)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-CASE-GEN001-EXISTENCE-001-r1-SEARCH-GEN001-EXISTENCE-001-WV-0051-4dae7ad0.json`
- mechanism: The declared context selects a different delivered Bool value on the two sides. Result equivalence ≈ identifies the input computations (same value and same convergence behaviour), so it cannot see which branch the context delivers.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package ([]); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); exploration receipts live under `machine-overview/runs/` and the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
