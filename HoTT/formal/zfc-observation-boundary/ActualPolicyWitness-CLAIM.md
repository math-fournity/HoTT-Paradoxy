# MP-ZFC-ACTUAL-POLICY-WITNESS-001

Source: [ActualPolicyWitness.lean](ActualPolicyWitness.lean).

## What the formal record represents

This source gives the exact **witness interface** required to machine-prove the
research initiator's full Q/P/A/B reductio.  The record requires six distinct
pieces of evidence:

1. a source card with formal F, named process Done D, promotion, and no supplied
   task-preserving bridge;
2. a source-to-policy adoption bridge, plus evidence that the actual policy is
   exactly the designated `ZFC-1` policy extension;
3. a named Q capability, its absence, and a rule that this absence permits P;
4. a P-to-A route;
5. a provenance-bearing P-to-B route;
6. an independent truth-adequacy / A-B incompatibility bridge.

The theorem `actual_witness_yields_false` proves `False` only after every field
is supplied.  It is the correct formal counterpart of the proposed reductio:
the source P card must not be mistaken for the adoption bridge, Q absence, HoTT
backtrace, or incompatibility condition.

## Concrete controls

`uouPromotionCard` is a finite transcription of the UOU source card. Lean
proves it has the P-candidate shape.  `source_card_does_not_force_community_adoption`
then constructs the indispensable negative control: the same source card can
exist while a policy has no direct P adoption.  This prevents a source-level P
from silently becoming “the community actually uses ZFC-1.”

## Non-goals

- No actual ZFC axiom system or model is encoded.
- No claim that any community accepts P, lacks Q, or uses a policy equivalent
  to `ZFC-1`.
- No claim that UOU's Done equals the user's circle Done, SEP's Done, or a
  physical completion condition.
- No actual HoTT PBacktrace and no actual A/B incompatibility.
- No conclusion that mathematics has lost truth, only the explicit place where
  a truth-adequacy premise must enter a formal reductio.
