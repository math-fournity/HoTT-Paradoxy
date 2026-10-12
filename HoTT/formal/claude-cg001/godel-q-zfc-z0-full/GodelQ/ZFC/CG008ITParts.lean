import GodelQ.ZFC.CG008SubstNine
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

set_option maxHeartbeats 800000 in
theorem iT_isUFormula (n p : V) (hp : Bootstrapping.IsUFormula ℒₒᵣ p) :
    Bootstrapping.IsUFormula ℒₛₑₜ (iT n p) := by
  show Bootstrapping.IsUFormula ℒₛₑₜ (iT.construction.result ℒₒᵣ n p)
  have hP : 𝚺ᴬ₁-Relation₃ (fun _ _ r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r) :=
    CG008Rel3Instance.isUFormula_relation3
  refine iT.construction.uformula_result_induction (L := ℒₒᵣ) hP (param := n) ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hp
  · -- refine_1：rel —— iTR 本身
    sorry
  · -- refine_2：nrel —— `neg` 保持公式性；`iTR` 的公式性由 `iTR_isUFormula` 给
    intro param k R v hR hv
    exact Bootstrapping.IsUFormula.neg (iTR_isUFormula param k R v hR hv)
  · -- refine_3：verum —— `c.verum param = ^⊤`
    intro param; exact Bootstrapping.IsUFormula.verum
  · -- refine_4：falsum
    intro param; exact Bootstrapping.IsUFormula.falsum
  · -- refine_5：and
    sorry
  · -- refine_6：or
    sorry
  · -- refine_7：all
    sorry
  · -- refine_8：exs
    sorry

end

end GodelQ.CG008ITParts
