import GodelQ.ZFC.ProbeE

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ProbeE

set_option maxHeartbeats 800000

namespace GodelQ.ProbeH

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ══ 三元 bvar 向量 ═══════════════════════════════════════════════════════

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

-- ══ ve0 ═════════════════════════════════════════════════════════════════

lemma shift_ve0 (f : V) : shift ℒₛₑₜ (ve0 0 f) = ve0 0 f := by
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

-- ══ qqAlls 与 shift 交换 ═════════════════════════════════════════════════

lemma shift_qqAlls {p k : V} (hp : IsUFormula ℒₛₑₜ p) :
    shift ℒₛₑₜ (qqAlls p k) = qqAlls (shift ℒₛₑₜ p) k := by
  induction k using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ k ih =>
    rw [qqAlls_succ, qqAlls_succ, Bootstrapping.shift_all (isUFormula_qqAlls.mpr hp), ih]

-- ══ subst (^#2 ∷ ?[#0, #1]) (cFunc k f) 在 shift 下 ═══════════════════════

lemma shift_subst_cFunc {n k f : V} (hk : k ≠ 0) :
    shift ℒₛₑₜ (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f))
      = subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f) := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc k f) := isSemiformula_cFunc_arity2 hk f
  have hv : IsSemitermVec ℒₛₑₜ 3 (3 + n)
      ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) := by
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
  rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
  rw [Bootstrapping.shift_substs hc hv,
      termShiftVec_three_bvars, shift_cFunc]

-- ══ ve2 与 shift 交换 ════════════════════════════════════════════════════

lemma shift_ve2 {n k f w w' : V} (hk : k ≠ 0)
    (hw0 : IsSemiformula ℒₛₑₜ (n + 1) w.[0])
    (hw1 : IsSemiformula ℒₛₑₜ (n + 1) w.[1])
    (hw'0 : w'.[0] = shift ℒₛₑₜ w.[0])
    (hw'1 : w'.[1] = shift ℒₛₑₜ w.[1]) :
    shift ℒₛₑₜ (ve2 n k f w) = ve2 n k f w' := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc k f) := isSemiformula_cFunc_arity2 hk f
  have hB : IsSemiformula ℒₛₑₜ (3 + n)
      (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) hc (by
      rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl,
        show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by
          simpa [show (3 : V) = 2 + 1 by norm_num, add_assoc] using two_lt_three_add n), ?_⟩
      rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by
          simpa [show (3 : V) = 1 + 1 + 1 by norm_num, add_assoc] using zero_lt_three_add n), ?_⟩
      rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
      exact ⟨IsSemiterm.bvar.mpr (by
          simpa [show (3 : V) = 1 + 1 + 1 by norm_num, add_assoc] using one_lt_three_add n),
        by simp⟩)
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

end GodelQ.ProbeH
