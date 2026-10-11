import GodelQ.ZFC.ShCraigElimSetup
import Foundation.FirstOrder.Incompleteness.Second

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。`axm` 支的四块拼接。

已证四块（前三条见 `ProbeHAxm.lean`，第四条见下）：
1. `σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ`
2. `⌜φ⌝ ∈ Sh.craig.Δ₁Class ⟹ ∃ σ ∈ Sh.craig, iT 0 ⌜φ⌝ = ⌜translate σ⌝`
3. `IsFormulaSet ℒₛₑₜ s → φ ∈ s → Provable 𝗭𝗙𝗖 φ → Derivable 𝗭𝗙𝗖 s`
4. `p ∈ Sh.craig.Δ₁Class ⟹ Sh.IsCraigAxiom p`（本文件）

**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeHAxm2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **第四块**：`p ∈ Sh.craig.Δ₁Class ⟹ Sh.IsCraigAxiom p`。 -/
lemma isCraigAxiom_of_mem_delta1 (p : V) (h : p ∈ Sh.craig.Δ₁Class) :
    Sh.IsCraigAxiom p := by
  rw [Theory.Δ₁Class] at h
  have h' := (Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff.mp h
  simpa using h'

end GodelQ.ProbeHAxm2
