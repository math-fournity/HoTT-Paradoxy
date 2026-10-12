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

## 用**层数感知**的归纳

`IsSemiformula.sigma1_structural_induction`（`Formula/Basic.lean:1484`）的谓词
`P : V → V → Prop` **吃层数**，且 `hall` 的归纳假设在层 **`n + 1`**：
`hall : IsSemiformula L (n+1) p → P (n+1) p → P n (^∀ p)`。
这正是 `iT_all`（`iT n (^∀ p) = ^∀ (imp domZero (iT (n+1) p))`）所需——
**一元 `sigma1_succ_induction` 不吃层数，所以先前卡住；换归纳原理即解决。** -/
theorem iT_isUFormula (n p : V) (hp : Bootstrapping.IsSemiformula ℒₒᵣ n p) :
    Bootstrapping.IsUFormula ℒₛₑₜ (iT n p) := by
  have hP : 𝚺ᴬ₁-Relation (fun n r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (iT n r)) := by
    definability
  refine Bootstrapping.IsSemiformula.sigma1_structural_induction (L := ℒₒᵣ) hP ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hp
  · -- rel：假设直接给 `IsSemitermVec L k n v`；用 `iT_rel` 换成 `iTR`
    intro n k R v hR hv
    rw [iT_rel hR hv.isUTermVec]
    exact (GodelQ.CG008ITR.iTR_isSemiformula n k R v
      (by rcases (Bootstrapping.Arithmetic.isRel_iff_LOR (V := V)).mp hR with ⟨h,-⟩ | ⟨h,-⟩ <;> rw [h])
      hv).isUFormula
  · -- nrel
    intro n k R v hR hv
    rw [iT_nrel hR hv.isUTermVec]
    exact Bootstrapping.IsUFormula.neg
      (GodelQ.CG008ITR.iTR_isSemiformula n k R v
        (by rcases (Bootstrapping.Arithmetic.isRel_iff_LOR (V := V)).mp hR with ⟨h,-⟩ | ⟨h,-⟩ <;> rw [h])
        hv).isUFormula
  · intro n
    rw [iT_verum]
    exact Bootstrapping.IsUFormula.verum
  · intro n
    rw [iT_falsum]
    exact Bootstrapping.IsUFormula.falsum
  · intro n p q hp hq ihp ihq
    rw [iT_and hp.isUFormula hq.isUFormula]
    exact Bootstrapping.IsUFormula.and.mpr ⟨ihp, ihq⟩
  · intro n p q hp hq ihp ihq
    rw [iT_or hp.isUFormula hq.isUFormula]
    exact Bootstrapping.IsUFormula.or.mpr ⟨ihp, ihq⟩
  · -- all：IH 在层 `n + 1`
    intro n p hp ih
    rw [iT_all hp.isUFormula]
    refine Bootstrapping.IsUFormula.all.mpr ?_
    refine Bootstrapping.IsUFormula.imp.mpr ⟨?_, ih⟩
    exact GodelQ.CG008VeParts.subst_singleton_isUFormula 0
      (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))
  · -- exs
    intro n p hp ih
    rw [iT_exs hp.isUFormula]
    refine Bootstrapping.IsUFormula.ex.mpr ?_
    refine Bootstrapping.IsUFormula.and.mpr ⟨?_, ih⟩
    exact GodelQ.CG008VeParts.subst_singleton_isUFormula 0
      (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))

end

end GodelQ.CG008ITParts

#print axioms GodelQ.CG008ITParts.iT_isUFormula
