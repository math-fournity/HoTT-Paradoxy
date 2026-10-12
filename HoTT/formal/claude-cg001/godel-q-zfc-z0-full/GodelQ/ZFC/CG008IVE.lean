import GodelQ.ZFC.CG008Conj
import GodelQ.ZFC.CG008RelCase2

/-!
# CG-008 · `iVE_isUFormula`
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008IVE
open GodelQ.ZFCArith GodelQ.Translate GodelQ.CG008VeParts GodelQ.CG008VeLevel GodelQ.CG008Ve2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 800000 in
/-- **`iVE n t` 是公式**（`t` 是项时）。

`iVE.construction` 的分支：
`bvar ↦ eqAtom (^#(z+1))`、`fvar ↦ eqAtom (^&x)`、`func ↦ if k = 0 then ve0 k f else ve2 …`。 -/
theorem iVE_isUFormula {n t : V} (ht : Bootstrapping.IsUTerm ℒₒᵣ t) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.iVE n t) := by
  apply Bootstrapping.IsUTerm.induction 𝚺
    (P := fun t ↦ Bootstrapping.IsUFormula ℒₛₑₜ (Translate.iVE n t)) ?_ ?_ ?_ ?_ t ht
  · -- `P` 的 Σ₁ 闸门：`iVE` 有 rank-1 实例（本包补的 `iVE_definable'`）
    have hP₀ : 𝚺ᴬ₁-Predicate (fun r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r) := inferInstance
    have hF : { Γ := 𝚺, rank := 1 }-Function₂ (Translate.iVE : V → V → V) :=
      GodelQ.Translate.iVE_definable' 𝚺 0
    have hf : 𝚺ᴬ₁.DefinableFunction (fun v : Fin 1 → V ↦ Translate.iVE n (v 0)) :=
      hF.comp (Bounding.HierarchySymbol.DefinableFunction.const n)
        (Bounding.HierarchySymbol.DefinableFunction.var 0)
    have hcomp := Bounding.HierarchySymbol.DefinablePred.comp hP₀ hf
    apply Bounding.HierarchySymbol.Definable.of_iff hcomp
    intro v
    simp
  · intro z
    rw [Translate.iVE, Bootstrapping.Language.TermRec.Construction.result_bvar]
    exact GodelQ.CG008RelCase2.eqAtom_isUFormula _ (Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := z + 1))
  · intro x
    rw [Translate.iVE, Bootstrapping.Language.TermRec.Construction.result_fvar]
    exact GodelQ.CG008RelCase2.eqAtom_isUFormula _ (Bootstrapping.IsUTerm.fvar (L := ℒₛₑₜ) x)
  · intro k f v hkf hv ih
    -- `func` 分支：`k = 0` 走 `ve0`，否则走 `ve2`
    -- 先展开 `iVE`，再用 `result_func'`（结果向量取 `resultVec`）
    show Bootstrapping.IsUFormula ℒₛₑₜ
      (Language.TermRec.Construction.result ℒₒᵣ Translate.iVE.construction ![n] (^func k f v))
    rw [Bootstrapping.Language.TermRec.Construction.result_func' (c := Translate.iVE.construction)
      (param := ![n]) hkf hv]
    simp only [Translate.iVE.construction]
    split_ifs with hk
    · -- `k = 0`：结果是 `ve0 k f`
      exact GodelQ.CG008VeLevel.ve0_isUFormula hk
    · -- `k ≠ 0`：结果是 `ve2 n k f (结果向量)`
      -- `ve2 n k f w = qqAlls (imp (conjunct 3 n 0 w.[0] ⋏ (conjunct 3 n 1 w.[1] ⋏ ⊤)) (subst …)) 2`
      -- 需要 `conjunct`（未证）与替换向量（`isSemitermVec_ve2vec` 的推广，分量是**结果向量**而非 `^#`）
      sorry

end GodelQ.CG008IVE

#print axioms GodelQ.CG008IVE.iVE_isUFormula
