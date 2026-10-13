import GodelQ.ZFC.ITSubstOpen5
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
namespace GodelQ.Probe3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
example (a : V) : len (a ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) = 3 := by
  rw [len_adjoin, len_adjoin, len_adjoin]; ring
example (a : V) : (a ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) = (a : V) ∷ ?[^#0, ^#1] := rfl
example (a : V) : len (?[a, (^#0 : V), ^#1] : V) = 3 := by
  rw [show (?[a, (^#0 : V), ^#1] : V) = a ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl,
    len_adjoin, len_adjoin, len_adjoin]; ring
end GodelQ.Probe3
