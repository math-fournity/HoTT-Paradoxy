import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeD3V2

#check FFL.FirstOrder.Arithmetic.provable_iff_provable_model
#check FFL.FirstOrder.Arithmetic.Bootstrapping.derivable_quote
#check FFL.FirstOrder.Arithmetic.Bootstrapping.provable_of_tprovable

-- Attempt: use provable_iff_provable_model to convert the V-model premise into the bare form
-- that Provable.sound accepts, then F, then internalize_provability (which yields the : V form).
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  have h_bare : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝) := provable_iff_provable_model.mpr h
  have h_syn : 𝗭𝗙𝗖 ⊢ arithTrln.translate τ := Provable.sound (T := 𝗭𝗙𝗖) h_bare
  have h2 : 𝗭𝗙𝗖 ⊢ arithTrln.translate (Z0Full.zfcTr τ) :=
    (Sh_provable_iff _).mp (WeakerThan.pbl (Z0Full.zfcTr.D1 ((Sh_provable_iff τ).mpr h_syn)))
  exact internalize_provability (T := 𝗭𝗙𝗖) h2

end GodelQ.ProbeD3V2
