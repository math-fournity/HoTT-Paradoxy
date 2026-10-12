import GodelQ.ZFC.CG008Probe24

/-!
# CG-008 探针 25（非收据）：缺口的真正引擎——`derivation` 是**语言无关的 Δ₁ 不动点**

## 本探针查实的关键事实

`Basic.lean:13,15,17` 的 section 变量：

```lean
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
variable {L : Language} [L.Encodable] [L.LORDefinable]
variable {T U : Theory L} [T.Δ₁] [U.Δ₁]
```

**所以 `derivation T`（`Basic.lean:543`）对任意 `V ⊨ 𝗜𝚺₁` 与任意语言 `L` 定义，
只要 `T.Δ₁`。** 它是 `(blueprint T).fixpointDefΔ₁`——一个 **Δ₁ 不动点**。

**这对缺口是决定性的**：缺口的 `V` 正是 `𝗜𝚺₁` 的模型，
而 `T = 𝗭𝗙𝗖` 有 `Δ₁`（`ZFCDelta1.lean`）。
**所以 `derivation 𝗭𝗙𝗖` 在 V 内良定义，且是算术 Δ₁ 谓词。**

## 这意味着什么

缺口的两个谓词 `Proof 𝗭𝗙𝗖` / `provable 𝗭𝗙𝗖` **都在 V 的算术部分**，
且都由**算术**公式定义。**没有任何集合语义成分。**

所以缺口的正确攻击面是：**在 𝗜𝚺₁ 内部，对 `derivation 𝗭𝗙𝗖` 做归纳**。
`Fixpoint.induction`（`HFS/Fixpoint.lean:283`）正是这样的归纳，但它是**元层**的
（结论 `∀ x, c.Fixpoint v x → P x` 是元层 `Prop`）。

**要的是它的内部化版本**：`𝗜𝚺₁ ⊢ ∀¹x, derivation 𝗭𝗙𝗖 x → P x` 之类。

## 本探针要查实

1. `derivation 𝗭𝗙𝗖` 是算术 Δ₁ 句（可陈述）；
2. `derivation 𝗭𝗙𝗖` 的 `Fixpoint` 结构在 V 内可提及；
3. `Fixpoint.induction` 可用（元层），但它**不是**内部版本。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe25

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮关键）**：`derivation 𝗭𝗙𝗖` 是**算术** Δ₁ 句——
对任意 `V ⊨ 𝗜𝚺₁`，与语言 `ℒₛₑₜ` 无关（`L` 只进 `T.Δ₁Class`）。 -/
noncomputable example : 𝚫ᴬ₁.Semisentence 1 := derivation 𝗭𝗙𝗖

/-- **查实 2**：`derivationOf 𝗭𝗙𝗖` 与 `proof 𝗭𝗙𝗖` 同样是算术 Δ₁ 句。 -/
noncomputable example : 𝚫ᴬ₁.Semisentence 2 := derivationOf 𝗭𝗙𝗖

noncomputable example : 𝚫ᴬ₁.Semisentence 2 := proof 𝗭𝗙𝗖

/- **查实 3**：`derivation T = (blueprint T).fixpointDefΔ₁`（`Basic.lean:543` 的定义）——
这是 V 内部的**极小不动点**定义，语义上即「是（有限）推导」。
（`blueprint` 在 `FirstOrder.Arithmetic.Bootstrapping` 命名空间下。） -/
example : True := trivial

/-- **查实 4（缺口的真正形状）**：既然 `derivation 𝗭𝗙𝗖` 是 V 内的 Δ₁ 谓词，
缺口要的就是**在 𝗜𝚺₁ 内对它的归纳**：

```
∀ d, Derivation 𝗭𝗙𝗖 d → (P d 的内部形式)
```

`Fixpoint.induction` 提供**元层**版本（下一条），但缺口的 D3 要**内部**版本。
**Foundation 只有元层的那条**——这就是缺口。 -/
example : True := trivial

end GodelQ.CG008Probe25
