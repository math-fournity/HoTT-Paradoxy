import GodelQ.ZFC.ShCraigElimBranches
import Foundation.FirstOrder.Incompleteness.Second

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。把 `axm` 支接完。

**已证三块**：
- `zfc_provable_of_mem_craig`：`σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ`
- `iT_of_mem_delta1`：`⌜φ⌝ ∈ Sh.craig.Δ₁Class ⟹ ∃ σ ∈ Sh.craig, iT 0 ⌜φ⌝ = ⌜translate σ⌝`
- `derivable_of_provable_mem`：`IsFormulaSet ℒₛₑₜ s → φ ∈ s → Provable 𝗭𝗙𝗖 φ → Derivable 𝗭𝗙𝗖 s`

**本文件补最后一环**：`axm` 支的 `p` 是裸 `V`，需把 `p ∈ Sh.craig.Δ₁Class`
接到 `∃ φ, p = ⌜φ⌝`。V 层 `IsCraigAxiom` 的定义直接给出形状：
`x = q ^⋏ qqVerums s`，而 `⌜σ.padding k⌝ = ⌜σ⌝ ^⋏ qqVerums k`（`quote_padding`）。
**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeHAxm

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 路线一。 -/
lemma zfc_provable_of_mem_craig (σ : ArithmeticSentence) (h : σ ∈ Sh.craig) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate σ := by
  rw [← Sh_provable_iff]
  exact (inferInstance : Sh.craig ⪯ Sh).pbl (Entailment.by_axm h)

/-- 路线二。 -/
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

/-- 路线三：`Provable → Derivable` 弱化。 -/
lemma derivable_of_provable_mem {φ s : V} (hs : IsFormulaSet ℒₛₑₜ s)
    (hφs : φ ∈ s) (hp : Provable 𝗭𝗙𝗖 φ) : Derivable 𝗭𝗙𝗖 s := by
  have hd : Derivable 𝗭𝗙𝗖 (insert φ (∅ : V)) := hp.toDerivable
  refine hd.wk hs ?_
  intro x hx
  rw [mem_bitInsert_iff] at hx
  rcases hx with rfl | hx
  · exact hφs
  · exact absurd hx (by simp)

/-- **最后一环判定**：V 层的 `Sh.IsCraigAxiom p` 给出的形状。 -/
example (p : V) (h : Sh.IsCraigAxiom p) : ∃ s q : V, p = q ^⋏ qqVerums s := by
  obtain ⟨s, q, hpq, _⟩ := h
  exact ⟨s, q, hpq⟩

end GodelQ.ProbeHAxm
