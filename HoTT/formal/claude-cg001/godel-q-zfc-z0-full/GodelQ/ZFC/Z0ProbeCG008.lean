import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open FFL.FirstOrder.Arithmetic.R0

namespace GodelQ.Z0ProbeCG008

-- Variant A: let `provable_iff_provable.mp h` drive τ's expected type (no annotation).
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate τ := by
  exact (provable_iff_provable (T := 𝗭𝗙𝗖)).mp h

-- Variant B: full closure via models_zfcTr_iff (already compiles) + Σ1-completeness.
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  have hm : 𝗭𝗙𝗖 ⊢ arithTrln.translate τ := by
    apply (models_zfcTr_iff V τ).mp
    exact h
  have hc : 𝗭𝗙𝗖 ⊢ arithTrln.translate (zfcTr τ) := by
    apply arithInterp.of_provability
    apply sigma_one_completeness (zfcTr_sigma1 τ)
    apply (models_zfcTr_iff ℕ τ).mpr
    exact (provable_iff_provable (T := 𝗭𝗙𝗖)).mpr hm
  exact internalize_provability (V := V) hc

end GodelQ.Z0ProbeCG008
