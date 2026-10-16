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

/-- `cFunc 0 f`（0 元函数符号）层级 1，对**任意** `f`（`ve0` 支要用）。 -/
lemma isSemiformula_cFunc_arity0 (f : V) : IsSemiformula ℒₛₑₜ 1 (cFunc 0 f) := by
  simp only [cFunc, cFuncN, reduceIte]
  split
  · rw [Sentence.coe_quote_eq_quote]
    simpa using Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.zero)
  · split
    · rename_i h
      exact absurd h (by decide)
    · rw [Sentence.coe_quote_eq_quote]
      simpa using Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.one)

/-- `cFunc k f`（2 元函数符号）层级 3，对 `k ≠ 0`（`ve2` 支要用）。 -/
lemma isSemiformula_cFunc_arity2 {k : V} (hk : k ≠ 0) (f : V) :
    IsSemiformula ℒₛₑₜ 3 (cFunc k f) := by
  simp only [cFunc, cFuncN, reduceIte]
  split
  · rename_i h
    exact absurd h hk
  · split
    · split
      · rename_i h
        exact absurd h (by decide)
      · rw [Sentence.coe_quote_eq_quote]
        simpa using
          Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.add)
    · split
      · rename_i h
        exact absurd h (by decide)
      · split
        · rename_i h
          exact absurd h (by decide)
        · rw [Sentence.coe_quote_eq_quote]
          simpa using
            Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.mul)

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


/-! ### `iVE` 的三条计算规则（2026-10-11 新增）

`iVE.construction` 的 fixpoint 语义给出三条化简规则；它们是 `isSemiformula_iVE` 的入口。 -/

@[simp] lemma iVE_bvar (n z : V) : iVE n (^#z) = eqAtom (^#(z + 1)) := by
  simp [iVE, iVE.construction]

@[simp] lemma iVE_fvar (n x : V) : iVE n (^&x) = eqAtom (^&x) := by
  simp [iVE, iVE.construction]

lemma iVE_func {n k f v : V} (hkf : (ℒₒᵣ).IsFunc k f) (hv : IsUTermVec ℒₒᵣ k v) :
    iVE n (^func k f v) =
      (if k = 0 then ve0 k f else ve2 n k f (iVE.construction.resultVec ℒₒᵣ ![n] k v)) := by
  rw [iVE, iVE.construction.result_func' hkf hv]; rfl

/-! ### `iVE` 的公式性（`isSemiformula_iVE`） -/

/-- 给 `iVE` 补层级实例：`definability` 证部分应用时需要（照 `shiftVec` 的先例）。 -/
instance iVE_definable : 𝚺ᴬ₁-Function₂ (iVE : V → V → V) := iVE_defined.to_definable
instance iVE_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] iVE := iVE_definable.of_sigmaOne

/-- 公式性对层数单调。 -/
lemma isSemiformula_mono {n m p : V} (h : IsSemiformula ℒₛₑₜ n p) (hnm : n ≤ m) :
    IsSemiformula ℒₛₑₜ m p := ⟨h.isUFormula, le_trans h.bv_le hnm⟩

/-- `eqAtom t = (^#0 = t)` 的公式性（层数 n ≥ 1，t 在层数 n）。 -/
lemma isSemiformula_eqAtom {n t : V} (hn : 0 < n) (ht : IsSemiterm ℒₛₑₜ n t) :
    IsSemiformula ℒₛₑₜ n (eqAtom t) := by
  rw [eqAtom, IsSemiformula.rel]
  refine ⟨?_, ?_⟩
  · rw [cEqN]; exact codeIn_rel_quote _
  · rw [show (?[^#0, t] : V) = (^#0 : V) ∷ (t ∷ 0) from rfl]
    rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr hn, ?_⟩
    rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨ht, by simp⟩

lemma zero_lt_three_add (n : V) : (0:V) < 3 + n := by
  have h := lt_add_self_add_one (0 : V) (n + 2)
  have e : n + 2 + 0 + 1 = 3 + n := by ring
  rwa [e] at h

lemma one_lt_three_add (n : V) : (1:V) < 3 + n := by
  have h := lt_add_self_add_one (1 : V) (n + 1)
  have e : n + 1 + 1 + 1 = 3 + n := by ring
  rwa [e] at h

lemma two_lt_three_add (n : V) : (2:V) < 3 + n := by
  have h := lt_add_self_add_one (2 : V) n
  have e : n + 2 + 1 = 3 + n := by ring
  rwa [e] at h

lemma zero_lt_two_add (n : V) : (0:V) < 2 + n := by
  have h := lt_add_self_add_one (0 : V) (n + 1)
  have e : (n + 1) + 0 + 1 = 2 + n := by ring
  rwa [e] at h

lemma one_lt_two_add (n : V) : (1:V) < 2 + n := by
  have h := lt_add_self_add_one (1 : V) n
  have e : n + 1 + 1 = 2 + n := by ring
  rwa [e] at h

/-- `ve0 k f` 的公式性（0 元支，层数 m ≥ 1）。 -/
lemma isSemiformula_ve0 {m f : V} (hm : 1 ≤ m) :
    IsSemiformula ℒₛₑₜ m (ve0 0 f) := by
  have h1 : IsSemiformula ℒₛₑₜ 1 (ve0 0 f) := by
    rw [ve0, IsSemiformula.imp]
    refine ⟨IsSemiformula.verum, ?_⟩
    exact IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := 1)
      (isSemiformula_cFunc_arity0 f)
      (isSemitermVec_single_bvar (n := 1) (by simp))
  exact isSemiformula_mono h1 hm

/-- `ve2 n k f w` 的公式性（2 元支，层数 n+1）。 -/
lemma isSemiformula_ve2 {n k f w : V} (hk : k ≠ 0)
    (hw0 : IsSemiformula ℒₛₑₜ (n + 1) w.[0]) (hw1 : IsSemiformula ℒₛₑₜ (n + 1) w.[1]) :
    IsSemiformula ℒₛₑₜ (n + 1) (ve2 n k f w) := by
  have hf : IsSemiformula ℒₛₑₜ 3 (cFunc k f) := isSemiformula_cFunc_arity2 hk f
  rw [ve2]
  refine IsSemiformula.qqAlls (n := n + 1) (k := 2) ?_
  have e : ((n + 1) + 2 : V) = 3 + n := by ring
  rw [e]
  rw [IsSemiformula.imp]
  refine ⟨?_, ?_⟩
  · rw [IsSemiformula.and]
    refine ⟨isSemiformula_conjunct (b := 3) (n := n) (i := 0) hw0 (zero_lt_three_add n), ?_⟩
    rw [IsSemiformula.and]
    exact ⟨isSemiformula_conjunct (b := 3) (n := n) (i := 1) hw1 (one_lt_three_add n),
      IsSemiformula.verum⟩
  · apply IsSemiformula.subst (L := ℒₛₑₜ) (n := 3) (m := 3 + n)
    · exact hf
    · rw [show (^#2 ∷ ?[^#0, ^#1] : V) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ 0 from rfl]
      rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr ?_, ?_⟩
      · simpa [show (3:V) = 2 + 1 by norm_num, add_assoc] using two_lt_three_add n
      · rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
        refine ⟨IsSemiterm.bvar.mpr ?_, ?_⟩
        · simpa [show (3:V) = 1 + 1 + 1 by norm_num, add_assoc] using zero_lt_three_add n
        · rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
          exact ⟨IsSemiterm.bvar.mpr (by
            simpa [add_assoc] using one_lt_three_add n), by simp⟩

/-- 算术语言只有 0 元与 2 元函数符号：`k ≠ 0` 时 `k = 2`。 -/
lemma k_eq_two_of_func {k f : V} (hkf : (ℒₒᵣ).IsFunc k f) (hk : k ≠ 0) : k = 2 := by
  rcases Arithmetic.isFunc_iff_LOR.mp hkf with h | h | h | h
  · exact absurd h.1 hk
  · exact absurd h.1 hk
  · exact h.1
  · exact h.1

/-- **`iVE` 的公式性**：项 t（层数 n）的变量等式码是公式（层数 n+1）。

用 `IsSemiterm.sigma1_induction`（项侧没有带层数的 TermRec 归纳）；三支
`bvar`/`fvar`/`func`，`func` 再分 `ve0`/`ve2`。 -/
lemma isSemiformula_iVE {n : V} : ∀ t, IsSemiterm ℒₒᵣ n t →
    IsSemiformula ℒₛₑₜ (n + 1) (iVE n t) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := n)
    (P := fun t ↦ IsSemiformula ℒₛₑₜ (n + 1) (iVE n t))
  · definability
  · intro z hz
    rw [iVE_bvar]
    exact isSemiformula_eqAtom (by simp)
      (IsSemiterm.bvar.mpr (by
        have h' := add_lt_add_right hz 1
        have e : (1 : V) + z = z + 1 := by ring
        have e2 : (1 : V) + n = n + 1 := by ring
        rwa [e, e2] at h'))
  · intro x
    rw [iVE_fvar]
    exact isSemiformula_eqAtom (by simp) (IsSemiterm.fvar (n + 1) x)
  · intro k f v hkf hv ih
    rw [iVE_func hkf hv.isUTerm]
    split
    · rename_i hk0
      subst hk0
      exact isSemiformula_ve0 (by simp)
    · rename_i hk0
      have hk2 := k_eq_two_of_func hkf hk0
      subst hk2
      apply isSemiformula_ve2 hk0
      · have h0 : (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[0] = iVE n v.[0] := by
          rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (by simp)]
          simp [iVE]
        rw [h0]
        exact ih 0 (by simp)
      · have h1 : (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[1] = iVE n v.[1] := by
          rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (by simp)]
          simp [iVE]
        rw [h1]
        exact ih 1 (by simp)

/-- 定义域限制 `domZero` 的公式性（层数 n+1）。 -/
lemma isSemiformula_domZero {n : V} : IsSemiformula ℒₛₑₜ (n + 1) domZero := by
  rw [domZero]
  exact IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := n + 1)
    isSemiformula_cDomN
    (isSemitermVec_single_bvar (n := n + 1) (by simp))

/-- **`iTR` 的公式性**：原子翻译码是公式（层数 n）。 -/
lemma isSemiformula_iTR {n k R v : V} (hR : (ℒₒᵣ).IsRel k R)
    (hv : IsSemitermVec ℒₒᵣ k n v) : IsSemiformula ℒₛₑₜ n (iTR n k R v) := by
  have hk2 : k = 2 := by
    rcases Arithmetic.isRel_iff_LOR.mp hR with h | h
    · exact h.1
    · exact h.1
  subst hk2
  rw [iTR]
  refine IsSemiformula.qqAlls (n := n) (k := 2) ?_
  have e : (n + 2 : V) = 2 + n := by ring
  rw [e]
  rw [IsSemiformula.imp]
  refine ⟨?_, ?_⟩
  · rw [IsSemiformula.and]
    refine ⟨?_, ?_⟩
    · exact isSemiformula_conjunct (b := 2) (n := n) (i := 0)
        (isSemiformula_iVE v.[0] (hv.nth (i := 0) (by simp))) (zero_lt_two_add n)
    · rw [IsSemiformula.and]
      refine ⟨?_, IsSemiformula.verum⟩
      exact isSemiformula_conjunct (b := 2) (n := n) (i := 1)
        (isSemiformula_iVE v.[1] (hv.nth (i := 1) (by simp))) (one_lt_two_add n)
  · apply IsSemiformula.subst (L := ℒₛₑₜ) (n := 2) (m := 2 + n)
    · exact isSemiformula_cRel R
    · rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ 0 from rfl]
      rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by
        simpa [show (2:V) = 1 + 1 by norm_num, add_assoc] using zero_lt_two_add n), ?_⟩
      rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
      exact ⟨IsSemiterm.bvar.mpr (by
        simpa [show (2:V) = 1 + 1 by norm_num, add_assoc] using one_lt_two_add n), by simp⟩

/-- **公式保持性主定理**：算术公式码的翻译仍是公式，层数不变。

`semiformula_result_induction` 把输出层 `param` 与输入层 `n` 独立量化；归纳谓词带
`param = n` 护罩（`iT` 改层：`iTR param …` 要求 `v` 在层 `param`）。 -/
theorem isSemiformula_iT {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    IsSemiformula ℒₛₑₜ n (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → IsSemiformula ℒₛₑₜ param (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → IsSemiformula ℒₛₑₜ param q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    have h := key hp (rfl : n = n)
    simpa [iT] using h
  · definability
  · intro n param k R v hR hv h
    rw [← h] at hv
    show IsSemiformula ℒₛₑₜ param (iTR param k R v)
    exact isSemiformula_iTR hR hv
  · intro n param k R v hR hv h
    rw [← h] at hv
    show IsSemiformula ℒₛₑₜ param (neg ℒₛₑₜ (iTR param k R v))
    exact IsSemiformula.neg (isSemiformula_iTR hR hv)
  · intro n param h
    show IsSemiformula ℒₛₑₜ param (^⊤)
    exact IsSemiformula.verum
  · intro n param h
    show IsSemiformula ℒₛₑₜ param (^⊥)
    exact IsSemiformula.falsum
  · intro n param p q hp hq ihp ihq h
    show IsSemiformula ℒₛₑₜ param
      ((UformulaRec1.Construction.result ℒₒᵣ iT.construction param p) ^⋏
       (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q))
    rw [IsSemiformula.and]
    exact ⟨ihp h, ihq h⟩
  · intro n param p q hp hq ihp ihq h
    show IsSemiformula ℒₛₑₜ param
      ((UformulaRec1.Construction.result ℒₒᵣ iT.construction param p) ^⋎
       (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q))
    rw [IsSemiformula.or]
    exact ⟨ihp h, ihq h⟩
  · intro n param p hp ih h
    rw [UformulaRec1.Construction.result_all (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param p = 1)]
    change IsSemiformula ℒₛₑₜ param
      (^∀ (imp ℒₛₑₜ domZero ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
        (iT.construction.allChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero, IsSemiformula.all, IsSemiformula.imp]
    refine ⟨isSemiformula_domZero (n := param), ?_⟩
    exact ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])
  · intro n param p hp ih h
    rw [UformulaRec1.Construction.result_exs (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param p = 1)]
    change IsSemiformula ℒₛₑₜ param
      (^∃ (domZero ^⋏ ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
        (iT.construction.exsChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero, IsSemiformula.exs, IsSemiformula.and]
    refine ⟨isSemiformula_domZero (n := param), ?_⟩
    exact ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])

end GodelQ.SeqTranslate
