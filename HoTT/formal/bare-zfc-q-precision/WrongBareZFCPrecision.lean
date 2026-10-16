/-!
Expected-negative control for MP-BARE-ZFC-Q-PRECISION-001.

This self-contained file preserves the same minimal two-world interface shape
as BareZFCPrecision.lean and deliberately tries to manufacture OriginDone from
the coarse resolved view. Lean must reject the strict-contract branch. It does
not prove anything about bare ZFC; it verifies that the control does not
silently turn an explicit task revision into a bridge.
-/

namespace WrongBareZFCPrecision

inductive CompletionWorld where
  | strictOriginal
  | revisedTask

inductive StandardResolutionView where
  | resolved

def standardResolutionView : CompletionWorld → StandardResolutionView
  | _ => .resolved

def OriginDone : CompletionWorld → Prop
  | .strictOriginal => False
  | .revisedTask => True

def Determines
    {World View : Type}
    (project : World → View)
    (observe : World → Prop) : Prop :=
  ∃ decode : View → Prop, ∀ world, observe world ↔ decode (project world)

theorem wrong_coarse_view_determines_origin_done :
    Determines standardResolutionView OriginDone := by
  refine ⟨fun _ => True, ?_⟩
  intro world
  cases world with
  | strictOriginal =>
      show False ↔ True
      exact Iff.rfl
  | revisedTask =>
      show True ↔ True
      exact Iff.rfl

end WrongBareZFCPrecision
