-- CG-009: upgraded conditional ShCraigElim — the `tshift` obligation is discharged.
-- Five obligations → four: {hall, hexs, axmBridge} plus the already-proven iT_neg.
import GodelQ.ZFC.TShiftBranches
import GodelQ.ZFC.ShCraigElimNegLaw

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.GateBranchesU2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 800000 in
/-- **Upgraded conditional ShCraigElim**: `iT_neg` (proven in `ShCraigElimNegLaw`) and
    `tshift` (proven in `TShiftFull`) are both discharged here.
    Only the three genuine obligations `hall` / `hexs` / `axmBridge` remain as premises.

    The `tshift` discharge works because `hShift`'s only call site has the formula-set
    evidence in hand: the induction gives `hs : IsFormulaSet s` for the sequent `s`,
    and `s = setShift (fstIdx d)` transfers it to `fstIdx d` by `isFormulaSet_of_setShift_eq`. -/
theorem shCraigElim_of_obligations'
    (hall : ∀ s' p' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (free (L := ℒₒᵣ) p')
        (setShift (L := ℒₒᵣ) s'))) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s'))
    (hexs : ∀ s' p' t' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (substs1 (L := ℒₒᵣ) t' p') s')) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s'))
    (axmBridge : ∀ p' : V, p' ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT (0 : V) p'))
    (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d) :
    GodelQ.GateBranches.Q d := by
  apply Derivation.induction1 (T := Sh.craig) 𝚺
    (hP := GodelQ.GateBranches.q_defined.to_definable) hd
  · intro s hs p hp hn
    exact GodelQ.GateBranches.hAxL
      (fun n p hp => GodelQ.ShCraigElimNegLaw.iT_neg (n := n) p hp) hs hp hn
  · intro s hs hv; exact GodelQ.GateBranches.hVerumIntro hs hv
  · intro s hs p q dp dq hpq hdp hdq ihp ihq
    exact GodelQ.GateBranches.hAnd hs hpq hdp hdq ihp ihq
  · intro s hs p q d hpq hd ih; exact GodelQ.GateBranches.hOr hs hpq hd ih
  · intro s hs p d hp hd ih
    exact GodelQ.GateBranches.hAll (fun p' hU h => hall s p' hU h) hs hp hd ih
  · intro s hs p t d hp ht hd ih
    exact GodelQ.GateBranches.hExs (fun p' t' hU h => hexs s p' t' hU h) hs hp hd ih
  · intro s hs d h hd ih; exact GodelQ.GateBranches.hWk hs h ih
  · intro s hs d h hd ih; exact GodelQ.TShiftBranches.hShift_uncond hs h ih
  · intro s hs p d₁ d₂ h₁ h₂ ih₁ ih₂
    exact GodelQ.GateBranches.hCut
      (fun n p hp => GodelQ.ShCraigElimNegLaw.iT_neg (n := n) p hp) hs h₁ h₂ ih₁ ih₂
  · intro s hs p hps hpT; exact GodelQ.GateBranches.hAxm axmBridge hs hps hpT

end GodelQ.GateBranchesU2

#print axioms GodelQ.GateBranchesU2.shCraigElim_of_obligations'
