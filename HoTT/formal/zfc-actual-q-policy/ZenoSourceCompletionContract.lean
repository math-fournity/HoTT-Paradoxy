/-!
`C-362` formalizes the completion-contract distinction extracted from the
fixed Norton/IEP source denominator.

It intentionally proves only the logical consequence of a source-certified
classification: a revised completion contract that does every indexed action
but requires no last action does not establish the stricter last-action
contract.  Lean cannot prove what a webpage says; the source classification is
recorded separately in `audit/20261004-ZFC-ACTUAL-Q-A2-标准解法来源完成合同.md`.
-/

namespace ZFCActualQSourceContract

inductive ResolutionJudgment where
  | originalResolved
  | revisedResolved
  | bridgeRequired
  | noPolicyClaim
deriving DecidableEq, Repr

/-- A completion contract separates the original task's Done predicate from
    the revised/model Done predicate and records whether an explicit bridge is
    available. -/
structure CompletionContract where
  originalDone : Prop
  revisedDone : Prop
  bridgePaid : Prop
  judgment : ResolutionJudgment

/-- The strict finite-task reading: completion includes a last indexed action.
    For an action family indexed by every natural number, this requires a
    natural number above every natural number. -/
def StrictLastActionCompletion : Prop :=
  ∃ last : Nat, ∀ action : Nat, action ≤ last

/-- The revised reading: every indexed action has been done; it does not add a
    requirement for a non-existent last member. -/
def RevisedAllActionsCompletion : Prop :=
  ∀ _action : Nat, True

theorem revised_all_actions_complete : RevisedAllActionsCompletion := by
  intro _action
  trivial

theorem strict_last_action_completion_impossible :
    ¬ StrictLastActionCompletion := by
  intro h
  rcases h with ⟨last, hlast⟩
  exact Nat.not_succ_le_self last (hlast (Nat.succ last))

/-- The source-facing contract used here is a finite, explicit model of the
    Norton classification: the source's resolution uses the revised contract,
    does not claim the strict bridge, and leaves the two predicates separate. -/
def nortonModeledContract : CompletionContract where
  originalDone := StrictLastActionCompletion
  revisedDone := RevisedAllActionsCompletion
  bridgePaid := False
  judgment := .revisedResolved

def TaskContractDivergence (contract : CompletionContract) : Prop :=
  contract.revisedDone ∧
  ¬ contract.originalDone ∧
  ¬ contract.bridgePaid ∧
  contract.judgment = .revisedResolved

def OriginalBridge (contract : CompletionContract) : Prop :=
  contract.revisedDone → contract.originalDone

theorem norton_modeled_contract_diverges :
    TaskContractDivergence nortonModeledContract := by
  refine ⟨revised_all_actions_complete, strict_last_action_completion_impossible, ?_, rfl⟩
  intro h
  exact h

theorem norton_modeled_contract_has_no_original_bridge :
    ¬ OriginalBridge nortonModeledContract := by
  intro bridge
  exact strict_last_action_completion_impossible (bridge revised_all_actions_complete)

theorem revised_judgment_is_not_original :
    nortonModeledContract.judgment ≠ .originalResolved := by
  decide

/-- A source that certifies only the revised contract cannot discharge the
    stronger `originalDone` conclusion required by C-359's promotion P. -/
theorem revised_contract_does_not_discharge_original_done :
    ¬ (nortonModeledContract.revisedDone → nortonModeledContract.originalDone) :=
  norton_modeled_contract_has_no_original_bridge

#print axioms revised_all_actions_complete
#print axioms strict_last_action_completion_impossible
#print axioms norton_modeled_contract_diverges
#print axioms norton_modeled_contract_has_no_original_bridge
#print axioms revised_judgment_is_not_original
#print axioms revised_contract_does_not_discharge_original_done

end ZFCActualQSourceContract
