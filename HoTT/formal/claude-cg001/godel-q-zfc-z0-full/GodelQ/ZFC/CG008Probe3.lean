import GodelQ.ZFC.ZFCSetInternal

/-!
# CG-008 探针 3（非收据）：§4 路线的第二个障碍——`V` 的结构类

交接单 §4 第 2 步要求自建 `set_sigma_one_complete`，前提取 `V↓[ℒₛₑₜ] ⊧ ψ`
（需要 `SetStructure V`）。缺口的 `V` 只有 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`（算术模型）。

本探针查实这个类型问题。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe3

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`SetStructure V` 能被 `infer_instance` 合成。

这一步**不报错**，说明这个上下文里确实存在一个 `Membership V V` 实例——
但它来自 `Arithmetic/Exponential/Bit.lean:28`：

```lean
instance : Membership V V := ⟨fun a i ↦ Bit i a⟩   -- 二进制编码
```

**不是** ZFC 的集合成员关系。所以任何用 `SetStructure V` 去实例化
`V↓[ℒₛₑₜ] ⊧ ψ` 的尝试，都会得到一个**语义错误**的引理——`∈` 被解释成比特。
`infer_instance` 不会报错，只会静默给出错的东西，这是本探针要固定下来的事实。 -/
example : SetStructure V := inferInstance

/-- **查实 2**：这个 `SetStructure` 实例确实解析到 `Bit`。
`Bit` 定义在 `Exponential/Bit.lean:23`（`def Bit (i a : V) : Prop := LenBit (Exp.exp i) a`）。
这里用 `Bit` 的类型确认它可被提到。 -/
example (a i : V) : Prop := Bit i a

/-- **查实 3**：缺口两端的 `V` 与集合语义的 `V` 不是同一个东西。
缺口的 `Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V)` 说的是「V 内部有一个编码为 V 元素的 𝗭𝗙𝗖 推导」，
与 `V↓[ℒₛₑₜ] ⊧ ·` 无关。 -/
example (ψ : SetTheorySentence) : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V) := id

end GodelQ.CG008Probe3
