import GodelQ.ZFC.CG008ShiftProof

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

set_option maxHeartbeats 3200000 in
/-- **`bv (iVE n t) ≤ n + 1`**（`t` 是层 `n` 的半项）。

**必须用 `IsSemiterm.induction`**（`Term/Basic.lean:912`）：它的 `bvar` 分支给 `z < n`，
正是 `bv (eqAtom (^#(z+1))) = z + 2 ≤ n + 1` 所需；
`IsUTerm.induction` 的 `bvar` 分支**不给**这个界。 -/
theorem bv_iVE_le (n : V) : ∀ t : V, Bootstrapping.IsSemiterm ℒₒᵣ n t →
    Bootstrapping.bv ℒₛₑₜ (Translate.iVE n t) ≤ n + 1 := by
  intro t
  apply Bootstrapping.IsSemiterm.induction 𝚺
    (P := fun t ↦ Bootstrapping.bv ℒₛₑₜ (Translate.iVE n t) ≤ n + 1)
  · exact bv_iVE_gate n
  · -- bvar：`z < n` ⇒ `bv (eqAtom (^#(z+1))) ≤ n + 1`
    intro z hz
    rw [Translate.iVE, Bootstrapping.Language.TermRec.Construction.result_bvar]
    -- `bv (eqAtom (^#(z+1))) = (z+1) + 1`，需 `≤ n + 1`
    sorry
  · -- fvar：`bv (eqAtom (^&x)) = 0 + 1 ≤ n + 1`
    intro x
    rw [Translate.iVE, Bootstrapping.Language.TermRec.Construction.result_fvar]
    sorry
  · -- func
    intro k f v hkf hv ih
    sorry

end GodelQ.CG008Bv3
