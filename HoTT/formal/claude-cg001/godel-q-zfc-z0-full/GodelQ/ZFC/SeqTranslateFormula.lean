import GodelQ.ZFC.SeqTranslate

/-!
# CG-007 · W8 第二层（三）：内部翻译所产出公式的编码是公式

`iT` 的构造（`InternalTranslate.lean:231`）把公式码送到公式码，但 `InternalTranslate.lean`
里**没有**证明这一点。第二层的每个规则支都要用 `IsFormulaSet`，所以这是地基。

本文件先证其中三条（`iT` 构造里 `rel`/`nrel` 支与合取项所依赖的固定公式码）。
关键是 `Sentence.coe_quote_eq_quote : (↑(⌜σ⌝ : ℕ) : V) = ⌜σ⌝`
（`Formula/Coding.lean:440`）——`cRelN`/`cDomN`/`cFuncN` 都定义成 **ℕ** 层的引号，
必须先搬到 `V` 才能用 `Sentence.quote_isSemiformula`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 关系符号的翻译公式码是公式（层级 = 元数 2）。 -/
lemma isSemiformula_cRel (R : V) : IsSemiformula ℒₛₑₜ 2 (cRel R) := by
  unfold cRel cRelN
  split <;> split <;>
    first
      | rw [Sentence.coe_quote_eq_quote]
        exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.eq)
      | rw [Sentence.coe_quote_eq_quote]
        exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.lt)

/-- 定义域公式 `x ∈ ω` 的码是公式（层级 1）。 -/
lemma isSemiformula_cDomN : IsSemiformula ℒₛₑₜ 1 (↑cDomN : V) := by
  unfold cDomN
  rw [Sentence.coe_quote_eq_quote]
  simpa using
    Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.domain)

/-- 0 元函数符号的定义公式码是公式（层级 1）。 -/
lemma isSemiformula_cFunc_zero : IsSemiformula ℒₛₑₜ 1 (cFunc 0 0) := by
  simp only [cFunc, cFuncN, reduceIte]
  rw [Sentence.coe_quote_eq_quote]
  simpa using
    Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.zero)

end GodelQ.SeqTranslate
