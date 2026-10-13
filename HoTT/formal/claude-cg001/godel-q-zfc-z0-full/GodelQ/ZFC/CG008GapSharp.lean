import GodelQ.ZFC.CG008ITQuoteClose
import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

/-!
# CG-008 · 缺口的**锐化**：D3 的前提已经给出一个 𝗜𝚺₁ 内的证明编码

## 本轮的新发现

`hD3G` 的前提是 `Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V)`。由 `models_zfcTr_iff`，
这就是 `V ⊨ zfcTr τ`。而 `zfcTr τ` 是 **Σ₁ 句**（`zfcTr_sigma1`），
所以 **𝗜𝚺₁ 自己的 Σ₁ 完全性**（`sigma_one_complete`）直接给出：

```
Provable 𝗜𝚺₁ (⌜zfcTr τ⌝ : V)        （V 内部的一条 𝗜𝚺₁ 证明编码）
```

**这把缺口锐化成一条更窄的命题**：只剩

```
Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate σ⌝ : V)     （σ 是 Σ₁ 句）
```

即「**内部化的解释保可证性**」——把 V 内部的一条 𝗜𝚺₁ 推导编码，
变成 V 内部的一条 𝗭𝗙𝗖 推导编码（结论是前者的翻译）。

## 为什么这一条仍然不是免费的（本节给出精确理由）

`paInterp.interpret_theory`（`PAModel.lean:246`）是**元层**的：
它对每个**标准**的 `φ ∈ 𝗜𝚺₁` 给一个元层证明对象，走的是
`SetTheory.complete`（完备性，语义论证）。它**不产生 V 内的元素 `d`**。

要做的事是把**整个解释在 V 内形式化**：需要一个 Σ₁ 可定义的函数
`axProof(φ) = ⌜𝗭𝗙𝗖 中 translate φ 的证明⌝`，并证明它对**每个**
（含**非标准**的）`φ ∈ 𝗜𝚺₁` 都有定义。非标准 `φ` 是归纳模式的非标准实例，
其翻译在 𝗭𝗙𝗖 中的可证性要靠「ω 验证归纳」那套论证——而
`models_PA_W` / `W_induction`（`PAModel.lean`）目前是**元层**的。

**所以缺口 = 把 `PAModel.lean` 的模型论论证在 V 内形式化。**
这是本轮把缺口定位到的最窄处。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008GapSharp
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
-- 宇宙取 `Type`：`models_zfcTr_iff` 只在 `Type` 上可用（与
-- `zfc_z0_full_of_D3_internalize` 的前提一致；`Z0Bridge` 同样取 `Type`）。
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **锐化一（本轮新证）**：`hD3G` 的前提给出一个 **V 内部的 𝗜𝚺₁ 证明编码**。

`zfcTr τ` 是 Σ₁ 句，故 𝗜𝚺₁ 的 Σ₁ 完全性直接适用。 -/
theorem d3_hypothesis_gives_ISigma1_proof (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗜𝚺₁ (⌜zfcTr τ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete (T := 𝗜𝚺₁) (V := V)
    (zfcTr_sigma1 τ) ((models_zfcTr_iff V τ).mpr h)

/-- **锐化二（单向，本轮新证）**：**窄命题比缺口强**——
窄命题（右）直接给出缺口（左）。

理由：缺口的前提 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝` 经锐化一给出
`Provable 𝗜𝚺₁ ⌜zfcTr τ⌝`（窄命题的前提），而两者的**结论相同**。

**反向不成立**（所以这不是等价）：窄命题的前提说的是
「V 内有一条 𝗜𝚺₁ 推导，其结论是 `zfcTr τ`」，缺口的前提说的是
「V 内有一条 𝗭𝗙𝗖 推导，其结论是 `translate τ`」。前者**不蕴含**后者——
`V ⊨ provabilityPred 𝗜𝚺₁ (zfcTr τ)` 与 `V ⊨ zfcTr τ` 之间的缺口
**正是 D3 本身**。所以这是一条**单向归约**，不是等价。 -/
theorem gap_of_internalized_interpretation
    (hR : ∀ {σ : ArithmeticSentence}, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
      Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)) :
    ∀ (τ : ArithmeticSentence),
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) :=
  fun τ h ↦ hR (zfcTr_sigma1 τ) (d3_hypothesis_gives_ISigma1_proof τ h)

end GodelQ.CG008GapSharp

#print axioms GodelQ.CG008GapSharp.d3_hypothesis_gives_ISigma1_proof
#print axioms GodelQ.CG008GapSharp.gap_of_internalized_interpretation
