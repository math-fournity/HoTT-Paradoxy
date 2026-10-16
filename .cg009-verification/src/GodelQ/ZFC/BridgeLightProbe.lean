-- CG-009 isolation probe: only the lightest conditional theorem of the WorkBuddy
-- Z0CraigBridge (verbatim body, no cl_prover), to determine whether the timeout of
-- the full file comes from the cl_prover-heavy siblings.
import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full

namespace GodelQ.BridgeLightProbe

/-- WB-CG007-C-001 body, verbatim from Z0CraigBridge.lean (no cl_prover). -/
theorem hbl3_of_reverse_on_image
    (bridge : ∀ σ : ArithmeticSentence,
      𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr σ) 🡒 zfcTr (zfcTr σ)) :
    zfcTr.HBL3 := by
  refine ⟨fun {σ} ↦ ?_⟩
  have hc : 𝗜𝚺₁ ⊢ zfcTr σ 🡒 provabilityPred Sh.craig (zfcTr σ) :=
    provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 σ)
  exact C_trans hc (bridge σ)

end GodelQ.BridgeLightProbe

#print axioms GodelQ.BridgeLightProbe.hbl3_of_reverse_on_image
