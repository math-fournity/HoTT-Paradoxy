import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
set_option maxHeartbeats 800000
namespace GodelQ.ProbeCP
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `termSubstVec` 的逐分量一致。 -/
lemma termSubstVec_congr {n w w' : V} (_hww : ∀ i < n, w.[i] = w'.[i]) :
    ∀ {k : V} {v : V}, IsSemitermVec ℒₛₑₜ k n v →
      (∀ i < k, termSubst ℒₛₑₜ w v.[i] = termSubst ℒₛₑₜ w' v.[i]) →
      termSubstVec ℒₛₑₜ k w v = termSubstVec ℒₛₑₜ k w' v := by
  intro k v hv ih
  apply nth_ext' k (by rw [len_termSubstVec hv.isUTerm])
    (by rw [len_termSubstVec hv.isUTerm])
  intro i hi
  rw [nth_termSubstVec hv.isUTerm hi, nth_termSubstVec hv.isUTerm hi]
  exact ih i hi

/-- `termSubst` 的前缀一致。 -/
lemma termSubst_congr {n w w' : V} (hww : ∀ i < n, w.[i] = w'.[i]) :
    ∀ t, IsSemiterm ℒₛₑₜ n t → termSubst ℒₛₑₜ w t = termSubst ℒₛₑₜ w' t := by
  intro t ht
  apply IsSemiterm.sigma1_induction (L := ℒₛₑₜ) (n := n)
    (P := fun t ↦ termSubst ℒₛₑₜ w t = termSubst ℒₛₑₜ w' t)
  · definability
  · intro z hz
    rw [termSubst_bvar, termSubst_bvar]
    exact hww z hz
  · intro x
    rw [termSubst_fvar, termSubst_fvar]
  · intro k f v hkf hv ih
    rw [termSubst_func hkf hv.isUTerm, termSubst_func hkf hv.isUTerm]
    congr 1
    exact termSubstVec_congr hww hv ih
  · exact ht

/-- **`subst` 只看前 `n` 个分量**：`w` 与 `w'` 在前 `n` 个分量上一致 ⟹ 结果一致。 -/
lemma subst_congr_prefix : ∀ {n : V} (p : V), IsSemiformula ℒₛₑₜ n p →
    ∀ {m w w' : V}, IsSemitermVec ℒₛₑₜ n m w → IsSemitermVec ℒₛₑₜ n m w' →
    (∀ i < n, w.[i] = w'.[i]) → subst ℒₛₑₜ w p = subst ℒₛₑₜ w' p := by
  intro n p hp
  apply IsSemiformula.pi1_structural_induction (L := ℒₛₑₜ) ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hp
  · definability
  · intro n k R v hR hv m w w' hw hw' H
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR hv.isUTerm,
      Bootstrapping.substs_rel (L := ℒₛₑₜ) hR hv.isUTerm]
    congr 1
    apply nth_ext' k (by rw [len_termSubstVec hv.isUTerm])
      (by rw [len_termSubstVec hv.isUTerm])
    intro i hi
    rw [nth_termSubstVec hv.isUTerm hi, nth_termSubstVec hv.isUTerm hi]
    exact termSubst_congr H v.[i] (hv.nth hi)
  · intro n k R v hR hv m w w' hw hw' H
    rw [Bootstrapping.substs_nrel (L := ℒₛₑₜ) hR hv.isUTerm,
      Bootstrapping.substs_nrel (L := ℒₛₑₜ) hR hv.isUTerm]
    congr 1
    apply nth_ext' k (by rw [len_termSubstVec hv.isUTerm])
      (by rw [len_termSubstVec hv.isUTerm])
    intro i hi
    rw [nth_termSubstVec hv.isUTerm hi, nth_termSubstVec hv.isUTerm hi]
    exact termSubst_congr H v.[i] (hv.nth hi)
  · intro n m w w' _ _ _
    simp
  · intro n m w w' _ _ _
    simp
  · intro n p q hp hq ihp ihq m w w' hw hw' H
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula,
      Bootstrapping.substs_and (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula,
      ihp hw hw' H, ihq hw hw' H]
  · intro n p q hp hq ihp ihq m w w' hw hw' H
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula,
      Bootstrapping.substs_or (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula,
      ihp hw hw' H, ihq hw hw' H]
  · intro n p hp ih m w w' hw hw' H
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hp.isUFormula,
      Bootstrapping.substs_all (L := ℒₛₑₜ) hp.isUFormula]
    congr 1
    refine ih hw.qVec hw'.qVec ?_
    intro i hi
    rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
    · simp [Bootstrapping.qVec]
    · have hj : j < n := by simpa using hi
      have h1 : (qVec ℒₛₑₜ w).[j + 1] = termBShift ℒₛₑₜ w.[j] := by
        rw [Bootstrapping.qVec, nth_adjoin_succ]
        rw [show len w = n from hw.lh]
        exact nth_termBShiftVec hw.isUTerm hj
      have h2 : (qVec ℒₛₑₜ w').[j + 1] = termBShift ℒₛₑₜ w'.[j] := by
        rw [Bootstrapping.qVec, nth_adjoin_succ]
        rw [show len w' = n from hw'.lh]
        exact nth_termBShiftVec hw'.isUTerm hj
      rw [h1, h2, H j hj]
  · intro n p hp ih m w w' hw hw' H
    rw [Bootstrapping.substs_ex (L := ℒₛₑₜ) hp.isUFormula,
      Bootstrapping.substs_ex (L := ℒₛₑₜ) hp.isUFormula]
    congr 1
    refine ih hw.qVec hw'.qVec ?_
    intro i hi
    rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
    · simp [Bootstrapping.qVec]
    · have hj : j < n := by simpa using hi
      have h1 : (qVec ℒₛₑₜ w).[j + 1] = termBShift ℒₛₑₜ w.[j] := by
        rw [Bootstrapping.qVec, nth_adjoin_succ]
        rw [show len w = n from hw.lh]
        exact nth_termBShiftVec hw.isUTerm hj
      have h2 : (qVec ℒₛₑₜ w').[j + 1] = termBShift ℒₛₑₜ w'.[j] := by
        rw [Bootstrapping.qVec, nth_adjoin_succ]
        rw [show len w' = n from hw'.lh]
        exact nth_termBShiftVec hw'.isUTerm hj
      rw [h1, h2, H j hj]

end GodelQ.ProbeCP
