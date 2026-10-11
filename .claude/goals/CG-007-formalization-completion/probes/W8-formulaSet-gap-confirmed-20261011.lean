import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAN
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 修法 1：把 IsFormulaSet 加进归纳不变量
-- 关键是它是否仍是 Σ1（induction1 的 hP 要求）
-- IsFormulaSet L s = ∀ p ∈ s, IsSemiformula L 0 p
-- 这是 Π1。与 Derivable（Σ1）合取：Σ1 ∧ Π1 —— 一般不是 Σ1！
--
-- 但注意：Derivable T s 蕴含 IsFormulaSet L s（Derivable.isFormulaSet）。
-- 所以如果我们用 Derivable 而非 Provable 作为主谓词，
-- IsFormulaSet 是**冗余**的——它由 Derivable 自动给出！
--
-- 真正缺的是 **ℒₒᵣ 侧的** IsFormulaSet，而 Derivable 给的是 ℒₛₑₜ 侧的。

-- 试：能否从 IsFormulaSet ℒₛₑₜ (translateSeq s) 推 IsFormulaSet ℒₒᵣ s？
-- 这需要 iT 的某种单射性/反映性。
-- 实际上：translateSeq s 的元素是 iT 0 x（x ∈ s）。
-- IsFormulaSet ℒₛₑₜ (translateSeq s) 说每个 iT 0 x 是 ℒₛₑₜ 公式。
-- 要推 IsSemiformula ℒₒᵣ 0 x，需要 iT 的反映性——大概很难。

-- 换个更简单的修法：**弱化 translateSeq_setShift 的假设**。
-- 它真正需要 IsFormulaSet 只是为了让 setShift 后的 translateSeq 元素仍是公式。
-- 也许有不需要公式集的版本？

-- 检验：translateSeq_setShift 能否在只有「像是公式集」时成立？
example {s : V} (hs : IsFormulaSet ℒₛₑₜ (translateSeq s)) :
    translateSeq (setShift ℒₒᵣ s) = setShift ℒₛₑₜ (translateSeq s) := by
  apply mem_ext; intro y
  simp only [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, ⟨z, hz, rfl⟩, rfl⟩
    exact ⟨iT 0 z, ⟨z, hz, rfl⟩, iT_shift (n := 0) z ?_⟩
  · rintro ⟨w, ⟨z, hz, rfl⟩, rfl⟩
    exact ⟨shift ℒₒᵣ z, ⟨z, hz, rfl⟩, (iT_shift (n := 0) z ?_).symm⟩
  -- 缺的正是 IsSemiformula ℒₒᵣ 0 z

end GodelQ.ProbeAN
