-- Master PoC: discharge the `hB` hypothesis of `ShCraigElimSetupQ.allKey_of_bridge`
-- by the m = 0 instance of the general opening law (`ITSubstOpen9.iT_subst_open`).
import GodelQ.ZFC.ITSubstOpen9

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.BridgeBProbe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- Bridge B — exactly the `hB` parameter shape of `allKey_of_bridge`. -/
theorem bridgeB (q : V) (hq : IsSemiformula ℒₒᵣ (1 : V) q) :
    subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) q) =
      iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) q) := by
  have h1 : IsSemiformula ℒₒᵣ ((0 : V) + 1) q := by
    rw [show (0 : V) + 1 = 1 from _root_.zero_add 1]
    exact hq
  have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) (0 : V) q h1
  rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
  rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
  exact h.symm

end GodelQ.BridgeBProbe

#print axioms GodelQ.BridgeBProbe.bridgeB
