-- CG-009: probe the rel branch of ishift.
import GodelQ.ZFC.ShiftDomZeroProbe

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IShiftRelProbe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- What does the rel branch's goal look like after iT_rel + shift_rel?
example {param k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    iTR param k R (termShiftVec ℒₒᵣ k v) = shift ℒₛₑₜ (iTR param k R v) := by
  rw [iTR, iTR]
  sorry

end GodelQ.IShiftRelProbe
