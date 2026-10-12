import GodelQ.ZFC.ITSubsts1

/-! # DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

set_option maxHeartbeats 4000000

namespace GodelQ.ProbeVe2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

example {v : V} (hv : IsUTermVec ℒₒᵣ 2 v) {a : V} (ha : a < 3) :
    subst ℒₛₑₜ (^#a ∷ ?[^&0] : V) (ve2 (1 : V) 2 (0 : V) ?[iVE (1 : V) v.[0], iVE (1 : V) v.[1]]) =
      subst ℒₛₑₜ (?[^#a] : V) (ve2 (0 : V) 2 (0 : V)
        ?[iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[0]),
          iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[1])]) := by
  have hF : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1] : V) (cFunc 2 (0 : V))) :=
    (IsSemiformula.subst (isSemiformula_cFunc_arity2 (by norm_num) (0 : V))
      (by
        rw [show (^#2 ∷ ?[^#0, ^#1] : V) = (?[^#2, ^#0, ^#1] : V) from rfl]
        rw [IsSemitermVec.doubleton]
        exact ⟨IsSemiterm.bvar.mpr (by norm_num), IsSemiterm.bvar.mpr (by norm_num)⟩)).isUFormula
  have hA0 : IsUFormula ℒₛₑₜ (conjunct 3 1 0 (iVE (1 : V) v.[0])) :=
    (isSemiformula_conjunct (isSemiformula_iVE v.[0] (hv.isUTerm.isSemitermVec.nth (by norm_num)))
      (zero_lt_three_add 1)).isUFormula
  have hA1 : IsUFormula ℒₛₑₜ (conjunct 3 1 1 (iVE (1 : V) v.[1])) :=
    (isSemiformula_conjunct (isSemiformula_iVE v.[1] (hv.isUTerm.isSemitermVec.nth (by norm_num)))
      (one_lt_three_add 1)).isUFormula
  have hB0 : IsUFormula ℒₛₑₜ (conjunct 3 0 0 (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[0]))) :=
    (isSemiformula_conjunct
      (isSemiformula_iVE _ (IsSemitermVec.termSubst hv.isSemitermVec
        (hv.isUTerm.isSemitermVec.nth (by norm_num)))) (zero_lt_three_add 0)).isUFormula
  have hB1 : IsUFormula ℒₛₑₜ (conjunct 3 0 1 (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[1]))) :=
    (isSemiformula_conjunct
      (isSemiformula_iVE _ (IsSemitermVec.termSubst hv.isSemitermVec
        (hv.isUTerm.isSemitermVec.nth (by norm_num)))) (one_lt_three_add 0)).isUFormula
  simp only [ve2, nth_adjoin_zero, nth_adjoin_one]
  rw [subst_qqAlls_two (IsUFormula.imp.mpr ⟨IsUFormula.and.mpr ⟨hA0, IsUFormula.and.mpr ⟨hA1, IsUFormula.verum⟩⟩, hF⟩),
    subst_qqAlls_two (IsUFormula.imp.mpr ⟨IsUFormula.and.mpr ⟨hB0, IsUFormula.and.mpr ⟨hB1, IsUFormula.verum⟩⟩, hF⟩)]
  trace_state
  sorry

end GodelQ.ProbeVe2
