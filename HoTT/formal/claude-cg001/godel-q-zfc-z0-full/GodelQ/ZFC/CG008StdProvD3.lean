import GodelQ.ZFC.ZFCSetSigma1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008StdProvD3

/-!
# CG-008 · 标准可证性谓词的 D3 不能用到 𝗭𝗙𝗖 上——因为**语言不同**，不是因为缺 Δ₁

## Foundation 的引理

```lean
theorem provable_D3 [𝗩𝗐⁻ ⪯ T] {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ provabilityPred T σ 🡒 provabilityPred T (provabilityPred T σ)
```

前提是 `T : ArithmeticTheory`，即 `Theory ℒₒᵣ`。

## 本文件的判定

`𝗭𝗙𝗖 : Theory ℒₛₑₜ`——**语言不同**，所以 `provable_D3` **无法实例化**到 `𝗭𝗙𝗖`。
这与 `[T.Δ₁]` 是否可用**无关**（`[𝗭𝗙𝗖.Δ₁]` 其实存在，见下）。

## 意义

它解释了一个看似矛盾的现象：`[Theory.Δ₁ 𝗭𝗙𝗖]` 存在（`ZFCDelta1.lean`），
但 D3 仍然到不了 `𝗭𝗙𝗖`——**卡在语言**，不在 Δ₁。
所以 §9.15 的「退到能用 Δ₁ 的最强内部理论」这个问法本身要改：
Δ₁ 已经有了，问题换成了「集合语言版的 Σ₁ 完备性」。

## 治理

Foundation 只读；本文件纯下游，不含未证标记，可进收据。
**不声称缺口已证**；`Z0Blocked.lean:65` 的未证标记仍在。 -/

/-- 语言类型见证 1：`Theory ℒₛₑₜ`（`𝗭𝗙𝗖` 所在的语言）。 -/
example : Type := Theory ℒₛₑₜ

/-- 语言类型见证 2：`Theory ℒₒᵣ`（`provable_D3` 要求的语言）。 -/
example : Type := Theory ℒₒᵣ

/-- `[𝗭𝗙𝗖.Δ₁]` **存在**（本树 `ZFCDelta1.lean`）——所以卡点不是 Δ₁。 -/
noncomputable example : (𝗭𝗙𝗖 : SetTheory).Δ₁ := inferInstance

end GodelQ.CG008StdProvD3
