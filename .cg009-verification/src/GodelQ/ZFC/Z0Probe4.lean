import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open FFL.FirstOrder.Arithmetic.R0

namespace GodelQ.Z0Probe4

/-- Carrier-consistent D3: lift the model-internal D3 implication (proven in
`zfcTr_D3_standard`) to a ZFC-derivable theorem via `complete 𝗜𝚺₁` + `arithInterp`,
then re-internalize at V. -/
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  have aux : 𝗜𝚺₁ ⊢ (zfcTr τ) 🡒 (zfcTr (zfcTr τ)) := by
    apply complete 𝗜𝚺₁ _
    intro W hW1 hW2
    apply Semantics.Imp.models_imply.mpr
    intro hp
    rw [models_zfcTr_iff W τ] at hp
    apply (models_zfcTr_iff W (zfcTr τ)).mpr
    exact @h W _ _ τ (models_zfcTr_iff W τ |>.mp hp)
  have hR : 𝗥₀ ⊢ (zfcTr τ) 🡒 (zfcTr (zfcTr τ)) :=
    WeakerThan.pbl (U := 𝗥₀) aux
  have hZ : 𝗭𝗙𝗖 ⊢ arithTrln.translate ((zfcTr τ) 🡒 (zfcTr (zfcTr τ))) :=
    arithInterp.of_provability hR
  have hZ2 : 𝗭𝗙𝗖 ⊢ arithTrln.translate (zfcTr τ) := by
    apply Entailment.by_modus_ponens
    exact hZ
    exact h
  exact internalize_provability (V := V) hZ2

end GodelQ.Z0Probe4
