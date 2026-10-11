-- CG-009 absorption: with the newly-proven iT_neg (from worktree cg007-w8-d3),
-- GateBranches' hAxL/hCut become UNCONDITIONAL.
import GodelQ.ZFC.GateBranches
import GodelQ.ZFC.ShCraigElimNegLaw

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.GateBranches

namespace GodelQ.GateBranchesU

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- hAxL, now unconditional (uses the proven iT_neg). -/
theorem hAxL_uncond {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : p ∈ s) (hn : neg ℒₒᵣ p ∈ s) : Q (axL s p) :=
  hAxL (fun n p' hp' => GodelQ.ShCraigElimNegLaw.iT_neg (n := n) p' hp') hs hp hn

/-- hCut, now unconditional. -/
theorem hCut_uncond {s p d₁ d₂ : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hd₁ : DerivationOf (L := ℒₒᵣ) Sh.craig d₁ (insert p s))
    (hd₂ : DerivationOf (L := ℒₒᵣ) Sh.craig d₂ (insert (neg ℒₒᵣ p) s))
    (ih₁ : Q d₁) (ih₂ : Q d₂) : Q (cutRule s p d₁ d₂) :=
  hCut (fun n p' hp' => GodelQ.ShCraigElimNegLaw.iT_neg (n := n) p' hp') hs hd₁ hd₂ ih₁ ih₂

end GodelQ.GateBranchesU

#print axioms GodelQ.GateBranchesU.hAxL_uncond
#print axioms GodelQ.GateBranchesU.hCut_uncond
