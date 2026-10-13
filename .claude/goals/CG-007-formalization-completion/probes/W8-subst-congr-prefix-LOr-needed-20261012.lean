import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`subst` 的「层数收缩」**：`subst ?[^#0,^&0] p = subst ?[^#0] p`（`p` 层 1）。

这是候选 1 的**关键桥**：`subst` 只看前 `n` 个分量（`subst_congr_prefix`），
故把长度 2 的向量缩到长度 1 不改变结果。 -/
lemma subst_two_eq_subst_one {p : V} (hp : IsSemiformula ℒₒᵣ (1:V) p) :
    subst ℒₒᵣ (?[^#0, ^&0] : V) p = subst ℒₒᵣ (?[^#0] : V) p := by
  have hv2 : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^#0, ^&0] : V) := by
    refine IsSemitermVec.iff.mpr ⟨?_, ?_⟩
    · rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
      simp only [len_adjoin, len_nil]; norm_num
    · intro j hj
      show IsSemiterm ℒₒᵣ (1:V) ((^#0 : V) ∷ ((^&0 : V) ∷ (0:V))).[j]
      rcases lt_two_cases hj with rfl | rfl
      · rw [nth_adjoin_zero]; exact IsSemiterm.bvar.mpr (by norm_num)
      · rw [nth_adjoin_one, nth_adjoin_zero]
        exact IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0
  have hv1 : IsSemitermVec ℒₒᵣ (1:V) (1:V) (?[^#0] : V) :=
    IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr (by norm_num))
  -- 用 `subst_congr_prefix` 的 ℒₒᵣ 版：先证它
  have key : ∀ {n : V} (q : V), IsSemiformula ℒₒᵣ n q →
      ∀ {k₁ k₂ m w w' : V}, n ≤ k₁ → n ≤ k₂ →
      IsSemitermVec ℒₒᵣ k₁ m w → IsSemitermVec ℒₒᵣ k₂ m w' →
      (∀ i < n, w.[i] = w'.[i]) → subst ℒₒᵣ w q = subst ℒₒᵣ w' q := by
    intro n q hq
    apply IsSemiformula.pi1_structural_induction (L := ℒₒᵣ) ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hq
    · definability
    · intro n k R v hR hv k₁ k₂ m w w' h1 h2 hw hw' H
      rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm,
        Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
      congr 1
      apply nth_ext' k (by rw [len_termSubstVec hv.isUTerm])
        (by rw [len_termSubstVec hv.isUTerm])
      intro i hi
      rw [nth_termSubstVec hv.isUTerm hi, nth_termSubstVec hv.isUTerm hi]
      exact termSubst_congr (L := ℒₒᵣ) (n := n) H v.[i] (hv.nth hi)
    · intro n k R v hR hv k₁ k₂ m w w' h1 h2 hw hw' H
      rw [Bootstrapping.substs_nrel (L := ℒₒᵣ) hR hv.isUTerm,
        Bootstrapping.substs_nrel (L := ℒₒᵣ) hR hv.isUTerm]
      congr 1
      apply nth_ext' k (by rw [len_termSubstVec hv.isUTerm])
        (by rw [len_termSubstVec hv.isUTerm])
      intro i hi
      rw [nth_termSubstVec hv.isUTerm hi, nth_termSubstVec hv.isUTerm hi]
      exact termSubst_congr (L := ℒₒᵣ) (n := n) H v.[i] (hv.nth hi)
    · intro n k₁ k₂ m w w' _ _ _ _ _; simp
    · intro n k₁ k₂ m w w' _ _ _ _ _; simp
    · intro n p q hp hq ihp ihq k₁ k₂ m w w' h1 h2 hw hw' H
      rw [Bootstrapping.substs_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
        Bootstrapping.substs_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
        ihp h1 h2 hw hw' H, ihq h1 h2 hw hw' H]
    · intro n p q hp hq ihp ihq k₁ k₂ m w w' h1 h2 hw hw' H
      rw [Bootstrapping.substs_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
        Bootstrapping.substs_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
        ihp h1 h2 hw hw' H, ihq h1 h2 hw hw' H]
    · intro n p hp ih k₁ k₂ m w w' h1 h2 hw hw' H
      rw [Bootstrapping.substs_all (L := ℒₒᵣ) hp.isUFormula,
        Bootstrapping.substs_all (L := ℒₒᵣ) hp.isUFormula]
      congr 1
      refine ih (add_le_add_iff_right (1:V) |>.mpr h1)
        (add_le_add_iff_right (1:V) |>.mpr h2) hw.qVec hw'.qVec ?_
      intro i hi
      rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
      · simp [Bootstrapping.qVec]
      · have hj : j < n := by simpa using hi
        have hj1 : j < k₁ := lt_of_lt_of_le hj h1
        have hj2 : j < k₂ := lt_of_lt_of_le hj h2
        simp only [Bootstrapping.qVec, nth_adjoin_succ]
        rw [show len w = k₁ from hw.lh, show len w' = k₂ from hw'.lh,
          nth_termBShiftVec hw.isUTerm hj1, nth_termBShiftVec hw'.isUTerm hj2, H j hj]
    · intro n p hp ih k₁ k₂ m w w' h1 h2 hw hw' H
      rw [Bootstrapping.substs_ex (L := ℒₒᵣ) hp.isUFormula,
        Bootstrapping.substs_ex (L := ℒₒᵣ) hp.isUFormula]
      congr 1
      refine ih (add_le_add_iff_right (1:V) |>.mpr h1)
        (add_le_add_iff_right (1:V) |>.mpr h2) hw.qVec hw'.qVec ?_
      intro i hi
      rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
      · simp [Bootstrapping.qVec]
      · have hj : j < n := by simpa using hi
        have hj1 : j < k₁ := lt_of_lt_of_le hj h1
        have hj2 : j < k₂ := lt_of_lt_of_le hj h2
        simp only [Bootstrapping.qVec, nth_adjoin_succ]
        rw [show len w = k₁ from hw.lh, show len w' = k₂ from hw'.lh,
          nth_termBShiftVec hw.isUTerm hj1, nth_termBShiftVec hw'.isUTerm hj2, H j hj]
  exact key p hp (by norm_num) (by norm_num) hv2 hv1 (fun j hj ↦ by
    have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
    subst hj0
    rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl,
      show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
    rw [nth_adjoin_zero, nth_adjoin_zero])

end GodelQ.ProbeFL
