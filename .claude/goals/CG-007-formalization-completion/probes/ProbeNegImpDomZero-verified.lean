/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。用于确定 `neg_imp_domZero` 的正确写法，**不是**收据源，**不是**数学主张。
2026-10-11 实测：`neg_imp_domZero_I` 与 `neg_imp_domZero_H` 编译 exit 0；
`neg_imp_domZero_J`（`simp` 一步到位写法）失败（`unsolved goals`），保留作为负对照。

关键发现：`IsUFormula` 假设必须写成 `IsUFormula ℒₛₑₜ (domZero : V)`，
否则推断出 `IsUFormula.{0,0}`，与目标里的 `{u_1,0}` 不匹配。
-/
import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeNegImp

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- minimal form: annotate domZero and chain the three rewrites
lemma neg_imp_domZero_I {x : V} (hx : IsUFormula ℒₛₑₜ x) :
    neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x := by
  have hd : IsUFormula ℒₛₑₜ (domZero : V) := (isSemiformula_domZero (n := 0)).isUFormula
  rw [imp, neg_or (L := ℒₛₑₜ) (IsUFormula.neg hd) hx, IsUFormula.neg_neg hd]

-- and does plain simp work with the annotated hypothesis?
lemma neg_imp_domZero_J {x : V} (hx : IsUFormula ℒₛₑₜ x) :
    neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x := by
  have hd : IsUFormula ℒₛₑₜ (domZero : V) := (isSemiformula_domZero (n := 0)).isUFormula
  simp [imp, IsUFormula.neg_neg hd]

end GodelQ.ProbeNegImp
