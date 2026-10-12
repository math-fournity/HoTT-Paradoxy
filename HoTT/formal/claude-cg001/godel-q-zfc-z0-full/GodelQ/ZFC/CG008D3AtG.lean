import GodelQ.ZFC.CG008Z0FromSingleD3

/-!
# CG-008 · 攻最后一条：`hD3G` 本身

## 目标

```
hD3G : 𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)          𝐆 := gödel (T₀ := 𝗜𝚺₁) zfcTr
```

**这是缺口现在**唯一**剩余的东西**（`CG008Z0FromSingleD3.lean` 已证：它 ⟹ Z0）。

## 为什么 `𝐆` 上的 `D3` 可能真的更容易

一般 `D3`（`∀ σ`）的标准证法是**形式化 Σ₁ 完全性**，跑遍 σ 的结构——
而 `ℒₛₑₜ` 无常项使 `toNumVec` 那一步无对偶（`CG008Correction.lean`）。

**但 `𝐆` 是固定的对角线句**，满足 `𝗜𝚺₁ ⊢ 𝐆 🡘 ∼zfcTr 𝐆`（`gödel_spec`）。

**关键想法**：`zfcTr 𝐆` 是 **Σ₁ 句**，而 `𝗜𝚺₁` **自己有** Σ₁ 完全性：

```lean
provable_sigma_one_complete (T := 𝗜𝚺₁) : 𝗜𝚺₁ ⊢ σ 🡒 provabilityPred 𝗜𝚺₁ σ
```

取 `σ := zfcTr 𝐆`，得 `𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 provabilityPred 𝗜𝚺₁ (zfcTr 𝐆)`。

**要的是** `zfcTr (zfcTr 𝐆)`，而白送的是 `provabilityPred 𝗜𝚺₁ (zfcTr 𝐆)`。
**两者的桥**：`provabilityPred 𝗜𝚺₁ ψ → zfcTr ψ`，即
「`𝗜𝚺₁` 证明了 ψ ⟹ `𝗭𝗙𝗖` 证明了 `translate ψ`」。

**元层版本已证**（`Z0PA.zfc_proves_PA_theorems`）。
**内部版本**是 `Z0Bridge` 的 `bridge`——**所以这条路又回到那条内部桥**。

## 但这次有个新东西

**`ψ := zfcTr 𝐆` 是 Σ₁ 句**，而**内部桥对 Σ₁ 句**也许比一般情形容易：
`translate` 作用在 Σ₁ 句上时，其结构比一般集合句简单。

**本文件试这条。**

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008D3AtG

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo GodelQ.CG008MonoExt GodelQ.CG008RedoPrereq GodelQ.CG008RedoActual
  GodelQ.CG008AbstractRedo GodelQ.CG008Instantiate GodelQ.CG008Z0FromSingleD3

open ProvabilityAbstraction (gödel gödel_spec)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 目标句。 -/
noncomputable abbrev G : Sentence ℒₒᵣ := gödel (T₀ := 𝗜𝚺₁) zfcTr

/-- **查实 1**：`zfcTr 𝐆` 是 **Σ₁ 句**——所以 `𝗜𝚺₁` 自己的 Σ₁ 完全性适用。 -/
example : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr G) := zfcTr_sigma1 G

/-- **查实 2**：`𝗜𝚺₁` 的 Σ₁ 完全性对 `zfcTr 𝐆` 给出**它自己的**可证性句。 -/
example : 𝗜𝚺₁ ⊢ zfcTr G 🡒 provabilityPred 𝗜𝚺₁ (zfcTr G) :=
  provable_sigma_one_complete (T := 𝗜𝚺₁) (zfcTr_sigma1 G)

/-- **查实 3（卡点，与之前一致）**：要接的是
`provabilityPred 𝗜𝚺₁ ψ → zfcTr ψ`——**内部桥**。

**所以 `𝐆` 上的 `D3` 也归约到同一条内部桥。** -/
example (ψ : ArithmeticSentence) : Prop :=
  𝗜𝚺₁ ⊢ provabilityPred 𝗜𝚺₁ ψ 🡒 zfcTr ψ

end GodelQ.CG008D3AtG
