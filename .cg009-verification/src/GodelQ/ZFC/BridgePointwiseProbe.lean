-- CG-009 P1-1 probe: cl_prover-free rewrite of dev-bd4295b5's
-- hbl3_of_pointwise_equivalence. The original body is `cl_prover [keyE (zfcTr σ)]`;
-- here we build the needed implication explicitly:
--   keyE (zfcTr σ) : 𝗜𝚺₁ ⊢ zfcTr (zfcTr σ) 🡘 provabilityPred Sh.craig (zfcTr σ)
-- The bridge wants: provabilityPred Sh.craig (zfcTr σ) 🡒 zfcTr (zfcTr σ), i.e. K_left of the iff.
import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full

namespace GodelQ.BridgePointwiseProbe

theorem hbl3_of_reverse_on_image
    (bridge : ∀ σ : ArithmeticSentence,
      𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr σ) 🡒 zfcTr (zfcTr σ)) :
    zfcTr.HBL3 := by
  refine ⟨fun {σ} ↦ ?_⟩
  have hc : 𝗜𝚺₁ ⊢ zfcTr σ 🡒 provabilityPred Sh.craig (zfcTr σ) :=
    provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 σ)
  exact C_trans hc (bridge σ)

theorem hbl3_of_pointwise_equivalence
    (keyE : ∀ σ : ArithmeticSentence,
      𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ) : zfcTr.HBL3 := by
  apply hbl3_of_reverse_on_image
  intro σ
  exact K_right (keyE (zfcTr σ))

end GodelQ.BridgePointwiseProbe

#print axioms GodelQ.BridgePointwiseProbe.hbl3_of_pointwise_equivalence
