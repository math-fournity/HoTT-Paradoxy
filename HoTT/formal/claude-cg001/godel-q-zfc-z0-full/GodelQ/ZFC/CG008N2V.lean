import GodelQ.ZFC.CG008Univ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008N2V

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

/-! # 精确缺口：ℕ → 任意 V 的搬运断言

## Foundation 已有的一半（机器核实）

* `natCastEmbedding : ℕ ↪ₛ[ℒₒᵣ] V`
  （`Definability/Absoluteness.lean:20`，前提只要 `[V ↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻]`）；
* `instance : ℬ[<, ℒₒᵣ].IsInitial (natCastEmbedding V)`（同文件 `:43`）；
* `sigma_one_upward`、`models_iff_of_Delta1` —— Σ₁ 沿此嵌入的绝对性
  （`Tarski/HierarchicalDefinability/Absoluteness.lean:93`、
   `Arithmetic/Definability/Absoluteness.lean:113`）。

**所以 ℒₒᵣ 侧的 ℕ ↔ V 搬运是现成的**——
「宇宙不匹配是障碍」在**算术侧**不成立，Master 的先例判断在这一侧对。

## 缺口在另一侧

`zfcTr sigma` 是 ℒₒᵣ 的 Σ₁ 句，这一侧搬运现成。
但结论 `iT 0 ⌜sigma⌝` 是 **ℒₜ 的元素**（集合句编码），
`Provable 𝗭𝗙𝗖 ·` 量的是 **ℒₜ 推导**。
从 ℒₒᵣ 的 Σ₁ 陈述跳到 ℒₜ 推导码，正是 `trProv` 里那一跃：
`trProv = "x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y"`。

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：`natCastEmbedding` 的类型可完整写出。 -/
noncomputable example (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] :
    Tarski.Structure.Embedding ℒₒᵣ ℕ V :=
  natCastEmbedding V

end GodelQ.CG008N2V
