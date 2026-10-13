import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsCore
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 义务 ③ 攻坚：LHS 完全展开到 `iTR` 层

卡点：`substs_rel` 之后要对**代入后的向量**再给 `iT_rel`，
所以需要 `IsUTermVec ℒᵣ 2 (termSubstVec ℒᵣ 2 ?[^&0] v)`。
用 `termSubstVec_isUTermVec` 型引理（若存在），否则由 `hv` 构造。 -/

#check @termSubstVec_isUTermVec
#check @Bootstrapping.termSubstVec_isUTermVec
#check @termSubstVec

end GodelQ.ProbeExsCore
