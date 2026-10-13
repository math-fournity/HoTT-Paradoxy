import GodelQ.ZFC.CG008Bridge1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008D3Chain

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008Bridge1
open ProvabilityAbstraction (gödel gödel_spec)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

noncomputable abbrev G : Sentence ℒₒᵣ := gödel (T₀ := 𝗜𝚺₁) zfcTr

/-! # `hD3G` 的链条：还剩什么

**目标**：`𝗜𝚺₁ ⊢ zfcTr → G → zfcTr (zfcTr G)`。

**已证的三段**（本轮）：

| 段 | 内容 | 文件 |
|---|---|---|
| 1 | `G ∈ Sh.craig → TrProvable ⌜G⌝` | `CG008Bridge1` |
| 2 | `iT 0 ⌜sigma⌝ = ⌜translate sigma⌝` | `iT_quote` |
| 3 | `𝗭𝗙𝗖 ⊢ φ → Provable 𝗭𝗙𝗖 ⌜φ⌝` | `internalize_provability` |

**Foundation 已给的**：

* `provable_sigma_one_complete (T := 𝗜𝚺₁)`：`𝗜𝚺₁ ⊢ σ → provabilityPred 𝗜𝚺₁ σ`
  （σ 是 Σ₁ 句；`zfcTr G` 是 Σ₁，故 `𝗜𝚺₁ ⊢ zfcTr G → provabilityPred 𝗜𝚺₁ (zfcTr G)`）
* `provable_internalize (T := Sh.craig)`：`Provable Sh.craig ⌜σ⌝ → Provable Sh.craig ⌜provabilityPred Sh.craig σ⌝`

**还缺的**：`provabilityPred 𝗜𝚺₁ ψ → zfcTr ψ` 与 `provabilityPred Sh.craig ψ → provabilityPred 𝗜𝚺₁ ψ`。

本文件把这些段的形状钉住。 -/

/-- **查实 1**：`zfcTr G` 是 Σ₁ 句，故 𝗜𝚺₁ 自己的 Σ₁ 完全性适用。 -/
example : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr G) := zfcTr_sigma1 G

/-- **查实 2**：本轮证的公理步内容，在 `G` 上。 -/
example (h : G ∈ Sh.craig) : TrProvable (⌜G⌝ : V) :=
  GodelQ.CG008Bridge1.craig_mem_to_TrProvable G h

end GodelQ.CG008D3Chain
