import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open FFL.FirstOrder.Arithmetic.R0

namespace GodelQ.Z0Probe5

/-- Internalized D3: `zfcTr τ → zfcTr (zfcTr τ)` as a meta ZFC theorem,
via the arithmetic `provable_D3` lifted through `arithInterp`, mirroring
`zfcTr_D3_standard`. Then re-internalize at V. -/
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  have hm : 𝗭𝗙𝗖 ⊢ arithTrln.translate τ :=
    (TProvable.iff_provable (T := 𝗭𝗙𝗖)).mp h
  exact h

end GodelQ.Z0Probe5
