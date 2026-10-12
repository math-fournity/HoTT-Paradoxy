import GodelQ.ZFC.CG008Conj
import GodelQ.ZFC.CG008RelCase2
import GodelQ.ZFC.CG008ShiftProof

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
      -- 两个参数：结果向量的分量在层 `1 + n` 是公式（由归纳假设 `ih`），
      -- 以及 `?[^#0, ^#1]` 是项向量
      -- `k ≠ 0` + `isFunc_iff_LOR` ⇒ `k = 2`
      have hk2 : k = 2 := by
        rcases (Bootstrapping.Arithmetic.isFunc_iff_LOR (V := V)).mp hkf with
          ⟨h, -⟩ | ⟨h, -⟩ | ⟨h, -⟩ | ⟨h, -⟩
        · exact absurd h hk
        · exact absurd h hk
        · exact h
        · exact h
      refine GodelQ.CG008ShiftProof.ve2_isUFormula n k f _ hk ?_ ?_
      · intro j hj
        -- `w.[j]` 是 `resultVec` 的第 `j` 项，由 `nth_resultVec` 化成 `iVE n v.[j]`
        show Bootstrapping.IsSemiformula ℒₛₑₜ (1 + n)
          ((Language.TermRec.Construction.resultVec ℒₒᵣ Translate.iVE.construction
            ![n] k v).[j])
        rw [Bootstrapping.Language.TermRec.Construction.nth_resultVec
          (L := ℒₒᵣ) (c := Translate.iVE.construction) (param := ![n])
          (w := v) hv (i := j) (by rw [hk2]; exact hj)]
        -- 层数升到 `1 + n`：`isSemiformula` 给的是 `bv (iVE n v.[j])`，
        -- 需 `bv ≤ 1 + n`。用 `iT`/`iVE` 的层数刻画——**这一步是本分支的最后一环**，
        -- 需要一条 `bv (iVE n t) ≤ n + 1` 的引理（对 `t` 归纳，与 `iVE` 的构造同步）。
        exact Bootstrapping.isSemiformula_iff.mpr
          ⟨ih j (by rw [hk2]; exact hj), by
            -- 先固定目标形状
            show Bootstrapping.bv ℒₛₑₜ (Translate.iVE n v.[j]) ≤ 1 + n
            sorry⟩
      · exact Bootstrapping.IsUTermVec.mkSeq₂_iff.mpr
          ⟨Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0),
           Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 1)⟩

end GodelQ.CG008IVE

#print axioms GodelQ.CG008IVE.iVE_isUFormula
