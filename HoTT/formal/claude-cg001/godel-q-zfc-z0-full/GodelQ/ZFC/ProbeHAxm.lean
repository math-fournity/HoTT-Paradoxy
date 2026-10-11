import GodelQ.ZFC.ShCraigElimBranches
import Foundation.FirstOrder.Incompleteness.Second

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。把 `axm` 支接完。

已证两条：
- `zfc_provable_of_mem_craig`：`σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ`
- `iT_of_mem_delta1`：`⌜φ⌝ ∈ Sh.craig.Δ₁Class ⟹ ∃ σ ∈ Sh.craig, iT 0 ⌜φ⌝ = ⌜translate σ⌝`

本文件补最后一步：从 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` 到
`Derivable 𝗭𝗙𝗖 (translateSeq s)`（`⌜translate σ⌝ ∈ translateSeq s` 由 `p ∈ s` 给）。
路线：`Provable.toDerivable` → `insert φ ∅` → `Derivable.wk` 弱化。
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

/-- 路线二：`⌜φ⌝ ∈ Sh.craig.Δ₁Class` 时 `iT 0 ⌜φ⌝` 是某个 `𝗭𝗙𝗖` 可证句的码。 -/
lemma iT_of_mem_delta1 (φ : ArithmeticSentence)
    (h : (⌜φ⌝ : V) ∈ Sh.craig.Δ₁Class) :
    ∃ σ : ArithmeticSentence, σ ∈ Sh.craig ∧ iT (0 : V) (⌜φ⌝ : V) = ⌜arithTrln.translate σ⌝ := by
  have h' := (FFL.FirstOrder.Arithmetic.Bootstrapping.Δ₁Class.mem_iff_s
    (T := Sh.craig) (φ := φ)).mp h
  obtain ⟨σ, hσ, hφ⟩ := h'
  have hφ' : φ = σ := Rewriting.emb_injective hφ
  subst hφ'
  refine ⟨φ, hσ, ?_⟩
  rw [show (0 : V) = ((0 : ℕ) : V) by simp, iT_quote]

/-- **最后一步**：从 `Provable 𝗭𝗙𝗖 φ` 到 `Derivable 𝗭𝗙𝗖 s`（当 `φ ∈ s` 且 `s` 是公式集）。 -/
lemma derivable_of_provable_mem {φ s : V} (hs : IsFormulaSet ℒₛₑₜ s)
    (hφs : φ ∈ s) (hp : Provable 𝗭𝗙𝗖 φ) : Derivable 𝗭𝗙𝗖 s := by
  have hd : Derivable 𝗭𝗙𝗖 (insert φ (∅ : V)) := hp.toDerivable
  refine hd.wk hs ?_
  intro x hx
  rw [mem_bitInsert_iff] at hx
  rcases hx with rfl | hx
  · exact hφs
  · exact absurd hx (by simp)

end GodelQ.ProbeHAxm
