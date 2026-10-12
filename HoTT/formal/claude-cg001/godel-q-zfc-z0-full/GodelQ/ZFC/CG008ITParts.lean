import GodelQ.ZFC.CG008SubstNine
import GodelQ.ZFC.CG008ITR
import GodelQ.ZFC.InternalTranslate

/-!
# CG-008 · `iT_isUFormula`——八种情形

归纳原理 `uformula_result_induction`（`Formula/Basic.lean:1161`）：
`c := iT.construction`、`L := ℒₒᵣ`、`P n p r := IsUFormula ℒₛₑₜ r`。

八个目标的形状（本轮查实，`refine` 后逐一可见）：

| # | 目标 |
|---|---|
| 1 (`refine_1`) | `∀ param k R v, IsRel k R → IsUTermVec k v → IsUFormula ℒₛₑₜ (iTR param k R v)` |
| 2 | `∀ param k R v, IsRel k R → IsUTermVec k v → IsUFormula ℒₛₑₜ (neg ℒₛₑₜ (iTR param k R v))` |
| 3 | `∀ param, IsUFormula ℒₛₑₜ ^⊤` |
| 4 | `∀ param, IsUFormula ℒₛₑₜ ^⊥` |
| 5 | `∀ param p q, IsUFormula p → IsUFormula q → … → IsUFormula ℒₛₑₜ (y1 ^⋏ y2)` |
| 6 | `∀ param p q, IsUFormula p → IsUFormula q → … → IsUFormula ℒₛₑₜ (y1 ^⋎ y2)` |
| 7 | `∀ param p, IsUFormula p → (∀ i < allSize, …) → IsUFormula ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero y))` |
| 8 | 同类，`^∃ (domZero ^⋏ y)` |

**第 3、4 条白给**（`IsUFormula.verum`/`falsum`）。
**第 2 条用 `IsUFormula.neg`**，5/6 用 `IsUFormula.and`/`or`。
**第 7、8 条要 `domZero` 是公式**（`CG008ITDom.lean` 已证）。
**第 1 条（`iTR`）是唯一真正的工作量。**
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITParts

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

section
variable {L : Language} [L.Encodable] [L.LORDefinable]

set_option maxHeartbeats 3200000 in
/-- **`iT n p` 是公式**（`p` 是**层 `n`** 的算术公式）。

## 假设必须带层数（本文件的结构性更正）

先前写的是 `IsUFormula ℒₒᵣ p → IsUFormula ℒₛₑₜ (iT n p)`——**证不出来**。
`iTR n k R v`/`iVE n t` 把 `n` 用进了**项的分量层**：
`conjunct 2 n 0 (iVE n v.[0])` 要 `v.[0]` 在层 `n` 是项。
`IsUFormula p` **不给**这个界（`IsUTermVec` 只给「是项」，不给层），
所以 `rel` 情形所需的 `IsSemitermVec ℒₒᵣ k n v` 拿不到。
**层数必须在假设里**——与 `CG008IVE.lean` 头部记的更正同源。

## 用层数感知的归纳

`semiformula_result_induction`（`Formula/Basic.lean:1578`）的谓词
`P : V → V → V → V → Prop` **吃「计算参数」与「层数」两个独立变量**，
所以取 `P param n p r := param = n → IsUFormula r`——
**把两者相等这件事带在谓词里**，归纳步就能把 `IsSemitermVec L k n v`
换成 `IsSemitermVec L k param v`。 -/
theorem iT_isUFormula (n p : V) (hp : Bootstrapping.IsSemiformula ℒₒᵣ n p) :
    Bootstrapping.IsUFormula ℒₛₑₜ (iT n p) := by
  have hP : 𝚺ᴬ₁-Relation₄
      (fun param n p r : V ↦ param = n → Bootstrapping.IsUFormula ℒₛₑₜ r) := by
    have h1 : 𝚺ᴬ₁.Definable (fun v : Fin 4 → V ↦ v 0 = v 1) :=
      Bounding.HierarchySymbol.DefinableRel.comp
        (Bounding.HierarchySymbol.DefinableRel.eq (V := V))
        (Bounding.HierarchySymbol.DefinableFunction.var 0)
        (Bounding.HierarchySymbol.DefinableFunction.var 1)
    have h2 : 𝚺ᴬ₁.Definable (fun v : Fin 4 → V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (v 3)) :=
      Bounding.HierarchySymbol.DefinablePred.comp
        (inferInstance : 𝚺ᴬ₁-Predicate (fun r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r))
        (Bounding.HierarchySymbol.DefinableFunction.var 3)
    have h3 := Bounding.HierarchySymbol.Definable.imp h1 h2
    apply Bounding.HierarchySymbol.Definable.of_iff h3
    intro v
    simp
  have key : ∀ {param n p : V}, Bootstrapping.IsSemiformula ℒₒᵣ n p →
      param = n → Bootstrapping.IsUFormula ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) := by
    intro param n p hp'
    refine iT.construction.semiformula_result_induction (L := ℒₒᵣ) hP ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hp'
    · -- rel：`IsSemitermVec L k n v` 经 `hpn` 换成层 `param`
      intro n param k R v hR hv hpn
      subst hpn
      exact (GodelQ.CG008ITR.iTR_isSemiformula n k R v
        (by rcases (Bootstrapping.Arithmetic.isRel_iff_LOR (V := V)).mp hR with ⟨h,-⟩ | ⟨h,-⟩ <;> rw [h])
        hv).isUFormula
    · -- nrel
      intro n param k R v hR hv hpn
      subst hpn
      exact Bootstrapping.IsUFormula.neg
        (GodelQ.CG008ITR.iTR_isSemiformula n k R v
          (by rcases (Bootstrapping.Arithmetic.isRel_iff_LOR (V := V)).mp hR with ⟨h,-⟩ | ⟨h,-⟩ <;> rw [h])
          hv).isUFormula
    · intro n param hpn; exact Bootstrapping.IsUFormula.verum
    · intro n param hpn; exact Bootstrapping.IsUFormula.falsum
    · intro n param p q hp hq ihp ihq hpn
      exact Bootstrapping.IsUFormula.and.mpr ⟨ihp hpn, ihq hpn⟩
    · intro n param p q hp hq ihp ihq hpn
      exact Bootstrapping.IsUFormula.or.mpr ⟨ihp hpn, ihq hpn⟩
    · -- all：`iT n (^∀ p) = ^∀ (imp domZero (iT (n+1) p))`
      intro n param p hp ih hpn
      rw [iT.construction.result_all hp.isUFormula rfl]
      simp only [Translate.iT.construction]
      refine Bootstrapping.IsUFormula.all.mpr ?_
      refine Bootstrapping.IsUFormula.imp.mpr ⟨?_, ?_⟩
      · exact GodelQ.CG008VeParts.subst_singleton_isUFormula 0
          (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))
      · exact ih 0 (by simp) (by rw [hpn])
    · -- exs
      intro n param p hp ih hpn
      rw [iT.construction.result_exs hp.isUFormula rfl]
      simp only [Translate.iT.construction]
      refine Bootstrapping.IsUFormula.ex.mpr ?_
      refine Bootstrapping.IsUFormula.and.mpr ⟨?_, ?_⟩
      · exact GodelQ.CG008VeParts.subst_singleton_isUFormula 0
          (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))
      · exact ih 0 (by simp) (by rw [hpn])
  exact key hp rfl

end

end GodelQ.CG008ITParts
