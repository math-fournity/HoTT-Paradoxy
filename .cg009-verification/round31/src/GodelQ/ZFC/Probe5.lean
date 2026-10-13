import GodelQ.ZFC.ITSubstOpen5
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
namespace GodelQ.Probe5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5

example : ∀ (m : V) (t : V), IsSemiterm ℒₒᵣ (m + 1) t →
    ∀ Vw Ww : V, IsUTermVec ℒₛₑₜ (m + 1) Vw → True := by
  intro m t
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := m + 1)
    (P := fun t ↦ ∀ Vw Ww : V, IsUTermVec ℒₛₑₜ (m + 1) Vw → True)
  · definability
  · intro z hz Vw Ww hV; trivial
  · intro x Vw Ww hV; trivial
  · intro k f v hkf hv ih Vw Ww hV; trivial
end GodelQ.Probe5
