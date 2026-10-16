# Machine-overview calibration report: MS-TASK-GEN001-DIVISIBILITY-001

- generated_at_utc: 2026-09-16T23:05:07.871139+00:00
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-GEN001-DIVISIBILITY-001/case-revision-1.json` (revision 1, sha256 `db39f1346e53961ce0251a881ff666799bc217329c112aef59d466428bf0e8a1`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/SEARCH-GEN001-DIVISIBILITY-001/RUN.json` (run `SEARCH-GEN001-DIVISIBILITY-001`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.5.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-DIVISIBILITY-v1` (PROFILE_QUALIFIED)

## What was searched

- declared grammar: `machine-overview/grammars/l1-divisibility-v1.json` (sha256 `9ffe28ef5a713dc060cd8df17fc863ac99e61f17d28e92fb9e55a6141f704f1d`)
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

### `VERIFY-GEN001-DIVISIBILITY-001` (witness WV-0001)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-DIVISIBILITY-001` (sha256 `e0ebce5391574f3128ec15b77055537022ddd169ee7fb784dfcc33956fc0e3d2`)
- candidate AST sha256: `9a92083e109d41ff259ce8cef960422f14a37d1733cdff674c232395ef72c8b0`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under deadline(0, □)
- target sha256: `ca09c74b988726da8e35e70fba316eb67e51718e9abb1d533781981a3c91bc8a`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-DIVISIBILITY-WV-0025` (witness WV-0025)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-DIVISIBILITY-001` (sha256 `e0ebce5391574f3128ec15b77055537022ddd169ee7fb784dfcc33956fc0e3d2`)
- candidate AST sha256: `b11463f9386e985ac94074f44f90537220a180b32b0d1bf82e7c0866042290f0`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 2 true; false↦ω})
- target sha256: `4990b5f42fe52e719baf9f46e143b336108115073af0be61caba76784c24ade2`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-DIVISIBILITY-WV-0026` (witness WV-0026)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-DIVISIBILITY-001` (sha256 `e0ebce5391574f3128ec15b77055537022ddd169ee7fb784dfcc33956fc0e3d2`)
- candidate AST sha256: `cc77de6db31c779cfd2deff3fd5bf011980f7d8105ad92b3e4d1801483053015`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ret 1 true; false↦ret 1 false})
- target sha256: `fb626d21d386df91be351435fc6c6d7870667cf465493f39a32c1ca497b3f029`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-DIVISIBILITY-WV-0027` (witness WV-0027)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-DIVISIBILITY-001` (sha256 `e0ebce5391574f3128ec15b77055537022ddd169ee7fb784dfcc33956fc0e3d2`)
- candidate AST sha256: `cdc3c36545720a5a85c9b271d67a99c2a711ff814d917c1a17223733d45f98e2`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 2 false})
- target sha256: `943fddf23282e046e9b73e09bb2b19305e04a983149570add60444307d27ec2a`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

### `VERIFY-GEN001-DIVISIBILITY-WV-0051` (witness WV-0051)

- proof origin: `coordinator_template`; status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; attempt: `1`
- source search run: `SEARCH-GEN001-DIVISIBILITY-001` (sha256 `e0ebce5391574f3128ec15b77055537022ddd169ee7fb784dfcc33956fc0e3d2`)
- candidate AST sha256: `4215579f8c15e0c17c571711fa5661ee4c2665f10a451e7123171eed50317a46`; target freeze: `FROZEN`
- statement: (ret 0 false, ret 1 false) under bind(□, λ{true↦ret 1 true; false↦ret 1 false}) → deadline(2, □)
- target sha256: `40c306bf48c86ca918ec1a7fe621b8f931b6878c5fad6a5b999c8208640239a1`
- replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel `verify`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `controls`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- kernel `negative-control`: exit 42, status `KERNEL_REJECTED_AS_EXPECTED`, expectation met `True`, diagnostic `EXPECTED_TYPE_REJECTION`
- kernel `verify-replay`: exit 0, status `KERNEL_ACCEPTED`, expectation met `True`, diagnostic `UNEXPECTED`
- related existing claims: []
- registers new claim: `False`

## Correspondence review `RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0025-b11463f9` (witness WV-0025)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0025-b11463f9.json`
- mechanism: The declared race context makes one side diverge while the other returns; ≈ cannot see completion order, so it identifies the two result-equivalent inputs.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0026-cc77de6d` (witness WV-0026)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0026-cc77de6d.json`
- mechanism: The declared context selects a different delivered Bool value on the two sides. Result equivalence ≈ identifies the input computations (same value and same convergence behaviour), so it cannot see which branch the context delivers.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0027-cdc3c365` (witness WV-0027)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0027-cdc3c365.json`
- mechanism: The declared race context makes one side diverge while the other returns; ≈ cannot see completion order, so it identifies the two result-equivalent inputs.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Correspondence review `RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0051-4215579f` (witness WV-0051)

- review: `/Volumes/D/HoTT-machine-overview/machine-overview/reviews/RV-MS-TASK-GEN001-DIVISIBILITY-001-r1-SEARCH-GEN001-DIVISIBILITY-001-WV-0051-4215579f.json`
- mechanism: The declared deadline consumer reads the round index n that the pinned constructor `ret n a` already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see the difference the deadline consumer reads.
- conclusion: `MODEL_ONLY_OPERATIONALLY_SPECIFIED`; task preservation `REVIEW_REQUIRED`; reality correspondence `UNRESOLVED`
- review checks: profile_qualified=PASS, grammar_membership=PASS, case_search_binding=PASS, witness_search_binding=PASS, declared_observation_kind=FAIL, declared_consumer_present=FAIL, compensation_classified=PASS

## Evidence boundaries

- This is a calibration instance of a mechanism already machine-proved in the pinned package ([]); it is not registered as a new mathematical claim.
- The verified statement is a ground instance inside the declared grammar; nothing here quantifies over all HoTT models, implementations, or physical time.
- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); exploration receipts live under `machine-overview/runs/` and the formal-evidence contract (`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.
