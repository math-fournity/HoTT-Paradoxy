-- CG-009: term-level iVE / termShift compatibility — func case (needed for ishift rel/nrel).
import GodelQ.ZFC.ShiftQuote

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEProbe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma shift_imp {p q : V} (hp : IsUFormula ℒₛₑₜ p) (hq : IsUFormula ℒₛₑₜ q) :
    shift (L := ℒₛₑₜ) (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (shift (L := ℒₛₑₜ) p) (shift (L := ℒₛₑₜ) q) := by
  rw [imp, imp, shift_or hp.neg hq]
  congr 1
  exact shift_neg hp.isSemiformula

/-- shift fixes `cFunc 0 f` (a numeral = a sentence quote). -/
lemma shift_cFunc0 (f : V) : shift (L := ℒₛₑₜ) (cFunc (V := V) 0 f) = cFunc (V := V) 0 f := by
  simp only [cFunc, cFuncN, reduceIte]
  split
  · rw [Sentence.coe_quote_eq_quote]
    exact GodelQ.ShiftQuote.shift_quote _
  · split
    · rename_i h; exact absurd h (by decide)
    · rw [Sentence.coe_quote_eq_quote]
      exact GodelQ.ShiftQuote.shift_quote _

/-- shift fixes `subst [#0] (cFunc 0 f)` — closed substitution. -/
lemma shift_subst_cFunc0 (f : V) :
    shift (L := ℒₛₑₜ) (subst ℒₛₑₜ (^#0 ∷ 0) (cFunc (V := V) 0 f)) =
      subst ℒₛₑₜ (^#0 ∷ 0) (cFunc (V := V) 0 f) := by
  rw [shift_substs (L := ℒₛₑₜ) (n := 1) (m := 1) (p := cFunc (V := V) 0 f)
    (isSemiformula_cFunc_arity0 f)
    (isSemitermVec_single_bvar (n := 1) (by simp))]
  congr 1
  · rw [termShiftVec_cons₁ (IsUTerm.bvar (L := ℒₛₑₜ)), termShift_bvar]
  · exact shift_cFunc0 f

/-- shift fixes ve0 (0-ary case). -/
lemma shift_ve0 (f : V) : shift (L := ℒₛₑₜ) (ve0 (V := V) 0 f) = ve0 (V := V) 0 f := by
  rw [ve0]
  rw [shift_imp IsUFormula.verum ?_]
  · rw [shift_verum (L := ℒₛₑₜ), shift_subst_cFunc0]
  · exact (IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := 1)
      (isSemiformula_cFunc_arity0 f)
      (isSemitermVec_single_bvar (n := 1) (by simp))).isUFormula

end GodelQ.IVEProbe

#print axioms GodelQ.IVEProbe.shift_ve0
