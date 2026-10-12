import GodelQ.ZFC.CG008Probe23

/-!
# CG-008 · Craig 路线的可行性核对（探针 23 的展开）

## 本轮发现

探针 23 查实了一件此前记录**未区分**的事：

| 理论 | `Δ₁` | 依据 |
|---|---|---|
| `Sh` | ❌ 不可能 | `CG008Delta1Wall.lean`（否则 𝗭𝗙𝗖 定理集递归，与 G1 矛盾） |
| **`Sh.craig`** | ✅ **有** | `CraigTrick.lean:311` 的 `Theory.instΔ₁Craig`（原始递归公理集） |

且 `Sh.craig ≊ Sh`（`CraigTrick.lean:334`，`Equiv.antisymm_iff`）。

**所以 `provable_D3 (T := Sh.craig)` 可用**——这是探针 15 里 `Sh` 做不到的事。
`provable_D3` 给出 `𝗜𝚺₁ ⊢ provable Sh.craig σ 🡒 provable Sh.craig (provable Sh.craig σ)`。

## 这条路能否推进缺口

缺口要的是（`CG008HBL3.lean`）：
`∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)`，其中 `zfcTr σ = trProv.val/[⌜σ⌝]`，
`trProv = ∃y, iTDef y 0 x ∧ provable 𝗭𝗙𝗖 y`。

**要接上的桥**：`zfcTr σ` 与 `provable Sh.craig σ` 在 𝗜𝚺₁ 内是否可证等价？
- `zfcTr σ ↔ Provable 𝗭𝗙𝗖 ⌜translate σ⌝`（`trProvable_quote`，语义层）；
- `provable Sh.craig σ` 说的是「`Sh.craig` 证明了 σ」；
- 而 `Sh.craig ≊ Sh`，`Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ translate σ`（`Sh_provable_iff`）。

**所以语义上两者等价**——但**内部**（𝗜𝚺₁ 内）的等价正是 `Z0Final.lean`
试过并失败的那条（「廉价传递」），它坍缩回 D3 本身。

## 本文件要查实的

1. `provable_D3 (T := Sh.craig)` 确实可用（陈述）；
2. `Sh.craig ≊ Sh` 的传递形式；
3. 关键：`zfcTr σ` 与 `provable Sh.craig σ` 的**内部**等价是否就是缺口本身。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008CraigRoute

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮关键）**：`provable_D3` 对 `Sh.craig` **可用**——
`Sh.craig` 有 `Δ₁`（`CraigTrick.lean:311`），而 `Sh` 没有。

这给出 `𝗜𝚺₁ ⊢ provable Sh.craig σ 🡒 provable Sh.craig (provable Sh.craig σ)`。 -/
example {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ (provabilityPred Sh.craig σ) 🡒
      (provabilityPred Sh.craig (provabilityPred Sh.craig σ)) :=
  provable_D3 (T := Sh.craig)

/-- **查实 2**：`Sh.craig` 与 `Sh` 等价——`T ≊ T.craig`。 -/
example : Sh ⪯ Sh.craig := inferInstance

example : Sh.craig ⪯ Sh := inferInstance

/-- **查实 3（本文件的要点）**：`zfcTr σ` 与 `provable Sh.craig σ` 的关系。

`zfcTr σ ↔ Provable 𝗭𝗙𝗖 ⌜translate σ⌝`（`trProvable_quote`，**语义**层），
而 `provable Sh.craig σ` 是「`Sh.craig` 证明了 σ」。
由 `Sh.craig ≊ Sh` 与 `Sh_provable_iff`，两者**语义等价**。

**但缺口要的是 𝗜𝚺₁ 内部的等价**，而那正是 `Z0Final.lean` 试过并失败的「廉价传递」——
它坍缩回 D3 本身。

本探针把这一点固定：`provable_D3 (T := Sh.craig)` 是**真的**、**可用的**、
但它的**结论句**是 `provable Sh.craig`，不是 `zfcTr`。 -/
example (σ : ArithmeticSentence) : Sh.craig ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ :=
  ⟨fun h ↦ (Sh_provable_iff σ).mp (WeakerThan.pbl h),
   fun h ↦ WeakerThan.pbl ((Sh_provable_iff σ).mpr h)⟩

end GodelQ.CG008CraigRoute
