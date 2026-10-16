import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.Z0Probe3

/-- Carrier-consistent D3 route via `tprovable_iff_provable` + the `zfcTr_D3_standard` body. -/
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  have hmeta : 𝗭𝗙𝗖 ⊢ ⌜arithTrln.translate τ⌝ :=
    (tprovable_iff_provable (T := 𝗭𝗙𝗖)).mp h |>.toDerivable
  have hmeta2 : 𝗭𝗙𝗖 ⊢ ⌜arithTrln.translate (zfcTr τ)⌝ :=
    (Sh_provable_iff (zfcTr τ)).mp
      (WeakerThan.pbl (zfcTr.D1 ((Sh_provable_iff τ).mpr hmeta)))
  exact internalize_provability (V := V) hmeta2

end GodelQ.Z0Probe3
