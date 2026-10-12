import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
set_option maxHeartbeats 800000
namespace GodelQ.ProbeIF5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 放宽版：`subst` 只看前 `bv p` 个分量

若 `w` 与 `w'` 在前 `n` 个分量上一致，则 `subst w p = subst w' p`（`p` 层 `n`）。
这条比 `subst_eq_self` 更基本，且足以覆盖 `cDomN` 的情形。 -/

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
    -- `termSubstVec k w v = termSubstVec k w' v`（逐分量用 `H`）
    sorry
  · intro n k R v hR hv m w w' hw hw' H
    rw [Bootstrapping.substs_nrel (L := ℒₛₑₜ) hR hv.isUTerm,
      Bootstrapping.substs_nrel (L := ℒₛₑₜ) hR hv.isUTerm]
    congr 1
    sorry
  · intro n m w w' _ _ _
    simp
  · intro n m w w' _ _ _
    simp
  · intro n p q hp hq ihp ihq m w w' hw hw' H
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula,
      Bootstrapping.substs_and (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula, ihp hw hw' H, ihq hw hw' H]
  · intro n p q hp hq ihp ihq m w w' hw hw' H
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula,
      Bootstrapping.substs_or (L := ℒₛₑₜ) hp.isUFormula hq.isUFormula, ihp hw hw' H, ihq hw hw' H]
  · intro n p hp ih m w w' hw hw' H
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hp.isUFormula,
      Bootstrapping.substs_all (L := ℒₛₑₜ) hp.isUFormula]
    congr 1
    sorry
  · intro n p hp ih m w w' hw hw' H
    rw [Bootstrapping.substs_ex (L := ℒₛₑₜ) hp.isUFormula,
      Bootstrapping.substs_ex (L := ℒₛₑₜ) hp.isUFormula]
    congr 1
    sorry

end GodelQ.ProbeIF5
