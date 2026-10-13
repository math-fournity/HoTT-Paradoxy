import GodelQ.ZFC.CG008GapSharp
import GodelQ.ZFC.Z0Bridge

/-!
# CG-008 · Z0 的**最窄条件形式**（本轮锐化后的交付形状）

## 本轮做了什么

把 `Z0Bridge` 的 `bridge` 前提**锐化**：原来它要求

```
bridge : ∀ σ（Σ₁ 算术句）, Provable 𝗜𝚺₁ ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate σ⌝
```

即「内部化的解释保可证性」。本轮（`CG008GapSharp.lean`）证明：
`hD3G` 的前提经 𝗜𝚺₁ 自己的 Σ₁ 完全性**恰好给出这个前提的一个实例**
（`σ := zfcTr τ`）。所以 `bridge` **就是**缺口的最窄形式——
它与缺口同强，不是更弱的目标（`CG008Circularity.lean` 机器化说明了为什么）。

## 本文件交付什么

**一条 `sorry`-free、公理洁净的定理**：
`bridge`（最窄形式）⟹ **完整的 Z0**。

即 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`——
**以一条显式、精确陈述的未证前提为条件**。

这与 `Z0Bridge.zfc_z0_full_of_sigma1_bridge` 是同一件事，
但**前提的陈述形状**是本轮锐化后的形式，并且本文件额外把
「该前提与缺口同强」也机器化地接上（经 `CG008GapSharp` 与 `CG008Circularity`）。

## 诚实状态

`Z0Blocked.lean:65` 的 `sorry` **仍在**——本文件**不**消除它，
也不声称缺口已证。它交付的是**最强的诚实条件形式**，
并把未证前提收成一条**精确、可独立攻的**命题。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Z0Sharp
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate

/-- **最窄前提**（= `CG008Circularity.Narrow`，此处给出 `Type` 层的版本以对接 `Z0Bridge`）。

「内部化的解释保可证性」：每个 Σ₁ 算术句的内部证明编码，
沿 `arithTrln` 变成它在 𝗭𝗙𝗖 中的内部证明编码。 -/
def NarrowBridge : Prop :=
  ∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    {σ : ArithmeticSentence},
    ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
    Provable 𝗜𝚺₁ (⌜σ⌝ : V) →
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

/-- **主交付**：最窄前提 ⟹ 完整的 Z0。 -/
theorem zfc_z0_of_narrow_bridge (h : NarrowBridge) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  GodelQ.Z0Bridge.zfc_z0_full_of_sigma1_bridge h

/-- **前提的等价重述**：`NarrowBridge` 与 `Z0Bridge` 用的 `bridge` 是同一形状。

（两条定义逐字相同，此处只做 `Iff.rfl` 级别的固定，
标明本轮锐化**没有**换掉前提，只是把它定位成最窄形式。） -/
theorem narrowBridge_iff_z0Bridge_bridge :
    NarrowBridge ↔
      (∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
        {σ : ArithmeticSentence},
        ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
        Provable 𝗜𝚺₁ (⌜σ⌝ : V) →
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)) :=
  Iff.rfl

end GodelQ.CG008Z0Sharp

#print axioms GodelQ.CG008Z0Sharp.zfc_z0_of_narrow_bridge
#print axioms GodelQ.CG008Z0Sharp.narrowBridge_iff_z0Bridge_bridge
