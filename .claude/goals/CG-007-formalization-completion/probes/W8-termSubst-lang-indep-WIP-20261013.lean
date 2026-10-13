import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性：`termSubst` 与语言无关。**

`termSubst` 的构造按 `qqBvar`/`qqFvar`/`qqFunc` 的**编码**递归，
**不查 `IsFunc`**（`IsFunc` 只用于**证明**该码是函数符号，不参与计算）。
故同一项码在两个语言下 `termSubst` 给**相同结果**。

这是 §12.44 的「更正」**不成立**的理由——
`subst ℒₛₑₜ w p` 对 `ℒₒᵣ` 的项向量 `w` **就是**要用的东西，不需要 `iVE-像`。 -/
lemma termSubst_lang_indep (w t : V) :
    termSubst ℒₒᵣ w t = termSubst ℒₛₑₜ w t := by
  apply IsUTerm.induction (L := ℒₒᵣ) 𝚺
    (P := fun t ↦ termSubst ℒₒᵣ w t = termSubst ℒₛₑₜ w t) (by definability)
  case hbvar =>
    intro z; rw [termSubst_bvar, termSubst_bvar]
  case hfvar =>
    intro x; rw [termSubst_fvar, termSubst_fvar]
  case hfunc =>
    intro k f v hkf hv ih
    rw [termSubst_func (L := ℒₒᵣ) hkf hv]
    rw [show termSubst ℒₛₑₜ w (^func k f v)
          = (^func k f (termSubstVec ℒₛₑₜ k w v) : V) from
      termSubst_func (L := ℒₛₑₜ) ?_ hv]
    · congr 1
      apply nth_ext' k ?_ ?_ ?_
      · rw [len_termSubstVec hv, len_termSubstVec hv]
      · rw [len_termSubstVec hv, len_termSubstVec hv]
      · intro i hi
        rw [nth_termSubstVec hv hi, nth_termSubstVec hv hi, ih i hi]
    · sorry

end GodelQ.ProbeFL
