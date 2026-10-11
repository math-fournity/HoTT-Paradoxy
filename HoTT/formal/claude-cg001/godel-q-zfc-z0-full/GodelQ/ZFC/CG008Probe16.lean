import GodelQ.ZFC.CG008Probe15

/-!
# CG-008 探针 16（非收据）：算术机器能否对 `𝗭𝗙𝗖` **陈述**

## 动机

`D3.lean:175` 的 `provable_internalize`：

```lean
theorem provable_internalize {σ : ArithmeticSentence} :
    Provable T (⌜σ⌝ : V) → Provable T (⌜provabilityPred T σ⌝ : V)
```

它在 namespace `Bootstrapping.Arithmetic` 里，`variable {T : ArithmeticTheory}`。

**但它的语句本身**只要求 `T : Theory L`（`Provable T` 的定义层面）。
所以问题是：**语句**能否对 `T = 𝗭𝗙𝗖` 写出来？若能，卡点就在证明而不在类型。

## 为什么这可能重要

`zfcTr : Provability 𝗜𝚺₁ Sh` 的 `prov = trProv.val`，而
`trProv σ ↔ Provable 𝗭𝗙𝗖 (⌜translate σ⌝ : V)`（`trProvable_quote`）。
缺口正是 `provable_internalize` 的 `T = 𝗭𝗙𝗖` 版本。

## 本探针要查实

1. `Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)` 对 `σ : ArithmeticSentence` 是否**可陈述**；
2. `provabilityPred 𝗭𝗙𝗖 σ` 是否**可构造**（它是算术句，`T` 只是被谈论的）；
3. `[𝗭𝗙𝗖.Δ₁]` 是否真的存在（`Z0Blocked` 说 `Sh` 没有，但 `𝗭𝗙𝗖` 应该有）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe16

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)` **可陈述**——`σ` 是算术句，
`𝗭𝗙𝗖 : Theory ℒₛₑₜ` 只是被谈论的理论。 -/
example (σ : ArithmeticSentence) : Prop := Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)

/-- **查实 2（修正一处预期）**：`provabilityPred 𝗭𝗙𝗖` 要求 `σ : Sentence ℒₛₑₜ`，
**不是**算术句——它返回**算术**句，但吃**集合**句。

`provabilityPred T σ = (provable T).val/[⌜σ⌝]`：`provable T` 是算术句，
而 `⌜σ⌝` 把 `σ` 的 Gödel 码代进去，所以 `σ` 必须是 `T` 的语言的句子。

**这正是缺口的形状**：缺口里 `σ = arithTrln.translate τ`（集合句），
所以 `provabilityPred 𝗭𝗙𝗖 (translate τ)` 才是那个算术句。 -/
noncomputable example (σ : SetTheorySentence) : ArithmeticSentence :=
  provabilityPred 𝗭𝗙𝗖 σ

/-- **查实 3**：`provable 𝗭𝗙𝗖` 是**算术** Σ₁ 句——`T` 的语言不进结果。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 1 := provable 𝗭𝗙𝗖

/-- **查实 4（关键）**：`[𝗭𝗙𝗖.Δ₁]` **存在**（`ZFCDelta1.lean` 已证）。

与 `Sh` 的对照：`Sh` 没有（探针 15 查实），而 `𝗭𝗙𝗖` 有。
**所以若缺口能以 `𝗭𝗙𝗖` 为被谈论的理论来证，`Δ₁` 不是障碍。** -/
noncomputable example : 𝗭𝗙𝗖.Δ₁ := inferInstance

/-- **查实 5**：`zfcTr` 的 `trProv` 与 `provable 𝗭𝗙𝗖` 的关系。

`trProv σ` 在语义上就是 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝`（`trProvable_quote`），
而 `provable 𝗭𝗙𝗖` 是那个 Σ₁ 句。**所以缺口的被谈论理论其实是 `𝗭𝗙𝗖`，不是 `Sh`**——
`Sh` 只是 `zfcTr` 的 `T` 参数（因为 `Provability T₀ T` 要求 `T₀ ⪯ T`）。

**这是本轮最重要的结构澄清**：`Sh` 出现在类型里是为了满足
`Provability 𝗜𝚺₁ Sh` 的形状（`bew_def : Sh ⊢ σ → 𝗜𝚺₁ ⊢ prov/[⌜σ⌝]`），
而 `prov` 的实际内容谈的是 `𝗭𝗙𝗖`。 -/
example (σ : ArithmeticSentence) :
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) :=
  trProvable_quote σ

end GodelQ.CG008Probe16
