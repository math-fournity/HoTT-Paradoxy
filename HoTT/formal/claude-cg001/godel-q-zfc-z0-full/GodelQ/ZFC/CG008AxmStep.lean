import GodelQ.ZFC.CG008WhichT

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008AxmStep

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 公理步的元层版本：`Sh.craig` 公理的翻译是 𝗭𝗙𝗖 定理

推导变换的**唯一实质处**是公理步（`CG008DerivationTransform.lean`）：
九种规则与理论无关、`of_ss` 原码搬运；只有 `axm` 要换 `T.Δ₁Class`。

**元层版本**：若 `sigma ∈ Sh.craig`，则 `𝗭𝗙𝗖 ⊢ translate sigma`。

这是公理步变换的元层内容——把它机器化是第一步。 -/

/-- **查实 1**：`Sh.craig` 公理经翻译是 𝗭𝗙𝗖 定理（元层）。 -/
example (sigma : ArithmeticSentence) (h : sigma ∈ Sh.craig) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate sigma := by
  have h1 : Sh.craig ⊢ sigma := by_axm h
  have h2 : Sh ⊢ sigma := (inferInstance : Sh.craig ⪯ Sh).wk h1
  exact (Sh_provable_iff sigma).mp h2

end GodelQ.CG008AxmStep
