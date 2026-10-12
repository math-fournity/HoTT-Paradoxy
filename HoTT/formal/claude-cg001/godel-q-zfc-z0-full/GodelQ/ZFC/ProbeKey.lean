import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeKey
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **决定性引理**：free (imp domZero (iT 1 p)) = iT 0 (free ℒₒᵣ p)
-- 若成立，hAll 的最后一步就是 exact ih'（完全不需要 weaken_imp / replace_of_imp）
-- 证法：free_imp_domZero + iT_free 的正确形状
example (p : V) (hpa : IsSemiformula ℒₒᵣ 1 p) :
    free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (1:V) p)) = iT (0:V) (free ℒₒᵣ p) := by
  rw [free_imp_domZero (V := V) (isSemiformula_iT (V := V) (n := (1:V)) p hpa)]
  -- 剩：imp (subst ?[^&0] domZero) (free (iT 1 p)) = iT 0 (free ℒₒᵣ p)
  sorry

end GodelQ.ProbeKey
