import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open FFL.FirstOrder.Arithmetic.R0

namespace GodelQ.Z0Probe2

/-- Test: can h : Provable ... : V be reused at : ℕ ? -/
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  have hN : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : ℕ) := h
  have hm : ℕ↓[ℒₒᵣ] ⊧ zfcTr τ := (models_zfcTr_iff ℕ τ).mpr hN
  have hR : 𝗥₀ ⊢ zfcTr τ := sigma_one_completeness (zfcTr_sigma1 τ) hm
  have hZ : 𝗭𝗙𝗖 ⊢ arithTrln.translate (zfcTr τ) := arithInterp.of_provability hR
  exact internalize_provability (V := V) hZ

end GodelQ.Z0Probe2
