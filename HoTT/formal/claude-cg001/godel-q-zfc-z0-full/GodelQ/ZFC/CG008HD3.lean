import GodelQ.ZFC.CG008FinalBridge

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008HD3

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 攻 `hD3G`：把它归约到**一条** ZFC 定理

**目标**：`𝗜𝚺₁ ⊢ zfcTr σ → zfcTr (zfcTr σ)`。

**归约**：经 `zfcTr.D1`，`𝗜𝚺₁ ⊢ zfcTr (zfcTr σ)` 归结为 `Sh ⊢ (zfcTr σ)`。

即 `𝗭𝗙𝗖 ⊢ translate (zfcTr σ)`。

而 `translate (zfcTr σ)` 是「ZFC 证明了 translate σ」的集合论翻译（Σ₁ 句）。

**所以 hD3G ⟺ `𝗭𝗙𝗖 ⊢ translate (zfcTr σ)`（在前件下）**。

本轮已证：`σ ∈ Sh.craig → 𝗭𝗙𝗖 ⊢ translate σ`（`CG008Bridge1`）。
**还差**：把「`σ ∈ Sh.craig`」换成「`zfcTr σ` 在 V 中为真」。 -/

/-- **查实 1**：`zfcTr.D1` 的形状——归约正是经它。 -/
example (sigma : ArithmeticSentence) (h : Sh ⊢ zfcTr sigma) : 𝗜𝚺₁ ⊢ zfcTr (zfcTr sigma) :=
  zfcTr.D1 h

end GodelQ.CG008HD3
