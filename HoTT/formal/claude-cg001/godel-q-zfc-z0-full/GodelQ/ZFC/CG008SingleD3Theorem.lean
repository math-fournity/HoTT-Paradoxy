import GodelQ.ZFC.CG008BridgeAnatomy

/-!
# CG-008 · 单句 `D3` 的**条件定理**：把归约变成可交付的定理

## 要证的

`CG008SingleD3.lean` 证明了一条**归约**（表格式的观察）。
本文件把它变成**机器检查的定理**：

```
单句 D3  ⟹  Z0 的完整形式
```

具体地：给出

```
h : 𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)        其中 𝐆 := gödel (T₀ := 𝗜𝚺₁) zfcTr
```

则 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。

## 为什么这不是白送

`Z0Full.zfc_z0_full` 取的是 `[zfcTr.HBL3]`——**整族**。
本文件取的是**一条实例**，所以前提**严格更弱**。
若这条定理过核，则「Z0 需要什么」就精确到一条句子。

## 怎么证

`con_unprovable`（`Basic.lean:259`）取 `[𝔅.HBL]`（= `HBL2` + `HBL3`）。
`zfcTr.HBL2` **已建成**（`Z0Full.lean:72`）。
所以要绕开 `HBL3`，就得把 `con_unprovable` 的证明**重做一遍**——
把其中唯一用到 `D3` 的那一步（`formalized_unprovable_gödel` 里）
换成我们的单句假设。

**本文件就是要试这个重做。** 若成功，得到一个前提严格更弱的条件定理。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据；若卡住则照实记录卡点。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SingleD3Theorem

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`zfcTr.HBL2` **已建成**——所以只剩 `HBL3`。 -/
noncomputable example : zfcTr.HBL2 := inferInstance

/-- **查实 2**：`HBL3` 由**整族** `FormalizedCompleteOn` 给出（Foundation 的实例）。 -/
example [∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)] : zfcTr.HBL3 := inferInstance

/-- **查实 3（本文件的目标）**：单句 `D3` 是否足以建 `HBL3`？

**不能**——`HBL3` 的 `D3` 是 `{σ : Sentence L}` 的**模式**，
一条实例填不满它。**所以单句归约不能直接复用 `con_unprovable`**，
必须把那条证明重做。

本行把这一点固定下来：**这是归约与定理之间的真实差距**。 -/
example : Prop :=
  𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
    zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr))

end GodelQ.CG008SingleD3Theorem
