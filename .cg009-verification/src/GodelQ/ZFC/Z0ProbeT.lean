import GodelQ.ZFC.Z0Full

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0ProbeT

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

-- Probe: does tprovable_iff_provable accept a set-language quote?
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (ψ : SetTheorySentence) :
    𝗭𝗙𝗖.internalize V ⊢ ⌜(ψ : Sentence ℒₛₑₜ)⌝ ↔ Provable 𝗭𝗙𝗖 (⌜(ψ : Sentence ℒₛₑₜ)⌝ : V) :=
  tprovable_iff_provable (T := 𝗭𝗙𝗖)

end GodelQ.Z0ProbeT
