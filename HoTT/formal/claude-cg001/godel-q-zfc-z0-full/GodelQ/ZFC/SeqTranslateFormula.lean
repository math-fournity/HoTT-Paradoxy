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

/-- `shiftVec b n = [^#b, …, ^#(b+n-1)]` 是合法的 `n` 元项向量，层数 `b+n`。 -/
lemma isSemitermVec_shiftVec (b : V) : ∀ (n : ℕ),
    IsSemitermVec ℒₛₑₜ (n : V) (b + (n : V)) (shiftVec b (n : V))
  | 0 => by simp
  | n + 1 => by
    push_cast
    rw [shiftVec_succ, IsSemitermVec.cons_iff]
    refine ⟨?_, ?_⟩
    · rw [IsSemiterm.bvar]
      calc b < (n : V) + b + 1 := lt_add_self_add_one b (n : V)
        _ = b + ((n : V) + 1) := by ring
    · have ih := isSemitermVec_shiftVec b n
      have h := IsSemitermVec.termBShiftVec (L := ℒₛₑₜ) ih
      simpa only [add_assoc] using h

/-- 单元素项向量 `?[^#i]`。 -/
lemma isSemitermVec_single_bvar {i n : V} (hi : i < n) :
    IsSemitermVec ℒₛₑₜ 1 n ?[^#i] :=
  IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr hi)

/-! ### `definability` 处理部分应用所需的层级实例

`shiftVec` 只有 `𝚺ᴬ₁-Function₂` 实例，而 `definability` 在证
`{Γ := 𝚺, rank := 1}.DefinableFunction fun v ↦ shiftVec b (v 78)`
（即固定首参的一元版）时，`aesop` 撞规则深度上限（30/50）而失败。
对照 Foundation 自己的 `disjSeqSubst`（`Formula/Iteration.lean:211`）——
它同时登记了 `𝚺ᴬ₁` 版与 **层级版** `Γᴬ_[m+1]-Function₃`，`definability` 才过。
给 `shiftVec` 补上同一个层级实例即可。 -/

instance shiftVec_definable : 𝚺ᴬ₁-Function₂ (shiftVec : V → V → V) :=
  shiftVec_defined.to_definable

instance shiftVec_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] shiftVec :=
  shiftVec_definable.of_sigmaOne

/-- `shiftVec b n` 对**任意 V 元素** `n` 都是合法的 `n` 元项向量（层数 `b+n`）。

第 11.1 节的 `n : ℕ` 版本不够：`conjunct` 的 `n` 是任意 V 元素。V 上的归纳原理是
`ISigma1.sigma1_succ_induction`（要求 `𝗜𝚺⁺₁`，但 `𝗜𝚺 1 ≊ 𝗜𝚺⁺ 1` 有实例，故 `𝗜𝚺₁` 即可）。 -/
lemma isSemitermVec_shiftVec_V (b : V) : ∀ n : V,
    IsSemitermVec ℒₛₑₜ n (b + n) (shiftVec b n) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ n ih =>
    rw [shiftVec_succ, IsSemitermVec.cons_iff]
    refine ⟨?_, ?_⟩
    · rw [IsSemiterm.bvar]
      calc b < n + b + 1 := lt_add_self_add_one b n
        _ = b + (n + 1) := by ring
    · have h := IsSemitermVec.termBShiftVec (L := ℒₛₑₜ) ih
      simpa only [add_assoc] using h

/-- 合取项 `conjunct b n i y` 的公式性（层级 `b+n`）。

`conjunct b n i y = (subst ?[^#i] cDomN) ^⋏ (subst (^#i ∷ shiftVec b n) y)`，
两条 `IsSemiformula.subst` + `IsSemiformula.and`；向量 `^#i ∷ shiftVec b n` 由
`IsSemitermVec.cons_iff` 拼，尾部就是上一条。 -/
lemma isSemiformula_conjunct {b n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y)
    (hi : i < b + n) : IsSemiformula ℒₛₑₜ (b + n) (conjunct b n i y) := by
  rw [conjunct, IsSemiformula.and]
  refine ⟨?_, ?_⟩
  · exact IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := b + n) hi)
  · refine IsSemiformula.subst (L := ℒₛₑₜ) hy ?_
    rw [IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec_V b n⟩

end GodelQ.SeqTranslate
