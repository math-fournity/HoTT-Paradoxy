import GodelQ.ZFC.ITSubstOpen5
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
namespace GodelQ.Probe6
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5

example (m : V) (Vw Ww : V) (hpre : ∀ k ≤ m, Vw.[k] = Ww.[k]) (hlast : Ww.[m+1] = ^&0) :
    True := by
  have hrel := VRel_transform (m := m) (i := 0) (Vw := Vw) (Ww := Ww)
    (by trivial : IsUTermVec ℒₛₑₜ (len Vw) Vw) (by trivial : IsUTermVec ℒₛₑₜ (len Ww) Ww)
    rfl rfl (by norm_num) ⟨hpre, hlast⟩
  trivial
end GodelQ.Probe6
