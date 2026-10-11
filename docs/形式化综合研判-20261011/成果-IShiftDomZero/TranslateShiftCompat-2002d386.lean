import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（十一）：`iVE`/`shift` 跨语言的原子相容律

`hAll` / `hExs` / `hShift` 三支要 `iT` 与 `shift`/`setShift`/`substs1` 的相容律。
这不是平凡交换：`iVE`（`ℒₒᵣ` 项 → `ℒₛₑₜ` 公式）与 `termShift`（`ℒₒᵣ` 项移位）
对变量的处理不同——

| 运算 | 对 `^#z`（bvar） | 对 `^&x`（fvar） |
|---|---|---|
| `iVE` | `eqAtom (^#(z + 1))` —— 码加一（`eqAtom` 引入一个绑定层） | `eqAtom (^&x)` —— 不动 |
| `termShift` | `^#z` —— 不动 | `^&(x + 1)` —— 码加一 |

本文件给出**原子层**的两条相容律，即 `eqAtom` 与 `shift ℒₛₑₜ` 的交换：

* `shift_eqAtom_bvar`：`shift (eqAtom ^#z) = eqAtom ^#z`
* `shift_eqAtom_fvar`：`shift (eqAtom ^&x) = eqAtom ^&(x + 1)`

二者合起来说明：**`iVE` 送 bvar/fvar 到 `eqAtom`，而 `shift` 在两侧对
fvar 加一、对 bvar 不动——顺序恰好对上。** 这是拼出 `iT_shift` 的第一步。

## 证明要点

`eqAtom t = ^rel 2 cEqN (^#0 ∷ t ∷ 0)`，故 `shift` 走 `shift_rel`
（要 `(ℒₛₑₜ).IsRel 2 cEqN`，由 `codeIn_rel_quote` 给）配 `termShiftVec_cons₂`，
再把 `termShift_bvar` / `termShift_fvar` 代掉即可。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.TranslateShiftCompat

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `eqAtom t` 的向量（`^#0 ∷ t ∷ 0`）是 `ℒₛₑₜ` 的项向量，层数 2。 -/
lemma isUTermVec_eqAtom_vec (t : V) (ht : IsUTerm ℒₛₑₜ t) :
    IsUTermVec ℒₛₑₜ (2 : V) ((^#0 : V) ∷ (t ∷ (0 : V))) := by
  have hz : IsUTermVec ℒₛₑₜ (0 : V) (0 : V) := IsUTermVec.empty
  have hvec : IsUTermVec ℒₛₑₜ (1 : V) (t ∷ (0 : V)) := by
    simpa using (IsUTermVec.adjoin (L := ℒₛₑₜ) (n := (0 : V)) hz ht)
  have := IsUTermVec.adjoin (L := ℒₛₑₜ) (n := (1 : V)) hvec (IsUTerm.bvar (z := 0))
  rw [show (1 : V) + 1 = (2 : V) by norm_num] at this
  exact this

/-- **bvar 版**：`shift ℒₛₑₜ (eqAtom ^#z) = eqAtom ^#z`。

`termShift` 对 bvar 不动，而 `iVE` 的 bvar 支只把码加一（在 `eqAtom` 内部完成），
故 `shift` 作用后不变。 -/
lemma shift_eqAtom_bvar (z : V) :
    shift ℒₛₑₜ (eqAtom (^#z : V)) = eqAtom (^#z : V) := by
  show shift ℒₛₑₜ (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V))
  rw [shift_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^#z) (IsUTerm.bvar (z := z)))]
  congr 1
  rw [termShiftVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := z))]
  rw [termShift_bvar, termShift_bvar]

/-- **fvar 版**：`shift ℒₛₑₜ (eqAtom ^&x) = eqAtom ^&(x + 1)`。

`termShift` 对 fvar 把码加一，与 `iVE` 的 fvar 支（不动）合起来，
正好给出「自由变量码加一」。 -/
lemma shift_eqAtom_fvar (x : V) :
    shift ℒₛₑₜ (eqAtom (^&x : V)) = eqAtom (^&(x + 1) : V) := by
  show shift ℒₛₑₜ (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&x : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&(x + 1) : V) ∷ (0 : V))
  rw [shift_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^&x) (IsUTerm.fvar x))]
  congr 1
  rw [termShiftVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.fvar x)]
  rw [termShift_bvar, termShift_fvar]

/-! ## 与 `hAll`/`hExs`/`hShift` 的接口（2026-10-11 分析，尚未完成）

三支最终要的是 `translateSeq` 与 `setShift` 的交换：

```
hShift : s = setShift (fstIdx d)  ⟹  Derivable 𝗭𝗙𝗖 (translateSeq s)
ih     : Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))
```

由 `mem_translateSeq_iff`（`y ∈ translateSeq s ↔ ∃ x ∈ s, y = iT 0 x`）
逐元素看，这归结为

```
iT 0 (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT 0 p)          -- 记作 iT_shift
```

而 `iT_shift` 的原子支（`iT_rel` + `shift_rel`）归结为

```
iTR 0 k R (termShiftVec ℒₒᵣ k v) = shift ℒₛₑₜ (iTR 0 k R v)
```

`iTR` 只用 `v.[0]`、`v.[1]` 且经 `iVE`，所以再归结为**项层**的

```
iVE n (termShift t) = shift ℒₛₑₜ (iVE n t)        -- 记作 iVE_shift
```

本文件的 `shift_eqAtom_bvar`/`shift_eqAtom_fvar` 正是 `iVE_shift` 的
bvar/fvar 两支（`termShift_bvar`/`termShift_fvar` 分别对上
`iVE_bvar` 的加一与 `iVE_fvar` 的不动）。剩下的 `func` 支要用
`IsSemiterm.sigma1_induction`（`isSemiformula_iVE` 的先例），
并处理 `iVE.construction.resultVec` 与 `termShiftVec` 的相容。

**下一步顺序**：`iVE_shift`（用 sigma1_induction，func 支参照
`isSemiformula_iVE` 的 `nth_resultVec` 写法）→ `iT_shift` → `translateSeq_setShift`
→ `hShift` / `hAll` / `hExs`。`hExs` 另需 `iT_substs1`（同形）。
-/

/-! ## 项层的两支（bvar / fvar）

`iVE_shift`（`iVE n (termShift t) = shift ℒₛₑₜ (iVE n t)`）的两支已可直接拼出；
`func` 支仍需 `iVE.construction.resultVec` 与 `termShiftVec` 的相容，未做。 -/

/-- **`iVE_shift` 的 bvar 支**：`iVE n (termShift ^#z) = shift ℒₛₑₜ (iVE n ^#z)`。

`termShift` 不动 bvar，`iVE` 的 bvar 支给出 `eqAtom ^#(z+1)`，
再用 `shift_eqAtom_bvar`。 -/
lemma iVE_shift_bvar (n z : V) :
    iVE n (termShift ℒₒᵣ (^#z : V)) = shift ℒₛₑₜ (iVE n (^#z : V)) := by
  rw [termShift_bvar, iVE_bvar]
  exact (shift_eqAtom_bvar (z + 1)).symm

/-- **`iVE_shift` 的 fvar 支**：`iVE n (termShift ^&x) = shift ℒₛₑₜ (iVE n ^&x)`。

`termShift` 把 fvar 码加一，`iVE` 的 fvar 支给出 `eqAtom ^&x`，
再用 `shift_eqAtom_fvar`。 -/
lemma iVE_shift_fvar (n x : V) :
    iVE n (termShift ℒₒᵣ (^&x : V)) = shift ℒₛₑₜ (iVE n (^&x : V)) := by
  rw [termShift_fvar]
  simp only [iVE_fvar]
  exact (shift_eqAtom_fvar x).symm


/-! ## 引号化句子的码在 `shift` 下不变（2026-10-11 新增）

`cFunc`/`cDomN`/`cRel` 都是 `Semisentence ℒₛₑₜ` 的引号（ℕ 层），搬到 `V` 层后
在 `shift ℒₛₑₜ` 下不变——这是 `ve0`/`ve2` 支的地基。

关键：`Semiformula.quote_shift` 要 `Semiproposition`（`ξ = ℕ`），而 `cFuncN` 的码
在 `Semisentence`（`ξ = Empty`）层；两者的 `V` 层码由 `rfl` 相同，
故 `show` 改型即可用。 -/

lemma rew_shift_eq_self {n : ℕ} (φ : Semiproposition ℒₛₑₜ n)
    (hf : ∀ x, ¬ φ.FVar? x) : Rewriting.shift φ = φ :=
  Semiformula.rew_eq_self_of (by intro x; rfl)
    (by intro x hx; exact absurd hx (hf x))

lemma not_fvar_emb {n : ℕ} (σ : Semisentence ℒₛₑₜ n) (x : ℕ) :
    ¬ (σ : Semiproposition ℒₛₑₜ n).FVar? x := by
  intro hx
  have h := Semiformula.lt_fvSup_of_fvar? hx
  rw [Semiformula.fvSup_sentence] at h
  exact absurd h (by simp)

/-- **引号化的 `Semisentence` 的码在 `shift` 下不变**（`V` 层）。 -/
lemma shift_quote_sentence {n : ℕ} (σ : Semisentence ℒₛₑₜ n) :
    shift ℒₛₑₜ (⌜σ⌝ : V) = ⌜σ⌝ := by
  have h : Rewriting.shift (σ : Semiproposition ℒₛₑₜ n) = (σ : Semiproposition ℒₛₑₜ n) :=
    rew_shift_eq_self _ (not_fvar_emb σ)
  rw [show (⌜σ⌝ : V) = ⌜(σ : Semiproposition ℒₛₑₜ n)⌝ from rfl,
      ← Semiformula.quote_shift (V := V) (σ : Semiproposition ℒₛₑₜ n), h]

@[simp] lemma shift_cFuncN (k f : ℕ) :
    shift ℒₛₑₜ ((cFuncN k f : ℕ) : V) = ((cFuncN k f : ℕ) : V) := by
  simp only [cFuncN]
  split <;> split <;>
    · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote]
      exact shift_quote_sentence _

@[simp] lemma shift_cFunc (k f : V) : shift ℒₛₑₜ (cFunc k f) = cFunc k f := by
  simp only [cFunc]
  split <;> split <;> rw [shift_cFuncN]

@[simp] lemma shift_cDomN : shift ℒₛₑₜ ((cDomN : ℕ) : V) = ((cDomN : ℕ) : V) := by
  rw [show (cDomN : ℕ) = ⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝ from rfl,
      FFL.FirstOrder.Sentence.coe_quote_eq_quote]
  exact shift_quote_sentence _

@[simp] lemma shift_cRelN (R : ℕ) :
    shift ℒₛₑₜ ((cRelN R : ℕ) : V) = ((cRelN R : ℕ) : V) := by
  simp only [cRelN]
  split <;>
    · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote]
      exact shift_quote_sentence _

@[simp] lemma shift_cRel (R : V) : shift ℒₛₑₜ (cRel R) = cRel R := by
  simp only [cRel]
  split <;> rw [shift_cRelN]

/-! ## `shiftVec` 的项层性质

`shiftVec b n = [^#b, …, ^#(b+n-1)]` 全是 bvar，故 `termShift` 不动它。 -/

lemma nth_shiftVec (b : V) : ∀ n : V, ∀ i < n, (shiftVec b n).[i] = ^#(b + i) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => intro i hi; exact absurd hi (by simp)
  case succ n ih =>
    intro i hi
    rw [shiftVec_succ]
    rcases zero_or_succ i with rfl | ⟨j, rfl⟩
    · simp
    · rw [nth_adjoin_succ]
      have hj : j < n := (add_lt_add_iff_right (a := (1 : V)) (b := j) (c := n)).mp hi
      rw [nth_termBShiftVec (isSemitermVec_shiftVec_V b n).isUTerm hj, ih j hj, termBShift_bvar]
      congr 1
      ring

@[simp] lemma termShiftVec_shiftVec_V (b n : V) :
    termShiftVec ℒₛₑₜ n (shiftVec b n) = shiftVec b n := by
  apply nth_ext' n
  · rw [len_termShiftVec (isSemitermVec_shiftVec_V b n).isUTerm]
  · exact (isSemitermVec_shiftVec_V b n).lh
  · intro i hi
    rw [nth_termShiftVec (isSemitermVec_shiftVec_V b n).isUTerm hi, nth_shiftVec b n i hi,
      termShift_bvar]

lemma isSemitermVec_shiftVec_cons {b n i : V} (hi : i < b + n) :
    IsSemitermVec ℒₛₑₜ (n + 1) (b + n) (^#i ∷ shiftVec b n) :=
  IsSemitermVec.cons_iff.mpr ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec_V b n⟩

/-! ## `conjunct` 与 `shift` 交换 -/

lemma shift_conjunct {b n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y)
    (hi : i < b + n) :
    shift ℒₛₑₜ (conjunct b n i y) = conjunct b n i (shift ℒₛₑₜ y) := by
  have hd : IsSemiformula ℒₛₑₜ 1 ((cDomN : ℕ) : V) := isSemiformula_cDomN
  have h1 : shift ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V) := by
    rw [Bootstrapping.shift_substs hd (isSemitermVec_single_bvar (n := i + 1) (by simp)),
      show (termShiftVec ℒₛₑₜ 1 (?[^#i] : V)) = ?[^#i] from by
        rw [show (1 : V) = 0 + 1 by norm_num,
          termShiftVec_cons (IsUTerm.bvar (z := i)) IsUTermVec.empty,
          termShift_bvar, termShiftVec_nil],
      shift_cDomN]
  have h2 : shift ℒₛₑₜ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)
      = subst ℒₛₑₜ (^#i ∷ shiftVec b n) (shift ℒₛₑₜ y) := by
    rw [Bootstrapping.shift_substs hy (isSemitermVec_shiftVec_cons hi),
      show (termShiftVec ℒₛₑₜ (n + 1) (^#i ∷ shiftVec b n)) = ^#i ∷ shiftVec b n from by
        rw [termShiftVec_cons (IsUTerm.bvar (z := i)) (isSemitermVec_shiftVec_V b n).isUTerm,
          termShift_bvar, termShiftVec_shiftVec_V]]
  have h1u : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hd
      (isSemitermVec_single_bvar (n := i + 1) (by simp))).isUFormula
  have h2u : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hy (isSemitermVec_shiftVec_cons hi)).isUFormula
  show shift ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)
      = subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (^#i ∷ shiftVec b n) (shift ℒₛₑₜ y)
  rw [Bootstrapping.shift_and h1u h2u, h1, h2]

/-! ## `ve0`/`ve2`/`qqAlls` 与 `shift` 交换 -/

/-- `ve0 0 f` 在 `shift` 下不变（`cFunc` 的码是引号化句子）。 -/
@[simp] lemma shift_ve0 (f : V) : shift ℒₛₑₜ (ve0 0 f) = ve0 0 f := by
  have hc : IsSemiformula ℒₛₑₜ 1 (cFunc 0 f) := isSemiformula_cFunc_arity0 f
  have hv : IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := 1) (by simp)
  have hs : IsSemiformula ℒₛₑₜ 1 (subst ℒₛₑₜ ?[^#0] (cFunc 0 f)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) hc hv
  rw [ve0, imp]
  rw [Bootstrapping.shift_or (IsUFormula.neg IsUFormula.verum) hs.isUFormula,
      Bootstrapping.shift_neg (n := 1) IsSemiformula.verum, shift_verum,
      Bootstrapping.shift_substs hc hv]
  rw [show (termShiftVec ℒₛₑₜ 1 (?[^#0] : V)) = ?[^#0] from by
        rw [show (1 : V) = 0 + 1 by norm_num,
          termShiftVec_cons (IsUTerm.bvar (z := 0)) IsUTermVec.empty,
          termShift_bvar, termShiftVec_nil],
      shift_cFunc]

/-- `qqAlls` 与 `shift` 交换（逐层加量词）。 -/
lemma shift_qqAlls {p k : V} (hp : IsUFormula ℒₛₑₜ p) :
    shift ℒₛₑₜ (qqAlls p k) = qqAlls (shift ℒₛₑₜ p) k := by
  induction k using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ k ih =>
    rw [qqAlls_succ, qqAlls_succ, Bootstrapping.shift_all (isUFormula_qqAlls.mpr hp), ih]

/-! ## 三元 bvar 向量与 `subst (^#2 ∷ ?[#0, #1]) (cFunc k f)` -/

lemma isUTermVec_three_bvars :
    IsUTermVec ℒₛₑₜ 3 ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
  ⟨by simp [show (3 : V) = 1 + 1 + 1 by norm_num], fun i hi ↦ by
    have hle : i ≤ 2 := lt_succ_iff_le.mp (by
      simpa [show (3 : V) = 2 + 1 by norm_num] using hi)
    rcases le_two_iff_eq_zero_or_one_or_two.mp hle with rfl | rfl | rfl <;> simp [IsUTerm.bvar]⟩

lemma termShiftVec_three_bvars :
    termShiftVec ℒₛₑₜ 3 ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V))
      = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) := by
  apply nth_ext' 3
  · rw [len_termShiftVec isUTermVec_three_bvars]
  · simp [show (3 : V) = 1 + 1 + 1 by norm_num]
  · intro i hi
    rw [nth_termShiftVec isUTermVec_three_bvars hi]
    have hle : i ≤ 2 := lt_succ_iff_le.mp (by
      simpa [show (3 : V) = 2 + 1 by norm_num] using hi)
    rcases le_two_iff_eq_zero_or_one_or_two.mp hle with rfl | rfl | rfl <;> simp [termShift_bvar]

lemma isSemitermVec_three_bvars (n : V) :
    IsSemitermVec ℒₛₑₜ 3 (3 + n) ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) := by
  rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
      simpa [show (3 : V) = 2 + 1 by norm_num, add_assoc] using two_lt_three_add n), ?_⟩
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
      simpa [show (3 : V) = 1 + 1 + 1 by norm_num, add_assoc] using zero_lt_three_add n), ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.bvar.mpr (by
      simpa [show (3 : V) = 1 + 1 + 1 by norm_num, add_assoc] using one_lt_three_add n),
    by simp⟩

lemma shift_subst_cFunc {n k f : V} (hk : k ≠ 0) :
    shift ℒₛₑₜ (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f))
      = subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f) := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc k f) := isSemiformula_cFunc_arity2 hk f
  rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
  rw [Bootstrapping.shift_substs hc (isSemitermVec_three_bvars n),
      termShiftVec_three_bvars, shift_cFunc]

/-- **`ve2` 与 `shift` 交换**。`w'` 是 `w` 的逐分量 `shift`。 -/
lemma shift_ve2 {n k f w w' : V} (hk : k ≠ 0)
    (hw0 : IsSemiformula ℒₛₑₜ (n + 1) w.[0])
    (hw1 : IsSemiformula ℒₛₑₜ (n + 1) w.[1])
    (hw'0 : w'.[0] = shift ℒₛₑₜ w.[0])
    (hw'1 : w'.[1] = shift ℒₛₑₜ w.[1]) :
    shift ℒₛₑₜ (ve2 n k f w) = ve2 n k f w' := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc k f) := isSemiformula_cFunc_arity2 hk f
  have hB : IsSemiformula ℒₛₑₜ (3 + n)
      (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)) := by
    rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
    exact IsSemiformula.subst (L := ℒₛₑₜ) hc (isSemitermVec_three_bvars n)
  have hA0 : IsSemiformula ℒₛₑₜ (3 + n) (conjunct 3 n 0 w.[0]) :=
    isSemiformula_conjunct (b := 3) (n := n) (i := 0) hw0 (zero_lt_three_add n)
  have hA1 : IsSemiformula ℒₛₑₜ (3 + n) (conjunct 3 n 1 w.[1]) :=
    isSemiformula_conjunct (b := 3) (n := n) (i := 1) hw1 (one_lt_three_add n)
  have hA01 : IsSemiformula ℒₛₑₜ (3 + n) (conjunct 3 n 1 w.[1] ^⋏ ^⊤) :=
    IsSemiformula.and.mpr ⟨hA1, IsSemiformula.verum⟩
  have hA : IsSemiformula ℒₛₑₜ (3 + n)
      (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hA0, hA01⟩
  have hsa : shift ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
      = conjunct 3 n 0 w'.[0] ^⋏ (conjunct 3 n 1 w'.[1] ^⋏ ^⊤) := by
    rw [Bootstrapping.shift_and hA0.isUFormula hA01.isUFormula,
      Bootstrapping.shift_and hA1.isUFormula IsUFormula.verum,
      shift_conjunct (b := 3) (n := n) (i := 0) hw0 (zero_lt_three_add n),
      shift_conjunct (b := 3) (n := n) (i := 1) hw1 (one_lt_three_add n),
      shift_verum, hw'0, hw'1]
  have hsb : shift ℒₛₑₜ (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f))
      = subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f) := shift_subst_cFunc (n := n) hk
  have hbody : IsUFormula ℒₛₑₜ
      (neg ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)) :=
    IsUFormula.or.mpr ⟨hA.isUFormula.neg, hB.isUFormula⟩
  have hgoal : shift ℒₛₑₜ (qqAlls (neg ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)) 2)
      = qqAlls (neg ℒₛₑₜ (conjunct 3 n 0 w'.[0] ^⋏ (conjunct 3 n 1 w'.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)) 2 := by
    rw [shift_qqAlls hbody,
      Bootstrapping.shift_or hA.isUFormula.neg hB.isUFormula,
      Bootstrapping.shift_neg (n := 3 + n) hA, hsa, hsb]
  rw [ve2]
  show shift ℒₛₑₜ (qqAlls (imp ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
      (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f))) 2) = _
  rw [show (imp ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
            (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)))
        = neg ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
          ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f) from rfl]
  rw [hgoal]
  rw [ve2]
  rw [show (imp ℒₛₑₜ (conjunct 3 n 0 w'.[0] ^⋏ (conjunct 3 n 1 w'.[1] ^⋏ ^⊤))
            (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)))
        = neg ℒₛₑₜ (conjunct 3 n 0 w'.[0] ^⋏ (conjunct 3 n 1 w'.[1] ^⋏ ^⊤))
          ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f) from rfl]

/-! ## `iVE_shift` 的 `func` 支与全称版本 -/

/-- **`iVE_shift` 的 `func` 支**：`iVE` 与 `termShift` 交换。

`termShift` 只改 `ℒₒᵣ` 侧的项（fvar 加一），`iVE` 把它送到 `ℒₛₑₜ` 的
`eqAtom`；`shift ℒₛₑₜ` 在 `ℒₛₑₜ` 侧对 fvar 也加一，故两条路一致。 -/
lemma iVE_shift_func {n k f v : V} (hkf : (ℒₒᵣ).IsFunc k f)
    (hv : IsSemitermVec ℒₒᵣ k n v)
    (ih : ∀ i < k, iVE n (termShift ℒₒᵣ v.[i]) = shift ℒₛₑₜ (iVE n v.[i])) :
    iVE n (termShift ℒₒᵣ (^func k f v)) = shift ℒₛₑₜ (iVE n (^func k f v)) := by
  rw [termShift_func hkf hv.isUTerm]
  rw [iVE_func hkf hv.termShiftVec.isUTerm, iVE_func hkf hv.isUTerm]
  by_cases hk : k = 0
  · subst hk
    simp only [ite_true]
    exact (shift_ve0 f).symm
  · have hk2 : k = 2 := k_eq_two_of_func hkf hk
    subst hk2
    simp only [show (2 : V) ≠ 0 by norm_num, if_false]
    refine (shift_ve2 (n := n) (k := 2) (f := f)
      (w := iVE.construction.resultVec ℒₒᵣ ![n] 2 v)
      (w' := iVE.construction.resultVec ℒₒᵣ ![n] 2 (termShiftVec ℒₒᵣ 2 v))
      (by norm_num) ?_ ?_ ?_ ?_).symm
    · rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (0 : V) < 2 by norm_num)]
      exact isSemiformula_iVE (n := n) v.[0] (hv.nth (i := 0) (by norm_num))
    · rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (1 : V) < 2 by norm_num)]
      exact isSemiformula_iVE (n := n) v.[1] (hv.nth (i := 1) (by norm_num))
    · rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.termShiftVec.isUTerm
            (show (0 : V) < 2 by norm_num),
          iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (0 : V) < 2 by norm_num),
          nth_termShiftVec hv.isUTerm (show (0 : V) < 2 by norm_num)]
      exact ih 0 (by norm_num)
    · rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.termShiftVec.isUTerm
            (show (1 : V) < 2 by norm_num),
          iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (1 : V) < 2 by norm_num),
          nth_termShiftVec hv.isUTerm (show (1 : V) < 2 by norm_num)]
      exact ih 1 (by norm_num)

/-- **`iVE` 与 `termShift` 的跨语言相容律**（一般项 `t`，层数 `n`）。

`termShift` 改 `ℒₒᵣ` 侧的 fvar（加一），`iVE` 送 fvar 到 `eqAtom ^&x` 不动；
`shift ℒₛₑₜ` 在 `ℒₛₑₜ` 侧对 fvar 也加一。bvar 两侧都不动。
故两条路一致——这是 `iT_shift` 的项层地基。 -/
theorem iVE_shift (n : V) : ∀ t, IsSemiterm ℒₒᵣ n t →
    iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := n)
    (P := fun t ↦ iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t))
  · definability
  · intro z hz
    exact iVE_shift_bvar n z
  · intro x
    exact iVE_shift_fvar n x
  · intro k f v hkf hv ih
    exact iVE_shift_func hkf hv ih


end GodelQ.TranslateShiftCompat

#print axioms GodelQ.TranslateShiftCompat.isUTermVec_eqAtom_vec
#print axioms GodelQ.TranslateShiftCompat.shift_eqAtom_bvar
#print axioms GodelQ.TranslateShiftCompat.shift_eqAtom_fvar
#print axioms GodelQ.TranslateShiftCompat.iVE_shift_bvar
#print axioms GodelQ.TranslateShiftCompat.iVE_shift_fvar
#print axioms GodelQ.TranslateShiftCompat.shift_quote_sentence
#print axioms GodelQ.TranslateShiftCompat.shift_cFunc
#print axioms GodelQ.TranslateShiftCompat.shift_cDomN
#print axioms GodelQ.TranslateShiftCompat.shift_cRel
#print axioms GodelQ.TranslateShiftCompat.termShiftVec_shiftVec_V
#print axioms GodelQ.TranslateShiftCompat.shift_conjunct
#print axioms GodelQ.TranslateShiftCompat.shift_ve0
#print axioms GodelQ.TranslateShiftCompat.shift_qqAlls
#print axioms GodelQ.TranslateShiftCompat.shift_ve2
#print axioms GodelQ.TranslateShiftCompat.iVE_shift_func
#print axioms GodelQ.TranslateShiftCompat.iVE_shift
