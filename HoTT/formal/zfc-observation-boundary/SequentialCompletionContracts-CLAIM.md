# MP-ZENO-SEQUENTIAL-COMPLETION-CONTRACTS-001

Source: [SequentialCompletionContracts.lean](SequentialCompletionContracts.lean).

## Exact formal claim

The source defines a trace with natural-number-indexed events. In the canonical
trace, each step `n` occurs at event `n`.

Lean proves, without axioms:

1. `canonical_trace_has_every_step_done`: each finite step has an occurrence;
2. `canonical_trace_has_no_final_action_done`: no natural-number index bounds
   all occurring steps, so the trace has no final action;
3. `every_step_done_not_equiv_final_action_done`: these two contracts are not
   equivalent on the canonical trace;
4. `every_step_done_does_not_imply_final_action_done`: the every-step contract
   alone does not imply the final-action contract.

## Research role

SEP's *Supertasks* entry explicitly distinguishes these two meanings of
“complete” for the Dichotomy. This formal model checks the smallest logical
shape of that distinction. It is a control for H103/H104/H105: a source must
not be treated as having paid a bridge to a stronger completion contract merely
because it has established that every indexed step occurs.

## Non-goals

- No real-analysis convergence theorem or real-time schedule.
- No physical-motion claim.
- No claim that UOU, SEP, any course text, or ZFC adopts either contract.
- No proof that a source's named Done is identical to this model's contracts.
- No ZFC inconsistency, Q absence, or P-to-HoTT-B provenance.
