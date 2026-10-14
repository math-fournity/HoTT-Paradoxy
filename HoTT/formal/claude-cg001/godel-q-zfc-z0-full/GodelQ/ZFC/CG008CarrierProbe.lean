import GodelQ.ZFC.CG008ThresholdCorrection

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory
open FFL.Entailment ProvabilityAbstraction

namespace GodelQ.CG008CarrierProbe

/-!
# CG-008 · carrier 缺口的正面证据：`Set.Func k = Empty`

与 `CG008ThresholdCorrection.lean` 合起来，把 C 的门槛钉成一句正面事实。

## 两半合起来

| 侧 | 载体 | 事实 |
|---|---|---|
| 算术 | `𝕹 (m : V)`（`typedNumeral`，`Term/Typed.lean:358`） | 取任意 V 元素；前提只要 `[ORingStructure V] [V ⊧* 𝗜𝚺₁]` |
| 集合 | 需要一个等价的「把 V 元素塞进 ℒₜ 常项位」 | **`Func k = Empty` ⟹ 没有这样的闭项** |

## 治理

Foundation 只读；本文件纯下游，不含未证标记，可进收据。
**不声称 C 已证**；`Z0Blocked.lean:65` 的未证标记仍在。 -/

/-- **关键事实**：ℒₛₑₜ 的 `Func k` 对**所有** `k` 都是 `Empty`——
集合语言没有函数符号，特别地 **arity 0 的常项也没有**。
`rfl` 即可（`Misc.lean:22`：`abbrev Func : ℕ → Type := fun _ ↦ Empty`）。 -/
example (k : ℕ) : FFL.FirstOrder.Language.Set.Func k = Empty := rfl

/-- 推论：`IsEmpty` 对任意 arity 成立。 -/
example (k : ℕ) : IsEmpty (FFL.FirstOrder.Language.Set.Func k) := by
  rw [FFL.FirstOrder.Language.Set.Func]
  infer_instance

end GodelQ.CG008CarrierProbe
