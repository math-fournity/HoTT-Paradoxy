/-!
`MP-ZENO-SEQUENTIAL-COMPLETION-CONTRACTS-001` formalizes the smallest logical
control behind the source distinction between “every indexed step occurs” and
“there is a last action.”  It is a finite Lean model of contracts over natural
number indices; it does not model real time, convergence, physical motion,
ZFC, or an actual Zeno resolution.
-/

namespace ZenoSequentialCompletionContracts

structure Trace where
  occurs : Nat → Nat → Prop

/-- The canonical indexed trace: step `n` occurs at its own event index `n`. -/
def canonicalTrace : Trace where
  occurs step event := event = step

/-- “Every step is carried out” has one event witness for each finite index. -/
def EveryStepDone (trace : Trace) : Prop :=
  ∀ step : Nat, ∃ event : Nat, trace.occurs step event

/-- “There is a final action” means all occurring step indices are bounded by
    one final index. -/
def FinalActionDone (trace : Trace) : Prop :=
  ∃ last : Nat, ∀ step event : Nat, trace.occurs step event → step ≤ last

theorem canonical_trace_has_every_step_done :
    EveryStepDone canonicalTrace := by
  intro step
  exact ⟨step, rfl⟩

theorem canonical_trace_has_no_final_action_done :
    ¬ FinalActionDone canonicalTrace := by
  rintro ⟨last, hlast⟩
  have nextOccurs : canonicalTrace.occurs (Nat.succ last) (Nat.succ last) := rfl
  exact Nat.not_succ_le_self last (hlast (Nat.succ last) (Nat.succ last) nextOccurs)

/-- A model can satisfy the every-step contract while failing the final-action
    contract. Therefore the two contracts are not equivalent merely from their
    shared everyday word “complete.” -/
theorem every_step_done_not_equiv_final_action_done :
    ¬ (EveryStepDone canonicalTrace ↔ FinalActionDone canonicalTrace) := by
  intro equivalent
  exact canonical_trace_has_no_final_action_done
    (equivalent.mp canonical_trace_has_every_step_done)

/-- The precise direction needed for a source-level bridge audit: a proof of
    every indexed occurrence is not, by itself, a proof of a last action. -/
theorem every_step_done_does_not_imply_final_action_done :
    ¬ (EveryStepDone canonicalTrace → FinalActionDone canonicalTrace) := by
  intro implication
  exact canonical_trace_has_no_final_action_done
    (implication canonical_trace_has_every_step_done)

#print axioms canonical_trace_has_every_step_done
#print axioms canonical_trace_has_no_final_action_done
#print axioms every_step_done_not_equiv_final_action_done
#print axioms every_step_done_does_not_imply_final_action_done

end ZenoSequentialCompletionContracts
