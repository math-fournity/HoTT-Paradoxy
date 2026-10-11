import GodelQ.ZFC.ShCraigElimBranches

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。`axm` 支的路线探索。

## 已确认的两条路线（都可用，但接进 `axm` 支还需对上类型）

**路线一**：`σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ`。
三步：`Sh.craig ⪯ Sh`（Foundation `CraigTrick.lean:321` 已有实例）
→ `Sh_provable_iff`（本包 `Z0Shadow.lean:45`）→ `Entailment.by_axm`。

**路线二**：`p = ⌜φ⌝` 且 `p ∈ Sh.craig.Δ₁Class` 时 `𝗭𝗙𝗖 ⊢ iT 0 p`。
用 Foundation 的 `Δ₁Class.mem_iff_s`
（`(⌜φ⌝ : V) ∈ T.Δ₁Class ↔ ∃ σ ∈ T, φ = σ`，在 `FFL.FirstOrder.Arithmetic.Bootstrapping`
命名空间下）把 `Δ₁Class` 的成员转成 `T` 的成员，再接路线一 + `iT_quote`。

## 未完成

类型与命名空间对齐（`Entailment SetTheory V` 实例的引入路径、`mem_iff_s` 的完整限定名）。
**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeHAxm

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 路线一：`σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ translate σ`。 -/
lemma zfc_provable_of_mem_craig (σ : ArithmeticSentence) (h : σ ∈ Sh.craig) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate σ := by
  rw [← Sh_provable_iff]
  exact (inferInstance : Sh.craig ⪯ Sh).pbl (Entailment.by_axm h)

end GodelQ.ProbeHAxm
