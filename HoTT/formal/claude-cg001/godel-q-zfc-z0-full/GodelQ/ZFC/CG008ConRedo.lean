import GodelQ.ZFC.CG008SingleD3Theorem

/-!
# CG-008 · 重做 `con_unprovable`：只用单句 `D3`

## 目标

在**本包内**重做抽象 G2 的证明，把其中唯一用到 `D3` 的那一步换成**单句假设**，
从而得到一条**前提严格更弱**的条件定理：

```
h : 𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)         𝐆 := gödel (T₀ := 𝗜𝚺₁) zfcTr
⟹ 𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)
```

## 要复制的证明链（`Basic.lean:243-268`）

```
formalized_unprovable_gödel : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆
  h₁ := D3 @ 𝐆                       ← **只换这一步**
  h₂ := 𝔅.mono' (gödel_spec 推 𝔅𝐆 → 𝔅(𝔅𝐆 🡒 ⊥))
  h₃ := D2 @ (𝔅𝐆, ⊥)
  cl_prover [h₁, h₂, h₃]

gödel_iff_con : T₀ ⊢ 𝐆 🡘 𝔅.con
  h₁ := formalized_consistent_of_existance_unprovable   （只用 D2、D1）
  h₂ := formalized_unprovable_gödel
  h₃ := gödel_spec
  cl_prover [h₁, h₂, h₃]

con_unprovable [Consistent T] : T ⊬ 𝔅.con
  ← gödel_iff_con + unprovable_gödel
```

**关键**：`h₁ := D3 @ 𝐆` 是**唯一**用到 `D3` 的地方，
且用在**固定的句子** `𝐆` 上。所以把 `D3` 换成单句假设后，
**整条链应当照跑**——前提是 `D2`（`HBL2`）与 `D1` 仍可用。

**`zfcTr.HBL2` 已建成**（`Z0Full.lean:72`），`D1` 由 `Provability` 结构自带。
**所以这条重做是可行的**——本文件来试。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据；若卡住则照实记录卡点。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ConRedo

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

noncomputable example : Diagonalization 𝗜𝚺₁ := inferInstance

noncomputable example : Provability 𝗜𝚺₁ Sh := zfcTr

/-- **查实 3（本文件的目标）**：把 `formalized_unprovable_gödel` 里
**唯一**用到 `D3` 的那一步，换成**单句假设**。

`D3 @ 𝐆` 被换成 `hD3G`——其余步骤（`𝔅.mono'`、`gödel_spec`、`D2`）不变。

本行只**陈述**这个替换后的目标（不证明），把重做的确切形状固定下来。 -/
example : Prop :=
  𝗜𝚺₁ ⊢ zfcTr.con 🡒 ∼zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr)

end GodelQ.CG008ConRedo
