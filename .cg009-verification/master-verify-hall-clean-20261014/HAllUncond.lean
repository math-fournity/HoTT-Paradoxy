-- CG-009: **hAll 无条件版** —— hAB 前提由 `HABElim.hAB_derivable` 现场供给。
--
-- `HAllProof.hAll_uncond` 的最后前提
--     hAB : Derivable (neg ℒₛₑₜ A ^⋎ B) ∅,  A := iT 0 (free p), B := free (imp domZero (iT 1 p))
-- 需要 `p` 是层 1 的公式。本文件补上那个公式性（从 `hs` + `hp` 出），
-- 然后把 `hAB` 填成 `HABElim.hAB_derivable p hpS`，得到**无额外前提**的 hAll。
--
-- ## 层 1 从哪来
--
-- `IsFormulaSet s` + `(^∀ p) ∈ s` ⟹ `IsSemiformula ℒₒᵣ 1 p`
-- （`IsSemiformula.all` 的 `n := 0` 实例：`(^∀ p) : 层 0` ⟺ `p : 层 1`）。
import GodelQ.ZFC.HABElim

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.HAllProof GodelQ.HABElim GodelQ.GateBranches

namespace GodelQ.HAllUncond
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hAll`，无算术前提**：hAB 由命题重言式现场满足。

前四条与 `HAllProof.hAll_uncond` 相同，第五条 hAB 不再是前提——
它由 `HABElim.hAB_derivable` 给出。 -/
theorem hAll_uncond' {s p d : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p : V) ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s)))
    (ih : Q d) :
    Q (allIntro s p d) := by
  -- p 是层 1 的公式（`^∀ p` 在层 0 的公式集 s 里）
  have hpU : IsUFormula ℒₒᵣ p := IsUFormula.all.mp ((hs (^∀ p) hp).isUFormula)
  have hpS : IsSemiformula ℒₒᵣ 1 p := by
    have h := (IsSemiformula.all (L := ℒₒᵣ) (n := (0 : V))).mp (hs (^∀ p) hp)
    rwa [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
  exact HAllProof.hAll_uncond hs hp hd ih (HABElim.hAB_derivable p hpS)

end GodelQ.HAllUncond

#print axioms GodelQ.HAllUncond.hAll_uncond'
