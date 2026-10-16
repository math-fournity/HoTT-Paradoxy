import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula.Functions
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeITR

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- Goal: iTR n k R v is a UFormula (layer-free), using only IsUFormula structural lemmas.
-- iTR n k R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤)) (subst ?[^#0,^#1] (cRel R))) 2
example (n k R v : V) (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    IsUFormula ℒₛₑₜ (iTR n k R v) := by
  rw [iTR]
  apply IsUFormula.qqAlls
  apply IsUFormula.imp
  · rw [IsUFormula.and]
    refine ⟨?_, ?_⟩
    · -- conjunct 2 n 0 (iVE n v.[0])
      have h0 := (iVE_quote _ _).isUFormula
      admit
    · rw [IsUFormula.and]
      refine ⟨?_, ?_⟩
      · admit
      · exact IsUFormula.verum
  · -- subst ?[^#0,^#1] (cRel R)
    admit

end GodelQ.ProbeITR
