import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`1 ≤ len w + 1`**（V 层）。 -/
lemma one_le_len_add_one (w : V) : (1:V) ≤ len w + 1 := by
  -- `1 ≤ len w + 1` ⟸ `0 ≤ len w`（`lt_succ_iff_le` 的逆）
  have h : (0:V) < len w + 1 := by
    have := lt_add_self_add_one (0:V) (len w)
    rwa [show len w + 0 + 1 = len w + 1 by ring] at this
  exact lt_succ_iff_le.mp (by simpa using h)

/-- **`subst_qVec_domZero'` 的层数放宽版**（只要求 `w` 是项向量）。 -/
lemma subst_qVec_domZero'' {w : V} (hw : IsUTermVec ℒₛₑₜ (len w) w) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN (V := V)]
  refine (subst_congr_prefix' (L := ℒₛₑₜ) (n := (1:V)) (m := (1:V))
    (k₁ := len (qVec ℒₛₑₜ w)) (k₂ := (1:V)) ((cDomN : ℕ) : V)
    (isSemiformula_cDomN (V := V))
    (by rw [TranslateShiftCompat.len_qVec hw]; exact one_le_len_add_one w)
    (by norm_num) ?_
    (IsSemitermVec.singleton.mpr
      ((IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)))
    ?_).trans ?_
  · -- `qVec w` 的项向量性（层取 1）
    refine IsSemitermVec.iff (L := ℒₛₑₜ) (k := len (qVec ℒₛₑₜ w)) (n := (1:V))
      (v := qVec ℒₛₑₜ w) |>.mpr ⟨rfl, fun i hi ↦ ?_⟩
    rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl] at hi ⊢
    rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
    · rw [nth_adjoin_zero]
      exact (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)
    · rw [nth_adjoin_succ]
      have hj' : j < len w := by
        have h := (add_lt_add_iff_right (1:V)).mp (by simpa using hi)
        rwa [len_termBShiftVec (V := V) (L := ℒₛₑₜ) hw] at h
      have hb := (termBV_termBShift_le (L := ℒₛₑₜ)
        (IsSemiterm.isUTerm (hw.nth hj')) (0:V)).mpr (IsSemiterm.bv (hw.nth hj'))
      exact ⟨(IsUTermVec.termBShiftVec (L := ℒₛₑₜ) (V := V) hw).nth
        (by rw [len_termBShiftVec (V := V) (L := ℒₛₑₜ) hw]; exact hj'), by simpa using hb⟩
  · intro j hj
    have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
    subst hj0
    rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
      rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl]
      rw [nth_adjoin_zero]]
    rw [show (?[^#0] : V).[0] = (^#0 : V) from by
      rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero]]
  · refine subst_eq_self (L := ℒₛₑₜ) (n := (1:V)) (w := (?[^#0] : V))
      (isSemiformula_cDomN (V := V))
      (IsSemitermVec.singleton.mpr
        ((IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num))) ?_
    intro i hi
    have hz : i = 0 := lt_one_iff_eq_zero.mp hi
    subst hz
    rw [show (?[^#0] : V).[0] = (^#0 : V) from by
      rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero]]

end GodelQ.ProbeFL
