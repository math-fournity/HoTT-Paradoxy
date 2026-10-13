import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeQName

#check @IsUTermVec.termSubst
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.termSubst
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.termSubstVec

end GodelQ.ProbeQName