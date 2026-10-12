import GodelQ.ZFC.CG008Probe22

/-!
# CG-008 探针 23（非收据）：`Sh.craig` 有没有 `Δ₁`——一条此前未机器核实的路

## 背景

探针 15 查实 `Sh.Δ₁` 无法合成（且更强：`Sh.standardProvability` 连提及都不行）。
`CG008Delta1Wall.lean` 论证 `Sh.Δ₁` **不可能**成立（否则 𝗭𝗙𝗖 定理集递归，与 G1 矛盾）。

**但 `Sh.craig` 是另一回事。** Craig 重公理化定理说：任一 r.e. 理论的
Craig 重公理化有一组**原始递归**的公理集。原始递归 ⇒ Δ₁。

**若 `Sh.craig.Δ₁` 成立**，则 `provable_D3 (T := Sh.craig)` 可用，
给出 `𝗜𝚺₁ ⊢ provable Sh.craig σ → provable Sh.craig (provable Sh.craig σ)`。

**这条路是否推进缺口？** 需要判断：
- `provable Sh.craig σ` 与 `provable Sh σ` 是否在 𝗜𝚺₁ 内可证等价；
- 以及它与 `zfcTr σ` 的关系。

记录里说「`Sh.craig` 捷径（`Δ₁ Sh` 不成立）」被排除——**本探针要核实那条排除
针对的到底是 `Sh.Δ₁` 还是 `Sh.craig.Δ₁`**，因为两者是不同的理论。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe23

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`Sh.craig` 的 `RE` 已证（`ShRE.lean`）。 -/
example [Sh.RE] : Sh.craig.RE := inferInstance

/-- **查实 2（关键发现）**：`Sh.craig.Δ₁` **能合成**！

报错信息显示实例名是 `Theory.instΔ₁Craig`——Foundation **已为
Craig 重公理化提供 `Δ₁` 实例**（原始递归的公理集 ⇒ Δ₁）。

**这与 `Sh.Δ₁` 形成对照**：`Sh` 无 `Δ₁`（探针 15，且不可能有，`CG008Delta1Wall.lean`），
但 `Sh.craig` **有**。所以 `provable_D3 (T := Sh.craig)` 可用。 -/
noncomputable example : Sh.craig.Δ₁ := inferInstance

/-- **查实 3**：于是 `Sh.craig` 的 `standardProvability` 的 `HBL3` **白送**。

这是探针 15 里 `Sh` 做不到的事——`Sh.craig` 做得到。
**关键问题变成**：`provable Sh.craig σ` 与 `zfcTr σ` 能否接上。 -/
noncomputable example : Sh.craig.standardProvability.HBL3 := inferInstance

/-- **查实 4**：`Sh.craig` 与 `Sh` 等价——`T ≊ T.craig`（`CraigTrick.lean:334`），
故两者互相弱于，可证性相同。 -/
example : Sh ⪯ Sh.craig := inferInstance

example : Sh.craig ⪯ Sh := inferInstance

/-- **查实 5**：`provable_D3` 对 `Sh.craig` **可用**——这是探针 15 里 `Sh` 做不到的事。 -/
example {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ (provabilityPred Sh.craig σ) 🡒
      (provabilityPred Sh.craig (provabilityPred Sh.craig σ)) :=
  provable_D3 (T := Sh.craig)

end GodelQ.CG008Probe23
