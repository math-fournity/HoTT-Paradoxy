-- CG-009: `iT_subst_open` 的 rel 支 —— `iTR` 与开口代入交换。
--
-- 目标（`q` 层 `m+1`，`q = ^rel 2 R v`）：
--     iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)
-- rel 支即：
--     iTR m 2 R (termSubstVec 2 (QvecVOr m) v) = subst (QvecV m) (iTR (m+1) 2 R v)
--
-- ## 结构
--
-- 两侧都展开成 `qqAlls _ 2`。RHS 用 `subst_qqAlls_two` 推入两层
-- （体内向量 `qVec²(QvecV m) = QvecV (m+2)`）。体内逐分量对齐：
--   * `conjunct 2 (m+1) i (iVE (m+1) v.[i])` 被 `QvecV (m+2)` 代入后
--     = `conjunct 2 m i (iVE m (termSubst (QvecVOr m) v.[i]))`（`subst_QvecV_conjunct_open`）
--     —— 其第二分量恰是 (★★) 在 `VRel_rel` 处的实例
--   * `subst ?[^#0,^#1] (cRel R)` 被固定（`subst_QvecV_cRel`，ITSubstOpen7）
import GodelQ.ZFC.ITSubstOpen7

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen8
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen2 GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4
open GodelQ.ITSubstOpen5 GodelQ.ITSubstOpen6 GodelQ.ITSubstOpen7

/-! ## 零件 M：conjunct 的开口展开（rel 支版，`b = 2`） -/

/-- **`conjunct` 的 rel 支开口展开**：

    subst (QvecV (m+2)) (conjunct 2 (m+1) i (iVE (m+1) t))
      = conjunct 2 m i (iVE m (termSubst (QvecVOr m) t))

第一分量（domZero 部分）由 `QvecV (m+2)` 在索引 `i ≤ 1` 处的恒等给出；
第二分量由 (★★)（`subst_iVE_open`）在 `VRel_rel` 处给出。 -/
lemma subst_QvecV_conjunct_open {m i t : V} (ht : IsSemiterm ℒₒᵣ (m + 1) t)
    (hi : i ≤ 1) :
    subst ℒₛₑₜ (QvecV (V := V) (m + 2)) (conjunct 2 (m + 1) i (iVE (m + 1) t))
      = conjunct 2 m i (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) t)) := by
  -- 界：i ≤ 1 ⟹ i < m+2（且 m+2 ≥ 2 > 1 ≥ i）
  have hi2'' : i < m + 2 := by
    have h := one_lt_two_add m
    have e : (2 : V) + m = m + 2 := by ring
    rw [e] at h
    exact lt_of_le_of_lt hi h
  have hi2 : i < 2 + (m + 1) := by
    have h := one_lt_three_add m
    have e : (3 : V) + m = 2 + (m + 1) := by ring
    rw [e] at h
    exact lt_of_le_of_lt hi h
  -- 公式性
  have hy' : IsSemiformula ℒₛₑₜ (m + 2) (iVE (m + 1) t) := by
    have h := isSemiformula_iVE (n := m + 1) t ht
    rwa [show ((m + 1) + 1 : V) = m + 2 by ring] at h
  have ht' : IsSemiterm ℒₒᵣ m (termSubst ℒₒᵣ (QvecVOr (V := V) m) t) :=
    IsSemitermVec.termSubst (L := ℒₒᵣ) (isSemitermVec_QvecVOr_low (m := m)) ht
  have hy : IsSemiformula ℒₛₑₜ (m + 1) (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) t)) :=
    isSemiformula_iVE (n := m) _ ht'
  have hdom' : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := i + 1) (by simp))).isUFormula
  have hbody' : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 2 (m + 1)) (iVE (m + 1) t)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hy'
      (isSemitermVec_cons_shiftVec2 (m := m) (i := i) hi2'')).isUFormula
  unfold conjunct
  rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hdom' hbody']
  congr 1
  · -- ① domZero 部分：QvecV (m+2) 在索引 i ≤ 1 处是 ^#i
    have hQ : IsSemitermVec ℒₛₑₜ (m + 3) (m + 3) (QvecV (V := V) (m + 2)) := by
      have h := isSemitermVec_QvecV (V := V) (m + 2)
      have e : (m + 2 : V) + 1 = m + 3 := by ring
      rwa [e] at h
    have hw : IsSemitermVec ℒₛₑₜ 1 (m + 3) (?[^#i] : V) :=
      isSemitermVec_single_bvar (n := m + 3) (by
        have h := one_lt_three_add m
        have e : (3 : V) + m = m + 3 := by ring
        rw [e] at h
        exact lt_of_le_of_lt hi h)
    rw [show subst ℒₛₑₜ (QvecV (V := V) (m + 2)) (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V))
        = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (m + 2)) (?[^#i] : V)) ((cDomN : ℕ) : V) from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) (n := m + 3) (m := m + 3)
        (p := ((cDomN : ℕ) : V)) isSemiformula_cDomN hQ hw]
    rw [GodelQ.IVEOpenFunc8.termSubstVec_one_QvecV_single hi2'']
  · -- ② 体部分：substs_substs 复合 + (★★)（VRel_rel 处）
    have hQ : IsSemitermVec ℒₛₑₜ (m + 3) (m + 3) (QvecV (V := V) (m + 2)) := by
      have h := isSemitermVec_QvecV (V := V) (m + 2)
      have e : (m + 2 : V) + 1 = m + 3 := by ring
      rwa [e] at h
    have hv2 : IsSemitermVec ℒₛₑₜ (m + 2) (m + 3) ((^#i : V) ∷ shiftVec 2 (m + 1)) :=
      isSemitermVec_cons_shiftVec2 (m := m) (i := i) hi2''
    rw [show subst ℒₛₑₜ (QvecV (V := V) (m + 2))
          (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 2 (m + 1)) (iVE (m + 1) t))
        = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2))
            ((^#i : V) ∷ shiftVec 2 (m + 1))) (iVE (m + 1) t) from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := m + 2) (n := m + 3) (m := m + 3)
        (p := iVE (m + 1) t) hy' hQ hv2]
    -- (★★).symm：Vw := ^#i ∷ shiftVec 2 m，Ww := termSubstVec (m+2) (QvecV (m+2)) (^#i ∷ shiftVec 2 (m+1))
    have hVw : IsUTermVec ℒₛₑₜ (m + 1) ((^#i : V) ∷ shiftVec 2 m) := by
      have h := IsUTermVec.adjoin (L := ℒₛₑₜ) (isSemitermVec_shiftVec_V 2 m).isUTerm
        (IsUTerm.bvar (z := i))
      rwa [show ((m : V) + 1) = m + 1 from rfl] at h
    have hWw : IsUTermVec ℒₛₑₜ ((m + 1) + 1)
        (termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2)) ((^#i : V) ∷ shiftVec 2 (m + 1))) := by
      have h := (IsSemitermVec.termSubstVec (L := ℒₛₑₜ) hQ hv2).isUTerm
      convert h using 1 <;> ring
    have hrel := VRel_rel (m := m) (j := i) hi2''
    exact (subst_iVE_open (m := m) t ht
      ((^#i : V) ∷ shiftVec 2 m)
      (termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2)) ((^#i : V) ∷ shiftVec 2 (m + 1)))
      hVw hWw hrel.1 hrel.2).symm


/-! ## 主定理（rel 支）：`iTR` 与开口代入交换 -/

/-- **`iTR` 的开口律**（`iT_subst_open` 的 rel 支）：

    iTR m 2 R (termSubstVec 2 (QvecVOr m) v) = subst (QvecV m) (iTR (m+1) 2 R v)

结构镜像 `ITRShift.iTR_shift`（`shift ↦ subst (QvecV m)`）；
关键零件：(★★) 经 `subst_QvecV_conjunct_open`、闭项 `subst_QvecV_cRel`。 -/
theorem iTR_subst_open {m R v : V} (hR : (ℒₒᵣ).IsRel 2 R)
    (hv : IsSemitermVec ℒₒᵣ 2 (m + 1) v) :
    iTR m 2 R (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v)
      = subst ℒₛₑₜ (QvecV (V := V) m) (iTR (m + 1) 2 R v) := by
  have hvT : IsUTermVec ℒₒᵣ 2 (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v) :=
    (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (isSemitermVec_QvecVOr_low (m := m))
      hv).isUTerm
  -- 分量：t.[i] = termSubst (QvecVOr m) v.[i]
  have ht0 : (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v).[0]
      = termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[0] :=
    nth_termSubstVec hv.isUTerm (by norm_num)
  have ht1 : (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) m) v).[1]
      = termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[1] :=
    nth_termSubstVec hv.isUTerm (by norm_num)
  -- 公式性
  have hs0 : IsSemiformula ℒₛₑₜ (m + 1)
      (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[0])) :=
    isSemiformula_iVE (n := m) _
      (IsSemitermVec.termSubst (L := ℒₒᵣ) (isSemitermVec_QvecVOr_low (m := m))
        (hv.nth (i := 0) (by norm_num)))
  have hs1 : IsSemiformula ℒₛₑₜ (m + 1)
      (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) v.[1])) :=
    isSemiformula_iVE (n := m) _
      (IsSemitermVec.termSubst (L := ℒₒᵣ) (isSemitermVec_QvecVOr_low (m := m))
        (hv.nth (i := 1) (by norm_num)))
  have hs0' : IsSemiformula ℒₛₑₜ ((m + 1) + 1) (iVE (m + 1) v.[0]) :=
    isSemiformula_iVE (n := m + 1) v.[0] (hv.nth (i := 0) (by norm_num))
  have hs1' : IsSemiformula ℒₛₑₜ ((m + 1) + 1) (iVE (m + 1) v.[1]) :=
    isSemiformula_iVE (n := m + 1) v.[1] (hv.nth (i := 1) (by norm_num))
  have hC : IsSemiformula ℒₛₑₜ (2 + (m + 1)) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) := by
    apply IsSemiformula.subst (L := ℒₛₑₜ) (n := 2) (m := 2 + (m + 1))
    · exact isSemiformula_cRel R
    · rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ 0 from rfl]
      exact GodelQ.ITRShift.isSemitermVec_two_bvars (m + 1)
  -- RHS 体内的公式性（层 m+3 = 2+(m+1)）
  have hB0 : IsSemiformula ℒₛₑₜ (2 + (m + 1)) (conjunct 2 (m + 1) 0 (iVE (m + 1) v.[0])) :=
    isSemiformula_conjunct (b := 2) (n := m + 1) (i := 0) hs0' (zero_lt_two_add (m + 1))
  have hB1 : IsSemiformula ℒₛₑₜ (2 + (m + 1)) (conjunct 2 (m + 1) 1 (iVE (m + 1) v.[1])) :=
    isSemiformula_conjunct (b := 2) (n := m + 1) (i := 1) hs1' (one_lt_two_add (m + 1))
  have hB01 : IsSemiformula ℒₛₑₜ (2 + (m + 1)) (conjunct 2 (m + 1) 1 (iVE (m + 1) v.[1]) ^⋏ ^⊤) :=
    IsSemiformula.and.mpr ⟨hB1, IsSemiformula.verum⟩
  have hB : IsSemiformula ℒₛₑₜ (2 + (m + 1))
      (conjunct 2 (m + 1) 0 (iVE (m + 1) v.[0]) ^⋏
        (conjunct 2 (m + 1) 1 (iVE (m + 1) v.[1]) ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hB0, hB01⟩
  have hbody : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 2 (m + 1) 0 (iVE (m + 1) v.[0]) ^⋏
          (conjunct 2 (m + 1) 1 (iVE (m + 1) v.[1]) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) :=
    (IsSemiformula.imp.mpr ⟨hB, hC⟩).isUFormula
  -- 向量：QvecV (m+2) 在层 m+3 处（长度 m+3）
  have hQ : IsSemitermVec ℒₛₑₜ (2 + (m + 1)) (2 + (m + 1)) (QvecV (V := V) (m + 2)) := by
    have h := isSemitermVec_QvecV (V := V) (m + 2)
    have e : (m + 2 : V) + 1 = 2 + (m + 1) := by ring
    rwa [e] at h
  -- LHS 展开
  rw [iTR]
  rw [ht0, ht1]
  -- RHS 展开
  conv_rhs => rw [iTR]
  rw [subst_qqAlls_two (W := QvecV (V := V) m) hbody]
  rw [show qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) m)) = QvecV (V := V) (m + 2) from by
    rw [← QvecV_succ m, ← QvecV_succ (m + 1)]
    congr 1
    ring]
  -- 先把两侧的 imp 都展开（RHS 的 imp 在 subst 内部，必须先生效）
  rw [imp]
  conv_rhs => rw [imp]
  -- 推入 RHS 体内的 subst
  rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hB.isUFormula.neg hC.isUFormula,
    Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := 2 + (m + 1)) hB hQ,
    Bootstrapping.substs_and (L := ℒₛₑₜ) hB0.isUFormula hB01.isUFormula,
    Bootstrapping.substs_and (L := ℒₛₑₜ) hB1.isUFormula IsUFormula.verum,
    Bootstrapping.substs_verum (L := ℒₛₑₜ)]
  -- 现在两侧同形，用三个关键等式收尾
  rw [subst_QvecV_conjunct_open (m := m) (i := 0) (t := v.[0])
      (hv.nth (i := 0) (by norm_num)) (by norm_num : (0 : V) ≤ 1),
    subst_QvecV_conjunct_open (m := m) (i := 1) (t := v.[1])
      (hv.nth (i := 1) (by norm_num)) (by norm_num : (1 : V) ≤ 1),
    subst_QvecV_cRel (m := m) (R := R)]

end GodelQ.ITSubstOpen8

#print axioms GodelQ.ITSubstOpen8.subst_QvecV_conjunct_open
#print axioms GodelQ.ITSubstOpen8.iTR_subst_open
