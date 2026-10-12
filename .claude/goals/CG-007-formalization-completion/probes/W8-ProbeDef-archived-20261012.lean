import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 2000000
namespace GodelQ.ProbeDef
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- DefinableRel₄ 能不能合成？先测最小例子
example : 𝚺ᴬ₁-Predicate fun p : V ↦
    iT (0:V) (free ℒₒᵣ p) = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT (1:V) p)) := by
  definability

end GodelQ.ProbeDef
