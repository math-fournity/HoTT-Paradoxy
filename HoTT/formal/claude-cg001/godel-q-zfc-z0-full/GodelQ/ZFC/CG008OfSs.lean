import GodelQ.ZFC.CG008DerivationTransform

/-!
# CG-008 · **重大发现**：`Derivation.of_ss` 让推导**沿公理集包含搬运**，码不变

## 读到的（`Syntax/Proof/Basic.lean:756`）

```lean
variable {U : Theory L} [U.Δ₁]
lemma of_ss (h : T.Δ₁Class (V := V) ⊆ U.Δ₁Class) {d : V} :
    Derivation T d → Derivation U d
```

**关键**：`of_ss` 把 `T` 的推导变成 `U` 的推导——**用的是同一个码 `d`**！
**不需要任何码变换。**

## 这对缺口意味着什么

缺口（`CG008BridgeAnatomy`）说：「要把 `d`（𝗜𝚺₁ 推导）变成 `d'`（𝗭𝗙𝗖 推导）」。
**但若 `𝗜𝚺₁.Δ₁Class ⊆ 𝗭𝗙𝗖.Δ₁Class`，则 `d` 本身就是 𝗭𝗙𝗖 的推导——无需变换！**

**然而这不直接够**：缺口要的**结论**不同——
- 前提的结论是 `translate τ`（𝗜𝚺₁ 证明了它）；
- 结论要的是 `translate (zfcTr τ)`（要 𝗭𝗙𝗖 证明它）。

**同一个码 `d` 的结论不会自动变。** 所以 `of_ss` 不能直接闭合缺口。

**但它大幅简化了「推导变换」**：**九种逻辑规则不需要处理**（`of_ss` 已覆盖），
**只有公理步**要处理——而公理步的码 `axm s p` 是**纯语法**的（tag 9），
**不含 `T`**！

**所以**：`d` 的**形状**在 `𝗜𝚺₁` 与 `𝗭𝗙𝗖` 里**相同**；
不同的只是「哪些 `p` 是公理」这个**谓词**。

## 这重写了缺口的形状

**不是**「码变换」，**而是**：
给定 `d` 与「`d` 是 `𝗜𝚺₁` 推导且结论是 `translate τ`」，
**造一个 `d'` 使得「`d'` 是 `𝗭𝗙𝗖` 推导且结论是 `translate (zfcTr τ)`」**。

**即：要「重新拼一个推导」**——用 𝗭𝗙𝗖 的公理替换 𝗜𝚺₁ 的公理步。

**这仍是 `Fixpoint` 层的构造**，但**范围窄得多**：
只需处理公理步的替换，逻辑规则原样保留。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008OfSs

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
  GodelQ.CG008D3AtG GodelQ.CG008CodeFunctions GodelQ.CG008DerivationTransform

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮要点）**：`Derivation.of_ss`——推导沿公理集包含搬运，**码不变**。

**这是本轮最重要的发现**：缺口不需要「码变换」，
因为**逻辑规则部分**可以原样搬运（同一个码）。 -/
example {T U : Theory ℒₛₑₜ} [T.Δ₁] [U.Δ₁]
    (h : T.Δ₁Class (V := V) ⊆ U.Δ₁Class) {d : V}
    (hd : Derivation T d) : Derivation U d :=
  Derivation.of_ss h hd

/-- **查实 2**：`axm` 是**纯语法**的——`axm s p = ⟪s, 9, p⟫ + 1`，
**不含 `T`**。所以推导的**形状**与理论无关；
不同的只是「哪些 `p` 是公理」这个**谓词** `T.Δ₁Class`。 -/
noncomputable example (s p : V) : V := Bootstrapping.axm s p

/-- **查实 3**：`Derivable` 层也有同样的搬运。 -/
example {T U : Theory ℒₛₑₜ} [T.Δ₁] [U.Δ₁]
    (h : T.Δ₁Class (V := V) ⊆ U.Δ₁Class) {s : V}
    (hd : Derivable T s) : Derivable U s :=
  Derivable.of_ss h hd

end GodelQ.CG008OfSs
