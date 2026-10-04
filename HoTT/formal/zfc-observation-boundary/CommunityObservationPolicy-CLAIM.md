# MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001

## Exact formal scope

Source: [CommunityObservationPolicy.lean](CommunityObservationPolicy.lean).

This is a bare-Lean **meta-policy calculus**. `baseZFC` is an arbitrary
predicate over four symbolic claims, not the language, axioms, models,
consistency, or proof relation of actual ZFC. The calculus formalizes the
logical skeleton of the research initiator's new proposal only after its
substantive bridges are made explicit.

| Symbol | Formal role | What still needs external/source work |
|---|---|---|
| `Q` | `hasObservationQ` in `CommunityAdoption` | A source-defined observational capacity about time/process completion. |
| `P` | `mathematicalIllusionP` | An exact assumption, acceptance rule, and reality/computability interpretation. |
| `A` | `desiredResolutionA` | The source-level judgment that a specified limit account resolves a specified Zeno/circle task. |
| `B` | `undesirableOutcomeB` | A fixed source-level account of the HoTT-side UR/unreasonable outcome and its relation to P. |
| `ZFC-1` | `zfc1 baseZFC = extend baseZFC P` | Evidence that the mathematical community actually operates with this extension. |

## Machine-checked theorems

1. `zfcPlusA_sameOperationalConsequences_as_zfc1`

   In this calculus, where the A-to-P and P-to-A rules are explicit, `baseZFC + A`
   and `baseZFC + P` have the same derivable consequences. This is the faithful
   formal replacement for the user's informal equality `ZFC-1 = ZFC+A = ZFC+P`.
   It is **not** literal equality of actual ZFC axiom sets.

2. `zfc1_derives_A_and_B`

   If P is admitted, the explicit policy derives both A and B. This formalizes
   the conjunctive fork `P → A ∧ B`.

3. `PBacktrace.exposes_P` and `zfc1_B_has_P_backtrace`

   A B outcome can only be said to be *traced back to P* when a derivation
   provenance object identifies the P-to-B branch. The model supplies such a
   backtrace for its own explicitly constructed `zfc1` branch; it does not say
   every actual HoTT-side B has that provenance.

4. `Q_absence_activates_operational_P`

   A `CommunityAdoption` record separately requires: absence of Q, permission
   from that absence, and adoption of the permitted P. The theorem exposes these
   as assumptions; it does not derive any one of them from bare ZFC.

5. `admitted_P_can_be_marked_illusory`

   An admitted P may coexist with an explicitly declared absence of both a
   computational and a reality bridge. It formalizes the proposed sense of
   “mathematical illusion” as a policy/interpretation claim.

6. `zfc1_produces_normative_tension`

   If a community values A and rejects B, P's policy consequences produce the
   desired-A / unwanted-B tension.

7. `object_level_false_requires_formal_incompatibility`

   `False` follows only after an additional formal incompatibility premise says
   A and B cannot coexist. “The community does not want B” alone is normative,
   not a proof that actual ZFC is inconsistent.

8. `Q_absence_activates_A_and_B` and
   `Q_absence_produces_normative_tension`

   The Q-absence/permission/adoption record makes the full proposed fork
   explicit: if those policy premises hold, the operational extension derives
   both A and B; with separately supplied values it produces a normative
   tension. Neither theorem identifies an actual community or actual ZFC.

9. `Q_absence_violates_truth_constraint` and
   `Q_absence_incompatible_A_and_B_yields_false`

   `False` follows only after adding either a formal truth constraint excluding
   B or an explicit incompatibility of the A/B consequences. This is the exact
   formal meaning available for the user's “mathematical truth” language; it
   is not supplied by the mere preference that B be unwanted.

10. `emptyTheory_derives_no_claim` and `zfc1_is_strict_over_empty`

    A negative control shows that the A/P cycle creates no claim from an empty
    base. In the calculus, P is obtained in `zfc1` because it is explicitly
    added. This prevents the model from treating P as already derived from
    bare ZFC.

11. `normative_tension_fixture_is_inhabited` and
    `normative_tension_fixture_not_formally_incompatible`

    A concrete abstract fixture satisfies the Q-missing/permission/adoption
    fields and gives a community that values A and rejects B. The tension is
    inhabited, so its presence cannot itself be substituted for the separate
    A/B incompatibility or truth constraint required for `False`.

12. `undesirable_derivation_has_base_or_policy`,
    `nonbase_undesirable_derivation_backtracks_to_policy`, and
    `zfc1_nonbase_B_backtracks_to_admitted_P`

    These theorems formalize the user's requested reductio-style return path.
    In this fixed calculus, a derivation of B either already comes from the
    base theory or uses the explicit `P → B` rule. If the base does not already
    contain B, the derivation yields P; in `zfc1`, it reaches the admitted P.
    This is a theorem about derivation provenance in the displayed policy
    calculus, not a claim that an actual HoTT result has an actual ZFC/P cause.

13. `base_B_is_an_alternative_derivation_origin`

    This is the required control for the preceding backtrace: a base theory
    can itself contain B, in which case observing B alone cannot identify P as
    its cause. The non-base premise is therefore not cosmetic.

### Development control

The first draft attempted a generic `induction` over a derivation whose result
index was already fixed to B. Lean rejected that elimination form because the
target index was not a variable; it never became a delivery receipt. The source
uses dependent `cases` instead, so only `base` and `pToB` are admissible B
origins. Run `-05` captured the repaired code before this claim text was
finalized; it is retained with its source manifest as a historical snapshot.
Fresh run `20261004-MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001-08` is the
authoritative check of the final repaired source-and-claim pair.

## Non-goals

- No theorem that ZFC is inconsistent, incomplete, or incapable of representing
  time, recursion, reals, limits, or HoTT syntax.
- No theorem that the mathematical community actually adopts P.
- No theorem that a limit account fails any specified motion task.
- No theorem that the HoTT `QuestioningDelay` result is B, or that the same task
  is present in the Zeno and HoTT sites.
- No claim that a missing bridge automatically makes a source owe a bridge.
- No assertion that an actual B has a P backtrace without a source-defined
  derivation/provenance and a proof that B was not already an independent base
  commitment.

The missing work is a source-and-task mapping: define actual Q/P/A/B, prove
the exact `A ↔ P` policy rule or a suitable replacement, establish an actual
P-to-B path, and separately decide whether B is merely an unwanted outcome or
is formally incompatible with A.
