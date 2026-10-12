import GodelQ.ZFC.CG008CraigBridge

/-!
# CG-008 · 缺口是**纯算术**的：集合语义不在其中

## 本轮的关键澄清

此前几轮（P1 尤其）把注意力放在**集合语言语义**上：
`setTheory_sigma₁_induction'` 的十情形、`ℒₛₑₜ` 无常项导致 `hMem`/`hNMem` 无解，等等。

**但缺口里 V 是 `𝗜𝚺₁` 的模型（算术！），不是 𝗭𝗙𝗖 的模型。**
缺口的两个句子都住在 V 的**算术部分**：

- 前提 `Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)`——
  `⌜·⌝` 是 `GödelNumber ℒₒᵣ (Sentence ℒₛₑₜ)`，即 `numeral ∘ encode`，是一个**数**；
- 结论 `Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)`——同样是数。

**所以缺口完全不涉及 `V↓[ℒₛₑₜ] ⊧ ·`。** 集合语言的语义、十情形归纳、
`ℒₛₑₜ` 无常项——**这些都不在缺口的路径上**。

## 缺口的纯算术形式

由 `iT_quote`（`InternalTranslate.lean:611`）：`iT n ⌜φ⌝ = ⌜translate φ⌝`（V 内）。
由 `trProvable_quote`：`zfcTr τ ↔ Provable 𝗭𝗙𝗖 ⌜translate τ⌝`。

所以缺口可以逐字写成**不含任何集合语义**的形式：

```
前提：∃ d : V, Proof 𝗭𝗙𝗖 d ⌜translate τ⌝
目标：∃ d' : V, Proof 𝗭𝗙𝗖 d' ⌜translate (zfcTr τ)⌝
```

而 `Proof`、`provable`、`iTDef` 全是**算术**谓词。

## 这对「下一步」的影响

P1 的 `hMem`/`hNMem` 障碍分析（`CG008MemCase.lean`）针对的是
**集合语言的 Σ₁ 归纳**——那条路（`set_sigma_one_complete`）**不是缺口需要的路**。

**缺口真正需要的是**：𝗜𝚺₁ 内部证明「ZFC 的可证性谓词满足 D3」，
而这是**纯算术**陈述，只是被谈论的理论 `T = 𝗭𝗙𝗖` 不是算术理论。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008PureArith

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本文件的要点）**：缺口的两个句子都在**算术**语言里。

`Provable 𝗭𝗙𝗖 ψ` 的定义是 `∃ d : V, Proof 𝗭𝗙𝗖 d ψ`，其中
`Proof` 是**算术**谓词（`proof T : 𝚫ᴬ₁.Semisentence 2`）。
所以缺口只谈 V 的算术部分——**`V↓[ℒₛₑₜ] ⊧ ·` 完全不出现**。 -/
example (ψ : V) : Provable 𝗭𝗙𝗖 ψ ↔ ∃ d, Proof 𝗭𝗙𝗖 d ψ := Iff.rfl

/-- **查实 2**：`proof` 是算术 Δ₁ 谓词。 -/
noncomputable example : 𝚫ᴬ₁.Semisentence 2 := proof 𝗭𝗙𝗖

-- **查实 3**：缺口的**纯算术形状**——两端都是「V 里有 𝗭𝗙𝗖 的证明码」：
--
--   ∀ τ, (∃ d : V, Proof 𝗭𝗙𝗖 d ⌜translate τ⌝) → (∃ d' : V, Proof 𝗭𝗙𝗖 d' ⌜translate (zfcTr τ)⌝)
--
-- 这就是 `Z0Blocked.zfcTr_D3_internalize` 的展开（**未证**；本文件不导入
-- `Z0Blocked.lean`，因为它带未证标记，本文件要保持可进收据）。
--
-- 用一条**同形但成立**的例子把形状固定下来（见证直接搬运）： -/
example (ψ : V) (h : ∃ d : V, Proof 𝗭𝗙𝗖 d ψ) : ∃ d' : V, Proof 𝗭𝗙𝗖 d' ψ := h

end GodelQ.CG008PureArith
