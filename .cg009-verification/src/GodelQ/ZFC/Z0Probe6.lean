import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open FFL.FirstOrder.Arithmetic.R0

namespace GodelQ.Z0Probe6

/-- Carrier-independent D3 route: the conclusion `Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)` only depends on the
standard Gödel code, so we strip the carrier by going to the outer derivability `𝗭𝗙𝗖 ⊢ σ`,
reason at the standard model ℕ (where `zfcTr_D3_standard` closes D3), then re-internalize. -/
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  have hm : 𝗭𝗙𝗖 ⊢ arithTrln.translate τ := Provable.toDerivable h
  have hN1 : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : ℕ) := internalize_provability (V := ℕ) hm
  have hmod1 : ℕ↓[ℒₒᵣ] ⊧ zfcTr τ := (models_zfcTr_iff ℕ τ).mpr hN1
  have himp : ℕ↓[ℒₒᵣ] ⊧ (zfcTr τ 🡒 zfcTr (zfcTr τ)) := zfcTr_D3_standard τ
  have hmod2 : ℕ↓[ℒₒᵣ] ⊧ zfcTr (zfcTr τ) := Semantics.Imp.models_imply.mp himp hmod1
  have hN2 : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : ℕ) :=
    (models_zfcTr_iff ℕ (zfcTr τ)).mpr hmod2
  have hm2 : 𝗭𝗙𝗖 ⊢ arithTrln.translate (zfcTr τ) := Provable.toDerivable hN2
  exact internalize_provability (V := V) hm2

end GodelQ.Z0Probe6
