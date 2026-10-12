import GodelQ.ZFC.CG008SubstNine
import GodelQ.ZFC.InternalTranslate

/-!
# CG-008 · `iT_isUFormula`——八种情形逐条攻

**归纳原理**（`Formula/Basic.lean:1161`，`uformula_result_induction`）：
取 `c := iT.construction`、`L := ℒₒᵣ`、`P n p r := IsUFormula ℒₛₑₜ r`。

| 情形 | 目标 | 零件 |
|---|---|---|
| `hverum` | `IsUFormula ℒₛₑₜ ^⊤` | ✅ 已有 |
| `hfalsum` | `IsUFormula ℒₛₑₜ ^⊥` | ✅ 已有 |
| `hand` | `IsUFormula ℒₛₑₜ (y₁ ^⋏ y₂)` | `IsUFormula.and` |
| `hor` | `IsUFormula ℒₛₑₜ (y₁ ^⋎ y₂)` | `IsUFormula.or` |
| `hnrel` | `IsUFormula ℒₛₑₜ (neg ℒₛₑₜ y)` | `IsUFormula.neg` |
| `hall` | `IsUFormula ℒₛₑₜ (^∀ (imp …))` | `IsUFormula.all` + `imp` 保持 + **`domZero` 是公式** |
| `hexs` | `IsUFormula ℒₛₑₜ (^∃ (domZero ^⋏ y))` | `IsUFormula.ex` + 同上 |
| `hrel` | `IsUFormula ℒₛₑₜ (iTR n k R v)` | **`iTR` 本身**，单独攻 |

`hall` 的归纳假设是
`∀ i < c.allSize param p, P (c.allChanges param i) p (c.result L (c.allChanges param i) p)`，
而 `allChanges n _ := n + 1`、`allSize n p := 1`
⇒ 归纳假设就是 **`IsUFormula ℒₛₑₜ (iT (n+1) p)`**，正是 `hall` 目标里 `ys.[0]` 的位置。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITParts

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

section
variable {L : Language} [L.Encodable] [L.LORDefinable]

/-- **查实 1**：`iT.construction.result` 的类型——`iT` 是它的特化。 -/
noncomputable example (n p : V) : V := iT.construction.result ℒₒᵣ n p

/-- **查实 2**：`uformula_result_induction` 的 `hP` 前提——`P n p r := IsUFormula ℒₛₑₜ r`。 -/
example : 𝚺ᴬ₁-Relation₃ (fun _ _ r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r) := by
  exact CG008Rel3Instance.isUFormula_relation3

end

end GodelQ.CG008ITParts
