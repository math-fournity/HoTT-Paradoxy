# MP-ZFC-META-OBSERVATION-CONSISTENCY-001

## Exact formal claims

Source: [MetaObservationConsistency.lean](MetaObservationConsistency.lean).

1. `unbridged_original_resolution_breaks_O3O5`:

   If a case requires a bridge, is judged to resolve the **original** task, and
   lacks bridge payment, then the formal O3–O5 adequacy policy is false.

2. `same_Q_opposite_judgments_break_uniformity`:

   If the *full* `QProfile` is identical for `zeno` and `hott`, but one is
   judged `originalResolved` and the other `bridgeRequired`, the assessment is
   not Q-uniform.

   `QProfile` explicitly includes O1 representation, O2 formal completion,
   O3 completion distinction, O4 same-task bridge verification, O5 meta-audit,
   plus bridge payment and original-task preservation.

3. `revised_resolution_is_not_original_resolution`:

   An explicitly revised completion judgment is distinct from a judgment that
   the original task has been resolved.

4. `coarse_shared_Q_can_have_different_judgments`:

   Sharing only `requiresBridge = true` does not force equal judgments: a
   genuine difference in payment or task preservation can justify a different
   outcome. This is a required anti-false-positive control.

5. `sameQ_fixture_breaks_O3O5` and `sameQ_fixture_breaks_uniformity`:

   The fixed conditional fixture with the same full unbridged Q profile and
   opposite Zeno/HoTT judgments violates both the O3–O5 adequacy policy and
   Q-uniformity.

6. `sameQ_fixture_has_O1O2_without_O3O5`:

   The same conditional fixture explicitly has O1/O2 resources while O3/O4/O5
   are false. This formalizes the candidate terminal wording's shape without
   asserting that actual ZFC has that exact profile.

## Research interpretation

This file formalizes the user's proposed comparison as a **conditional policy
theorem**. It proves neither that ZFC makes the listed judgments nor that the
Zeno and HoTT cases actually have identical full Q profiles. Those are
source-and-task mapping obligations. The theorem proves what follows once they
are independently established:

```text
same full Q profile + opposite original-resolution/bridge-required judgments
    => not a uniform O3–O5 assessment policy.
```

This is not an object-language contradiction of ZFC. It is a formal
inconsistency of a proposed metatheoretic observation/judgment policy under
the stated hypotheses.

## Proof scope

- Assistant: Lean 4.34.1 core kernel.
- Dependencies: Lean prelude only; all printed theorems have no axioms,
  imports, `sorry`, or classical choice.
- Claim identity: `CONTRIBUTOR_CANDIDATE_NOT_CURRENT` until canonical review
  maps actual Zeno and HoTT evidence into the full `QProfile` fields.
