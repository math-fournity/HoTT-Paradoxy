import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFJ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 目标：`iT_substs1`（一般层 1 的 σ）

```
iT 0 (subst ?[^&0] σ) = subst ?[^&0] (iT 1 σ)      （σ 层 1）
```

用 `semiformula_result_induction`。本文件先立**骨架**（9 支），
逐支填；`rel` 支已由原子情形（`iT_substs1_atom` 的推广）覆盖。

**层数账**：`iT` 的 `all`/`exs` 支把层数 `param ↦ param+1`，
`subst` 推过 `qqAlls` 时向量 `w ↦ qVec w`。两者**同步**，
故归纳不变量取 `P param n p q := param = n → iT param (subst ?[^&0] p) = subst ?[^&0] q`。
-/

/-- `subst` 推过 `qqAlls`（Nat 归纳 + `congr 3`）。 -/
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

/-- `subst (qVec w) domZero = domZero`（层 1 项向量 `w`）。 -/
lemma subst_qVec_domZero' {w : V} (hw : IsSemitermVec ℒₛₑₜ (len w) (1:V) w) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN (V := V)]
  have hd : IsSemiformula ℒₛₑₜ (1:V) ((cDomN : ℕ) : V) := isSemiformula_cDomN (V := V)
  have hlen : (1:V) ≤ len (qVec ℒₛₑₜ w) := by
    rw [Bootstrapping.qVec]; simp [len_adjoin]
  have hW : IsSemitermVec ℒₛₑₜ (len (qVec ℒₛₑₜ w)) (2:V) (qVec ℒₛₑₜ w) := by
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
      have hbv : termBV ℒₛₑₜ (termBShift ℒₛₑₜ w.[l]) ≤ (1:V) + 1 :=
        (termBV_termBShift_le (L := ℒₛₑₜ) (hw.nth hl).isUTerm (1:V)).mpr (hw.nth hl).bv
      exact ⟨(hw.nth hl).isUTerm.termBShift, by norm_num at hbv ⊢; exact hbv⟩
  refine (subst_congr_prefix (V := V) (n := (1:V)) (m := (2:V))
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

/-- `subst` 推过两层 `qqAlls`（`k = 2` 的专用版，避免一般版的 `whnf` 爆炸）。 -/
lemma substs_qqAlls_two {X : V} (hX : IsUFormula ℒₛₑₜ X) :
    subst ℒₛₑₜ (?[^&0] : V) (qqAlls X (2:V))
      = qqAlls (subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) X) (2:V) := by
  rw [show (2:V) = ((2:ℕ):V) by norm_num, substs_qqAlls 2 X (?[^&0] : V) hX]
  congr 2
  -- `(qVec)^[2] ?[^&0] = ?[^#0,^#1,^&0]`
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

/-- `?[^#0,^#1,^&0]` 是长度 3、层数 2 的项向量。 -/
lemma isSemitermVec_W3 : IsSemitermVec ℒₛₑₜ (3:V) (2:V) (?[^#0, ^#1, ^&0] : V) := by
  refine IsSemitermVec.iff.mpr ⟨?_, fun j hj ↦ ?_⟩
  · rw [show (?[^#0, ^#1, ^&0] : V)
          = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
    simp only [len_adjoin, len_nil]; norm_num
  · rw [show (?[^#0, ^#1, ^&0] : V)
          = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl] at hj ⊢
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

/-- `imp A X` 的 `IsUFormula`（`A` 抽象为 `Y`）。 -/
lemma hbody' {X Y : V} (hY : IsUFormula ℒₛₑₜ Y) (hX : IsUFormula ℒₛₑₜ X) :
    IsUFormula ℒₛₑₜ (imp ℒₛₑₜ Y X) :=
  IsUFormula.or.mpr ⟨hY.neg, hX⟩

/-- **`rel` 支（一般 `v`）** —— 逐步 bisect（当前只到左侧内层）。 -/
lemma branch_rel {R v : V} (hR : (ℒₒᵣ).IsRel (2:V) R) (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 R v)) := by
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  have htv : IsUTermVec ℒₒᵣ (2:V) (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v) :=
    (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (V := V)
      (IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (2:V)) 0))
      hv).isUTerm
  rw [iT_rel (V := V) (n := (0:V)) (k := (2:V)) (R := R)
    (v := termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v) hR htv]
  rw [iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := R) (v := v) hR hv.isUTerm]
  rw [iTR, iTR]
  rw [show (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v).[0]
        = termSubst ℒₒᵣ (?[^&0] : V) v.[0] from
      nth_termSubstVec hv.isUTerm (by norm_num),
    show (termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) v).[1]
        = termSubst ℒₒᵣ (?[^&0] : V) v.[1] from
      nth_termSubstVec hv.isUTerm (by norm_num)]
  have hYs : IsSemiformula ℒₛₑₜ (3:V) (conjunct 2 1 0 (iVE (1:V) v.[0]) ^⋏
      (conjunct 2 1 1 (iVE (1:V) v.[1]) ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr
      ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (0:V))
        (isSemiformula_iVE (n := (1:V)) v.[0] (hv.nth (by norm_num))) (by norm_num),
       IsSemiformula.and.mpr
        ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
          (isSemiformula_iVE (n := (1:V)) v.[1] (hv.nth (by norm_num))) (by norm_num),
         IsSemiformula.verum⟩⟩
  have hY : IsUFormula ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) v.[0]) ^⋏
      (conjunct 2 1 1 (iVE (1:V) v.[1]) ^⋏ ^⊤)) := hYs.isUFormula
  have hX : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel R)
      (IsSemitermVec.doubleton.mpr
        ⟨(IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (0:V))).mpr (by norm_num),
         (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (1:V))).mpr (by norm_num)⟩)).isUFormula
  rw [substs_qqAlls_two (hbody' hY hX)]
  congr 1
  -- 内层：`subst ?[^#0,^#1,^&0] (imp A C) = imp A' C`
  rw [show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl,
    show (imp ℒₛₑₜ _ _ : V) = (neg ℒₛₑₜ _ ^⋎ _ : V) from rfl]
  rw [Bootstrapping.substs_or (L := ℒₛₑₜ) (w := (?[^#0, ^#1, ^&0] : V))
    (p := (neg ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) v.[0]) ^⋏
      (conjunct 2 1 1 (iVE (1:V) v.[1]) ^⋏ ^⊤))))
    (q := (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)))
    hY.neg hX]
  congr 1
  · -- `neg` 分量
    rw [Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := (3:V)) (m := (2:V))
      (p := (conjunct 2 1 0 (iVE (1:V) v.[0]) ^⋏
        (conjunct 2 1 1 (iVE (1:V) v.[1]) ^⋏ ^⊤))) hYs isSemitermVec_W3]
    congr 1
    -- `subst ?[^#0,^#1,^&0] (A0 ⋏ A1) = A0' ⋏ A1'`
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ)
      (isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (0:V))
        (isSemiformula_iVE (n := (1:V)) v.[0] (hv.nth (by norm_num))) (by norm_num)).isUFormula
      (IsUFormula.and.mpr
        ⟨(isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
          (isSemiformula_iVE (n := (1:V)) v.[1] (hv.nth (by norm_num))) (by norm_num)).isUFormula,
         IsUFormula.verum⟩)]
    congr 1
    · rw [conjunct, conjunct]
      congr 1
      · -- 第一分量：`subst ?[^#0] cDomN` 在 `W` 下不动
        exact (subst_congr_prefix (V := V) (n := (1:V)) (m := (2:V)) (k₁ := (3:V)) (k₂ := (1:V))
          (w := (?[^#0, ^#1, ^&0] : V)) (w' := (?[^#0] : V)) (subst ℒₛₑₜ (?[^#0] : V) (↑cDomN : V))
          (IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
            (isSemitermVec_single_bvar (n := (2:V)) (by norm_num))).isUFormula
          (by norm_num) (by norm_num)
          isSemitermVec_W3
          (isSemitermVec_single_bvar (n := (1:V)) (by norm_num))
          (fun j hj ↦ by
            have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
            subst hj0
            rw [show (?[^#0, ^#1, ^&0] : V)
                  = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl,
              show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
            simp only [nth_adjoin_zero])).symm
      · sorry
    · sorry
  · -- `cRel` 分量
    sorry
  sorry

end GodelQ.ProbeFJ
