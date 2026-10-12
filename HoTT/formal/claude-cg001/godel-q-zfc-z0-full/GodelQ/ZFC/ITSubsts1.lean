import GodelQ.ZFC.ITShift
import GodelQ.ZFC.ShiftConjunct

/-!
# CG-007 · W8 第二层（十七）：`iT` 与变量代换的相容律

`hAll` 支需要：把 `iT 1 q` 的自由变量换成 `^&0`（即 `free`/`substs1` 所做的事），
等价于先把 `q` 的自由变量换掉再以层 0 翻译：

```
subst ℒₛₑₜ ?[^&0] (iT 1 q) = iT 0 (subst ℒₒᵣ ?[^&0] q)          -- 桥（本文件的目标）
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

end GodelQ.ITSubsts1
