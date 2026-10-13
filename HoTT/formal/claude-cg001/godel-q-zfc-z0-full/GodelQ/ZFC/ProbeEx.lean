import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeEx
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- hExs：^∃ p ∈ s，子推导在 substs1 ℒᵣ t p ⫽ s（**没有 setShift！**）
-- Derivable.exs 要 Derivable (substs1 ℒₜ ??? (iT 1 p) ⫽ s)
-- ih 给的是 Derivable (translateSeq (fstIdx dd))
--      = Derivable (insert (iT 0 (substs1 ℒᵣ t p)) (translateSeq s))
--
-- 所以 hExs 的核心等式是：
--   iT 0 (substs1 ℒᵣ t p) = substs1 ℒₜ ?? (iT 1 p)
-- 注意：hExs 没有 free、没有 setShift、没有 shift！比 hAll 简单。

#check @iT_exs
#check @substs1
#check @iVE_subst_term
#check @iVE
end GodelQ.ProbeEx
