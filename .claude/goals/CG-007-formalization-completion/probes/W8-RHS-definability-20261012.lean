import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeRHS
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- RHS 作为 (param, q) 的 Σ1 函数
example : 𝚺ᴬ₁-Function₂ (fun param q : V =>
    imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ param q))) := by
  definability

end GodelQ.ProbeRHS
