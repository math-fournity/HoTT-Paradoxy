-- CG-009: (★★) —— 开口律的项层核心引理（完整版）。
--
--     subst Vw (iVE m (termSubst (QvecVOr m) t)) = subst Ww (iVE (m+1) t)
--
-- 其中 `VRel m Vw Ww`（`len Vw = m+1`、`len Ww = m+2`）。
--
-- ## 用途
--
-- `iT_subst_open` 的 rel 支（取 `Vw = ^#j ∷ shiftVec 2 m`、`Ww = [^#j, ^#2, …, ^#(m+1), ^&0]`）
-- 与 func 支（`ve2` 的向量）都归约到此。
--
-- ## 归纳（对 `t`，用 `IsSemiterm.sigma1_induction`）
--
-- * bvar：`(QvecVOr m).[z]` 是 `^#z`（z<m）或 `^&0`（z=m）；两侧 `eqAtom` 的读位由 `VRel` 给出
-- * fvar：`termSubst` 不动 fvar；`subst_iVE_fvar_eq`
-- * func k=0：`ve0` 不含参数向量；`subst_iVE_func_zero_eq`
-- * func k=2：`ve2` 下降两层，向量变换为 `Vw₁, Ww₁`（`VRel_transform` 保持关系），
--   对 `v.[i]` 用归纳假设（`subst_ve2_general`）
import GodelQ.ZFC.ITSubstOpen5

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen6
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5

/-! ## 零件 A：`subst` 下降 `qqAlls B 2`（任意向量版） -/

/-- **`subst` 下降 `qqAlls B 2`（任意向量版）**：体内向量是 `qVec (qVec W)`。 -/
lemma subst_qqAlls_two {W B : V} (hB : IsUFormula ℒₛₑₜ B) :
    subst ℒₛₑₜ W (qqAlls B 2) = qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ W)) B) 2 := by
  rw [show qqAlls B 2 = ^∀ (^∀ B) from by
    rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ]
    rw [show (1 : V) = 0 + 1 by norm_num, qqAlls_succ, qqAlls_zero]]
  rw [show qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ W)) B) 2
      = ^∀ (^∀ subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ W)) B) from by
    rw [show (2 : V) = 1 + 1 by norm_num, qqAlls_succ]
    rw [show (1 : V) = 0 + 1 by norm_num, qqAlls_succ, qqAlls_zero]]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) (IsUFormula.all.mpr hB)]
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hB]

/-! ## 零件 B：`qVec² X` 固定 `subst ?[^#i] cDomN`（i ∈ {0,1}） -/

/-- **`qVec² X` 固定 `subst ?[^#i] cDomN`**（`i ≤ 1` 时 `(qVec² X).[i] = ^#i`，与 `X` 无关）。 -/
lemma subst_qvec2_cDomN {X i : V} (hX : IsUTermVec ℒₛₑₜ (len X) X) (hi : i ≤ 1) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)) (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V)) =
      subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V) := by
  have hQ3 : IsSemitermVec ℒₛₑₜ ((len X + 1) + 1)
      ((listMax (termBVVec ℒₛₑₜ (len X) X) + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)) :=
    hX.isSemitermVec.qVec.qVec
  have hlt : i < (len X + 1) + 1 := lt_of_le_of_lt hi (lt_add_self_add_one 1 (len X))
  have hw : IsSemitermVec ℒₛₑₜ 1 ((len X + 1) + 1) (?[^#i] : V) :=
    isSemitermVec_single_bvar (n := (len X + 1) + 1) hlt
  rw [show subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ X))
        (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)) (?[^#i] : V))
        ((cDomN : ℕ) : V) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) (p := ((cDomN : ℕ) : V))
      isSemiformula_cDomN hQ3 hw]
  rw [show (?[^#i] : V) = (^#i : V) ∷ (0 : V) from rfl,
    termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar]
  rcases le_one_iff_eq_zero_or_one.mp hi with rfl | rfl
  · rw [nth_qVec_qVec_zero]
  · rw [nth_qVec_qVec_one hX]

/-! ## 零件 C：`QvecVOr m` 的低层版本（层 `m` 而非 `m+1`） -/

lemma nth_QvecVOr {m j : V} (hj : j ≤ m) :
    (QvecVOr (V := V) m).[j] = if j = m then (^&0 : V) else ^#j := by
  rcases eq_or_lt_of_le hj with rfl | hlt
  · rw [if_pos rfl, nth_QvecVOr_last]
  · rw [if_neg (ne_of_lt hlt), nth_QvecVOr_lt m j hlt]

/-- `QvecVOr m` 在**层 `m`** 下也是项向量（项为 `^#0, …, ^#(m-1), ^&0`，最大 bvar 索引 `m-1`）。 -/
lemma isSemitermVec_QvecVOr_low {m : V} :
    IsSemitermVec ℒₒᵣ (m + 1) m (QvecVOr (V := V) m) := by
  refine IsSemitermVec.iff.mpr ⟨len_QvecVOr m, ?_⟩
  intro i hi
  rw [nth_QvecVOr (lt_succ_iff_le.mp hi)]
  split
  · exact IsSemiterm.fvar m 0
  · rename_i hne
    exact IsSemiterm.bvar.mpr (lt_of_le_of_ne (lt_succ_iff_le.mp hi) hne)

/-! ## 零件 D：`qVec² X` 的项层展开（`cFunc` 代入向量的第一项） -/

/-- `termSubstVec 3 (qVec² X) [^#2, ^#0, ^#1] = [termBShift² X.[0], ^#0, ^#1]`（逐项）。 -/
lemma termSubstVec_three_qvec2 {X : V} (hX : IsUTermVec ℒₛₑₜ (len X) X)
    (hpos : (0 : V) < len X) :
    termSubstVec ℒₛₑₜ 3 (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)) ((^#2 : V) ∷ ?[^#0, ^#1]) =
      ?[termBShift ℒₛₑₜ (termBShift ℒₛₑₜ X.[0]), ^#0, ^#1] := by
  have hv : IsUTermVec ℒₛₑₜ 3 ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
    isUTermVec_three_bvars
  apply nth_ext' 3
  · rw [len_termSubstVec hv]
  · rw [show (?[termBShift ℒₛₑₜ (termBShift ℒₛₑₜ X.[0]), (^#0 : V), ^#1] : V)
        = termBShift ℒₛₑₜ (termBShift ℒₛₑₜ X.[0]) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl,
      len_adjoin, len_adjoin, len_adjoin]
    norm_num
  · intro j hj
    have hle : j ≤ 2 := lt_succ_iff_le.mp (by
      simpa [show (3 : V) = 2 + 1 by norm_num] using hj)
    rcases le_two_iff_eq_zero_or_one_or_two.mp hle with rfl | rfl | rfl
    · rw [nth_termSubstVec hv (by norm_num : (0 : V) < 3), nth_adjoin_zero, termSubst_bvar]
      rw [show (2 : V) = 0 + 2 by norm_num, nth_qVec_qVec hX hpos, nth_adjoin_zero]
    · rw [nth_termSubstVec hv (by norm_num : (1 : V) < 3)]
      rw [show ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)).[1] = ^#0 from by
        rw [show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]]
      rw [termSubst_bvar, nth_qVec_qVec_zero]
      rw [show ((termBShift ℒₛₑₜ (termBShift ℒₛₑₜ X.[0]) : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)).[1]
          = ^#0 from by
        rw [show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]]
    · rw [nth_termSubstVec hv (by norm_num : (2 : V) < 3)]
      rw [show ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)).[2] = ^#1 from by
        rw [show (2 : V) = 1 + 1 by norm_num, nth_adjoin_succ,
          show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]]
      rw [termSubst_bvar, nth_qVec_qVec_one hX]
      rw [show ((termBShift ℒₛₑₜ (termBShift ℒₛₑₜ X.[0]) : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)).[2]
          = ^#1 from by
        rw [show (2 : V) = 1 + 1 by norm_num, nth_adjoin_succ,
          show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]]


/-! ## 变换后的代入向量（缩写） -/

/-- LHS 侧的变换向量。 -/
noncomputable abbrev Vw1 (m Vw i : V) : V :=
  termSubstVec ℒₛₑₜ (m + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) ((^#i : V) ∷ shiftVec 3 m)

/-- RHS 侧的变换向量。 -/
noncomputable abbrev Ww1 (m Ww i : V) : V :=
  termSubstVec ℒₛₑₜ ((m + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww)) ((^#i : V) ∷ shiftVec 3 (m + 1))

/-! ## 零件 E：conjunct 的开口展开（任意向量版） -/

/-- **conjunct 的开口展开（任意向量版）**：
    `subst (qVec² Vw) (conjunct 3 m i y)`
    `= (subst ?[^#i] cDomN) ⋏ subst (termSubstVec (m+1) (qVec² Vw) (^#i ∷ shiftVec 3 m)) y`。 -/
lemma subst_qvec2_conjunct_gen {m i y Vw : V} (hVw : IsUTermVec ℒₛₑₜ (m + 1) Vw)
    (hy : IsSemiformula ℒₛₑₜ (m + 1) y) (hi : i ≤ 1) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) (conjunct 3 m i y) =
      subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V) ^⋏
        subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (m + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
          ((^#i : V) ∷ shiftVec 3 m)) y := by
  have hi3 : i < 3 + m := lt_of_le_of_lt hi (one_lt_three_add m)
  have h1 : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := i + 1) (by simp))).isUFormula
  have h2 : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 m) y) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hy
      (isSemitermVec_shiftVec_cons (b := 3) (n := m) (i := i) hi3)).isUFormula
  have hQ : IsSemitermVec ℒₛₑₜ ((m + 1) + 1 + 1)
      ((listMax (termBVVec ℒₛₑₜ (m + 1) Vw) + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) :=
    hVw.isSemitermVec.qVec.qVec
  have hv : IsSemitermVec ℒₛₑₜ (m + 1) ((m + 1) + 1 + 1) ((^#i : V) ∷ shiftVec 3 m) :=
    LayerMono.IsSemitermVec.mono
      (isSemitermVec_shiftVec_cons (b := 3) (n := m) (i := i) hi3)
      (le_of_eq (by ring : (3 : V) + m = (m + 1) + 1 + 1))
  unfold conjunct
  rw [Bootstrapping.substs_and (L := ℒₛₑₜ) h1 h2]
  congr 1
  · exact subst_qvec2_cDomN (hVw.lh ▸ hVw) hi
  · rw [show subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 m) y)
        = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (m + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
            ((^#i : V) ∷ shiftVec 3 m)) y from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := m + 1) (n := (m + 1) + 1 + 1)
        (m := (listMax (termBVVec ℒₛₑₜ (m + 1) Vw) + 1) + 1) (p := y) hy hQ hv]

/-! ## 零件 F：`qVec²` 固定 cFunc 代入（只读 `X.[0]`） -/

/-- `subst (qVec² X) (subst [^#2,^#0,^#1] (cFunc 2 f))` 只依赖 `X.[0]`。 -/
lemma subst_qvec2_cFunc_gen {m f Vw Ww : V} (hVw : IsUTermVec ℒₛₑₜ (m + 1) Vw)
    (hWw : IsUTermVec ℒₛₑₜ (m + 2) Ww) (h0 : Vw.[0] = Ww.[0]) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) =
      subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f) := isSemiformula_cFunc_arity2 (by norm_num) f
  have hQv : IsSemitermVec ℒₛₑₜ ((m + 1) + 1 + 1)
      ((listMax (termBVVec ℒₛₑₜ (m + 1) Vw) + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) :=
    hVw.isSemitermVec.qVec.qVec
  have hQw : IsSemitermVec ℒₛₑₜ ((m + 2) + 1 + 1)
      ((listMax (termBVVec ℒₛₑₜ (m + 2) Ww) + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww)) :=
    hWw.isSemitermVec.qVec.qVec
  have hvv : IsSemitermVec ℒₛₑₜ 3 ((m + 1) + 1 + 1) ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
    LayerMono.IsSemitermVec.mono (isSemitermVec_three_bvars m)
      (le_of_eq (by ring : (3 : V) + m = (m + 1) + 1 + 1))
  have hvw : IsSemitermVec ℒₛₑₜ 3 ((m + 2) + 1 + 1) ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
    LayerMono.IsSemitermVec.mono (isSemitermVec_three_bvars (m + 1))
      (le_of_eq (by ring : (3 : V) + (m + 1) = (m + 2) + 1 + 1))
  rw [show subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 3 (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
          ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V))) (cFunc 2 f) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 3) (n := (m + 1) + 1 + 1)
      (m := (listMax (termBVVec ℒₛₑₜ (m + 1) Vw) + 1) + 1) (p := cFunc 2 f) hc hQv hvv]
  rw [show subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 3 (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww))
          ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V))) (cFunc 2 f) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 3) (n := (m + 2) + 1 + 1)
      (m := (listMax (termBVVec ℒₛₑₜ (m + 2) Ww) + 1) + 1) (p := cFunc 2 f) hc hQw hvw]
  rw [show termSubstVec ℒₛₑₜ 3 (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
        ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V))
      = ?[termBShift ℒₛₑₜ (termBShift ℒₛₑₜ Vw.[0]), ^#0, ^#1] from
    termSubstVec_three_qvec2 (hVw.lh ▸ hVw) (by rw [← hVw.lh]; exact lt_of_le_of_lt zero_le (lt_add_one m))]
  rw [show termSubstVec ℒₛₑₜ 3 (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww))
        ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V))
      = ?[termBShift ℒₛₑₜ (termBShift ℒₛₑₜ Ww.[0]), ^#0, ^#1] from
    termSubstVec_three_qvec2 (hWw.lh ▸ hWw) (by
      rw [← hWw.lh]
      exact lt_of_le_of_lt zero_le (by
        have h := lt_add_one (m + 1)
        rwa [show ((m + 1) + 1 : V) = m + 2 by ring] at h))]
  rw [h0]


/-! ## 零件 H：`ve2` 的开口展开（任意向量版） -/

/-- **`ve2` 与开口代入交换（任意向量版）**。

`hsub0`/`hsub1` 是归纳假设在两个 `i` 分量上的实例（向量已变换为 `Vw1`/`Ww1`）。 -/
lemma subst_ve2_gen {m f w w' Vw Ww : V}
    (hVw : IsUTermVec ℒₛₑₜ (m + 1) Vw) (hWw : IsUTermVec ℒₛₑₜ ((m + 1) + 1) Ww)
    (hw0 : IsSemiformula ℒₛₑₜ (m + 1) w.[0]) (hw1 : IsSemiformula ℒₛₑₜ (m + 1) w.[1])
    (hw'0 : IsSemiformula ℒₛₑₜ ((m + 1) + 1) w'.[0])
    (hw'1 : IsSemiformula ℒₛₑₜ ((m + 1) + 1) w'.[1])
    (h0 : Vw.[0] = Ww.[0])
    (hsub0 : subst ℒₛₑₜ (Vw1 m Vw 0) w.[0] = subst ℒₛₑₜ (Ww1 m Ww 0) w'.[0])
    (hsub1 : subst ℒₛₑₜ (Vw1 m Vw 1) w.[1] = subst ℒₛₑₜ (Ww1 m Ww 1) w'.[1]) :
    subst ℒₛₑₜ Vw (ve2 m 2 f w) = subst ℒₛₑₜ Ww (ve2 (m + 1) 2 f w') := by
  have hC : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) := by
    rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
    exact (IsSemiformula.subst (L := ℒₛₑₜ)
      (isSemiformula_cFunc_arity2 (by norm_num : (2 : V) ≠ 0) f)
      (isSemitermVec_three_bvars 0)).isUFormula
  have hP0 : IsSemiformula ℒₛₑₜ (3 + m) (conjunct 3 m 0 w.[0]) :=
    isSemiformula_conjunct (b := 3) (n := m) (i := 0) hw0 (zero_lt_three_add m)
  have hP1 : IsSemiformula ℒₛₑₜ (3 + m) (conjunct 3 m 1 w.[1]) :=
    isSemiformula_conjunct (b := 3) (n := m) (i := 1) hw1 (one_lt_three_add m)
  have hP : IsSemiformula ℒₛₑₜ (3 + m)
      (conjunct 3 m 0 w.[0] ^⋏ (conjunct 3 m 1 w.[1] ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hP0, IsSemiformula.and.mpr ⟨hP1, IsSemiformula.verum⟩⟩
  have hP0' : IsSemiformula ℒₛₑₜ (3 + (m + 1)) (conjunct 3 (m + 1) 0 w'.[0]) :=
    isSemiformula_conjunct (b := 3) (n := m + 1) (i := 0) hw'0 (zero_lt_three_add (m + 1))
  have hP1' : IsSemiformula ℒₛₑₜ (3 + (m + 1)) (conjunct 3 (m + 1) 1 w'.[1]) :=
    isSemiformula_conjunct (b := 3) (n := m + 1) (i := 1) hw'1 (one_lt_three_add (m + 1))
  have hP' : IsSemiformula ℒₛₑₜ (3 + (m + 1))
      (conjunct 3 (m + 1) 0 w'.[0] ^⋏ (conjunct 3 (m + 1) 1 w'.[1] ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hP0', IsSemiformula.and.mpr ⟨hP1', IsSemiformula.verum⟩⟩
  have hBV : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 3 m 0 w.[0] ^⋏ (conjunct 3 m 1 w.[1] ^⋏ ^⊤))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))) :=
    IsUFormula.imp.mpr ⟨hP.isUFormula, hC⟩
  have hBW : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 3 (m + 1) 0 w'.[0] ^⋏ (conjunct 3 (m + 1) 1 w'.[1] ^⋏ ^⊤))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f))) :=
    IsUFormula.imp.mpr ⟨hP'.isUFormula, hC⟩
  -- 向量实例
  have hQ : IsSemitermVec ℒₛₑₜ (3 + m)
      ((listMax (termBVVec ℒₛₑₜ (m + 1) Vw) + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) := by
    have h := hVw.isSemitermVec.qVec.qVec
    rw [show ((m + 1) + 1 + 1 : V) = 3 + m by ring] at h
    exact h
  have hQ' : IsSemitermVec ℒₛₑₜ (3 + (m + 1))
      ((listMax (termBVVec ℒₛₑₜ ((m + 1) + 1) Ww) + 1) + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww)) := by
    have h := hWw.isSemitermVec.qVec.qVec
    rw [show (((m + 1) + 1) + 1 + 1 : V) = 3 + (m + 1) by ring] at h
    exact h
  -- 两侧体内展开
  have hVbody : subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
      (imp ℒₛₑₜ (conjunct 3 m 0 w.[0] ^⋏ (conjunct 3 m 1 w.[1] ^⋏ ^⊤))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)))
      = neg ℒₛₑₜ
          ((subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (Vw1 m Vw 0) w.[0])
           ^⋏ ((subst ℒₛₑₜ (?[^#1] : V) ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (Vw1 m Vw 1) w.[1])
              ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw))
          (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) := by
    rw [imp]
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hP.isUFormula.neg hC]
    rw [Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 3 + m) hP hQ]
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hP0.isUFormula
      (IsSemiformula.and.mpr ⟨hP1, IsSemiformula.verum⟩).isUFormula]
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hP1.isUFormula IsUFormula.verum]
    rw [Bootstrapping.substs_verum (L := ℒₛₑₜ)]
    rw [subst_qvec2_conjunct_gen (m := m) (i := 0) (y := w.[0]) (Vw := Vw) hVw hw0
        (by norm_num : (0 : V) ≤ 1),
      subst_qvec2_conjunct_gen (m := m) (i := 1) (y := w.[1]) (Vw := Vw) hVw hw1
        (by norm_num : (1 : V) ≤ 1)]
  have hWbody : subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww))
      (imp ℒₛₑₜ (conjunct 3 (m + 1) 0 w'.[0] ^⋏ (conjunct 3 (m + 1) 1 w'.[1] ^⋏ ^⊤))
        (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)))
      = neg ℒₛₑₜ
          ((subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (Ww1 m Ww 0) w'.[0])
           ^⋏ ((subst ℒₛₑₜ (?[^#1] : V) ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (Ww1 m Ww 1) w'.[1])
              ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww))
          (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) := by
    rw [imp]
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hP'.isUFormula.neg hC]
    rw [Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 3 + (m + 1)) hP' hQ']
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hP0'.isUFormula
      (IsSemiformula.and.mpr ⟨hP1', IsSemiformula.verum⟩).isUFormula]
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hP1'.isUFormula IsUFormula.verum]
    rw [Bootstrapping.substs_verum (L := ℒₛₑₜ)]
    rw [subst_qvec2_conjunct_gen (m := m + 1) (i := 0) (y := w'.[0]) (Vw := Ww) hWw hw'0
        (by norm_num : (0 : V) ≤ 1),
      subst_qvec2_conjunct_gen (m := m + 1) (i := 1) (y := w'.[1]) (Vw := Ww) hWw hw'1
        (by norm_num : (1 : V) ≤ 1)]
  -- C 两侧相等
  have hWw2 : IsUTermVec ℒₛₑₜ (m + 2) Ww := by
    have h := hWw
    rw [show ((m + 1) + 1 : V) = m + 2 by ring] at h
    exact h
  have hCeq := subst_qvec2_cFunc_gen (m := m) (f := f) hVw hWw2 h0
  -- 组装
  rw [ve2, ve2]
  rw [subst_qqAlls_two (W := Vw) hBV, subst_qqAlls_two (W := Ww) hBW]
  congr 1
  rw [hVbody, hWbody, hCeq]
  refine congrArg₂ (fun a b => neg ℒₛₑₜ a ^⋎ b) ?_ rfl
  refine congrArg₂ (fun a b => a ^⋏ b) ?_ ?_
  · exact congrArg₂ (fun a b => a ^⋏ b) rfl hsub0
  · exact congrArg₂ (fun a b => a ^⋏ b)
      (congrArg₂ (fun a b => a ^⋏ b) rfl hsub1) rfl

/-! ## 主定理：(★★) -/

/-! ## 零件 I：k=0 支的 IsUTermVec 版本

`ITSubstOpen5.subst_iVE_func_zero_eq` 要求 `IsSemitermVec`；归纳里只有 `IsUTermVec`。
用 `IsUTermVec.isSemitermVec`（层数 `listMax`，结论不依赖该层）桥接。 -/

/-- k=0 支（`IsUTermVec` 版）：`subst Vw (ve0 0 f) = subst Ww (ve0 0 f)`。 -/
lemma subst_iVE_func_zero_eq_uterm {m f Vw Ww : V} (hkf : (ℒₒᵣ).IsFunc 0 f)
    (hV : IsUTermVec ℒₛₑₜ (m + 1) Vw) (hW : IsUTermVec ℒₛₑₜ ((m + 1) + 1) Ww)
    (hposV : (0 : V) < len Vw) (hposW : (0 : V) < len Ww)
    (h0 : Vw.[0] = Ww.[0]) :
    subst ℒₛₑₜ Vw (ve0 0 f) = subst ℒₛₑₜ Ww (ve0 0 f) := by
  have hc : IsSemiformula ℒₛₑₜ 1 (cFunc 0 f) := isSemiformula_cFunc_arity0 f
  have hv : IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := 1) (by simp)
  have hs : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ?[^#0] (cFunc 0 f)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hc hv).isUFormula
  simp only [ve0, imp]
  simp only [Bootstrapping.substs_or (L := ℒₛₑₜ) (IsUFormula.neg IsUFormula.verum) hs]
  have hV' : IsSemitermVec ℒₛₑₜ (len Vw) (listMax (termBVVec ℒₛₑₜ (len Vw) Vw)) Vw := by
    have h := hV.isSemitermVec
    rwa [hV.lh] at h
  have hW' : IsSemitermVec ℒₛₑₜ (len Ww) (listMax (termBVVec ℒₛₑₜ (len Ww) Ww)) Ww := by
    have h := hW.isSemitermVec
    rwa [hW.lh] at h
  rw [subst_quoted_reads_zero (c := cFunc 0 f) hc hV' hposV,
      subst_quoted_reads_zero (c := cFunc 0 f) hc hW' hposW, h0]
  simp only [Bootstrapping.neg_verum (L := ℒₛₑₜ), Bootstrapping.substs_falsum (L := ℒₛₑₜ)]

-- **(★★) 开口律的项层核心引理**。
--
-- 对层 `m+1` 的项 `t` 与满足 `VRel m Vw Ww` 的项向量 `Vw`（长 `m+1`）、`Ww`（长 `m+2`）：
--
--     subst Vw (iVE m (termSubst (QvecVOr m) t)) = subst Ww (iVE (m+1) t)
--
/-- (★★) 的归纳谓词（命名 def —— definability 需要 `unfold` 后形状）。 -/
def QPred (m : V) (t : V) : Prop :=
  ∀ Vw Ww : V, IsUTermVec ℒₛₑₜ (m + 1) Vw → IsUTermVec ℒₛₑₜ ((m + 1) + 1) Ww →
    (∀ k ≤ m, Vw.[k] = Ww.[k]) → Ww.[m + 1] = ^&0 →
    subst ℒₛₑₜ Vw (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) t))
      = subst ℒₛₑₜ Ww (iVE (m + 1) t)

theorem subst_iVE_open : ∀ (m : V) (t : V), IsSemiterm ℒₒᵣ (m + 1) t →
    ∀ Vw Ww : V, IsUTermVec ℒₛₑₜ (m + 1) Vw → IsUTermVec ℒₛₑₜ ((m + 1) + 1) Ww →
      (∀ k ≤ m, Vw.[k] = Ww.[k]) → Ww.[m + 1] = ^&0 →
      subst ℒₛₑₜ Vw (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) t))
        = subst ℒₛₑₜ Ww (iVE (m + 1) t) := by
  intro m t
  apply IsSemiterm.induction 𝚷 (L := ℒₒᵣ) (n := m + 1) (P := QPred (V := V) m)
  · unfold QPred
    definability
  · -- bvar
    intro z hz
    unfold QPred
    intro Vw Ww hV hW hpre hlast
    exact GodelQ.ITSubstOpen3.subst_iVE_bvar_eq (m := m) (z := z) (Vw := Vw) (Ww := Ww) hz
      (hpre 0 zero_le) (fun hz' => hpre (z + 1) (lt_iff_succ_le.mp hz')) hlast
  · -- fvar
    intro x
    unfold QPred
    intro Vw Ww hV hW hpre hlast
    exact GodelQ.ITSubstOpen5.subst_iVE_fvar_eq (m := m) (x := x) (hpre 0 zero_le)
  · -- func
    intro k f v hkf hv ih
    unfold QPred at ih ⊢
    intro Vw Ww hV hW hpre hlast
    rw [termSubst_func hkf hv.isUTerm]
    rw [iVE_func hkf ((IsSemitermVec.termSubstVec (L := ℒₒᵣ) (w := QvecVOr (V := V) m)
      (isSemitermVec_QvecVOr m) hv).isUTerm)]
    rw [iVE_func hkf hv.isUTerm]
    by_cases hk : k = 0
    · -- k = 0
      subst hk
      simp only [ite_true]
      have hposV : (0 : V) < len Vw := by
        rw [← hV.lh]
        exact lt_of_le_of_lt zero_le (lt_add_one m)
      have hposW : (0 : V) < len Ww := by
        rw [← hW.lh]
        exact lt_of_le_of_lt zero_le (lt_add_one (m + 1))
      exact subst_iVE_func_zero_eq_uterm (m := m) (f := f) hkf
        hV hW hposV hposW (hpre 0 zero_le)
    · -- k = 2
      have hk2 := k_eq_two_of_func hkf hk
      subst hk2
      simp only [show (2 : V) ≠ 0 by norm_num, if_false]
      have hvT : IsSemitermVec ℒₒᵣ 2 (m + 1) (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v) :=
        IsSemitermVec.termSubstVec (L := ℒₒᵣ) (isSemitermVec_QvecVOr m) hv
      -- 分量引理：参数向量分量 = iVE 形状
      have hwL0 : (iVE.construction.resultVec ℒₒᵣ ![(m : V)] 2
          (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v)).[0]
          = iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[0]) := by
        rw [iVE.construction.nth_resultVec ℒₒᵣ ![(m : V)] hvT.isUTerm (by norm_num : (0:V) < 2),
          nth_termSubstVec hv.isUTerm (by norm_num : (0:V) < 2)]
        simp only [iVE]
      have hwL1 : (iVE.construction.resultVec ℒₒᵣ ![(m : V)] 2
          (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v)).[1]
          = iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[1]) := by
        rw [iVE.construction.nth_resultVec ℒₒᵣ ![(m : V)] hvT.isUTerm (by norm_num : (1:V) < 2),
          nth_termSubstVec hv.isUTerm (by norm_num : (1:V) < 2)]
        simp only [iVE]
      have hwR0 : (iVE.construction.resultVec ℒₒᵣ ![(m + 1 : V)] 2 v).[0] = iVE (m + 1) v.[0] := by
        rw [iVE.construction.nth_resultVec ℒₒᵣ ![(m + 1 : V)] hv.isUTerm (by norm_num : (0:V) < 2)]
        simp only [iVE]
      have hwR1 : (iVE.construction.resultVec ℒₒᵣ ![(m + 1 : V)] 2 v).[1] = iVE (m + 1) v.[1] := by
        rw [iVE.construction.nth_resultVec ℒₒᵣ ![(m + 1 : V)] hv.isUTerm (by norm_num : (1:V) < 2)]
        simp only [iVE]
      -- 公式性
      have hwL0f : IsSemiformula ℒₛₑₜ (m + 1)
          (iVE.construction.resultVec ℒₒᵣ ![(m : V)] 2
            (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v)).[0] := by
        rw [hwL0]
        exact isSemiformula_iVE (n := m)
          (termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[0])
          (IsSemitermVec.termSubst (L := ℒₒᵣ) (isSemitermVec_QvecVOr_low (m := m))
            (hv.nth (by norm_num : (0:V) < 2)))
      have hwL1f : IsSemiformula ℒₛₑₜ (m + 1)
          (iVE.construction.resultVec ℒₒᵣ ![(m : V)] 2
            (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v)).[1] := by
        rw [hwL1]
        exact isSemiformula_iVE (n := m)
          (termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[1])
          (IsSemitermVec.termSubst (L := ℒₒᵣ) (isSemitermVec_QvecVOr_low (m := m))
            (hv.nth (by norm_num : (1:V) < 2)))
      have hwR0f : IsSemiformula ℒₛₑₜ ((m + 1) + 1)
          (iVE.construction.resultVec ℒₒᵣ ![(m + 1 : V)] 2 v).[0] := by
        rw [hwR0]
        exact isSemiformula_iVE (n := m + 1) v.[0] (hv.nth (by norm_num : (0:V) < 2))
      have hwR1f : IsSemiformula ℒₛₑₜ ((m + 1) + 1)
          (iVE.construction.resultVec ℒₒᵣ ![(m + 1 : V)] 2 v).[1] := by
        rw [hwR1]
        exact isSemiformula_iVE (n := m + 1) v.[1] (hv.nth (by norm_num : (1:V) < 2))
      -- 变换向量的合法性
      have hV1 : IsUTermVec ℒₛₑₜ (m + 1) (Vw1 m Vw 0) := by
        have hw := hV.isSemitermVec.qVec.qVec
        have hv0 : IsSemitermVec ℒₛₑₜ (m + 1) ((m + 1) + 1 + 1) ((^#0 : V) ∷ shiftVec 3 m) :=
          LayerMono.IsSemitermVec.mono
            (isSemitermVec_shiftVec_cons (b := 3) (n := m) (i := 0) (zero_lt_three_add m))
            (le_of_eq (by ring : (3 : V) + m = (m + 1) + 1 + 1))
        exact (IsSemitermVec.termSubstVec (L := ℒₛₑₜ) hw hv0).isUTerm
      have hV1' : IsUTermVec ℒₛₑₜ (m + 1) (Vw1 m Vw 1) := by
        have hw := hV.isSemitermVec.qVec.qVec
        have hv0 : IsSemitermVec ℒₛₑₜ (m + 1) ((m + 1) + 1 + 1) ((^#1 : V) ∷ shiftVec 3 m) :=
          LayerMono.IsSemitermVec.mono
            (isSemitermVec_shiftVec_cons (b := 3) (n := m) (i := 1) (one_lt_three_add m))
            (le_of_eq (by ring : (3 : V) + m = (m + 1) + 1 + 1))
        exact (IsSemitermVec.termSubstVec (L := ℒₛₑₜ) hw hv0).isUTerm
      have hW1 : IsUTermVec ℒₛₑₜ ((m + 1) + 1) (Ww1 m Ww 0) := by
        have hw := hW.isSemitermVec.qVec.qVec
        have hv0 : IsSemitermVec ℒₛₑₜ ((m + 1) + 1) (((m + 1) + 1) + 1 + 1)
            ((^#0 : V) ∷ shiftVec 3 (m + 1)) :=
          LayerMono.IsSemitermVec.mono
            (isSemitermVec_shiftVec_cons (b := 3) (n := m + 1) (i := 0) (zero_lt_three_add (m + 1)))
            (le_of_eq (by ring : (3 : V) + (m + 1) = ((m + 1) + 1) + 1 + 1))
        exact (IsSemitermVec.termSubstVec (L := ℒₛₑₜ) hw hv0).isUTerm
      have hW1' : IsUTermVec ℒₛₑₜ ((m + 1) + 1) (Ww1 m Ww 1) := by
        have hw := hW.isSemitermVec.qVec.qVec
        have hv0 : IsSemitermVec ℒₛₑₜ ((m + 1) + 1) (((m + 1) + 1) + 1 + 1)
            ((^#1 : V) ∷ shiftVec 3 (m + 1)) :=
          LayerMono.IsSemitermVec.mono
            (isSemitermVec_shiftVec_cons (b := 3) (n := m + 1) (i := 1) (one_lt_three_add (m + 1)))
            (le_of_eq (by ring : (3 : V) + (m + 1) = ((m + 1) + 1) + 1 + 1))
        exact (IsSemitermVec.termSubstVec (L := ℒₛₑₜ) hw hv0).isUTerm
      -- VRel 变换保持（VRel_transform 的输出 W 侧长度写作 m+2，改写为 (m+1)+1）
      have hV' : IsUTermVec ℒₛₑₜ (len Vw) Vw := by rw [← hV.lh]; exact hV
      have hW' : IsUTermVec ℒₛₑₜ (len Ww) Ww := by rw [← hW.lh]; exact hW
      have hrel0 := VRel_transform (m := m) (i := 0) hV' hW'
        (hV.lh.symm) (by rw [← hW.lh]; ring) (by norm_num : (0 : V) ≤ 1) ⟨hpre, hlast⟩
      rw [show (m + 2 : V) = (m + 1) + 1 by ring] at hrel0
      have hrel1 := VRel_transform (m := m) (i := 1) hV' hW'
        (hV.lh.symm) (by rw [← hW.lh]; ring) (by norm_num : (1 : V) ≤ 1) ⟨hpre, hlast⟩
      rw [show (m + 2 : V) = (m + 1) + 1 by ring] at hrel1
      -- 组装：subst_ve2_gen，hsub_i 由归纳假设在**变换向量**处实例化
      exact subst_ve2_gen (m := m) (f := f)
        (w := iVE.construction.resultVec ℒₒᵣ ![(m : V)] 2
          (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v))
        (w' := iVE.construction.resultVec ℒₒᵣ ![(m + 1 : V)] 2 v)
        hV hW hwL0f hwL1f hwR0f hwR1f (hpre 0 zero_le)
        (by
          rw [hwL0, hwR0]
          exact ih 0 (by norm_num : (0:V) < 2) (Vw1 m Vw 0) (Ww1 m Ww 0)
            hV1 hW1 hrel0.1 hrel0.2)
        (by
          rw [hwL1, hwR1]
          exact ih 1 (by norm_num : (1:V) < 2) (Vw1 m Vw 1) (Ww1 m Ww 1)
            hV1' hW1' hrel1.1 hrel1.2)

end GodelQ.ITSubstOpen6
#print axioms GodelQ.ITSubstOpen6.subst_qqAlls_two
#print axioms GodelQ.ITSubstOpen6.subst_qvec2_cDomN
#print axioms GodelQ.ITSubstOpen6.isSemitermVec_QvecVOr_low
#print axioms GodelQ.ITSubstOpen6.termSubstVec_three_qvec2
#print axioms GodelQ.ITSubstOpen6.subst_qvec2_conjunct_gen
#print axioms GodelQ.ITSubstOpen6.subst_qvec2_cFunc_gen
#print axioms GodelQ.ITSubstOpen6.subst_ve2_gen
#print axioms GodelQ.ITSubstOpen6.subst_iVE_func_zero_eq_uterm
#print axioms GodelQ.ITSubstOpen6.subst_iVE_open
