import GodelQ.ZFC.ITShift
import GodelQ.ZFC.ShiftConjunct

/-!
# CG-007 · W8 第二层（十七）：`iT` 与变量代换的相容律

`hAll` 支需要：把 `iT 1 q` 的自由变量换成 `^&0`（即 `free`/`substs1` 所做的事），
等价于先把 `q` 的自由变量换掉再以层 0 翻译：

```
subst ℒₛₑₜ ?[^&0] (iT 1 q) = iT 0 (termSubst ℒₒᵣ ?[^&0] q)      -- 桥（本文件的目标）
```

`q` 层 1。**机制**：`iVE m ^#z = eqAtom ^#(z+1)`——`iVE` 把 bvar 索引整体加一，
而 `free` 用的向量 `?[^&0]` 在两层量词（`iTR` 的 `qqAlls _ 2`）下长成
`qVec (qVec ?[^&0]) = [#0, #1, ^&0]`——末位的 `^&0` 正好落进被换名的槽。

本文件先证**项层子律 T1**（`t` 层 1）：

```
subst (^#a ∷ ?[^&0]) (iVE 1 t) = subst ?[^#a] (iVE 0 (subst ?[^&0] t))
```

bvar/fvar 支直接算；func 支分 `k = 0`（`ve0`，走 `substs_substs`）与
`k = 2`（`ve2`，走 `subst_qqAlls_two`/`subst_conjunct` + 归纳假设）。

## 陷阱（本会话踩过两次）

`qVec` 用 `termBShift`（bvar **+1**、fvar **不动**），不是 `termShift`（fvar +1）。
按 `termShift` 手算会得出「桥不成立」的**假反例**：实测 `qVec ?[^&0] = [#0, ^&0]`。
-/

set_option maxHeartbeats 8000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 向量工具 -/

lemma len_f0 : len (V := V) (?[^&0] : V) = 1 := by
  rw [len_adjoin]; norm_num

lemma qVec_f0 : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  simp [qVec, len_f0, termBShiftVec_cons, termBShiftVec_nil, termBShift_fvar]

lemma qVec_qVec_f0 : qVec ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) = (?[^#0, ^#1, ^&0] : V) := by
  simp [qVec, len_f0, len_adjoin, termBShiftVec_cons, termBShiftVec_nil,
    termBShift_bvar, termBShift_fvar]

lemma qVec_a0 (a : V) : qVec ℒₛₑₜ (^#a ∷ ?[^&0] : V) = (?[^#0, ^#(a + 1), ^&0] : V) := by
  simp [qVec, len_adjoin, len_f0, termBShiftVec_cons, termBShiftVec_nil,
    termBShift_bvar, termBShift_fvar]

lemma qVec_qVec_a0 (a : V) :
    qVec ℒₛₑₜ (qVec ℒₛₑₜ (^#a ∷ ?[^&0] : V)) = (?[^#0, ^#1, ^#(a + 2), ^&0] : V) := by
  simp [qVec, len_adjoin, len_f0, termBShiftVec_cons, termBShiftVec_nil,
    termBShift_bvar, termBShift_fvar]
  ring_nf

lemma qVec_a (a : V) : qVec ℒₛₑₜ (?[^#a] : V) = (?[^#0, ^#(a + 1)] : V) := by
  simp [qVec, len_adjoin, termBShiftVec_cons, termBShiftVec_nil, termBShift_bvar]

lemma qVec_qVec_a (a : V) :
    qVec ℒₛₑₜ (qVec ℒₛₑₜ (?[^#a] : V)) = (?[^#0, ^#1, ^#(a + 2)] : V) := by
  simp [qVec, len_adjoin, termBShiftVec_cons, termBShiftVec_nil, termBShift_bvar]
  ring_nf

/-- `qqAlls p 2 = ^∀ (^∀ p)`。 -/
lemma qqAlls_two (p : V) : qqAlls p 2 = (^∀ (^∀ p) : V) := by
  rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ,
    show (1 : V) = 0 + 1 by norm_num, qqAlls_succ, qqAlls_zero]

/-- `subst` 穿过两层 `qqAlls`：向量变 `qVec (qVec w)`。 -/
lemma subst_qqAlls_two {p w : V} (hp : IsUFormula ℒₛₑₜ p) :
    subst ℒₛₑₜ w (qqAlls p 2) = qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) p) 2 := by
  rw [qqAlls_two p, substs_all (IsUFormula.all.mpr hp), substs_all hp, qqAlls_two]

/-- `subst` 与 `imp` 相容。 -/
lemma subst_imp {n p q m w : V} (hp : IsSemiformula ℒₛₑₜ n p) (hq : IsSemiformula ℒₛₑₜ n q)
    (hw : IsSemitermVec ℒₛₑₜ n m w) :
    subst ℒₛₑₜ w (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (subst ℒₛₑₜ w p) (subst ℒₛₑₜ w q) := by
  rw [imp, imp, substs_or hp.neg.isUFormula hq.isUFormula]
  congr 1
  exact substs_neg hp hw

/-- `subst` 穿过合取块（`conjunct`）。 -/
lemma subst_conjunct {b n i y m w : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y) (hi : i < b + n)
    (hw : IsSemitermVec ℒₛₑₜ (b + n) m w) :
    subst ℒₛₑₜ w (conjunct b n i y) =
      (subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 w (?[^#i] : V)) (cDomN : V)) ^⋏
      (subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (n + 1) w (^#i ∷ shiftVec b n)) y) := by
  have hvec : IsSemitermVec ℒₛₑₜ (n + 1) (b + n) (^#i ∷ shiftVec b n) := by
    rw [IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec_V b n⟩
  have hA : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#i] : V) (cDomN : V)) :=
    (IsSemiformula.subst isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := b + n) hi)).isUFormula
  have hB : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y) :=
    (IsSemiformula.subst hy hvec).isUFormula
  simp only [conjunct]
  rw [substs_and hA hB]
  congr 1
  · exact substs_substs isSemiformula_cDomN hw
      (isSemitermVec_single_bvar (n := b + n) (by simpa [hw.lh] using hi))
  · exact substs_substs hy hw hvec

/-- `termSubstVec` 固定 `?[^#i]`（`w.[i] = ^#i` 时）。 -/
lemma termSubstVec_a_i {w i : V} (hi : w.[i] = (^#i : V)) :
    termSubstVec ℒₛₑₜ 1 w (?[^#i] : V) = (?[^#i] : V) := by
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar, hi]

/-- `termSubstVec 2 w (^#i ∷ ?[^#j])`（`w.[i] = ^#i`、`w.[j] = ^#j` 时不动）。 -/
lemma termSubstVec_cons_a {w i j : V} (hi : w.[i] = (^#i : V)) (hj : w.[j] = (^#j : V)) :
    termSubstVec ℒₛₑₜ 2 w (^#i ∷ ?[^#j] : V) = (^#i ∷ ?[^#j] : V) := by
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := j)),
    termSubst_bvar, termSubst_bvar, hi, hj]

/-- `termSubstVec 2 w ?[^#0, t]` 的求值（`termSubstVec_cons₂` 的字面量 2 正好对上）。 -/
lemma termSubstVec_two {w t : V} (ht : IsUTerm ℒₛₑₜ t) :
    termSubstVec ℒₛₑₜ 2 w (?[^#0, t] : V) = (w.[0] ∷ termSubst ℒₛₑₜ w t ∷ 0) := by
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := 0)) ht, termSubst_bvar]

/-! ## `eqAtom` 的代入 -/

/-- `subst (u ∷ w') (eqAtom t) = ^rel 2 cEqN ?[u, termSubst (u ∷ w') t]`（**任意**尾向量）。 -/
lemma subst_eqAtom_cons {u w' t : V} (hu : IsUTerm ℒₛₑₜ u)
    (ht : IsUTerm ℒₛₑₜ t) :
    subst ℒₛₑₜ (u ∷ w') (eqAtom t) =
      (^rel 2 (↑cEqN) ?[u, termSubst ℒₛₑₜ (u ∷ w') t] : V) := by
  have hv : IsUTermVec ℒₛₑₜ 2 ((^#0 : V) ∷ (t ∷ (0 : V))) :=
    GodelQ.TranslateShiftCompat.isUTermVec_eqAtom_vec t ht
  rw [eqAtom, substs_rel (by rw [cEqN]; exact codeIn_rel_quote _) hv]
  congr 1
  rw [show ((^#0 : V) ∷ (t ∷ (0 : V))) = (?[^#0, t] : V) from rfl,
    termSubstVec_two ht, nth_adjoin_zero]

/-- `subst (^#a ∷ ?[^&0]) (eqAtom t) = ^rel 2 cEqN ?[#a, termSubst (^#a ∷ ?[^&0]) t]`。 -/
lemma subst_eqAtom_a0 {a t : V} (ht : IsUTerm ℒₛₑₜ t) :
    subst ℒₛₑₜ (^#a ∷ ?[^&0] : V) (eqAtom t) =
      (^rel 2 (↑cEqN) ?[^#a, termSubst ℒₛₑₜ (^#a ∷ ?[^&0] : V) t] : V) :=
  subst_eqAtom_cons (IsUTerm.bvar (z := a)) ht

/-- `subst ?[^#a] (eqAtom t) = ^rel 2 cEqN ?[#a, termSubst ?[^#a] t]`。 -/
lemma subst_eqAtom_a {a t : V} (ht : IsUTerm ℒₛₑₜ t) :
    subst ℒₛₑₜ (?[^#a] : V) (eqAtom t) =
      (^rel 2 (↑cEqN) ?[^#a, termSubst ℒₛₑₜ (?[^#a] : V) t] : V) :=
  subst_eqAtom_cons (IsUTerm.bvar (z := a)) ht

/-- `termSubstVec 1 (^#a ∷ w') ?[^#0] = ?[^#a]`。 -/
lemma termSubstVec_a0_n0 {a w' : V} :
    termSubstVec ℒₛₑₜ 1 (^#a ∷ w') (?[^#0] : V) = (?[^#a] : V) := by
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := 0)), termSubst_bvar, nth_adjoin_zero]

/-- `termSubstVec 1 ?[^#a] ?[^#0] = ?[^#a]`。 -/
lemma termSubstVec_a_n0 {a : V} :
    termSubstVec ℒₛₑₜ 1 (?[^#a] : V) (?[^#0] : V) = (?[^#a] : V) := by
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := 0)), termSubst_bvar, nth_adjoin_zero]

/-! ## 项层子律 T1 本体 -/

/-- `resultVec ![n] 2 v = ?[iVE n v.[0], iVE n v.[1]]`。 -/
lemma resultVec_two_eq {n v : V} (hv : IsUTermVec ℒₒᵣ 2 v) :
    iVE.construction.resultVec ℒₒᵣ ![n] 2 v = (?[iVE n v.[0], iVE n v.[1]] : V) := by
  refine nth_ext' (2 : V) ?_ ?_ ?_
  · rw [iVE.construction.resultVec_lh ℒₒᵣ ![n] hv]
  · rw [len_adjoin, len_adjoin]; norm_num
  · intro i hi
    rcases le_one_iff_eq_zero_or_one.mp (lt_two_iff_le_one.mp hi) with rfl | rfl
    · rw [GodelQ.IVeShift.resultVec2_nth hv (by norm_num)]
      simp
    · rw [GodelQ.IVeShift.resultVec2_nth hv (by norm_num)]
      simp [Matrix.vecTail, Matrix.vecHead]

end GodelQ.ITSubsts1

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `ve0` 的代入

`ve0 k f = imp ⊤ (subst ?[^#0] (cFunc k f))`——体是代换（`cFunc k f` 层 1）。
两侧的 `substs_substs` 用**同一个层** `m`：内向量 `?[^#0]` 的长度 1 决定 `l = 1`（= `cFunc` 的层），
外向量长度分别是 2（左，`^#a ∷ ?[^&0]`）与 1（右，`?[^#a]`）。 -/

/-- 向量 `^#a ∷ ?[^&0]`（长 2、层 `m`，`a < m`）。 -/
lemma isSemitermVec_a0 {a m : V} (ha : a < m) :
    IsSemitermVec ℒₛₑₜ 2 m (^#a ∷ ?[^&0] : V) := by
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr ha, ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.fvar m (0 : V), by simp⟩

/-- 向量 `?[^#a]`（长 1、层 `m`，`a < m`）。 -/
lemma isSemitermVec_a {a m : V} (ha : a < m) : IsSemitermVec ℒₛₑₜ 1 m (?[^#a] : V) :=
  isSemitermVec_single_bvar ha

/-- 向量 `?[^#0]`（长 1、层 `m`，`0 < m`）。 -/
lemma isSemitermVec_0 {m : V} (hm : 0 < m) : IsSemitermVec ℒₛₑₜ 1 m (?[^#0] : V) :=
  isSemitermVec_single_bvar hm

/-- `subst w (subst ?[^#0] (cFunc k f)) = subst (termSubstVec 1 w ?[^#0]) (cFunc k f)`
（`w` 长 2、层 `m`；`substs_substs` 里 `v` 的层 = `w` 的长度，故 `?[^#0]` 取层 2）。 -/
lemma subst_ve0_body {k f w : V} {m : V} (hcf : IsSemiformula ℒₛₑₜ 1 (cFunc k f))
    (hw : IsSemitermVec ℒₛₑₜ 2 m w) (hb : IsSemitermVec ℒₛₑₜ 1 2 (?[^#0] : V)) :
    subst ℒₛₑₜ w (subst ℒₛₑₜ (?[^#0] : V) (cFunc k f)) =
      subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 w (?[^#0] : V)) (cFunc k f) :=
  substs_substs hcf hw hb

/-- 同上的 `w` 长 1 版本（`?[^#0]` 取层 1）。 -/
lemma subst_ve0_body₁ {k f w : V} {m : V} (hcf : IsSemiformula ℒₛₑₜ 1 (cFunc k f))
    (hw : IsSemitermVec ℒₛₑₜ 1 m w) (hb : IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V)) :
    subst ℒₛₑₜ w (subst ℒₛₑₜ (?[^#0] : V) (cFunc k f)) =
      subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 w (?[^#0] : V)) (cFunc k f) :=
  substs_substs hcf hw hb

/-- **T1 的 `ve0` 支**：`k = 0` 时两边相等（无绑定子）。

两侧各自走 `subst_imp`（`ve0` 的外层 `imp ⊤`）+ `substs_substs`（体）：
左向量长 2、右向量长 1，故 `subst_imp` 的层分别取 2 与 1；
两侧最后都化成 `imp ⊤ (subst ?[^#a] (cFunc k f))`。 -/
lemma iVE_subst_ve0 {a k f : V} {m : V} (ha : a < m)
    (hcf : IsSemiformula ℒₛₑₜ 1 (cFunc k f)) :
    subst ℒₛₑₜ (^#a ∷ ?[^&0] : V) (ve0 k f) =
      subst ℒₛₑₜ (?[^#a] : V) (ve0 k f) := by
  have hb2 : IsSemitermVec ℒₛₑₜ 1 2 (?[^#0] : V) := isSemitermVec_0 (by norm_num)
  have hb1 : IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V) := isSemitermVec_0 (by norm_num)
  have hX2 : IsSemiformula ℒₛₑₜ 2 (subst ℒₛₑₜ (?[^#0] : V) (cFunc k f)) :=
    IsSemiformula.subst hcf hb2
  have hX1 : IsSemiformula ℒₛₑₜ 1 (subst ℒₛₑₜ (?[^#0] : V) (cFunc k f)) :=
    IsSemiformula.subst hcf hb1
  have hL : IsSemitermVec ℒₛₑₜ 2 m (^#a ∷ ?[^&0] : V) := isSemitermVec_a0 ha
  have hR : IsSemitermVec ℒₛₑₜ 1 m (?[^#a] : V) := isSemitermVec_a ha
  have eL : subst ℒₛₑₜ (^#a ∷ ?[^&0] : V) (ve0 k f) =
      imp ℒₛₑₜ ^⊤ (subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (^#a ∷ ?[^&0] : V) (?[^#0] : V))
        (cFunc k f)) := by
    simp only [ve0]
    rw [subst_imp (n := 2) (m := m) (IsSemiformula.verum (n := 2)) hX2 hL, substs_verum]
    exact congrArg (imp ℒₛₑₜ ^⊤) (subst_ve0_body hcf hL hb2)
  have eR : subst ℒₛₑₜ (?[^#a] : V) (ve0 k f) =
      imp ℒₛₑₜ ^⊤ (subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (?[^#a] : V) (?[^#0] : V))
        (cFunc k f)) := by
    simp only [ve0]
    rw [subst_imp (n := 1) (m := m) (IsSemiformula.verum (n := 1)) hX1 hR, substs_verum]
    exact congrArg (imp ℒₛₑₜ ^⊤) (subst_ve0_body₁ hcf hR hb1)
  rw [eL, eR, termSubstVec_a0_n0, termSubstVec_a_n0]

/-- 右式的直接形态：`subst ?[^#a] (iVE 0 (subst ?[^&0] t))` 对 `t = ^#0` 与 `t = ^&x`。 -/
lemma rhs_bvar (a : V) :
    subst ℒₛₑₜ (?[^#a] : V) (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) (^#0 : V))) =
      (^rel 2 (↑cEqN) ?[^#a, ^&0] : V) := by
  have h : termSubst ℒₒᵣ (?[^&0] : V) (^#0 : V) = (^&0 : V) := by
    rw [termSubst_bvar, nth_adjoin_zero]
  rw [h, iVE_fvar, subst_eqAtom_a (IsUTerm.fvar (0 : V))]
  rw [termSubst_fvar]

/-- 右式的直接形态（fvar 版）。 -/
lemma rhs_fvar (a x : V) :
    subst ℒₛₑₜ (?[^#a] : V) (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) (^&x : V))) =
      (^rel 2 (↑cEqN) ?[^#a, ^&x] : V) := by
  have h : termSubst ℒₒᵣ (?[^&0] : V) (^&x : V) = (^&x : V) := termSubst_fvar x
  rw [h, iVE_fvar, subst_eqAtom_a (IsUTerm.fvar x)]
  rw [termSubst_fvar]

end GodelQ.ITSubsts1

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **T1**（`t` 层 1）：`subst (^#a ∷ ?[^&0]) (iVE 1 t) = subst ?[^#a] (iVE 0 (termSubst ?[^&0] t))`。

归纳谓词取 `∀ a < m, <T1 在 a>`——`ve2` 支对每个参数 `v.[i]` 要在 `a := i`
处用归纳假设，故归纳必须对 `a` 全称（**有界**全称，`definability` 可接受）。

`a < m` 里 `m` 是层。`ve2` 支的调用处取 `m := 3`（`W'` 长 4、层 3），
`i ∈ {0,1}` 都有 `i < 3`。 -/
lemma iVE_subst_a0 {m : V} : ∀ t, IsSemiterm ℒₒᵣ 1 t → ∀ a : V, a < m →
    subst ℒₛₑₜ (^#a ∷ ?[^&0] : V) (iVE (1 : V) t) =
      subst ℒₛₑₜ (?[^#a] : V) (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) t)) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := (1 : V))
    (P := fun t ↦ ∀ a : V, a < m →
      subst ℒₛₑₜ (^#a ∷ ?[^&0] : V) (iVE (1 : V) t) =
        subst ℒₛₑₜ (?[^#a] : V) (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) t)))
  · definability
  · -- bvar：`z < 1` ⇒ `z = 0`
    intro z hz a _
    have hz0 : z = 0 := lt_one_iff_eq_zero.mp hz
    subst hz0
    rw [iVE_bvar]
    rw [show (^#(0 + 1) : V) = (^#1 : V) by norm_num]
    rw [subst_eqAtom_a0 (IsUTerm.bvar (z := 1))]
    rw [termSubst_bvar]
    simp only [nth_adjoin_one, nth_adjoin_zero]
    exact (rhs_bvar a).symm
  · -- fvar
    intro x a _
    rw [iVE_fvar, subst_eqAtom_a0 (IsUTerm.fvar x), termSubst_fvar]
    exact (rhs_fvar a x).symm
  · -- func
    intro k f v hkf hv ih
    by_cases hk : k = 0
    · subst hk
      have hv0 : v = (0 : V) := by
        have h : IsUTermVec ℒₒᵣ 0 v := hv.isUTerm
        exact IsUTermVec.empty_iff.mp h
      subst hv0
      intro a ha
      have hsub0 : termSubst ℒₒᵣ (?[^&0] : V) (^func 0 f (0 : V)) =
          (^func 0 f (0 : V) : V) := by
        rw [termSubst_func hkf (IsUTermVec.empty (L := ℒₒᵣ) (V := V)), termSubstVec_nil]
      rw [hsub0]
      rw [iVE_func hkf (IsUTermVec.empty (L := ℒₒᵣ) (V := V)),
        iVE_func hkf (IsUTermVec.empty (L := ℒₒᵣ) (V := V))]
      simp only [ite_true]
      exact iVE_subst_ve0 ha (isSemiformula_cFunc_arity0 f)
    · -- k = 2：`ve2`，两层绑定子
      have hk2 := k_eq_two_of_func hkf hk
      subst hk2
      intro a ha
      -- 归纳假设在 `a := i` 处的两个实例
      have ih0 := ih 0 (by norm_num) a ha
      have ih1 := ih 1 (by norm_num) a ha
      -- 体的公式性（两侧共用的结论项 `cFunc 2 f`）
      have hcf : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f) := isSemiformula_cFunc_arity2 (by norm_num) f
      have hv0 : IsSemiterm ℒₒᵣ 1 v.[0] := hv.nth (i := 0) (by norm_num)
      have hv1 : IsSemiterm ℒₒᵣ 1 v.[1] := hv.nth (i := 1) (by norm_num)
      have hvec1 : IsSemitermVec ℒₒᵣ 1 1 (?[^&0] : V) := by
        rw [IsSemitermVec.singleton]
        exact IsSemiterm.fvar 1 (0 : V)
      have hvt : IsSemitermVec ℒₒᵣ 2 1 (termSubstVec ℒₒᵣ 2 (?[^&0] : V) v) :=
        IsSemitermVec.termSubstVec (k := 2) (n := 1) (m := 1) (v := v)
          (w := (?[^&0] : V)) hvec1 hv
      -- 内层先展开（右侧的 `iVE 0` 参数里有 `termSubst`）
      rw [termSubst_func hkf hv.isUTerm]
      -- 两侧 `iVE` 展开
      rw [iVE_func hkf hv.isUTerm, iVE_func hkf hvt.isUTerm]
      simp only [if_neg (by norm_num : ¬(2 : V) = 0)]
      rw [resultVec_two_eq hv.isUTerm, resultVec_two_eq hvt.isUTerm]
      -- 两侧各推两层 `qqAlls`（`W' := qVec (qVec w)`）
      have hA : IsUFormula ℒₛₑₜ
          (conjunct 3 1 0 (iVE (1 : V) v.[0]) ^⋏
            (conjunct 3 1 1 (iVE (1 : V) v.[1]) ^⋏ ^⊤)) :=
        IsUFormula.and.mpr ⟨(isSemiformula_conjunct
            (isSemiformula_iVE v.[0] hv0) (zero_lt_three_add 1)).isUFormula,
          IsUFormula.and.mpr ⟨(isSemiformula_conjunct
            (isSemiformula_iVE v.[1] hv1) (one_lt_three_add 1)).isUFormula,
            IsUFormula.verum⟩⟩
      have hB : IsUFormula ℒₛₑₜ
          (conjunct 3 0 0 (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[0])) ^⋏
            (conjunct 3 0 1 (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[1])) ^⋏ ^⊤)) :=
        IsUFormula.and.mpr ⟨(isSemiformula_conjunct
            (isSemiformula_iVE _ (hvt.nth (i := 0) (by norm_num))) (zero_lt_three_add 0)).isUFormula,
          IsUFormula.and.mpr ⟨(isSemiformula_conjunct
            (isSemiformula_iVE _ (hvt.nth (i := 1) (by norm_num))) (one_lt_three_add 0)).isUFormula,
            IsUFormula.verum⟩⟩
      have hF : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1] : V) (cFunc 2 f)) :=
        (IsSemiformula.subst hcf (by
          rw [show (?[^#2, ^#0, ^#1] : V) = ((^#2 : V) ∷ ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))))
            from rfl]
          rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
          refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
          rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
          exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩)).isUFormula
      rw [subst_qqAlls_two (IsUFormula.imp.mpr ⟨hA, hF⟩),
        subst_qqAlls_two (IsUFormula.imp.mpr ⟨hB, hF⟩)]
      congr 1
      rw [subst_imp hA hF (isSemitermVec_W' a),
        subst_imp hB hF (isSemitermVec_V' a)]
      congr 1
      · -- 合取块：逐 `conjunct` 用 `subst_conjunct` + 归纳假设
        rw [substs_and (by
            rw [conjunct]
            exact IsUFormula.and.mpr
              ⟨(IsSemiformula.subst isSemiformula_cDomN
                  (isSemitermVec_single_bvar (n := 4) (by norm_num))).isUFormula,
                (IsSemiformula.subst (isSemiformula_iVE v.[0] hv0) (by
                  rw [IsSemitermVec.cons_iff]
                  exact ⟨IsSemiterm.bvar.mpr (by norm_num), isSemitermVec_shiftVec_V 3 1⟩)).isUFormula⟩)
          (IsUFormula.and.mpr ⟨(by
            rw [conjunct]
            exact IsUFormula.and.mpr
              ⟨(IsSemiformula.subst isSemiformula_cDomN
                  (isSemitermVec_single_bvar (n := 4) (by norm_num))).isUFormula,
                (IsSemiformula.subst (isSemiformula_iVE v.[1] hv1) (by
                  rw [IsSemitermVec.cons_iff]
                  exact ⟨IsSemiterm.bvar.mpr (by norm_num), isSemitermVec_shiftVec_V 3 1⟩)).isUFormula⟩⟩,
            IsUFormula.verum⟩)]
        sorry
      · -- 结论项
        exact (subst_concl_W' (a := a) hcf).trans (subst_concl_V' (a := a) hcf).symm

end GodelQ.ITSubsts1

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `ve2` 支的向量工具

`W' := qVec (qVec (^#a ∷ ?[^&0])) = ?[^#0, ^#1, ^#(a+2), ^&0]`（长 4、层 3）。
`ve2` 支里每个 `conjunct 3 1 i` 的 `y` 槽向量是 `^#i ∷ shiftVec 3 1 = ?[^#i, ^#3]`，
在 `W'` 下逐分量变成 `?[^#i, ^&0]`——**这正是 T1 里那个向量的来源**。 -/

/-- `W'` 的显式形态。 -/
lemma W'_eq (a : V) :
    qVec ℒₛₑₜ (qVec ℒₛₑₜ (^#a ∷ ?[^&0] : V)) = (?[^#0, ^#1, ^#(a + 2), ^&0] : V) :=
  qVec_qVec_a0 a

/-- `W'` 是长 4、层 `a+3` 的项向量。 -/
lemma isSemitermVec_W' (a : V) :
    IsSemitermVec ℒₛₑₜ 4 (a + (1 + 1 + 1)) (?[^#0, ^#1, ^#(a + 2), ^&0] : V) := by
  rw [show (?[^#0, ^#1, ^#(a + 2), ^&0] : V) =
    ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ ((^&0 : V) ∷ (0 : V))))) from rfl]
  rw [show (4 : V) = 3 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
    have h := one_lt_three_add a
    rw [show (3 : V) + a = a + (1 + 1 + 1) by ring] at h
    exact h), ?_⟩
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
    have h := lt_add_self_add_one (a + 2) (0 : V)
    have e1 : (0 : V) + (a + 2) + 1 = a + (1 + 1 + 1) := by ring
    have e2 : a + 2 = a + (1 + 1) := by ring
    rw [e1] at h
    rw [e2] at h
    exact h), by simp⟩

/-- `V' := qVec (qVec ?[^#a]) = ?[^#0, ^#1, ^#(a+2)]`（长 3、层 `a+3`）。 -/
lemma isSemitermVec_V' (a : V) :
    IsSemitermVec ℒₛₑₜ 3 (a + (1 + 1 + 1)) (?[^#0, ^#1, ^#(a + 2)] : V) := by
  rw [show (?[^#0, ^#1, ^#(a + 2)] : V) =
    ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ (0 : V)))) from rfl]
  rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
    have h := one_lt_three_add a
    rw [show (3 : V) + a = a + (1 + 1 + 1) by ring] at h
    exact h), by simp⟩

/-- `termSubstVec 1 W' ?[^#i] = ?[^#i]`（`i < 2`）。 -/
lemma termSubstVec_W'_i {a i : V} (hi : i < 2) :
    termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#i] : V) = (?[^#i] : V) := by
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar]
  rcases le_one_iff_eq_zero_or_one.mp (lt_two_iff_le_one.mp hi) with rfl | rfl
  · rw [nth_adjoin_zero]
  · rw [nth_adjoin_one, nth_adjoin_zero]

/-- `termSubstVec 2 W' ?[^#i, ^#3] = ?[^#i, ^&0]`（`i < 2`）。 -/
lemma termSubstVec_W'_i3 {a i : V} (hi : i < 2) :
    termSubstVec ℒₛₑₜ 2 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#i, ^#3] : V)
      = (?[^#i, ^&0] : V) := by
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := 3)),
    termSubst_bvar, termSubst_bvar]
  congr 1
  · rcases le_one_iff_eq_zero_or_one.mp (lt_two_iff_le_one.mp hi) with rfl | rfl
    · rw [nth_adjoin_zero]
    · rw [nth_adjoin_one, nth_adjoin_zero]
  · rw [show (?[^#0, ^#1, ^#(a + 2), ^&0] : V) =
        ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ ((^&0 : V) ∷ (0 : V))))) from rfl]
    rw [show (3 : V) = 2 + 1 by norm_num, nth_adjoin_succ]
    rw [show (2 : V) = 1 + 1 by norm_num, nth_adjoin_succ]
    rw [show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]

/-- `termSubstVec 1 V' ?[^#i] = ?[^#i]`（`i < 2`）。 -/
lemma termSubstVec_V'_i {a i : V} (hi : i < 2) :
    termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#i] : V) = (?[^#i] : V) := by
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar]
  rcases le_one_iff_eq_zero_or_one.mp (lt_two_iff_le_one.mp hi) with rfl | rfl
  · rw [nth_adjoin_zero]
  · rw [nth_adjoin_one, nth_adjoin_zero]

/-- `termSubstVec 1 V' ?[^#i, 0]` 里第二分量不存在，故只需首分量：`?[^#i]`。 -/
lemma termSubstVec_V'_i_single {a i : V} (hi : i < 2) :
    termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#i] : V) = (?[^#i] : V) :=
  termSubstVec_V'_i hi

end GodelQ.ITSubsts1

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `termSubstVec 3 w ?[t₂, t₁, t₀] = ?[termSubst w t₂, termSubst w t₁, termSubst w t₀]`。 -/
lemma termSubstVec_three {w t₂ t₁ t₀ : V} (h₂ : IsUTerm ℒₛₑₜ t₂) (h₁ : IsUTerm ℒₛₑₜ t₁)
    (h₀ : IsUTerm ℒₛₑₜ t₀) :
    termSubstVec ℒₛₑₜ 3 w (?[t₂, t₁, t₀] : V)
      = (?[termSubst ℒₛₑₜ w t₂, termSubst ℒₛₑₜ w t₁, termSubst ℒₛₑₜ w t₀] : V) := by
  rw [show (?[t₂, t₁, t₀] : V) = (t₂ ∷ (t₁ ∷ (t₀ ∷ (0 : V)))) from rfl]
  rw [show (3 : V) = 2 + 1 by norm_num,
    termSubstVec_cons h₂ (by
      have := (IsUTermVec.adjoin₁_iff.mpr h₀).adjoin h₁
      rw [show (1 : V) + 1 = 2 by norm_num] at this
      exact this)]
  rw [show (2 : V) = 1 + 1 by norm_num,
    termSubstVec_cons h₁ (IsUTermVec.adjoin₁_iff.mpr h₀),
    termSubstVec_cons₁ h₀]

/-- `termSubstVec 3 W' ?[^#2, ^#0, ^#1] = ?[^#(a+2), ^#0, ^#1]`（结论项的向量）。 -/
lemma termSubstVec_W'_concl (a : V) :
    termSubstVec ℒₛₑₜ 3 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#2, ^#0, ^#1] : V)
      = (?[^#(a + 2), ^#0, ^#1] : V) := by
  rw [termSubstVec_three (IsUTerm.bvar (z := 2)) (IsUTerm.bvar (z := 0))
    (IsUTerm.bvar (z := 1))]
  rw [termSubst_bvar, termSubst_bvar, termSubst_bvar]
  rw [show (?[^#0, ^#1, ^#(a + 2), ^&0] : V) =
      ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ ((^&0 : V) ∷ (0 : V))))) from rfl]
  rw [show (2 : V) = 1 + 1 by norm_num, nth_adjoin_succ]
  rw [show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ]
  rw [show (0 : V) + 1 = 1 by norm_num, nth_adjoin_one]
  rw [nth_adjoin_zero, nth_adjoin_zero, nth_adjoin_zero]

/-- `termSubstVec 3 V' ?[^#2, ^#0, ^#1] = ?[^#(a+2), ^#0, ^#1]`（结论项的向量，右侧）。 -/
lemma termSubstVec_V'_concl (a : V) :
    termSubstVec ℒₛₑₜ 3 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#2, ^#0, ^#1] : V)
      = (?[^#(a + 2), ^#0, ^#1] : V) := by
  rw [termSubstVec_three (IsUTerm.bvar (z := 2)) (IsUTerm.bvar (z := 0))
    (IsUTerm.bvar (z := 1))]
  rw [termSubst_bvar, termSubst_bvar, termSubst_bvar]
  rw [show (?[^#0, ^#1, ^#(a + 2)] : V) =
      ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ (0 : V)))) from rfl]
  rw [show (2 : V) = 1 + 1 by norm_num, nth_adjoin_succ]
  rw [show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ]
  rw [show (0 : V) + 1 = 1 by norm_num, nth_adjoin_one]
  rw [nth_adjoin_zero, nth_adjoin_zero, nth_adjoin_zero]

/-- 结论项：`subst W' (subst (^#2 ∷ ?[^#0,^#1]) (cFunc 2 f)) = subst ?[^#(a+2),^#0,^#1] (cFunc 2 f)`。 -/
lemma subst_concl_W' {a f : V} (hcf : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f)) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^#(a + 2), ^&0] : V)
        (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1] : V) (cFunc 2 f)) =
      subst ℒₛₑₜ (?[^#(a + 2), ^#0, ^#1] : V) (cFunc 2 f) := by
  have hv3 : IsSemitermVec ℒₛₑₜ 3 3 (?[^#2, ^#0, ^#1] : V) := by
    rw [show (?[^#2, ^#0, ^#1] : V) = ((^#2 : V) ∷ ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))))
      from rfl]
    rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
    rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩
  rw [substs_substs (l := 3) (n := 4) (m := a + (1 + 1 + 1)) (p := cFunc 2 f) hcf
    (isSemitermVec_W' a) (by
      rw [show (?[^#2, ^#0, ^#1] : V) = ((^#2 : V) ∷ ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))))
        from rfl]
      rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
      rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
      exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩),
    termSubstVec_W'_concl]

/-- 结论项（右侧）。 -/
lemma subst_concl_V' {a f : V} (hcf : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f)) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^#(a + 2)] : V)
        (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1] : V) (cFunc 2 f)) =
      subst ℒₛₑₜ (?[^#(a + 2), ^#0, ^#1] : V) (cFunc 2 f) := by
  have hv3 : IsSemitermVec ℒₛₑₜ 3 3 (?[^#2, ^#0, ^#1] : V) := by
    rw [show (?[^#2, ^#0, ^#1] : V) = ((^#2 : V) ∷ ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))))
      from rfl]
    rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
    rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩
  rw [substs_substs (l := 3) (n := 3) (m := a + (1 + 1 + 1)) (p := cFunc 2 f) hcf
    (isSemitermVec_V' a) (by
      rw [show (?[^#2, ^#0, ^#1] : V) = ((^#2 : V) ∷ ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))))
        from rfl]
      rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
      rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
      exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩),
    termSubstVec_V'_concl]

end GodelQ.ITSubsts1
