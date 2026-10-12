import GodelQ.ZFC.CG008SingleD3

/-!
# CG-008 · 攻单句 D3：`𝐆 ↔ ∼zfcTr 𝐆` 能否替代一般模式

## 目标

```
目标：𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)          𝐆 := gödel zfcTr
```

## 为什么它可能比一般模式容易

**一般模式**（对任意 σ）：要证 `zfcTr σ → zfcTr (zfcTr σ)`，
标准证法是**形式化 Σ₁ 完全性**——跑遍 σ 的结构，
而 `ℒₛₑₜ` 无常项使 `toNumVec` 那一步无对偶。

**单句**：`𝐆` 是**对角线句**，满足 `𝗜𝚺₁ ⊢ 𝐆 🡘 ∼zfcTr 𝐆`（`gödel_spec`）。

**关键想法**：`zfcTr 𝐆` 是 Σ₁ 句，所以 `□(zfcTr 𝐆)` 的形式化完全性
**只需要 `zfcTr 𝐆` 本身的 Σ₁ 完全性**——而不是 `𝐆` 的结构归纳。

而 `zfcTr 𝐆` 是**算术**句（`provable 𝗭𝗙𝗖` 的实例），
所以 **`𝗜𝚺₁` 自己的 Σ₁ 完全性可能直接可用**！

**具体地**：`provable_sigma_one_complete (T := 𝗜𝚺₁)` 给
`𝗜𝚺₁ ⊢ σ → □σ` 对 Σ₁ 句 σ。
取 `σ := zfcTr 𝐆`——**但 `□ = provabilityPred 𝗜𝚺₁`，不是 `zfcTr`**。
**这就是卡点**：要的是 `zfcTr (zfcTr 𝐆)`，而白送的是 `provabilityPred 𝗜𝚺₁ (zfcTr 𝐆)`。

**两者是否等价？** `zfcTr ψ` 说「𝗭𝗙𝗖 证明 `translate ψ`」；
`provabilityPred 𝗜𝚺₁ ψ` 说「`𝗜𝚺₁` 证明 ψ」。
**对 `ψ = zfcTr 𝐆`，前者强于后者**（𝗭𝗙𝗖 比 𝗜𝚺₁ 强）。

**所以需要的桥是**：`provabilityPred 𝗜𝚺₁ ψ → zfcTr ψ`
——即「`𝗜𝚺₁` 证明了 ψ ⟹ 𝗭𝗙𝗖 证明 `translate ψ`」。
**这由 `paInterp.of_provability` 给出（`Z0PA.lean` 已用）！**

## 本文件要试的

把上面这条链**真的接起来**——若成功，单句 D3 得证，缺口大幅缩小。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件**含探针**（可能有未证标记）；若成功则另建收据文件。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SingleD3Attack

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`provabilityPred 𝗜𝚺₁ ψ → zfcTr ψ` 的**元层**版本——
由 `paInterp`（𝗭𝗙𝗖 ⊳ 𝗣𝗔）与 `𝗜𝚺₁ ⪯ 𝗣𝗔` 给出。 -/
example (ψ : ArithmeticSentence) (h : 𝗜𝚺₁ ⊢ ψ) : 𝗭𝗙𝗖 ⊢ arithTrln.translate ψ :=
  ZFCZ0.zfc_proves_PA_theorems (Entailment.WeakerThan.pbl h)

/-- **查实 2（本文件的要点）**：`provable_sigma_one_complete` 对 `T = 𝗜𝚺₁` 给出
**`𝗜𝚺₁` 自己的** Σ₁ 完全性——但结论里的 `□` 是 `provabilityPred 𝗜𝚺₁`。 -/
example {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    𝗜𝚺₁ ⊢ σ 🡒 provabilityPred 𝗜𝚺₁ σ :=
  provable_sigma_one_complete (T := 𝗜𝚺₁) hσ

/-- **查实 3（卡点）**：要的是 `zfcTr (zfcTr 𝐆)`，白送的是
`provabilityPred 𝗜𝚺₁ (zfcTr 𝐆)`。两者的桥是元层的（查实 1），
而缺口要**内部**的桥——`𝗜𝚺₁ ⊢ provabilityPred 𝗜𝚺₁ ψ → zfcTr ψ`。

**这正是 `Z0Bridge.lean` 的 `bridge` 前提**（内部解释）。
**所以单句 D3 归约到同一条内部桥，没有绕开它。** -/
example (ψ : ArithmeticSentence) : Prop :=
  𝗜𝚺₁ ⊢ provabilityPred 𝗜𝚺₁ ψ 🡒 zfcTr ψ

end GodelQ.CG008SingleD3Attack
