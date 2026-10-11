import GodelQ.ZFC.ShCraigElimBranches
import Foundation.FirstOrder.Incompleteness.Second

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。攻 `axm` 支。
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

/-- 路线二（第一步）：先把 `mem_iff_s` 转成 `Sh.craig` 的成员。 -/
lemma mem_craig_of_mem_delta1 (φ : ArithmeticSentence)
    (h : (⌜φ⌝ : V) ∈ Sh.craig.Δ₁Class) : ∃ σ : ArithmeticSentence, σ ∈ Sh.craig := by
  have h' := (FFL.FirstOrder.Arithmetic.Bootstrapping.Δ₁Class.mem_iff_s
    (T := Sh.craig) (φ := φ)).mp h
  obtain ⟨σ, hσ, _⟩ := h'
  exact ⟨σ, hσ⟩

/-- **`axm` 支的核心**：`⌜φ⌝ ∈ Sh.craig.Δ₁Class` 时 `iT 0 ⌜φ⌝` 就是某个 `𝗭𝗙𝗖` 可证句的码。

结论写成 `∃ σ : ArithmeticSentence, σ ∈ Sh.craig ∧ iT (0:V) (⌜φ⌝:V) = ⌜arithTrln.translate σ⌝`
——把 `Entailment` 实例的搜索推给调用方，本引理只做码层的等式。 -/
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

end GodelQ.ProbeHAxm
