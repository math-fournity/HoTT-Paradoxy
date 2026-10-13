-- CG-009: shift_conjunct — needed for the func case of iVE_shift.
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShiftConjunctProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- First check: is subst ?[^#i] cDomN actually definitionally ^#i ∷ 0?
example (i : V) : (subst ℒₛₑₜ ?[^#i] (cDomN : V)) = subst ℒₛₑₜ (^#i ∷ 0) (cDomN : V) := rfl

-- shift of the domZero part: the vector is [#i], and cDomN is a sentence quote.
lemma shift_subst_domN (i : V) :
    shift (L := ℒₛₑₜ) (subst ℒₛₑₜ ?[^#i] (cDomN : V)) = subst ℒₛₑₜ ?[^#i] (cDomN : V) := by
  rw [shift_substs (L := ℒₛₑₜ) (n := 1) (m := 1) (p := (cDomN : V))
    isSemiformula_cDomN
    (isSemitermVec_single_bvar (n := 1) (by simp))]
  congr 1
  · -- termShiftVec 1 1 (^#i ∷ 0) = ^#i ∷ 0
    rw [termShiftVec_cons₁ (IsUTerm.bvar (L := ℒₛₑₜ)), termShift_bvar]
  · -- shift cDomN = cDomN
    rw [Sentence.coe_quote_eq_quote]
    exact GodelQ.ShiftQuote.shift_quote _

end GodelQ.ShiftConjunctProbe

#print axioms GodelQ.ShiftConjunctProbe.shift_subst_domN
