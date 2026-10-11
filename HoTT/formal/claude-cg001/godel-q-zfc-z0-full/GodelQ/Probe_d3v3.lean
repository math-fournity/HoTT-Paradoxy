import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeD3V3

#check provable_iff_provable
#check FFL.FirstOrder.Arithmetic.provable_D3

-- Attempt A: rewrite the :V quote to the definitional (ℕ) form that Provable.sound accepts.
theorem zfcTr_D3_internalize_A {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  have h_syn : 𝗭𝗙𝗖 ⊢ arithTrln.translate τ :=
    Provable.sound (T := 𝗭𝗙𝗖) (by simpa [Sentence.quote_def, Semiformula.quote_def] using h)
  have h2 : 𝗭𝗙𝗖 ⊢ arithTrln.translate (Z0Full.zfcTr τ) :=
    (Sh_provable_iff _).mp (WeakerThan.pbl (Z0Full.zfcTr.D1 ((Sh_provable_iff τ).mpr h_syn)))
  exact internalize_provability (T := 𝗭𝗙𝗖) h2

end GodelQ.ProbeD3V3
