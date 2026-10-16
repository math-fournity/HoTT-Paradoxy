-- CG-009 P1-1 probe: cl_prover-free rewrite of dev-bd4295b5's
-- zfc_z0_full_of_reverse_at_bottom_s2 ("a reverse bridge at bottom suffices for the final Z0").
-- Structure and hypotheses verbatim from Z0CraigBridge.lean; the two cl_prover calls are
-- replaced by explicit modus ponens (K_right / contra).
import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full

namespace GodelQ.BottomStage2

theorem zfc_z0_full_of_reverse_at_bottom_s2
    (bridge : 𝗜𝚺₁ ⊢ provabilityPred Sh.craig (⊥ : ArithmeticSentence) 🡒 zfcTr ⊥) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  intro h
  have hz : Sh ⊢ (𝗭𝗙𝗖.consistent : ArithmeticSentence) := (Sh_provable_iff _).mpr h
  have he : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    WeakerThan.pbl zfcTr_con_iff
  have hp : Sh ⊢ zfcTr.con := K_right he ⨀ hz
  have hb : Sh ⊢ provabilityPred Sh.craig (⊥ : ArithmeticSentence) 🡒 zfcTr ⊥ :=
    WeakerThan.pbl bridge
  have hc : Sh ⊢ Sh.craig.consistent.val := by
    exact contra hb ⨀ hp
  exact craig_consistent_unprovable_of_RE Sh hc

end GodelQ.BottomStage2

#print axioms GodelQ.BottomStage2.zfc_z0_full_of_reverse_at_bottom_s2
