-- CG-009: `iVE_open` 的 func 支 —— `ve2` 与开口代入交换。
--
-- ## 结构（与 `TranslateShiftCompat.shift_ve2` 同构，`shift ↦ subst (QvecV (mm+1))`）
--
-- `ve2 n 2 f w = qqAlls B 2`，`B = imp (A₀ ⋏ (A₁ ⋏ ⊤)) C`，
-- `A_i = conjunct 3 n i w.[i]`，`C = subst [^#2,^#0,^#1] (cFunc 2 f)`，`n = mm+1`。
--
-- `subst (QvecV (mm+1))` 下降两层绑定 ⇒ 体内向量 = `qVec²(QvecV (mm+1)) = QvecV (mm+3)`：
--   * `A_i` 部分：`conjunct 3 (mm+1) i y` 的两个分量都只读索引 ≤ mm+2，
--     而 `QvecV (mm+3)` 在 `j < mm+3` 处是 `^#j`（`subst_QvecV_conjunct` 的 `b=3` 版）；
--   * `C` 部分：`[^#2,^#0,^#1]` 只读索引 0,1,2（`termSubstVec_three_QvecV_three`）。
-- 于是两侧体内公式相同（`w'.[i] = subst (QvecV (mm+1)) w.[i]`）。
import GodelQ.ZFC.IVEOpenFunc12

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc15
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- `subst (QvecV (mm+1))` 的下降：`qqAlls B 2` 处体内向量是 `QvecV (mm+3)`。 -/
lemma subst_QvecV_qqAlls_two {mm B : V} (hB : IsUFormula ℒₛₑₜ B) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (qqAlls B 2) =
      qqAlls (subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) B) 2 := by
  have hvec : qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) (mm + 1))) = QvecV (V := V) (mm + 3) := by
    rw [← QvecV_succ (mm + 1)]
    have e : (mm + 1 : V) + 1 = mm + 2 := by ring
    rw [e, ← QvecV_succ (mm + 2)]
    congr 1
    ring
  rw [show qqAlls B 2 = ^∀ (^∀ B) from by
    rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ,
      show (1 : V) = 0 + 1 by norm_num, qqAlls_succ, qqAlls_zero]]
  rw [show qqAlls (subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) B) 2 = ^∀ (^∀ (subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) B)) from by
    rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ,
      show (1 : V) = 0 + 1 by norm_num, qqAlls_succ, qqAlls_zero]]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) (IsUFormula.all.mpr hB)]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hB, hvec]

end GodelQ.IVEOpenFunc15

#print axioms GodelQ.IVEOpenFunc15.subst_QvecV_qqAlls_two



namespace GodelQ.IVEOpenFunc15
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- `mm + 3 < mm + 4`. -/
lemma lt_add_three_four (mm : V) : (mm + 3 : V) < mm + 4 := by
  have h := lt_add_one (mm + 3)
  have e : (mm + 3 : V) + 1 = mm + 4 := by ring
  rwa [e] at h

/-- **`conjunct` 的交换律**：`QvecV (mm+3)` 把 `conjunct` 推到内层代入之后。
    桥接引理是 `substVec_func_eq`（两个复合向量相等）。 -/
lemma subst_QvecV_conjunct_comm {mm i y : V} (hy : IsSemiformula ℒₛₑₜ (mm + 2) y)
    (hi : i < mm + 3) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) (conjunct 3 (mm + 1) i y) =
      conjunct 3 (mm + 1) i (subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) y) := by
  have hi4 : i < mm + 4 := lt_trans hi (lt_add_three_four mm)
  have hQ3 : IsSemitermVec ℒₛₑₜ (mm + 4) (mm + 4) (QvecV (V := V) (mm + 3)) :=
    isSemitermVec_QvecV_three (n := mm)
  have hQ1 : IsSemitermVec ℒₛₑₜ (mm + 2) (mm + 2) (QvecV (V := V) (mm + 1)) := by
    have h := isSemitermVec_QvecV (V := V) (mm + 1)
    have e : (mm + 1 : V) + 1 = mm + 2 := by ring
    rwa [e] at h
  have hv : IsSemitermVec ℒₛₑₜ (mm + 2) (mm + 4)
      ((^#i : V) ∷ shiftVec 3 (mm + 1)) :=
    isSemitermVec_cons_shiftVec3 mm i hi4
  have hw : IsSemitermVec ℒₛₑₜ 1 (mm + 4) (?[^#i] : V) :=
    isSemitermVec_single_bvar (n := mm + 4) (by
      have e : (mm + 3 : V) + 1 = mm + 4 := by ring
      exact e ▸ hi4)
  have hdom : subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V) := by
    rw [show subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V))
          = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (mm + 3)) (?[^#i] : V))
            ((cDomN : ℕ) : V) from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) (n := mm + 4) (m := mm + 4)
        (p := ((cDomN : ℕ) : V)) isSemiformula_cDomN hQ3 hw]
    rw [show (?[^#i] : V) = (^#i : V) ∷ (0 : V) from rfl,
      termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar,
      GodelQ.ITRSubstOpen.nth_QvecV_lt (mm + 3) i hi]
  have hbody : subst ℒₛₑₜ (QvecV (V := V) (mm + 3))
        (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 (mm + 1)) y)
      = subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 (mm + 1))
        (subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) y) := by
    rw [show subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 (mm + 1)) y)
          = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (mm + 2) (QvecV (V := V) (mm + 3))
              ((^#i : V) ∷ shiftVec 3 (mm + 1))) y from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := mm + 2) (n := mm + 4) (m := mm + 4)
        (p := y) hy hQ3 hv]
    rw [show subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 (mm + 1)) (subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) y)
          = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (mm + 2) ((^#i : V) ∷ shiftVec 3 (mm + 1))
              (QvecV (V := V) (mm + 1))) y from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := mm + 2) (n := mm + 2) (m := mm + 4)
        (p := y) hy hv hQ1]
    rw [show termSubstVec ℒₛₑₜ (mm + 2) (QvecV (V := V) (mm + 3))
          ((^#i : V) ∷ shiftVec 3 (mm + 1))
        = termSubstVec ℒₛₑₜ (mm + 2) ((^#i : V) ∷ shiftVec 3 (mm + 1))
          (QvecV (V := V) (mm + 1)) from by
      have h := GodelQ.IVEOpenFunc6.substVec_func_eq mm i hi4 (by
        intro h; rw [h] at hi
        exact absurd hi (not_lt_of_ge (le_refl (mm + 3))))
      have e : ((mm + 1) + 1 : V) = mm + 2 := by ring
      rw [e] at h
      exact h.symm]
  unfold conjunct
  rw [Bootstrapping.substs_and (L := ℒₛₑₜ) (V := V)
    (IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN hw).isUFormula
    (IsSemiformula.subst (L := ℒₛₑₜ) hy hv).isUFormula]
  rw [hdom, hbody]

end GodelQ.IVEOpenFunc15

#print axioms GodelQ.IVEOpenFunc15.subst_QvecV_conjunct_comm

namespace GodelQ.IVEOpenFunc15
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- `subst (QvecV (mm+3)) (subst [^#2,^#0,^#1] (cFunc 2 f)) = subst [^#2,^#0,^#1] (cFunc 2 f)`。 -/
lemma subst_QvecV_subst_cFunc' {mm f : V} :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 3))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) =
      subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f) := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f) :=
    isSemiformula_cFunc_arity2 (by norm_num : (2 : V) ≠ 0) f
  have hQ3 : IsSemitermVec ℒₛₑₜ (mm + 4) (mm + 4) (QvecV (V := V) (mm + 3)) :=
    isSemitermVec_QvecV_three (n := mm)
  have hv : IsSemitermVec ℒₛₑₜ 3 (mm + 4) ((^#2 : V) ∷ ?[^#0, ^#1]) := by
    rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
    have h := isSemitermVec_three_bvars (mm + 1)
    have e : (3 : V) + (mm + 1) = mm + 4 := by ring
    rw [e] at h
    exact h
  rw [show subst ℒₛₑₜ (QvecV (V := V) (mm + 3))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 3 (QvecV (V := V) (mm + 3))
          ((^#2 : V) ∷ ?[^#0, ^#1])) (cFunc 2 f) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 3) (n := mm + 4) (m := mm + 4)
      (p := cFunc 2 f) hc hQ3 hv]
  rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
  rw [GodelQ.IVEOpenFunc10.termSubstVec_three_QvecV_three (mm := mm)]

end GodelQ.IVEOpenFunc15

#print axioms GodelQ.IVEOpenFunc15.subst_QvecV_subst_cFunc'

namespace GodelQ.IVEOpenFunc15
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- **`ve2` 与 `subst (QvecV (mm+1))` 交换**（`k = 2` 支）。

`w'.[i] = subst (QvecV (mm+1)) w.[i]`（逐分量），结论把外层代入推进两层绑定子。 -/
lemma subst_QvecV_ve2 {mm f w w' : V} (hk : (2 : V) ≠ 0)
    (hw0 : IsSemiformula ℒₛₑₜ (mm + 2) w.[0])
    (hw1 : IsSemiformula ℒₛₑₜ (mm + 2) w.[1])
    (hw'0 : subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) w.[0] = w'.[0])
    (hw'1 : subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) w.[1] = w'.[1]) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (ve2 (mm + 1) 2 f w) = ve2 (mm + 1) 2 f w' := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f) := isSemiformula_cFunc_arity2 hk f
  have hB : IsUFormula ℒₛₑₜ
      (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) := by
    rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
    exact (IsSemiformula.subst (L := ℒₛₑₜ) (m := 3 + (mm + 1)) hc
      (isSemitermVec_three_bvars (mm + 1))).isUFormula
  have hw0' : IsSemiformula ℒₛₑₜ (mm + 1 + 1) w.[0] := by
    have e : (mm + 1 + 1 : V) = mm + 2 := by ring
    rwa [e]
  have hw1' : IsSemiformula ℒₛₑₜ (mm + 1 + 1) w.[1] := by
    have e : (mm + 1 + 1 : V) = mm + 2 := by ring
    rwa [e]
  have hA0 : IsSemiformula ℒₛₑₜ (3 + (mm + 1)) (conjunct 3 (mm + 1) 0 w.[0]) :=
    isSemiformula_conjunct (b := 3) (n := mm + 1) (i := 0) hw0' (zero_lt_three_add (mm + 1))
  have hA1 : IsSemiformula ℒₛₑₜ (3 + (mm + 1)) (conjunct 3 (mm + 1) 1 w.[1]) :=
    isSemiformula_conjunct (b := 3) (n := mm + 1) (i := 1) hw1' (one_lt_three_add (mm + 1))
  have hA01 : IsSemiformula ℒₛₑₜ (3 + (mm + 1)) (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤) :=
    IsSemiformula.and.mpr ⟨hA1, IsSemiformula.verum⟩
  have hA : IsSemiformula ℒₛₑₜ (3 + (mm + 1))
      (conjunct 3 (mm + 1) 0 w.[0] ^⋏ (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hA0, hA01⟩
  -- 体内公式
  have hbody : IsUFormula ℒₛₑₜ
      (neg ℒₛₑₜ (conjunct 3 (mm + 1) 0 w.[0] ^⋏ (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) :=
    IsUFormula.or.mpr ⟨hA.isUFormula.neg, hB⟩
  -- 体内 = 目标体内的公式
  have hinner : subst ℒₛₑₜ (QvecV (V := V) (mm + 3))
      (neg ℒₛₑₜ (conjunct 3 (mm + 1) 0 w.[0] ^⋏ (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))
      = neg ℒₛₑₜ (conjunct 3 (mm + 1) 0 w'.[0] ^⋏ (conjunct 3 (mm + 1) 1 w'.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f) := by
    have hQ3' : IsSemitermVec ℒₛₑₜ (3 + (mm + 1)) (mm + 4) (QvecV (V := V) (mm + 3)) := by
      have h := isSemitermVec_QvecV_three (n := mm)
      have e : (3 : V) + (mm + 1) = mm + 4 := by ring
      rw [e]
      exact h
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hA.isUFormula.neg hB,
      Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 3 + (mm + 1)) hA hQ3',
      Bootstrapping.substs_and (L := ℒₛₑₜ) hA0.isUFormula hA01.isUFormula,
      Bootstrapping.substs_and (L := ℒₛₑₜ) hA1.isUFormula IsUFormula.verum,
      Bootstrapping.substs_verum (L := ℒₛₑₜ)]
    have h0lt : (0 : V) < mm + 3 := by
      have h := zero_lt_three_add mm
      have e : (3 : V) + mm = mm + 3 := by ring
      rwa [e] at h
    have h1lt : (1 : V) < mm + 3 := by
      have h := one_lt_three_add mm
      have e : (3 : V) + mm = mm + 3 := by ring
      rwa [e] at h
    rw [subst_QvecV_conjunct_comm (mm := mm) (i := 0) hw0 h0lt,
      subst_QvecV_conjunct_comm (mm := mm) (i := 1) hw1 h1lt,
      hw'0, hw'1, subst_QvecV_subst_cFunc']
  -- 目标体的公式性（供 substs_all 用）
  rw [ve2]
  show subst ℒₛₑₜ (QvecV (V := V) (mm + 1))
      (qqAlls (neg ℒₛₑₜ (conjunct 3 (mm + 1) 0 w.[0] ^⋏ (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) 2) = _
  rw [subst_QvecV_qqAlls_two (mm := mm) hbody]
  rw [ve2]
  rw [show imp ℒₛₑₜ (conjunct 3 (mm + 1) 0 w'.[0] ^⋏ (conjunct 3 (mm + 1) 1 w'.[1] ^⋏ ^⊤))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))
      = neg ℒₛₑₜ (conjunct 3 (mm + 1) 0 w'.[0] ^⋏ (conjunct 3 (mm + 1) 1 w'.[1] ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f) from rfl]
  rw [hinner]

end GodelQ.IVEOpenFunc15

#print axioms GodelQ.IVEOpenFunc15.subst_QvecV_ve2
