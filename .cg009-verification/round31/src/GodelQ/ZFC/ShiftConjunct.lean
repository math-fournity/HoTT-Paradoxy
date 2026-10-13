import GodelQ.ZFC.ShiftTools

/-!
# CG-007 · W8 第二层（十四）：`shift` 与 `conjunct`/`ve2` 的相容律

`iVE_shift` 的 func 支（`k ≠ 0`，即 `ve2`）需要 `shift` 与 `ve2` 各组成部分相容；
`iT_shift` 的 rel/nrel 支再复用其中的合取块部分。本文件把这条链补齐：

1. `shift_subst_cDomN`：`subst ?[^#i] cDomN` 在 `shift` 下不动（`cDomN` 是句子引号）；
2. `termBShiftVec_termShiftVec` / `termShiftVec_shiftVec`：`termShiftVec` 与
   `termBShiftVec` 点相容，故 `termShiftVec` 固定 `shiftVec b n`（**任意 V 元素** `n`，
   走 `sigma1_succ_induction`——`isSemitermVec_shiftVec_V` 的先例）；
3. `shift_qqAlls`：`shift` 与叠合量词 `qqAlls` 交换；
4. `shift_conjunct`：`shift (conjunct b n i y) = conjunct b n i (shift y)`；
5. `shift_cFunc` / `shift_cRel` 与两条闭代换不变律：引号在 `shift` 下不动；
6. `shift_and_pair` / `shift_ve2`：`ve2` 整块的成品（`iTR` 的相容律在
   `IVeShift.lean` 的 `iTR_shift`，因为 `iTR` 体内要用 `iVE_shift`）。

## 参数序（先前反复出错处，已用类型探针确认）

- `IsSemitermVec L k n v`：`k` = **向量长度**，`n` = **层数**。
- `shift_substs (hp : IsSemiformula L n p) : IsSemitermVec L n m w → ...`：
  这里 `n` 是**长度**、`m` 是**层数**——与 `IsSemitermVec` 的定义顺序**相反**。
  故 `shift_substs` 的 `(n := 1) (m := 1)` 表示「长度 1、层数 1」。

`conjunct b n i y = (subst ?[^#i] cDomN) ^⋏ (subst (^#i ∷ shiftVec b n) y)`：
第一项闭（`cDomN` 是 `Semisentence ℒₛₑₜ 1` 的引号），第二项含 `y`；
`shiftVec b n = bvs b n = [#b, #(b+1), …]` 全是 bvar，`termShiftVec` 不动它。
-/

set_option maxHeartbeats 4000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ShiftTools

namespace GodelQ.ShiftConjunct

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 1. `subst ?[^#i] cDomN` 在 `shift` 下不动 -/

/-- `subst ?[^#i] cDomN` 在 `shift` 下不动（`cDomN` 是句子引号，代换后仍闭）。

`i` 只受「作为层 `m` 的项」这一条件约束，故 `i < m` 即可（`i < 1` 是旧版）。 -/
lemma shift_subst_cDomN {i m : V} (hi : i < m) :
    shift (L := ℒₛₑₜ) (subst ℒₛₑₜ (?[^#i] : V) (cDomN : V)) =
      subst ℒₛₑₜ (?[^#i] : V) (cDomN : V) := by
  rw [shift_substs (L := ℒₛₑₜ) (n := 1) (m := m) (p := (cDomN : V))
    (isSemiformula_cDomN)
    (isSemitermVec_single_bvar hi)]
  congr 1
  · rw [show (1 : V) = 0 + 1 by norm_num,
      termShiftVec_cons (ht := IsUTerm.bvar) (hts := IsUTermVec.empty)]
    rw [termShift_bvar, termShiftVec_nil]
  · rw [cDomN_eq]
    exact GodelQ.ShiftTools.shift_quote _

/-! ## 2. 向量层：`termShiftVec` 与 `termBShiftVec` 交换 -/

/-- `termShiftVec` 与 `termBShiftVec` 交换（点相容 + `nth_ext'`）。

逐分量看就是 `termBShift_termShift`（项层交换律）。 -/
lemma termBShiftVec_termShiftVec {k v : V} (hv : IsUTermVec ℒₛₑₜ k v) :
    termShiftVec ℒₛₑₜ k (termBShiftVec ℒₛₑₜ k v) =
      termBShiftVec ℒₛₑₜ k (termShiftVec ℒₛₑₜ k v) := by
  apply nth_ext' k
  · rw [len_termShiftVec hv.termBShiftVec]
  · rw [len_termBShiftVec hv.termShiftVec]
  · intro i hi
    rw [nth_termShiftVec hv.termBShiftVec hi, nth_termBShiftVec hv hi,
      nth_termBShiftVec hv.termShiftVec hi, nth_termShiftVec hv hi,
      termBShift_termShift (IsUTerm.isSemiterm (hv.nth hi))]

/-- `termShiftVec` 固定 `shiftVec b n`（全是 bvar），对**任意 V 元素** `n`。 -/
lemma termShiftVec_shiftVec (b : V) : ∀ n : V,
    termShiftVec ℒₛₑₜ n (shiftVec b n) = shiftVec b n := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ n ih =>
    rw [shiftVec_succ,
      termShiftVec_cons (ht := IsUTerm.bvar (z := b))
        (hts := (isSemitermVec_shiftVec_V b n).isUTerm.termBShiftVec),
      termShift_bvar, termBShiftVec_termShiftVec (isSemitermVec_shiftVec_V b n).isUTerm, ih]

/-! ## 3. `shift` 与叠合量词交换 -/

/-- `shift` 与叠合量词 `qqAlls` 交换。 -/
lemma shift_qqAlls {p k : V} (hp : IsUFormula ℒₛₑₜ p) :
    shift ℒₛₑₜ (qqAlls p k) = qqAlls (shift ℒₛₑₜ p) k := by
  induction k using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ k ih =>
    rw [qqAlls_succ, shift_all (isUFormula_qqAlls.mpr hp), ih, qqAlls_succ]

/-! ## 4. 合取块与 `shift` 相容 -/

/-- **合取块与 `shift` 相容**：`shift (conjunct b n i y) = conjunct b n i (shift y)`。

第一项走 `shift_subst_cDomN`，第二项走 `shift_substs` + `termShiftVec_shiftVec`。 -/
lemma shift_conjunct {b n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y) (hi : i < b + n) :
    shift ℒₛₑₜ (conjunct b n i y) = conjunct b n i (shift ℒₛₑₜ y) := by
  have hvec : IsSemitermVec ℒₛₑₜ (n + 1) (b + n) (^#i ∷ shiftVec b n) := by
    rw [IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec_V b n⟩
  have hA : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#i] : V) (cDomN : V)) :=
    (IsSemiformula.subst isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := b + n) hi)).isUFormula
  have hB : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y) :=
    (IsSemiformula.subst hy hvec).isUFormula
  rw [conjunct, shift_and hA hB, shift_subst_cDomN hi, shift_substs hy hvec]
  congr 1
  rw [termShiftVec_cons (ht := IsUTerm.bvar) (hts := (isSemitermVec_shiftVec_V b n).isUTerm),
    termShift_bvar, termShiftVec_shiftVec b n]

/-- 合取对 `shift` 的分配律（`y0 ⋏ (y1 ⋏ ⊤)` 形状，`ve2`/`iTR` 的共同体）。 -/
lemma shift_and_pair {y0 y1 : V} (h0 : IsUFormula ℒₛₑₜ y0) (h1 : IsUFormula ℒₛₑₜ y1) :
    shift ℒₛₑₜ (y0 ^⋏ (y1 ^⋏ ^⊤)) = shift ℒₛₑₜ y0 ^⋏ (shift ℒₛₑₜ y1 ^⋏ ^⊤) := by
  rw [shift_and h0 (IsUFormula.and.mpr ⟨h1, IsUFormula.verum⟩),
    shift_and h1 IsUFormula.verum, shift_verum]

/-! ## 5. 引号与闭代换不动 -/

/-- `shift` 固定 `cFunc k f`（函数定义公式的编码，是引号）。

四个分支都是 `↑⌜σ⌝`（`σ : Semisentence ℒₛₑₜ n`），故 `coe_quote_eq_quote` 归到
V 层引号再走 `shift_quote`。`k = 0` 分支与 `ShiftTools.shift_cFunc0` 同形。 -/
lemma shift_cFunc (k f : V) : shift ℒₛₑₜ (cFunc k f) = cFunc k f := by
  rw [cFunc]
  split
  · split
    · rw [cFuncN, if_pos rfl, if_pos rfl, Sentence.coe_quote_eq_quote]
      exact GodelQ.ShiftTools.shift_quote _
    · rw [cFuncN, if_pos rfl, if_neg (by decide : ¬(1:ℕ) = 0), Sentence.coe_quote_eq_quote]
      exact GodelQ.ShiftTools.shift_quote _
  · split
    · rw [cFuncN, if_neg (by decide : ¬(2:ℕ) = 0), if_pos rfl, Sentence.coe_quote_eq_quote]
      exact GodelQ.ShiftTools.shift_quote _
    · rw [cFuncN, if_neg (by decide : ¬(2:ℕ) = 0), if_neg (by decide : ¬(1:ℕ) = 0),
        Sentence.coe_quote_eq_quote]
      exact GodelQ.ShiftTools.shift_quote _

/-- `shift` 固定 `cRel R`（关系定义公式的编码，是引号）。 -/
lemma shift_cRel (R : V) : shift ℒₛₑₜ (cRel R) = cRel R := by
  rw [cRel]
  split
  · rw [cRelN, if_pos rfl, Sentence.coe_quote_eq_quote]
    exact GodelQ.ShiftTools.shift_quote _
  · rw [cRelN, if_neg (by decide : ¬(1:ℕ) = 0), Sentence.coe_quote_eq_quote]
    exact GodelQ.ShiftTools.shift_quote _

/-- `?[^#0, ^#1]` 是 `ℒₛₑₜ` 的项向量（长度 2）。 -/
lemma isUTermVec_v01 : IsUTermVec ℒₛₑₜ 2 (?[^#0, ^#1] : V) := by
  have h1 : IsUTermVec ℒₛₑₜ 1 (^#1 ∷ (0 : V)) := by
    simpa using (IsUTermVec.adjoin (L := ℒₛₑₜ) (n := 0) IsUTermVec.empty (IsUTerm.bvar (z := 1)))
  simpa using (IsUTermVec.adjoin (L := ℒₛₑₜ) (n := 1) h1 (IsUTerm.bvar (z := 0)))

/-- `termShiftVec` 固定 `?[^#0, ^#1]`。 -/
lemma termShiftVec_v01 : termShiftVec ℒₛₑₜ 2 (?[^#0, ^#1] : V) = (?[^#0, ^#1] : V) := by
  rw [termShiftVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := 1)),
    termShift_bvar, termShift_bvar]

/-- `?[^#0, ^#1]` 是层 2 的项向量。 -/
lemma isSemitermVec_v01 : IsSemitermVec ℒₛₑₜ 2 2 (?[^#0, ^#1] : V) := by
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩

/-- `^#2 ∷ ?[^#0, ^#1]` 是层 3 的项向量。 -/
lemma isSemitermVec_sve2 : IsSemitermVec ℒₛₑₜ 3 3 (^#2 ∷ ?[^#0, ^#1] : V) := by
  rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩

/-- `termShiftVec` 固定 `^#2 ∷ ?[^#0, ^#1]`。 -/
lemma termShiftVec_sve2 :
    termShiftVec ℒₛₑₜ 3 (^#2 ∷ ?[^#0, ^#1] : V) = (^#2 ∷ ?[^#0, ^#1] : V) := by
  rw [show (3 : V) = 2 + 1 by norm_num,
    termShiftVec_cons (ht := IsUTerm.bvar (z := 2)) (hts := isUTermVec_v01),
    termShift_bvar, termShiftVec_v01]

/-- 闭代换 `subst (^#2 ∷ ?[^#0, ^#1]) (cFunc k f)` 在 `shift` 下不动（`ve2` 的结论项）。 -/
lemma shift_subst_cFunc_closed {k : V} (hk : k ≠ 0) (f : V) :
    shift ℒₛₑₜ (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc k f)) =
      subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc k f) := by
  rw [shift_substs (n := 3) (m := 3) (p := cFunc k f)
    (isSemiformula_cFunc_arity2 hk f) isSemitermVec_sve2]
  congr 1
  · exact termShiftVec_sve2
  · exact shift_cFunc k f

/-- 闭代换 `subst ?[^#0, ^#1] (cRel R)` 在 `shift` 下不动（`iTR` 的结论项）。 -/
lemma shift_subst_cRel_closed (R : V) :
    shift ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) =
      subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R) := by
  rw [shift_substs (n := 2) (m := 2) (p := cRel R) (isSemiformula_cRel R) isSemitermVec_v01]
  congr 1
  · exact termShiftVec_v01
  · exact shift_cRel R

/-! ## 6. `ve2` 整块 -/

/-- **`ve2` 与 `shift` 相容**（任意向量 `w`；`ve2` 只读 `w.[0]`、`w.[1]`）。

`shift` 穿透叠合量词与蕴涵；合取块走 `shift_conjunct`，闭代换项走
`shift_subst_cFunc_closed`。 -/
lemma shift_ve2 {n k f w : V} (hk : k ≠ 0)
    (h0 : IsSemiformula ℒₛₑₜ (n + 1) w.[0]) (h1 : IsSemiformula ℒₛₑₜ (n + 1) w.[1]) :
    shift ℒₛₑₜ (ve2 n k f w) =
      ve2 n k f (?[shift ℒₛₑₜ w.[0], shift ℒₛₑₜ w.[1]] : V) := by
  have hc0 : IsUFormula ℒₛₑₜ (conjunct 3 n 0 w.[0]) :=
    (isSemiformula_conjunct h0 (zero_lt_three_add n)).isUFormula
  have hc1 : IsUFormula ℒₛₑₜ (conjunct 3 n 1 w.[1]) :=
    (isSemiformula_conjunct h1 (one_lt_three_add n)).isUFormula
  have hA : IsUFormula ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤)) :=
    IsUFormula.and.mpr ⟨hc0, IsUFormula.and.mpr ⟨hc1, IsUFormula.verum⟩⟩
  have hB : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc k f)) :=
    (IsSemiformula.subst (isSemiformula_cFunc_arity2 hk f) isSemitermVec_sve2).isUFormula
  simp only [ve2, nth_adjoin_zero, nth_adjoin_one]
  rw [shift_qqAlls (IsUFormula.imp.mpr ⟨hA, hB⟩), shift_imp hA hB, shift_and_pair hc0 hc1,
    shift_conjunct h0 (zero_lt_three_add n), shift_conjunct h1 (one_lt_three_add n),
    shift_subst_cFunc_closed hk f]

end GodelQ.ShiftConjunct

#print axioms GodelQ.ShiftConjunct.shift_subst_cDomN
#print axioms GodelQ.ShiftConjunct.termBShiftVec_termShiftVec
#print axioms GodelQ.ShiftConjunct.termShiftVec_shiftVec
#print axioms GodelQ.ShiftConjunct.shift_qqAlls
#print axioms GodelQ.ShiftConjunct.shift_conjunct
#print axioms GodelQ.ShiftConjunct.shift_and_pair
#print axioms GodelQ.ShiftConjunct.shift_cFunc
#print axioms GodelQ.ShiftConjunct.shift_cRel
#print axioms GodelQ.ShiftConjunct.isUTermVec_v01
#print axioms GodelQ.ShiftConjunct.termShiftVec_v01
#print axioms GodelQ.ShiftConjunct.isSemitermVec_v01
#print axioms GodelQ.ShiftConjunct.isSemitermVec_sve2
#print axioms GodelQ.ShiftConjunct.termShiftVec_sve2
#print axioms GodelQ.ShiftConjunct.shift_subst_cFunc_closed
#print axioms GodelQ.ShiftConjunct.shift_subst_cRel_closed
#print axioms GodelQ.ShiftConjunct.shift_ve2
