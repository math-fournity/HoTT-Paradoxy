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

end GodelQ.ITSubstOpen6

#print axioms GodelQ.ITSubstOpen6.subst_ve2_gen
#print axioms GodelQ.ITSubstOpen6.subst_qqAlls_two
#print axioms GodelQ.ITSubstOpen6.subst_qvec2_cDomN
#print axioms GodelQ.ITSubstOpen6.isSemitermVec_QvecVOr_low
#print axioms GodelQ.ITSubstOpen6.termSubstVec_three_qvec2
#print axioms GodelQ.ITSubstOpen6.subst_qvec2_conjunct_gen
#print axioms GodelQ.ITSubstOpen6.subst_qvec2_cFunc_gen
