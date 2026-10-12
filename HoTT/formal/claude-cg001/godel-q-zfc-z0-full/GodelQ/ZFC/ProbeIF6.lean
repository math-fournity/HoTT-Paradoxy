import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
set_option maxHeartbeats 800000
namespace GodelQ.ProbeIF6
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 项层的「前缀代入」：`termSubst` 只看 `bv t` 个分量 -/

/-- `termSubstVec` 的逐分量一致。 -/
lemma termSubstVec_congr {n w w' : V} (hww : ∀ i < n, w.[i] = w'.[i]) :
    ∀ {k : V} {v : V}, IsSemitermVec ℒₛₑₜ k n v →
      (∀ i < k, termSubst ℒₛₑₜ w v.[i] = termSubst ℒₛₑₜ w' v.[i]) →
      termSubstVec ℒₛₑₜ k w v = termSubstVec ℒₛₑₜ k w' v := by
  intro k v hv ih
  apply nth_ext' k (by rw [len_termSubstVec hv.isUTerm])
    (by rw [len_termSubstVec hv.isUTerm])
  intro i hi
  rw [nth_termSubstVec hv.isUTerm hi, nth_termSubstVec hv.isUTerm hi]
  exact ih i hi

lemma termSubst_congr {n w w' : V} (hww : ∀ i < n, w.[i] = w'.[i]) :
    ∀ t, IsSemiterm ℒₛₑₜ n t → termSubst ℒₛₑₜ w t = termSubst ℒₛₑₜ w' t := by
  intro t ht
  apply IsSemiterm.sigma1_induction (L := ℒₛₑₜ) (n := n) (P := fun t ↦
    termSubst ℒₛₑₜ w t = termSubst ℒₛₑₜ w' t)
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

end GodelQ.ProbeIF6
