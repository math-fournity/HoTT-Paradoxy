/-!
`MP-BARE-ZFC-Q-PRECISION-001` is an interface-relative formal control for
F-049, the question whether a bare-ZFC-facing foundation interface has enough
observation to distinguish a model's completion from an original process
completion.

The two worlds below are a *finite source-contract model*, not the syntax or a
model of ZFC.  They deliberately share the same `StandardResolutionView` and
the same `FormalDone`, while preserving two different completion contracts:

* `strictOriginal`: the original, stricter process contract is not done;
* `revisedTask`: a revised contract is done.

The kernel proves that no decoder seeing only this fixed standard-resolution
view can determine `OriginDone`.  It also proves two positive controls:

* an enriched completion-contract view can determine `OriginDone`;
* a finite code carrying the missing contract bit can determine it.

Consequently this source proves neither that bare ZFC cannot encode processes
nor that ZFC is inconsistent.  The source binding to a ZFC-supported Standard
Solution is external and is stated in the package claim/source card.
-/

namespace BareZFCPrecision

/-- The two completion-contract worlds in the frozen Norton/IEP source model.
    They differ only at the process-contract layer that the coarse resolution
    view intentionally does not retain. -/
inductive CompletionWorld where
  | strictOriginal
  | revisedTask
deriving DecidableEq, Repr

/-- What the coarse standard-solution application reports for either world. -/
inductive StandardResolutionView where
  | resolved
deriving DecidableEq, Repr

/-- The fixed application interface forgets which completion contract was
    retained before its `resolved` verdict was issued. -/
def standardResolutionView : CompletionWorld → StandardResolutionView
  | _ => .resolved

/-- Both worlds have the coarse/model-side completion used by the application
    interface. -/
def FormalDone : CompletionWorld → Prop
  | _ => True

/-- The original process completion is deliberately not identified with the
    coarse model-side verdict: it fails in the strict-contract world and holds
    after the contract is revised. -/
def OriginDone : CompletionWorld → Prop
  | .strictOriginal => False
  | .revisedTask => True

/-- The Q-side requirement for one world: a formal completion may only be
    promoted when it reaches the retained origin-completion predicate. -/
def QNeed (world : CompletionWorld) : Prop :=
  FormalDone world → OriginDone world

/-- An observation interface has enough precision for a predicate when a
    decoder using only its visible output gives the predicate in every world. -/
def Determines
    {World View : Type}
    (project : World → View)
    (observe : World → Prop) : Prop :=
  ∃ decode : View → Prop, ∀ world, observe world ↔ decode (project world)

/-- A fixed interface pays the completion bridge only when `FormalDone` can be
    promoted for every world it claims to resolve. -/
def CompletionBridgePaid : Prop :=
  ∀ world : CompletionWorld, FormalDone world → OriginDone world

theorem strict_formal_done : FormalDone .strictOriginal := by
  trivial

theorem revised_formal_done : FormalDone .revisedTask := by
  trivial

theorem strict_origin_not_done : ¬ OriginDone .strictOriginal := by
  intro h
  exact h

theorem revised_origin_done : OriginDone .revisedTask := by
  trivial

theorem standard_view_collapses_contracts :
    standardResolutionView .strictOriginal =
      standardResolutionView .revisedTask := by
  rfl

/-- M2: the fixed coarse standard-resolution view cannot determine the original
    process completion, because it gives the same output to two worlds with
    opposite `OriginDone`. -/
theorem standard_view_does_not_determine_origin_done :
    ¬ Determines standardResolutionView OriginDone := by
  intro h
  rcases h with ⟨decode, hdecode⟩
  have strictDecode : OriginDone .strictOriginal ↔ decode .resolved := by
    exact hdecode .strictOriginal
  have revisedDecode : OriginDone .revisedTask ↔ decode .resolved := by
    exact hdecode .revisedTask
  have resolved : decode .resolved := revisedDecode.mp revised_origin_done
  exact strict_origin_not_done (strictDecode.mpr resolved)

/-- The same fixed interface cannot pay a universal `FormalDone → OriginDone`
    bridge. -/
theorem standard_view_does_not_pay_completion_bridge :
    ¬ CompletionBridgePaid := by
  intro bridge
  exact strict_origin_not_done (bridge .strictOriginal strict_formal_done)

/-- M3 positive control: once the interface carries the completion contract
    itself, `OriginDone` is exactly recoverable. -/
def richCompletionView : CompletionWorld → CompletionWorld := id

theorem rich_completion_view_determines_origin_done :
    Determines richCompletionView OriginDone := by
  refine ⟨OriginDone, ?_⟩
  intro world
  rfl

/-- A finite code is another explicit positive control.  It is a small data
    representation, not a claim that bare ZFC lacks set encodings. -/
def processContractCode : CompletionWorld → Nat
  | .strictOriginal => 0
  | .revisedTask => 1

def decodeOriginFromCode : Nat → Prop
  | 0 => False
  | 1 => True
  | _ => False

theorem coded_completion_view_determines_origin_done :
    Determines processContractCode OriginDone := by
  refine ⟨decodeOriginFromCode, ?_⟩
  intro world
  cases world with
  | strictOriginal =>
      show False ↔ False
      exact Iff.rfl
  | revisedTask =>
      show True ↔ True
      exact Iff.rfl

/-- The full finite Q profile for this concrete control: a coarse completion
    view has an unpaid observation/bridge obligation, while an enriched view
    removes precisely that information loss. -/
theorem coarse_view_has_q_precision_gap_with_rich_controls :
    (¬ Determines standardResolutionView OriginDone) ∧
      (¬ CompletionBridgePaid) ∧
      Determines richCompletionView OriginDone ∧
      Determines processContractCode OriginDone := by
  exact ⟨standard_view_does_not_determine_origin_done,
    standard_view_does_not_pay_completion_bridge,
    rich_completion_view_determines_origin_done,
    coded_completion_view_determines_origin_done⟩

#print axioms strict_formal_done
#print axioms revised_formal_done
#print axioms strict_origin_not_done
#print axioms revised_origin_done
#print axioms standard_view_collapses_contracts
#print axioms standard_view_does_not_determine_origin_done
#print axioms standard_view_does_not_pay_completion_bridge
#print axioms rich_completion_view_determines_origin_done
#print axioms coded_completion_view_determines_origin_done
#print axioms coarse_view_has_q_precision_gap_with_rich_controls

end BareZFCPrecision
