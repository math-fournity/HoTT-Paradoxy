import GodelQ.ZFC.CG008ShiftProof
import GodelQ.ZFC.CG008Bv2

/-!
# CG-008 · `bv (iVE n t) ≤ n + 1`：Σ₁ 闸门
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Bv3
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **Σ₁ 闸门**：`P t := bv (iVE n t) ≤ n + 1` 是 Σ₁ 可定义。 -/
theorem bv_iVE_gate (n : V) :
    𝚺ᴬ₁-Predicate (fun t : V ↦ Bootstrapping.bv ℒₛₑₜ (Translate.iVE n t) ≤ n + 1) := by
  have hF : { Γ := 𝚺, rank := 1 }-Function₂ (Translate.iVE : V → V → V) :=
    GodelQ.Translate.iVE_definable' 𝚺 0
  have hf : 𝚺ᴬ₁.DefinableFunction (fun v : Fin 1 → V ↦ Translate.iVE n (v 0)) :=
    hF.comp (Bounding.HierarchySymbol.DefinableFunction.const n)
      (Bounding.HierarchySymbol.DefinableFunction.var 0)
  have hcomp : { Γ := 𝚺, rank := 1 }-Function₁
      (fun r : V ↦ Bootstrapping.bv ℒₛₑₜ r) :=
    Bounding.HierarchySymbol.DefinableFunction.of_sigmaOne
      (L := ℒₒᵣ)
      (inferInstance : 𝚺ᴬ₁-Function₁ (fun r : V ↦ Bootstrapping.bv ℒₛₑₜ r))
  have h1 : 𝚺ᴬ₁.DefinableFunction (fun v : Fin 1 → V ↦
      Bootstrapping.bv ℒₛₑₜ (Translate.iVE n (v 0))) :=
    hcomp.comp hf
  have hle := Bounding.HierarchySymbol.DefinableRel.comp
    (Bounding.HierarchySymbol.DefinableRel.arithmetic_le (V := V) (ℌ := 𝚺ᴬ₁))
    h1 (Bounding.HierarchySymbol.DefinableFunction.const (n + 1))
  apply Bounding.HierarchySymbol.Definable.of_iff hle
  intro v
  simp

-- **`bv_eqAtom_le` 未证**：`bv_rel` 已能应用（`IsRel` 由 `isRel_quote_quote` 给，
-- 因 `cEqN = Encodable.encode Language.Eq.eq`），`listMaxss_le_iff` 已过，
-- `nth_termBVVec` 已过，两条分量引理（`CG008Bv2.nth_vec₂_zero/one`）已证。
-- **只剩最后一步的 `Zero ?m` 合成歧义**：目标里 `(^#0 ∷ t ∷ (0 : V)).[0]` 的
-- `∷`/`nth` 记法在 `V` 上要一个 `Zero` 实例，而它应由 `ORingStructure` 提供——
-- 疑需把 `∷` 写成 `adjoin` 的显式形式（`Vec.adjoin`）绕开记法的合成。

end GodelQ.CG008Bv3
