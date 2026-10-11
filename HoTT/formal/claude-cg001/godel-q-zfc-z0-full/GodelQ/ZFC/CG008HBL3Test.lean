import GodelQ.ZFC.CG008HBL3

/-!
# CG-008 · 探针 14（非收据）：`zfcTr.FormalizedCompleteOn (zfcTr σ)` 能否建成

## 目标形状

`CG008HBL3.lean` 把缺口改述为 `zfcTr.HBL3`，而 Foundation 给了充分条件
`∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`，即

```
∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)
```

展开 `zfcTr_def`（`zfcTr σ = trProv.val/[⌜σ⌝]`）与 `trProvable_quote`，
这条说的是

```
∀ σ, 𝗜𝚺₁ ⊢ (V ⊨ zfcTr σ) → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝
```

**这正是 `zfcTr_D3_internalize` 的 𝗜𝚺₁ 内部形式**——所以它**不可能**白送；
若能白送，Z0 就成立了。

## 本探针要查实的是：它**到底**卡在哪一步

`zfcTr σ` 的 `bew_def`（`Z0Full.lean:62-63`）已经证过一次同形的东西：

```lean
bew_def {σ} h := complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦
  (models_trProv_iff V σ).mpr (internalize_provability ((Sh_provable_iff σ).mp h))
```

即：**从 `Sh ⊢ σ`（外部元层）出发**，用 `internalize_provability` 得到
`Provable 𝗭𝗙𝗖 ⌜translate σ⌝`，再 `complete 𝗜𝚺₁` 收成 𝗜𝚺₁ 的定理。

**关键对照**：`bew_def` 的前提是**元层的** `Sh ⊢ σ`；
而 `FormalizedCompleteOn (zfcTr σ)` 要的前提是**内部的** `zfcTr σ`（即 `V ⊨ zfcTr σ`）。

从「V 内部的 `zfcTr σ` 成立」到「元层的 `Sh ⊢ σ`」需要**可靠性**
（`Provable.sound` 一类），而 `Provable.sound` 只接受标准模型 ℕ 的报价
（`Z0Blocked.lean` 诊断第 2 条已记录）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008HBL3Test

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`zfcTr` 的 D1 已建成——**前提是元层的 `Sh ⊢ σ`**。 -/
example {σ : ArithmeticSentence} (h : Sh ⊢ σ) : 𝗜𝚺₁ ⊢ zfcTr σ :=
  zfcTr.D1 h

/-- **查实 2（关键对照）**：`FormalizedCompleteOn` 要的形状——**前提是内部的**。

它是 `class`，字段是 `formalized_complete_on : T₀ ⊢ σ 🡒 𝔅 σ`。
取 `𝔅 := zfcTr`、`σ := zfcTr σ₀`，得 `𝗜𝚺₁ ⊢ zfcTr σ₀ 🡒 zfcTr (zfcTr σ₀)`。 -/
example (σ : ArithmeticSentence) [zfcTr.FormalizedCompleteOn (zfcTr σ)] :
    𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ) :=
  Provability.formalized_complete_on (𝔅 := zfcTr) (σ := zfcTr σ)

/-- **查实 3**：`Sh` 是算术理论的**影子**——`Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ translate σ`。 -/
example (σ : ArithmeticSentence) : Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ :=
  Sh_provable_iff σ

/-- **查实 4**：`bew_def` 的证明机制——从元层 `Sh ⊢ σ` 到 𝗜𝚺₁ 的定理。

本探针记录：这条**已存在**且**工作**，它证明的是 D1；
而缺口要的 D3 需要把前提从**元层**换成**内部**，
这一步在 Foundation 现有 API 下没有桥（`Provable.sound` 只接受 ℕ 报价）。 -/
example {σ : ArithmeticSentence} (h : Sh ⊢ σ) : 𝗜𝚺₁ ⊢ zfcTr σ :=
  zfcTr.D1 h

end GodelQ.CG008HBL3Test
