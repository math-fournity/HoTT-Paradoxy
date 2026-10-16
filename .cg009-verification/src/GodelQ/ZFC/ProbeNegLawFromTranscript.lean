import GodelQ.ZFC.SeqTranslateFormula

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。判定两件事：
1. 2026-10-11 WorkBuddy 会话（GUI 导出对话录第 1265–1345 行）给的 `iT_neg` 九支填法
   原样搬来能不能编译；
2. 若不能，照**已证**的 `isSemiformula_iT`（`SeqTranslateFormula.lean:348–406`）的
   结构重排（`?_` 占位 + definability 后置 + 八支），能否走通。

**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeNegLawFromTranscript

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 照已证骨架重排：`P` 带 `param = n` 护罩，八支按 Foundation 真实顺序，
definability 放最后。 -/
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using key hp (rfl : n = n)
  · definability
  · intro n param k R v hR hv h
    rw [← h] at hv
    rw [neg_rel (L := ℒₒᵣ) hR hv, iT_nrel hR hv, iT_rel hR hv]
  · intro n param k R v hR hv h
    rw [← h] at hv
    rw [neg_nrel (L := ℒₒᵣ) hR hv, iT_rel hR hv,
      IsUFormula.neg_neg (isSemiformula_iTR hR hv).isUFormula]
  · intro n param h
    rw [neg_verum (L := ℒₒᵣ), iT_falsum, neg_verum (L := ℒₛₑₜ)]
  · intro n param h
    rw [neg_falsum (L := ℒₒᵣ), iT_verum, neg_falsum (L := ℒₛₑₜ)]
  · intro n param p q hp hq ihp ihq h
    rw [neg_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula]
    rw [iT_or (IsUFormula.neg hp.isUFormula) (IsUFormula.neg hq.isUFormula)]
    rw [iT_and hp.isUFormula hq.isUFormula]
    rw [neg_and (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
      (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋏ ·) (ihp h) (ihq h)
  · intro n param p q hp hq ihp ihq h
    rw [neg_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula]
    rw [iT_and (IsUFormula.neg hp.isUFormula) (IsUFormula.neg hq.isUFormula)]
    rw [iT_or hp.isUFormula hq.isUFormula]
    rw [neg_or (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
      (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋎ ·) (ihp h) (ihq h)
  · intro n param p hp ih h
    rw [← h] at hp
    rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula)]
    rw [UformulaRec1.Construction.result_exs (c := iT.construction) (L := ℒₒᵣ)
      (IsUFormula.neg hp.isUFormula) (rfl : iT.construction.exsSize param (neg ℒₒᵣ p) = 1)]
    rw [show iT (param + 1) (neg ℒₒᵣ p) =
        iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p) by simp [iT.construction]]
    rw [← ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
    simp [iT.construction, neg, imp, domZero]
  · intro n param p hp ih h
    rw [← h] at hp
    rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula)]
    rw [UformulaRec1.Construction.result_all (c := iT.construction) (L := ℒₒᵣ)
      (IsUFormula.neg hp.isUFormula) (rfl : iT.construction.allSize param (neg ℒₒᵣ p) = 1)]
    rw [show iT (param + 1) (neg ℒₒᵣ p) =
        iT (iT.construction.allChanges param 0) (neg ℒₒᵣ p) by simp [iT.construction]]
    rw [← ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
    simp [iT.construction, neg, imp, domZero]

end GodelQ.ProbeNegLawFromTranscript

#print axioms GodelQ.ProbeNegLawFromTranscript.iT_neg
