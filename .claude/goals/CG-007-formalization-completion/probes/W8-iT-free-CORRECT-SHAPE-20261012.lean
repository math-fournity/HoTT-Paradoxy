import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeWk
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 归一化看两侧：iT 0 (free p) 与 imp (subst ?[^&0] domZero) (free (iT 1 p))
example (p : V) (hpa : IsSemiformula ℒₒᵣ 1 p) :
    iT (0:V) (free ℒₒᵣ p) = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT (1:V) p)) := by
  simp only [iT, free, iVE_bvar, iVE_fvar, eqAtom, substs_rel, termSubstVec_cons₂,
    termSubst_bvar, termSubst_fvar, nth_adjoin_zero, nth_adjoin_one, free_imp_domZero]

end GodelQ.ProbeWk
