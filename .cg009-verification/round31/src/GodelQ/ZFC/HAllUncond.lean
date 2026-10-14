-- CG-009: **hAll 无条件版** —— 把 HABElim.hAB_derivable 接进 hAll_uncond。
--
-- `HAllProof.hAll_uncond` 的唯一前提是
--   hAB : Derivable 𝗭𝗙𝗖 (insert (neg (iT 0 (free p)) ⋎ free (imp domZero (iT 1 p))) ∅)
-- 而 `HABElim.hAB_derivable` 正是它的**无条件**证明（0 sorryAx，公理三条）。
-- 故 hAll 现在无条件。
import GodelQ.ZFC.HABElim
import GodelQ.ZFC.HAllProof

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.HAllUncond

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **hAll 无条件**：最后一条前提 `hAB` 由 `HABElim.hAB_derivable` 提供。 -/
theorem hAll {s p d : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p : V) ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s)))
    (ih : Q d) :
    Q (allIntro s p d) := by
  have hpS : IsSemiformula ℒₒᵣ 1 p := by
    have := (IsSemiformula.all (L := ℒₒᵣ) (n := 0)).mp (hs (^∀ p) hp)
    simpa using this
  exact GodelQ.HAllProof.hAll_uncond hs hp hd ih
    (GodelQ.HABElim.hAB_derivable p hpS)

end GodelQ.HAllUncond

#print axioms GodelQ.HAllUncond.hAll
