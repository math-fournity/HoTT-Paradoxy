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

/-! ## `subst` 与 `ve2` 相容（独立引理，照 `ShiftConjunct.shift_ve2` 的形状）

`ve2 n k f W = qqAlls (imp (conjunct 3 n 0 W.[0] ^⋏ (conjunct 3 n 1 W.[1] ^⋏ ⊤)) F) 2`。

`subst w` 推两层 `qqAlls` 后向量变 `qVec (qVec w)`，于是 `conjunct 3 n i W.[i]`
的 `y` 槽向量是 `termSubstVec 2 (qVec (qVec w)) (^#i ∷ shiftVec 3 n)`。
**本引理只做这一步**（不涉及 `iVE`），把 `ve2` 的体展开一次；
调用方（`iVE_subst_a0` 的 `k = 2` 支）只需把两侧各代进这条引理，
再用 T1 在 `a := i` 的实例收尾。 -/

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


/-- `IsSemitermVec` 对层数单调（任意语言）。 -/
lemma isSemitermVec_mono {L : Language} [L.Encodable] [L.LORDefinable]
    {k n m v : V} (h : IsSemitermVec L k n v) (hnm : n ≤ m) :
    IsSemitermVec L k m v where
  isUTermVec := h.isUTermVec
  bv hi := le_trans (h.bv hi) hnm

/-- `subst w (ve2 n k f W)` 的规范形态（`W` 长 2）。 -/
lemma subst_ve2 {n f w W m : V}
    (hW0 : IsSemiformula ℒₛₑₜ (n + 1) W.[0]) (hW1 : IsSemiformula ℒₛₑₜ (n + 1) W.[1])
    (hcf : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f))
    (hw : IsSemitermVec ℒₛₑₜ (3 + n) m (qVec ℒₛₑₜ (qVec ℒₛₑₜ w))) :
    subst ℒₛₑₜ w (ve2 n 2 f W) =
      qqAlls (imp ℒₛₑₜ
        (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ w))
            (conjunct 3 n 0 W.[0] ^⋏ (conjunct 3 n 1 W.[1] ^⋏ ^⊤)))
        (subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 3 (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) (^#2 ∷ ?[^#0, ^#1] : V))
          (cFunc 2 f))) 2 := by
  have hA : IsSemiformula ℒₛₑₜ (3 + n)
      (conjunct 3 n 0 W.[0] ^⋏ (conjunct 3 n 1 W.[1] ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨isSemiformula_conjunct hW0 (zero_lt_three_add n),
      IsSemiformula.and.mpr ⟨isSemiformula_conjunct hW1 (one_lt_three_add n),
        IsSemiformula.verum⟩⟩
  have hv3 : IsSemitermVec ℒₛₑₜ 3 3 (?[^#2, ^#0, ^#1] : V) := by
    rw [show (?[^#2, ^#0, ^#1] : V) = ((^#2 : V) ∷ ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))))
      from rfl]
    rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
    rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩
  have hF : IsSemiformula ℒₛₑₜ (3 + n) (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1] : V) (cFunc 2 f)) :=
    isSemiformula_mono (IsSemiformula.subst hcf hv3) (by
      have h := le_add_self (a := (3 : V)) (b := n)
      rwa [show n + 3 = 3 + n by ring] at h)
  have hw3 : IsSemitermVec ℒₛₑₜ (3 + n) m (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) := hw
  simp only [ve2, nth_adjoin_zero, nth_adjoin_one]
  rw [subst_qqAlls_two (IsUFormula.imp.mpr ⟨hA.isUFormula, hF.isUFormula⟩),
    subst_imp (n := 3 + n) (m := m) hA hF hw3]
  congr 1
  rw [substs_substs (l := 3) (n := 3 + n) (m := m) (p := cFunc 2 f) hcf hw3
    (isSemitermVec_mono hv3 (by
      have h := le_add_self (a := (3 : V)) (b := n)
      rwa [show n + 3 = 3 + n by ring] at h))]


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

/-- **T1**（`t` 层 1）：`subst (^#a ∷ ?[^&0]) (iVE 1 t) = subst ?[^#a] (iVE 0 (termSubst ?[^&0] t))`。

归纳谓词取 `∀ a < m, <T1 在 a>`——`ve2` 支对每个参数 `v.[i]` 要在 `a := i`
处用归纳假设，故归纳必须对 `a` 全称（**有界**全称，`definability` 可接受）。

`a < m` 里 `m` 是层。`ve2` 支的调用处取 `m := 3`（`W'` 长 4、层 3），
`i ∈ {0,1}` 都有 `i < 3`。 -/
lemma iVE_subst_a0 {m : V} (hm : (3 : V) ≤ m) :
    ∀ t, IsSemiterm ℒₒᵣ 1 t → ∀ a : V, a < m →
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
      have hcf : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f) := isSemiformula_cFunc_arity2 (by norm_num) f
      have hv0 : IsSemiterm ℒₒᵣ 1 v.[0] := hv.nth (i := 0) (by norm_num)
      have hv1 : IsSemiterm ℒₒᵣ 1 v.[1] := hv.nth (i := 1) (by norm_num)
      -- 向量 `?[^&0]` 的**层是 0**（fvar 没有 bvar）——这正是 `iVE 0` 能成立的原因
      have hvec1 : IsSemitermVec ℒₒᵣ 1 0 (?[^&0] : V) := by
        rw [IsSemitermVec.singleton]
        exact IsSemiterm.fvar 0 (0 : V)
      have hvt : IsSemitermVec ℒₒᵣ 2 0 (termSubstVec ℒₒᵣ 2 (?[^&0] : V) v) :=
        IsSemitermVec.termSubstVec (k := 2) (n := 1) (m := 0) (v := v)
          (w := (?[^&0] : V)) hvec1 hv
      -- 内层先展开（右侧的 `iVE 0` 参数里有 `termSubst`）
      rw [termSubst_func hkf hv.isUTerm]
      -- 两侧 `iVE` 展开
      rw [iVE_func hkf hv.isUTerm, iVE_func hkf hvt.isUTerm]
      simp only [if_neg (by norm_num : ¬(2 : V) = 0)]
      rw [resultVec_two_eq hv.isUTerm, resultVec_two_eq hvt.isUTerm]
      -- 左侧（`n = 1`，向量 `^#a ∷ ?[^&0]`）
      rw [subst_ve2 (n := 1) (f := f) (w := (^#a ∷ ?[^&0] : V)) (m := a + (1 + 1 + 1))
          (W := (?[iVE (1 : V) v.[0], iVE (1 : V) v.[1]] : V))
          (by simpa using isSemiformula_iVE v.[0] hv0)
          (by simpa using isSemiformula_iVE v.[1] hv1) hcf
          (by
            rw [qVec_qVec_a0 a]
            exact isSemitermVec_W' a)]
      -- 右侧：`W` 的分量是 `iVE 0 (termSubstVec 2 ?[^&0] v).[i]`，
      -- 先用 `nth_termSubstVec` 换成 `subst_ve2` 要的逐点形态（在 `iVE 0` 的参数里）
      conv_rhs => rw [show (termSubstVec ℒₒᵣ 2 (?[^&0] : V) v).[0] =
          termSubst ℒₒᵣ (?[^&0] : V) v.[0] from nth_termSubstVec hv.isUTerm (by norm_num),
        show (termSubstVec ℒₒᵣ 2 (?[^&0] : V) v).[1] =
          termSubst ℒₒᵣ (?[^&0] : V) v.[1] from nth_termSubstVec hv.isUTerm (by norm_num)]
      rw [subst_ve2 (n := 0) (f := f) (w := (?[^#a] : V)) (m := a + (1 + 1 + 1))
          (W := (?[iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[0]),
            iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[1])] : V))
          (by
            have h0 : IsSemiterm ℒₒᵣ 0 (termSubst ℒₒᵣ (?[^&0] : V) v.[0]) := by
              rw [← nth_termSubstVec hv.isUTerm (show (0 : V) < 2 by norm_num)]
              exact hvt.nth (i := 0) (by norm_num)
            rw [nth_adjoin_zero]
            exact isSemiformula_iVE (V := V) (n := (0 : V))
              (termSubst ℒₒᵣ (?[^&0] : V) v.[0]) h0)
          (by
            have h1 : IsSemiterm ℒₒᵣ 0 (termSubst ℒₒᵣ (?[^&0] : V) v.[1]) := by
              rw [← nth_termSubstVec hv.isUTerm (show (1 : V) < 2 by norm_num)]
              exact hvt.nth (i := 1) (by norm_num)
            rw [nth_adjoin_one, nth_adjoin_zero]
            exact isSemiformula_iVE (V := V) (n := (0 : V))
              (termSubst ℒₒᵣ (?[^&0] : V) v.[1]) h1) hcf
          (by
            rw [qVec_qVec_a a]
            rw [show (3 : V) + 0 = 3 by norm_num]
            exact isSemitermVec_V' a)]
      congr 1
      rw [show (qVec ℒₛₑₜ (qVec ℒₛₑₜ (^#a ∷ ?[^&0] : V)) : V) =
            (?[^#0, ^#1, ^#(a + 2), ^&0] : V) from qVec_qVec_a0 a,
        show (qVec ℒₛₑₜ (qVec ℒₛₑₜ (?[^#a] : V)) : V) =
            (?[^#0, ^#1, ^#(a + 2)] : V) from qVec_qVec_a a]
      -- 先把三个 `(x ∷ y ∷ 0).[0/1]` 归一成 `x`／`y`
      simp only [nth_adjoin_zero, nth_adjoin_one]
      -- 目标里的向量是展开的 `∷` 形状；`isSemitermVec_W'` 给的是 `?[…]` 形状
      have hWL : IsSemitermVec ℒₛₑₜ 4 (a + (1 + 1 + 1))
          ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ ((^&0 : V) ∷ (0 : V))))) := by
        rw [show ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ ((^&0 : V) ∷ (0 : V))))) =
            (?[^#0, ^#1, ^#(a + 2), ^&0] : V) from rfl]
        exact isSemitermVec_W' a
      have hVL : IsSemitermVec ℒₛₑₜ 3 (a + (1 + 1 + 1))
          ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ (0 : V)))) := by
        rw [show ((^#0 : V) ∷ ((^#1 : V) ∷ ((^#(a + 2) : V) ∷ (0 : V)))) =
            (?[^#0, ^#1, ^#(a + 2)] : V) from rfl]
        exact isSemitermVec_V' a
      -- 逐 `conjunct` 推过 `subst`（先把外层的 `⋏` 分开，再逐个用 `subst_conjunct`）
      have hc0 : IsUFormula ℒₛₑₜ (conjunct 3 1 0 (iVE (1 : V) v.[0])) :=
        (isSemiformula_conjunct (isSemiformula_iVE v.[0] hv0)
          (zero_lt_three_add 1)).isUFormula
      have hc1 : IsUFormula ℒₛₑₜ (conjunct 3 1 1 (iVE (1 : V) v.[1])) :=
        (isSemiformula_conjunct (isSemiformula_iVE v.[1] hv1)
          (one_lt_three_add 1)).isUFormula
      have hpt0 : (termSubstVec ℒₒᵣ 2 (?[^&0] : V) v).[0] = termSubst ℒₒᵣ (?[^&0] : V) v.[0] :=
        nth_termSubstVec hv.isUTerm (by norm_num)
      have hpt1 : (termSubstVec ℒₒᵣ 2 (?[^&0] : V) v).[1] = termSubst ℒₒᵣ (?[^&0] : V) v.[1] :=
        nth_termSubstVec hv.isUTerm (by norm_num)
      have ht0 : IsSemiterm ℒₒᵣ 0 (termSubst ℒₒᵣ (?[^&0] : V) v.[0]) := by
        rw [← hpt0]; exact hvt.nth (i := 0) (by norm_num)
      have ht1 : IsSemiterm ℒₒᵣ 0 (termSubst ℒₒᵣ (?[^&0] : V) v.[1]) := by
        rw [← hpt1]; exact hvt.nth (i := 1) (by norm_num)
      have hd0 : IsUFormula ℒₛₑₜ
          (conjunct 3 0 0 (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[0]))) := by
        rw [← hpt0]
        exact (isSemiformula_conjunct (isSemiformula_iVE (n := (0 : V)) _ (hvt.nth (i := 0) (by norm_num))) (zero_lt_three_add 0)).isUFormula
      have hd1 : IsUFormula ℒₛₑₜ
          (conjunct 3 0 1 (iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[1]))) := by
        rw [← hpt1]
        exact (isSemiformula_conjunct (isSemiformula_iVE (n := (0 : V)) _ (hvt.nth (i := 1) (by norm_num))) (one_lt_three_add 0)).isUFormula
      have ht0 : IsSemiterm ℒₒᵣ 0 (termSubst ℒₒᵣ (?[^&0] : V) v.[0]) := by
        rw [← nth_termSubstVec (L := ℒₒᵣ) hv.isUTerm (show (0 : V) < 2 by norm_num)]
        exact hvt.nth (i := 0) (by norm_num)
      have ht1 : IsSemiterm ℒₒᵣ 0 (termSubst ℒₒᵣ (?[^&0] : V) v.[1]) := by
        rw [← nth_termSubstVec (L := ℒₒᵣ) hv.isUTerm (show (1 : V) < 2 by norm_num)]
        exact hvt.nth (i := 1) (by norm_num)
      -- 把 `subst` 分到合取支（两层）
      rw [substs_and hc0 (IsUFormula.and.mpr ⟨hc1, IsUFormula.verum⟩)]
      rw [substs_and hc1 IsUFormula.verum]
      rw [substs_and hd0 (IsUFormula.and.mpr ⟨hd1, IsUFormula.verum⟩)]
      rw [substs_and hd1 IsUFormula.verum]
      conv_lhs => rw [
        subst_conjunct (n := 1) (y := iVE (1 : V) v.[0])
          (hy := isSemiformula_iVE v.[0] hv0) (hi := zero_lt_three_add 1)
          (hw := isSemitermVec_W' a),
        subst_conjunct (n := 1) (y := iVE (1 : V) v.[1])
          (hy := isSemiformula_iVE v.[1] hv1) (hi := one_lt_three_add 1)
          (hw := isSemitermVec_W' a)]
      conv_rhs => rw [
        subst_conjunct (b := 3) (n := (0 : V))
          (y := iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[0]))
          (hy := isSemiformula_iVE (V := V) (n := (0 : V))
            (termSubst ℒₒᵣ (?[^&0] : V) v.[0]) ht0)
          (hi := zero_lt_three_add 0)
          (hw := by rw [show (3 : V) + 0 = 3 by norm_num]; exact isSemitermVec_V' a),
        subst_conjunct (b := 3) (n := (0 : V))
          (y := iVE (0 : V) (termSubst ℒₒᵣ (?[^&0] : V) v.[1]))
          (hy := isSemiformula_iVE (V := V) (n := (0 : V))
            (termSubst ℒₒᵣ (?[^&0] : V) v.[1]) ht1)
          (hi := one_lt_three_add 0)
          (hw := by rw [show (3 : V) + 0 = 3 by norm_num]; exact isSemitermVec_V' a)]
      -- `cDomN` 槽向量：`termSubstVec 1 W' ?[^#i]` / `termSubstVec 1 V' ?[^#i]`
      have eC0 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#0] : V)
          = (?[^#0] : V) := termSubstVec_W'_i (a := a) (i := 0) (by norm_num)
      have eD0 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#0] : V)
          = (?[^#0] : V) := termSubstVec_V'_i (a := a) (i := 0) (by norm_num)
      have eC1 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#1] : V)
          = (?[^#1] : V) := termSubstVec_W'_i (a := a) (i := 1) (by norm_num)
      have eD1 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#1] : V)
          = (?[^#1] : V) := termSubstVec_V'_i (a := a) (i := 1) (by norm_num)
      have eC0 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#0] : V)
          = (?[^#0] : V) := termSubstVec_W'_i (a := a) (i := 0) (by norm_num)
      have eC1 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2), ^&0] : V) (?[^#1] : V)
          = (?[^#1] : V) := termSubstVec_W'_i (a := a) (i := 1) (by norm_num)
      have eD0 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#0] : V)
          = (?[^#0] : V) := termSubstVec_V'_i (a := a) (i := 0) (by norm_num)
      have eD1 : termSubstVec ℒₛₑₜ 1 (?[^#0, ^#1, ^#(a + 2)] : V) (?[^#1] : V)
          = (?[^#1] : V) := termSubstVec_V'_i (a := a) (i := 1) (by norm_num)
      have eW0 : termSubstVec ℒₛₑₜ (1 + 1) (?[^#0, ^#1, ^#(a + 2), ^&0] : V)
          (^#0 ∷ shiftVec 3 1) = (?[^#0, ^&0] : V) := by
        rw [show (^#0 ∷ shiftVec 3 1 : V) = (?[^#0, ^#3] : V) from by
          rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero,
            termBShiftVec_nil]]
        rw [show (1 : V) + 1 = 2 by norm_num]
        exact termSubstVec_W'_i3 (a := a) (i := 0) (by norm_num)
      have eV0 : termSubstVec ℒₛₑₜ (0 + 1) (?[^#0, ^#1, ^#(a + 2)] : V)
          (^#0 ∷ shiftVec 3 0) = (?[^#0] : V) := by
        rw [show (^#0 ∷ shiftVec 3 0 : V) = (?[^#0] : V) from by rw [shiftVec_zero]]
        rw [show (0 : V) + 1 = 1 by norm_num]
        exact termSubstVec_V'_i (a := a) (i := 0) (by norm_num)
      have eW1 : termSubstVec ℒₛₑₜ (1 + 1) (?[^#0, ^#1, ^#(a + 2), ^&0] : V)
          (^#1 ∷ shiftVec 3 1) = (?[^#1, ^&0] : V) := by
        rw [show (^#1 ∷ shiftVec 3 1 : V) = (?[^#1, ^#3] : V) from by
          rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero,
            termBShiftVec_nil]]
        rw [show (1 : V) + 1 = 2 by norm_num]
        exact termSubstVec_W'_i3 (a := a) (i := 1) (by norm_num)
      have eV1 : termSubstVec ℒₛₑₜ (0 + 1) (?[^#0, ^#1, ^#(a + 2)] : V)
          (^#1 ∷ shiftVec 3 0) = (?[^#1] : V) := by
        rw [show (^#1 ∷ shiftVec 3 0 : V) = (?[^#1] : V) from by rw [shiftVec_zero]]
        rw [show (0 : V) + 1 = 1 by norm_num]
        exact termSubstVec_V'_i (a := a) (i := 1) (by norm_num)
      -- 两侧逐字同形，只差两个 `y` 槽的 T1 实例（`a := 0` 与 `a := 1`）
      refine congrArg₂ (imp ℒₛₑₜ) ?_ ?_
      refine congrArg₂ (· ^⋏ ·) ?_ ?_
      · rw [eC0, eD0, eW0, eV0]
        refine congrArg₂ (· ^⋏ ·) rfl ?_
        exact ih 0 (by norm_num) (0 : V) (lt_of_lt_of_le (by norm_num : (0 : V) < 3) hm)
      · refine congrArg₂ (· ^⋏ ·) ?_ ?_
        · rw [eC1, eD1, eW1, eV1]
          refine congrArg₂ (· ^⋏ ·) rfl ?_
          exact ih 1 (by norm_num) (1 : V) (lt_of_lt_of_le (by norm_num : (1 : V) < 3) hm)
        · rw [substs_verum, substs_verum]
      · rw [termSubstVec_W'_concl a, termSubstVec_V'_concl a]
end GodelQ.ITSubsts1

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

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

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

end GodelQ.ITSubsts1

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`conjunct_rename_second` 的项层推广**（`t` 层 1，`i < 2`）：

```
subst W (subst (^#i ∷ ?[^#2]) (iVE 1 t)) = subst ?[^#i] (iVE 0 (termSubst ?[^&0] t))
```

（`W = ?[^#0, ^#1, ^&0]`）。**由 T1（`iVE_subst_a0`）+ `substs_substs` 直接给出**：

`substs_substs` 把两次代换并成一次，向量变成
`termSubstVec 2 W (^#i ∷ ?[^#2]) = ^#i ∷ ^&0 ∷ 0`（`W.[i] = ^#i`，`W.[2] = ^&0`），
正是 T1 的向量 `^#a ∷ ?[^&0]`（`a := i`）。 -/
lemma isSemitermVec_W3 : IsSemitermVec ℒₛₑₜ (3:V) (2:V) (?[^#0, ^#1, ^&0] : V) := by
  refine IsSemitermVec.iff.mpr ⟨?_, fun j hj ↦ ?_⟩
  · rw [show (?[^#0, ^#1, ^&0] : V)
          = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
    simp only [len_adjoin, len_nil]; norm_num
  · show IsSemiterm ℒₛₑₜ (2:V)
      (((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))))).[j]
    rcases zero_or_succ j with (rfl | ⟨l, rfl⟩)
    · simp only [nth_adjoin_zero]; exact IsSemiterm.bvar.mpr (by norm_num)
    · rcases zero_or_succ l with (rfl | ⟨m, rfl⟩)
      · simp only [nth_adjoin_succ, nth_adjoin_zero]
        exact IsSemiterm.bvar.mpr (by norm_num)
      · have hm : m = 0 := by
          have h := hj
          rw [show (3:V) = (1:V) + 1 + 1 from by norm_num] at h
          have h2 := (add_lt_add_iff_right (1:V)).mp ((add_lt_add_iff_right (1:V)).mp h)
          exact lt_one_iff_eq_zero.mp h2
        subst hm
        simp only [nth_adjoin_succ, nth_adjoin_zero]
        exact IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) 0

/-- **`conjunct_rename_second` 的项层推广**（`t` 层 1，`i < 2`）：

```
subst W (subst (^#i ∷ ?[^#2]) (iVE 1 t)) = subst ?[^#i] (iVE 0 (termSubst ?[^&0] t))
```

由 T1（`iVE_subst_a0`）+ `substs_substs` 直接给出。 -/
lemma conjunct_rename_second_gen {i t : V} (hi : i < 2) (ht : IsSemiterm ℒₒᵣ (1:V) t) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 1) (iVE (1:V) t))
      = subst ℒₛₑₜ (?[^#i] : V) (iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V) t)) := by
  rw [show shiftVec (V := V) 2 1 = (?[^#2] : V) from by
    rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero, termBShiftVec_nil]]
  -- 内层向量 `^#i ∷ ?[^#2]`：长度 2、层数 3
  have hV : (^#i ∷ (?[^#2] : V) : V) = (^#i : V) ∷ ((^#2 : V) ∷ (0:V)) := rfl
  have hV2 : IsSemitermVec ℒₛₑₜ (2:V) (3:V) (^#i ∷ (?[^#2] : V)) := by
    rw [hV, show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr (lt_of_lt_of_le hi (by norm_num : (2:V) ≤ 3)), ?_⟩
    rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩
  -- `iVE 1 t` 的层数是 2
  have hiVE : IsSemiformula ℒₛₑₜ (2:V) (iVE (1:V) t) := by
    have h := isSemiformula_iVE (n := (1:V)) t ht
    rwa [show (1:V) + 1 = 2 by norm_num] at h
  -- 并成一次代换
  rw [substs_substs (L := ℒₛₑₜ) (l := (2:V)) (n := (3:V)) (m := (2:V))
    (p := iVE (1:V) t) (w := (?[^#0, ^#1, ^&0] : V)) (v := (^#i ∷ (?[^#2] : V)))
    hiVE isSemitermVec_W3 hV2]
  -- 向量恒等：`termSubstVec 2 W (^#i ∷ ?[^#2]) = ?[^#i, ^&0]`
  have hW : (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) := rfl
  have hvec : termSubstVec ℒₛₑₜ (2:V) (?[^#0, ^#1, ^&0] : V) (^#i ∷ (?[^#2] : V))
      = (?[^#i, ^&0] : V) := by
    rw [hW, hV]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := (2:V)))]
    rw [termSubst_bvar, termSubst_bvar]
    rw [show ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V)))).[i] = (^#i : V) from by
      rcases GodelQ.TranslateShiftCompat.lt_two_cases hi with rfl | rfl <;> simp]
    rw [show ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V)))).[2] = (^&0 : V) from by simp]
  rw [hvec]
  -- 目标正是 T1（`a := i`，`m := 3`）
  exact iVE_subst_a0 (m := (3:V)) (by norm_num) t ht i (lt_of_lt_of_le hi (by norm_num))

/-! ## 桥 `B(q)`：`iT` 与变量代换的相容律

```
subst ?[^&0] (iT 1 q) = iT 0 (subst ?[^&0] q)      -- q 层 1
```

归纳谓词带 `param = n` 护罩（照 `iT_shift` / `iT_neg` 的先例），
九支：rel / nrel / verum / falsum / and / or / all / exs + 骨架。
**原子支走 T1**（`iVE_subst_a0`）；**量词支**的关键是
`iT` 给每个量词多引一个 `domZero`，而 `subst (qVec w) domZero = domZero`
（**注意不是** `subst ?[^&0] domZero = domZero`，后者是假命题）。 -/

/-- `?[^&x]` 是任意语言、任意层的项向量（fvar 无 bvar）。 -/
lemma isSemitermVec_fvar (L : Language) [L.Encodable] [L.LORDefinable] (n x : V) :
    IsSemitermVec L 1 n (?[^&x] : V) :=
  IsSemitermVec.singleton.mpr (IsSemiterm.fvar n x)

/-- `subst ℒₒᵣ ?[^&0]` 之后的公式仍是 `IsUFormula`（无层谓词，故只要公式性）。
`n = 1` 让向量长度（1）与层数对上。 -/
lemma isSemiformula_subst_uformula {n p : V} (hn : n = (1:V)) (hp : IsSemiformula ℒₒᵣ n p) :
    IsUFormula ℒₒᵣ (subst ℒₒᵣ (?[^&0] : V) p) := by
  subst hn
  exact (IsSemiformula.subst (L := ℒₒᵣ) (n := (1:V)) (m := (1:V)) hp
    (isSemitermVec_fvar ℒₒᵣ (1:V) (0:V))).isUFormula

/-- `subst ℒₒᵣ ?[^&0]` 保持层数（`subst` 不改层；`?[^&0]` 长度 1，故要求 `n = 1`）。 -/
lemma isSemiformula_subst_fvar {n p : V} (hn : n = (1:V)) (hp : IsSemiformula ℒₒᵣ n p) :
    IsSemiformula ℒₒᵣ n (subst ℒₒᵣ (?[^&0] : V) p) := by
  subst hn
  exact IsSemiformula.subst (L := ℒₒᵣ) (n := (1:V)) (m := (1:V)) hp
    (isSemitermVec_fvar ℒₒᵣ (1:V) (0:V))

/-- **`subst (qVec w) domZero = domZero`**（`w` 是**任意**项向量，层数任意）。

`qVec w` 首分量恒为 `^#0`（`substs_all` 的防捕获位），保护 `domZero` 自己的 `#0`。 -/
lemma subst_qVec_domZero_gen {w k : V} (hw : IsSemitermVec ℒₛₑₜ (len w) k w) (hk : k = len w) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [GodelQ.TranslateShiftCompat.domZero_eq_cDomN (V := V)]
  have hd : IsSemiformula ℒₛₑₜ (1:V) ((cDomN : ℕ) : V) := isSemiformula_cDomN (V := V)
  have hlen : (1:V) ≤ len (qVec ℒₛₑₜ w) := by
    rw [Bootstrapping.qVec]; simp [len_adjoin]
  have hW : IsSemitermVec ℒₛₑₜ (len (qVec ℒₛₑₜ w)) (k + 1) (qVec ℒₛₑₜ w) := by
    refine IsSemitermVec.iff.mpr ⟨rfl, fun j hj ↦ ?_⟩
    have hj' : j < len (termBShiftVec ℒₛₑₜ (len w) w) + 1 := by
      rw [← len_adjoin, ← Bootstrapping.qVec]; exact hj
    rcases zero_or_succ j with (rfl | ⟨l, rfl⟩)
    · rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
        rw [Bootstrapping.qVec]; simp only [nth_adjoin_zero]]
      exact IsSemiterm.bvar.mpr (by norm_num)
    · have hl : l < len w := by
        have h := (add_lt_add_iff_right (1:V)).mp hj'
        rw [show len (termBShiftVec ℒₛₑₜ (len w) w) = len w from
          len_termBShiftVec (V := V) (L := ℒₛₑₜ) (k := len w) (ts := w) hw.isUTerm] at h
        exact h
      have hq1 : (qVec ℒₛₑₜ w).[l + 1] = (termBShiftVec ℒₛₑₜ (len w) w).[l] := by
        rw [Bootstrapping.qVec]; exact nth_adjoin_succ _ _ _
      rw [hq1, nth_termBShiftVec (V := V) (L := ℒₛₑₜ) (k := len w) (ts := w) (i := l)
        hw.isUTerm hl]
      have hbv : termBV ℒₛₑₜ (termBShift ℒₛₑₜ w.[l]) ≤ k + 1 :=
        (termBV_termBShift_le (L := ℒₛₑₜ) (hw.nth hl).isUTerm k).mpr (hw.nth hl).bv
      exact ⟨(hw.nth hl).isUTerm.termBShift, hbv⟩
  refine (GodelQ.TranslateShiftCompat.subst_congr_prefix (V := V) (n := (1:V)) (m := (k + 1))
    (k₁ := len (qVec ℒₛₑₜ w)) (k₂ := (1:V))
    (w := (qVec ℒₛₑₜ w)) (w' := (?[^#0] : V)) ((cDomN : ℕ) : V) hd
    hlen (by norm_num) hW
    (IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr (by norm_num)))
    (fun j hj ↦ by
      have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
      subst hj0
      rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
        rw [Bootstrapping.qVec]; simp only [nth_adjoin_zero]]
      rw [show (?[^#0] : V).[0] = (^#0 : V) from by simp only [nth_adjoin_zero]])).trans ?_
  refine subst_eq_self (L := ℒₛₑₜ) (n := (1:V)) (w := (?[^#0] : V))
    (p := ((cDomN : ℕ) : V)) hd
    (isSemitermVec_single_bvar (n := (1:V)) (by norm_num)) ?_
  intro i hi
  have hz : i = 0 := lt_one_iff_eq_zero.mp hi
  subst hz
  simp

/-! ## `subst` 推过 `qqAlls`（2026-10-12 新增）

`subst` 每推过一层 `^∀`，向量就换成 `qVec w`——这是 `substs_all` 的防捕获机制，
`iT` 的量词支要靠它把向量长度与层数对齐。 -/

/-- `subst` 推过 `qqAlls · k`：向量迭代 `k` 次 `qVec`。 -/
lemma substs_qqAlls : ∀ (k : ℕ) (X w : V), IsUFormula ℒₛₑₜ X →
    subst ℒₛₑₜ w (qqAlls X (k : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[k] w) X) (k : V) := by
  intro k
  induction k with
  | zero => intro X w _; simp
  | succ j ih =>
    intro X w hX
    rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
    rw [qqAlls_succ]
    have hu : IsUFormula ℒₛₑₜ (qqAlls X (j : V)) := isUFormula_qqAlls.mpr hX
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hu]
    rw [ih X (qVec ℒₛₑₜ w) hX]
    rw [qqAlls_succ]
    congr 3

/-- `qVec` 迭代两次作用在 `?[^&0]` 上给出 `[#0, #1, ^&0]`。 -/
lemma qVec_two : (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) := by
  rw [Function.iterate_succ_apply', Function.iterate_one]
  rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
    rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
    rw [show (1:V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]]
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^&0] : V) = (2:V) from by simp [len_adjoin, len_nil]; norm_num]
  rw [show (2:V) = 0 + 1 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
      (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
    termBShift_bvar, show (0:V) + 1 = 1 by norm_num,
    termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]

/-! ## 桥 `B(q)`：`iT` 与变量代换的相容律

```
iT 0 (subst ℒₒᵣ ?[^&0] σ) = subst ℒₛₑₜ ?[^&0] (iT 1 σ)      （σ 层 1）
```

用 `semiformula_result_induction`（Σ1 谓词，带 `param = n` 护罩）。
向量**固定为 `?[^&0]`**——层数账全在 `param` 里走：`iT` 的 `all`/`exs` 支把
`param ↦ param+1`，而 `subst` 推过 `qqAlls` 时向量变成 `qVec ?[^&0]`，
两者**同步**（`qVec ?[^&0] = ?[^#0, ^&0]` 的 `^#0` 保护绑定变量）。

**为什么不用 `∀ w` 版本**：`∀ w, IsSemitermVec …` 使谓词成为 Π1，
`semiformula_result_induction` 要 Σ1；而且量词支需要把 `ℒₛₑₜ` 的 `qVec w`
当 `ℒₒᵣ` 向量用，跨语言那条路是多余的。 -/
theorem iT_substs1 {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p → (n : V) = 1 →
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) p)
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n → param = (1:V) →
      iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) p)
        = subst ℒₛₑₜ (?[^&0] : V)
            (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → param = (1:V) →
        iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) p)
          = subst ℒₛₑₜ (?[^&0] : V) q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp h1
    have hh := key hp (rfl : n = n) h1
    rw [h1] at hh
    simpa only [iT] using hh
  · definability
  · -- rel
    intro n param k R v hR hv h h1
    -- `k = 2`（算术语言只有 0 元与 2 元关系符号）
    have hk : k = (2:V) := by
      rcases Arithmetic.isRel_iff_LOR.mp hR with hh | hh
      · exact hh.1
      · exact hh.1
    subst hk
    -- 两侧都展开成 `iTR`
    rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
    -- `substs_rel` 产出的向量是 `termSubstVec 2 ?[^&0] v`；
    -- `?[^&0]` 的层数 = `n`（= 原公式层数）
    -- `hv` 的层是 `n`；右侧用层 `(1:V)`。`h : (1:V) = n`，故造一个层 `(1:V)` 的副本。
    have hvp : IsSemitermVec ℒₒᵣ (2:V) param v := by rw [h]; exact hv
    have hvw : IsSemitermVec ℒₒᵣ (1:V) param (?[^&0] : V) :=
      IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) param (0:V))
    have hsub2 : IsSemitermVec ℒₒᵣ (2:V) (1:V)
        (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v) := by
      have hv1 : IsSemitermVec ℒₒᵣ (2:V) (1:V) v := by
        rwa [show param = (1:V) from h1] at hvp
      exact IsSemitermVec.termSubstVec (k := (2:V)) (v := v) hvw hv1
    rw [iT_rel hR hsub2.isUTerm]
    rw [show param = (1:V) from h1]
    change iTR 0 2 R (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v) =
      subst ℒₛₑₜ (?[^&0] : V) (iTR (1:V) 2 R v)
    rw [iTR, iTR]
    -- 分量展开
    rw [show (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v).[0]
          = termSubst ℒₒᵣ (?[^&0] : V) v.[0] from
        nth_termSubstVec hv.isUTerm (by norm_num),
      show (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v).[1]
          = termSubst ℒₒᵣ (?[^&0] : V) v.[1] from
        nth_termSubstVec hv.isUTerm (by norm_num)]
    -- 右侧先推 `subst` 过 `qqAlls · 2`
    have hYs : IsSemiformula ℒₛₑₜ (3:V)
        (conjunct 2 (1:V) 0 (iVE (1:V) v.[0]) ^⋏
          (conjunct 2 (1:V) 1 (iVE (1:V) v.[1]) ^⋏ ^⊤)) :=
      IsSemiformula.and.mpr
        ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (0:V))
          (isSemiformula_iVE (n := (1:V)) v.[0] (hvp.nth (by norm_num)))
          (by rw [h1]; norm_num),
         IsSemiformula.and.mpr
          ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
            (isSemiformula_iVE (n := (1:V)) v.[1] (hvp.nth (by norm_num)))
            (by rw [h1]; norm_num),
           IsSemiformula.verum⟩⟩
    have hX : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
      (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel R)
        (IsSemitermVec.doubleton.mpr
          ⟨IsSemiterm.bvar.mpr (by norm_num), IsSemiterm.bvar.mpr (by norm_num)⟩)).isUFormula
    rw [substs_qqAlls_two (IsUFormula.or.mpr ⟨hYs.isUFormula.neg, hX⟩)]
    congr 1
    -- 内层：`imp` 展成 `neg ⋎`，两侧分配
    rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl,
      show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
    rw [substs_or (L := ℒₛₑₜ) (w := (?[^#0, ^#1, ^&0] : V))
      (p := neg ℒₛₑₜ (conjunct 2 (1:V) 0 (iVE (1:V) v.[0]) ^⋏
        (conjunct 2 (1:V) 1 (iVE (1:V) v.[1]) ^⋏ ^⊤)))
      (q := subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) hYs.isUFormula.neg hX]
    congr 1
    · -- `neg` 分量：`substs_neg` + 两个合取块换名（`conjunct_rename_second_gen`）
      rw [substs_neg (L := ℒₛₑₜ) (n := (3:V)) (m := (3:V))
        (p := (conjunct 2 (1:V) 0 (iVE (1:V) v.[0]) ^⋏
          (conjunct 2 (1:V) 1 (iVE (1:V) v.[1]) ^⋏ ^⊤))) hYs
        (isSemitermVec_W3)]
      congr 1
      rw [substs_and (L := ℒₛₑₜ)
        (isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (0:V))
          (isSemiformula_iVE (n := (1:V)) v.[0] (hvp.nth (by norm_num)))
          (by rw [h1]; norm_num)).isUFormula
        (IsUFormula.and.mpr
          ⟨(isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
            (isSemiformula_iVE (n := (1:V)) v.[1] (hvp.nth (by norm_num)))
            (by rw [h1]; norm_num)).isUFormula,
           IsUFormula.verum⟩)]
      congr 1
      · -- 第一分量
        rw [conjunct, conjunct]
        congr 1
        · -- `subst ?[^#0] cDomN` 在 W 下不动
          exact (GodelQ.TranslateShiftCompat.subst_congr_prefix (V := V)
            (n := (1:V)) (m := (2:V)) (k₁ := (3:V)) (k₂ := (1:V))
            (w := (?[^#0, ^#1, ^&0] : V)) (w' := (?[^#0] : V))
            (subst ℒₛₑₜ (?[^#0] : V) (↑cDomN : V))
            (IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
              (isSemitermVec_single_bvar (n := (2:V)) (by norm_num)))
            (by norm_num) (by norm_num) isSemitermVec_W3
            (isSemitermVec_single_bvar (n := (1:V)) (by norm_num))
            (fun j hj ↦ by
              have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
              subst hj0
              rw [show (?[^#0, ^#1, ^&0] : V)
                    = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl,
                  show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
              simp only [nth_adjoin_zero])).symm
        · -- 第二分量：走 T1
          rw [show ((1:V) : V) = 1 from h1]
          rw [show shiftVec (V := V) 2 1 = (?[^#2] : V) from by
            rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero,
              termBShiftVec_nil]]
          rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
          exact conjunct_rename_second_gen (i := (0:V)) (by norm_num)
            (hv.nth (by norm_num))
      · -- 第二块（`conjunct 2 (1:V) 1 … ^⋏ ⊤`）
        rw [substs_and (L := ℒₛₑₜ)
          (isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
            (isSemiformula_iVE (n := (1:V)) v.[1] (hvp.nth (by norm_num)))
            (by rw [h1]; norm_num)).isUFormula
          IsUFormula.verum,
          substs_verum]
        congr 1
        rw [conjunct, conjunct]
        congr 1
        · exact (GodelQ.TranslateShiftCompat.subst_congr_prefix (V := V)
            (n := (1:V)) (m := (2:V)) (k₁ := (3:V)) (k₂ := (1:V))
            (w := (?[^#0, ^#1, ^&0] : V)) (w' := (?[^#1] : V))
            (subst ℒₛₑₜ (?[^#1] : V) (↑cDomN : V))
            (IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
              (isSemitermVec_single_bvar (n := (2:V)) (by norm_num)))
            (by norm_num) (by norm_num) isSemitermVec_W3
            (isSemitermVec_single_bvar (n := (1:V)) (by norm_num))
            (fun j hj ↦ by
              have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
              subst hj0
              rw [show (?[^#0, ^#1, ^&0] : V)
                    = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl,
                  show (?[^#1] : V) = ((^#1 : V) ∷ (0:V)) from rfl]
              simp only [nth_adjoin_zero])).symm
        · rw [show ((1:V) : V) = 1 from h1]
          rw [show shiftVec (V := V) 2 1 = (?[^#2] : V) from by
            rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero,
              termBShiftVec_nil]]
          rw [show (?[^#1] : V) = ((^#1 : V) ∷ (0:V)) from rfl]
          exact conjunct_rename_second_gen (i := (1:V)) (by norm_num)
            (hv.nth (by norm_num))
    · -- `cRel` 分量：引号化句子，`subst` 不动
      rw [show subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))
          = subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R) from by
        have hid : subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R) = cRel R :=
          subst_eq_self (L := ℒₛₑₜ) (n := (2:V)) (isSemiformula_cRel R)
            (IsSemitermVec.doubleton.mpr
              ⟨IsSemiterm.bvar.mpr (by norm_num), IsSemiterm.bvar.mpr (by norm_num)⟩)
            (fun i hi ↦ by
              rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0:V)) from rfl]
              rcases lt_two_cases hi with rfl | rfl <;> simp)
        rw [hid]
        exact (GodelQ.TranslateShiftCompat.subst_congr_prefix (V := V)
          (n := (2:V)) (m := (2:V)) (k₁ := (3:V)) (k₂ := (2:V))
          (w := (?[^#0, ^#1, ^&0] : V)) (w' := (?[^#0, ^#1] : V)) (cRel R)
          (isSemiformula_cRel R) (by norm_num) (by norm_num) isSemitermVec_W3
          (IsSemitermVec.doubleton.mpr
            ⟨IsSemiterm.bvar.mpr (by norm_num), IsSemiterm.bvar.mpr (by norm_num)⟩)
          (fun j hj ↦ by
            rw [show (?[^#0, ^#1, ^&0] : V)
                  = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl,
                show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0:V)) from rfl]
            rcases lt_two_cases hj with rfl | rfl <;> simp)).trans hid]
  · -- nrel
    intro n param k R v hR hv h h1
    sorry
  · -- verum
    intro n param h h1
    show iT (0:V) (subst ℒₒᵣ (?[^&0] : V) ^⊤) = subst ℒₛₑₜ (?[^&0] : V) (iT.construction.verum param)
    rw [substs_verum, iT_verum]
    exact (substs_verum (L := ℒₛₑₜ) (?[^&0] : V)).symm
  · -- falsum
    intro n param h h1
    show iT (0:V) (subst ℒₒᵣ (?[^&0] : V) ^⊥) = subst ℒₛₑₜ (?[^&0] : V) (iT.construction.falsum param)
    rw [substs_falsum, iT_falsum]
    exact (substs_falsum (L := ℒₛₑₜ) (?[^&0] : V)).symm
  · -- and
    intro n param p q hp hq ihp ihq h h1
    rw [← h] at hp hq
    show iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (p ^⋏ q)) =
      subst ℒₛₑₜ (?[^&0] : V) (iT.construction.and param p q
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q))
    rw [substs_and hp.isUFormula hq.isUFormula]
    conv_rhs => rw [show iT.construction.and param p q
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q)
        = (iT param p ^⋏ iT param q) from rfl]
    rw [iT_and (isSemiformula_subst_uformula h1 hp) (isSemiformula_subst_uformula h1 hq)]
    rw [substs_and (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋏ ·) (ihp h h1) (ihq h h1)
  · -- or
    intro n param p q hp hq ihp ihq h h1
    rw [← h] at hp hq
    show iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (p ^⋎ q)) =
      subst ℒₛₑₜ (?[^&0] : V) (iT.construction.or param p q
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q))
    rw [substs_or hp.isUFormula hq.isUFormula]
    conv_rhs => rw [show iT.construction.or param p q
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
        (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q)
        = (iT param p ^⋎ iT param q) from rfl]
    rw [iT_or (isSemiformula_subst_uformula h1 hp) (isSemiformula_subst_uformula h1 hq)]
    rw [substs_or (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋎ ·) (ihp h h1) (ihq h h1)
  · -- all
    intro n param p hp ih h h1
    rw [← h] at hp
    -- 目标：`iT 0 (subst ?[^&0] (^∀ p)) = subst ?[^&0] (result param (^∀ p))`
    -- 左：`subst ℒₒᵣ` 推过 `^∀`，再 `iT_all`
    rw [Bootstrapping.substs_all (L := ℒₒᵣ) hp.isUFormula]
    have hvw : IsSemitermVec ℒₒᵣ (1:V) (param + 1) (?[^&0] : V) :=
      IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (param + 1) (0:V))
    -- `qVec ?[^&0] = ?[^#0, ^&0]`（长度 2 = param + 1，因 param = 1）
    have hqvS0 : IsSemitermVec ℒₛₑₜ (1:V) (param + 1) (?[^&0] : V) :=
      IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (param + 1) (0:V))
    have hqvS : IsSemitermVec ℒₛₑₜ (param + 1) (param + 1) (qVec ℒₛₑₜ (?[^&0] : V)) := by
      have h := IsSemitermVec.qVec (k := (1:V)) hqvS0
      rw [show (1:V) + 1 = param + 1 from by rw [h1]] at h
      exact h
    have hqv : qVec ℒₒᵣ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
      rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
      rw [show (1:V) = 0 + 1 by norm_num,
        termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
        termBShift_fvar, termBShiftVec_nil]
    have hvw' : IsSemitermVec ℒₒᵣ (param + 1) (param + 1) (qVec ℒₒᵣ (?[^&0] : V)) := by
      rw [hqv, show (param : V) + 1 = 2 from by rw [h1]; norm_num]
      exact IsSemitermVec.doubleton.mpr
        ⟨IsSemiterm.bvar.mpr (by norm_num), IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (2:V) (0:V)⟩
    rw [iT_all (hp.subst hvw').isUFormula]
    -- 右：`result_all` 展开
    rw [UformulaRec1.Construction.result_all (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param p = 1)]
    change (^∀ (imp ℒₛₑₜ domZero (iT (0 + 1) (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) p))) : V) =
      subst ℒₛₑₜ (?[^&0] : V)
        (^∀ (imp ℒₛₑₜ domZero
          ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
            (iT.construction.allChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∀ (imp ℒₛₑₜ domZero (iT (0 + 1) (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) p))) : V) =
      subst ℒₛₑₜ (?[^&0] : V)
        (^∀ (imp ℒₛₑₜ domZero (iT (iT.construction.allChanges param 0) p)))
    rw [show iT.construction.allChanges param 0 = param + 1 from rfl]
    rw [substs_all (L := ℒₛₑₜ)
      (IsUFormula.imp.mpr ⟨(isSemiformula_domZero (n := param)).isUFormula,
        (isSemiformula_iT p hp).isUFormula⟩)]
    congr 1
    -- 现在：`imp domZero (iT 1 (subst (qVec ?[^&0]) p))
    --        = imp (subst (qVec ?[^&0]) domZero) (iT param (subst (qVec ?[^&0]) p))`
    rw [subst_imp (n := (param + 1)) (m := (param + 1 + 1))
      (isSemiformula_domZero (n := param))
      (isSemiformula_iT p hp)
      (by
        have h := hqvS
        rw [show (param + 1 : V) = param + 1 + 1 from by omega] at h
        exact h)]
    show imp ℒₛₑₜ (subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (domZero (V := V)))
        (iT param (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) p)) =
      imp ℒₛₑₜ (subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (domZero (V := V)))
        (iT param (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) p))
    rw [subst_qVec_domZero_gen (isSemitermVec_fvar ℒₛₑₜ (1:V) (0:V)) (by rfl)]
    -- 现在：`imp domZero (iT (0+1) X) = imp domZero (iT param X)`，其中 `param = 1`
    rw [show (0 : V) + 1 = param from by rw [h1]; norm_num]
  · -- exs
    intro n param p hp ih h h1
    rw [← h] at hp
    rw [Bootstrapping.substs_ex (L := ℒₒᵣ) hp.isUFormula]
    have hvw : IsSemitermVec ℒₒᵣ (1:V) (param + 1) (?[^&0] : V) :=
      IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (param + 1) (0:V))
    have hvw' : IsSemitermVec ℒₒᵣ (param + 1) (param + 1) (?[^&0] : V) := by
      rw [h1]; exact IsSemitermVec.singleton.mpr
        (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (2:V) (0:V))
    rw [iT_exs (hp.subst hvw').isUFormula]
    rw [UformulaRec1.Construction.result_exs (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param p = 1)]
    change (^∃ (domZero ^⋏ iT (0 + 1) (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) p)) : V) =
      subst ℒₛₑₜ (?[^&0] : V)
        (^∃ (domZero ^⋏
          ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
            (iT.construction.exsChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∃ (domZero ^⋏ iT (0 + 1) (subst ℒₒᵣ (qVec ℒₒᵣ (?[^&0] : V)) p)) : V) =
      subst ℒₛₑₜ (?[^&0] : V)
        (^∃ (domZero ^⋏ iT (iT.construction.exsChanges param 0) p))
    rw [show iT.construction.exsChanges param 0 = param + 1 from rfl]
    rw [substs_ex (L := ℒₛₑₜ)
      (IsUFormula.and.mpr ⟨(isSemiformula_domZero (n := param)).isUFormula,
        (isSemiformula_iT p hp).isUFormula⟩)]
    congr 1
    rw [substs_and (L := ℒₛₑₜ) (isSemiformula_domZero (n := param)).isUFormula
      (isSemiformula_iT p hp).isUFormula]
    rw [subst_qVec_domZero_gen (isSemitermVec_fvar ℒₛₑₜ (1:V) (0:V)) (by rfl)]
    rw [show (0 : V) + 1 = param from by rw [h1]; norm_num]

/-- **桥 `B(q)`**（`hkey_probe` 需要的形状，`n = 1`，方向取反）。 -/
theorem iT_substs1' {q : V} (hq : IsSemiformula ℒₒᵣ 1 q) :
    subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) q) =
      iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) q) :=
  (iT_substs1 q hq (by norm_num)).symm

end GodelQ.ITSubsts1
