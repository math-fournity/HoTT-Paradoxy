import GodelQ.ZFC.CG008Correction
import Foundation.FirstOrder.Incompleteness.ProvabilityAbstraction.Refutability

/-!
# CG-008 · 重大发现：抽象 G2 只需**单句** `FormalizedCompleteOn`，不是整族 `HBL3`

## 读到的（`Incompleteness/ProvabilityAbstraction/Refutability.lean`）

```lean
lemma unprovable_flon [consis : Consistent T] [𝔅.FormalizedCompleteOn 𝐉] :
    T ⊬ flon 𝔅 𝔚
```

其中 `𝐉 := jeroslow 𝔚` 是**一个固定的句子**（`jeroslow_def` 的对角线句）。

**注意前提**：`[𝔅.FormalizedCompleteOn 𝐉]`——**只对 `𝐉` 这一句**，
不是 `∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)`（那才是 `HBL3` 的充分条件）。

## 这对缺口意味着什么

此前几轮（`CG008HBL3.lean`、`CG008Final.lean`）把缺口定型为
**整族** `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`。

**若 Z0 可以改走 `unprovable_flon` 这条抽象 G2**，
则只需 `zfcTr.FormalizedCompleteOn 𝐉` 的**一条实例**——
前提从「元层全称的族」降到「一条固定的句子」。

**这可能把缺口从「一个模式」降为「一条实例」。**

## 但要核实的

1. `unprovable_flon` 的类型对 `𝔅 = zfcTr` 是否可实例化（`L = L₀ = ℒₒᵣ`？）；
2. `flon 𝔅 𝔚` 与 Z0 要的 `zfcTr.con` 是什么关系——**若不等，这条路不直接给 Z0**；
3. `𝔚`（`Refutability`）从哪来。

**第 2 条是关键**：`unprovable_flon` 给的是 `T ⊬ flon 𝔅 𝔚`，
而 Z0 要的是 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。
**两者是不同的句子**——除非 `flon` 与 `con` 等价（`safe` 说的是
「不（`𝔅 x` 且 `𝔚 x`）」，与一致性句不同）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SingleSentence

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮的发现）**：`unprovable_flon` 的**前提只针对单句** `𝐉`。

对比：`HBL3` 的充分条件 `[∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)]` 是**整族**。
`unprovable_flon` 只要 `[𝔅.FormalizedCompleteOn 𝐉]`。 -/
example {L : Language} [L.DecidableEq] [L.ReferenceableBy L] {T₀ T : Theory L}
    [Diagonalization T₀] [T₀ ⪯ T] {𝔅 : Provability T₀ T}
    {𝔚 : ProvabilityAbstraction.Refutability T₀ T}
    [Consistent T] [𝔅.FormalizedCompleteOn (ProvabilityAbstraction.jeroslow 𝔚)] :
    T ⊬ ProvabilityAbstraction.flon 𝔅 𝔚 :=
  ProvabilityAbstraction.unprovable_flon

/-- **查实 2（关键对照）**：`flon` 的形状——`∀x, ¬(𝔅 x ∧ 𝔚 x)`。

**它不是一致性句 `𝔅.con = ∼𝔅 ⊥`**（`Basic.lean:39`）。
所以 `unprovable_flon` **不直接**给出 Z0 要的 `zfcTr.con` 不可证。 -/
example {L : Language} [L.ReferenceableBy L] {T₀ : Theory L} {T : Theory L}
    (𝔅 : Provability T₀ T) (𝔚 : ProvabilityAbstraction.Refutability T₀ T) :
    ProvabilityAbstraction.flon 𝔅 𝔚 =
      (∀¹ ProvabilityAbstraction.safe 𝔅 𝔚) := rfl

end GodelQ.CG008SingleSentence
