/-!
Expected-negative control for MP-T-PRECISION-TOBS-001.

It deliberately tries to manufacture a decoder for a coarse observation that
maps both finite worlds to the same output while their task predicate has
opposite truth values. Lean must reject the erased branch at False iff True.
-/

namespace WrongObservationPrecision

inductive TinyWorld where
  | retained
  | erased

inductive CoarseView where
  | collapsed

def coarseObservation : TinyWorld → CoarseView
  | _ => .collapsed

def taskDone : TinyWorld → Prop
  | .retained => True
  | .erased => False

def Determines
    {World View : Type}
    (project : World → View)
    (observe : World → Prop) : Prop :=
  ∃ decode : View → Prop, ∀ world, observe world ↔ decode (project world)

theorem wrong_coarse_decoder :
    Determines coarseObservation taskDone := by
  refine ⟨fun _ => True, ?_⟩
  intro world
  cases world with
  | retained =>
      show True ↔ True
      exact Iff.rfl
  | erased =>
      show False ↔ True
      exact Iff.rfl

end WrongObservationPrecision
