/-
  Negative control for CG001-C-61 (expected KERNEL_REJECTED).
  proof id : MP-CG001-TERRA-MODELS-UIP-LEAN-NEG-001

  The stateful server of Terra's T2 model denies the second redemption of the
  same code.  Claiming by rfl that the second copy is granted must be
  rejected: the kernel computes `denied`, not `granted accessToken`.  This
  shows the transcription is checked, not merely parsed.
-/
import TerraModelsUIP

open CG001.TerraModelsUIP

theorem secondCopyAlsoGranted :
    secondAttempt.1 = Reply.granted Token.accessToken := rfl
