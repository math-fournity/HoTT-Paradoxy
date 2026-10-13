-- CG-009: pieces for the ve2 case of iVE_shift.
import GodelQ.ZFC.TranslateShiftCompat
import GodelQ.ZFC.ShiftQuote

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.Ve2ShiftProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- shift fixes the domZero-part of `conjunct` at layer 3 (where i ∈ {0,1,2}). -/
lemma shift_subst_domN3 (i : V) (hi : i < 3) :
    shift (L := ℒₛₑₜ) (subst ℒₛₑₜ ?[^#i] (cDomN : V)) = subst ℒₛₑₜ ?[^#i] (cDomN : V) := by
  rw [shift_substs (L := ℒₛₑₜ) (n := 1) (m := 3) (p := (cDomN : V))
    isSemiformula_cDomN (isSemitermVec_single_bvar (i := i) (n := 3) hi)]
  congr 1
  · have hv : (?[^#i] : V) = ^#i ∷ (0 : V) := rfl
    rw [hv, termShiftVec_cons₁ (IsUTerm.bvar (L := ℒₛₑₜ)), termShift_bvar]
  · rw [show (↑cDomN : V) = ⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝ from cDomN_eq]
    exact GodelQ.ShiftQuote.shift_quote _

-- KEY FACT: shiftVec b n is a vector of bvars only; termShiftVec leaves bvars alone,
-- so termShiftVec 1 (shiftVec b n) should equal shiftVec b n.
#check @shiftVec
#check @termShiftVec

end GodelQ.Ve2ShiftProbe

#print axioms GodelQ.Ve2ShiftProbe.shift_subst_domN3
