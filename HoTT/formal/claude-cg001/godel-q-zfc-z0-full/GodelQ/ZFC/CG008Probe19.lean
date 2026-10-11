import GodelQ.ZFC.CG008Probe18

/-!
# CG-008 探针 19（非收据）：`𝗭𝗙𝗖.standardProvability` 与 `provable_D3` 能否直接用

## 探针 18 的结果

`FFL.FirstOrder.Language.LORDefinable ℒₛₑₜ` **合成成功**（`rc=0`）。
加上 `[𝗭𝗙𝗖.Δ₁]`（`ZFCDelta1.lean`），`standardProvability` 的三个前提
（`[L.Encodable]`、`[L.LORDefinable]`、`[T.Δ₁]`）**全部就位**。

## 本探针查实

1. `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 能否建成；
2. `provable_D3` 对 `T = 𝗭𝗙𝗖` 能否**陈述**；
3. 若两者都行，缺口是否就此闭合——**这是本轮最关键的检验**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe19

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18

/-- **查实 1**：`𝗭𝗙𝗖.standardProvability` **能建成**——
`Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 的一个实例。

这是探针 16-18 一路追下来的结果：多语言 `Provability` +
`ℒₒᵣ` 的通用 `GödelNumber` + `ℒₛₑₜ.LORDefinable` + `𝗭𝗙𝗖.Δ₁`，
四个条件都满足。 -/
noncomputable example : Provability 𝗜𝚺₁ 𝗭𝗙𝗖 := 𝗭𝗙𝗖.standardProvability

/-- **查实 2（决定性检验）**：`provable_D3` 对 `T = 𝗭𝗙𝗖` 能否陈述？

`provable_D3` 的语句（`StandardProvability.lean:71`）：

```lean
theorem provable_D3 [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ □σ 🡒 □□σ
```

**注意 `{σ : ArithmeticSentence}` 是写死的**——不是 `Sentence L`。
所以对 `T = 𝗭𝗙𝗖`，`□σ = provabilityPred 𝗭𝗙𝗖 σ` 要求
`σ : Sentence ℒₛₑₜ`，而 `provable_D3` 只接受 `ArithmeticSentence`。
**类型不匹配**。

本探针用「能否给出实例」来固定这一点。 -/
example {σ : ArithmeticSentence} : 𝗜𝚺₁ ⊢ (provabilityPred 𝗜𝚺₁ σ) 🡒
    (provabilityPred 𝗜𝚺₁ (provabilityPred 𝗜𝚺₁ σ)) :=
  provable_D3 (T := 𝗜𝚺₁)

end GodelQ.CG008Probe19
