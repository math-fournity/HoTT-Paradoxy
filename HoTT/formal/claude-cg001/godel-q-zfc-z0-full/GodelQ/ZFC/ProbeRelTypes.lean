import GodelQ.ZFC.TranslateShiftCompat
import GodelQ.ZFC.SubstITR

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
set_option maxHeartbeats 4000000

namespace GodelQ.ProbeRelTypes
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 读清所有相关引理的**完整类型**（含隐式参数）
#check @IsSemitermVec.termSubstVec
#check @iT_rel
#check @substs_rel
#check @isSemiformula_iVE
#check @isSemiformula_conjunct
#check @iTR
#check @Bootstrapping.termSubstVec
#check @iVE_subst_a0

end GodelQ.ProbeRelTypes
