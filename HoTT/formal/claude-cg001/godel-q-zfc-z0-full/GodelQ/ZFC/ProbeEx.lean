import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeEx
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 先算 termSubst ?[^&0] ^#0 —— 用 termSubst_bvar + nth
example : termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V) = (^&(0:V) : V) := by
  rw [termSubst_bvar, nth_cons_zero]
  rfl

-- 连带：iVE 0 (termSubst ?[^&0] ^#0) = eqAtom ^&0
example : iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V))
    = eqAtom (^&(0:V) : V) := by
  rw [show termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V) = (^&(0:V) : V) from by
    rw [termSubst_bvar, nth_cons_zero]]
  rfl

end GodelQ.ProbeEx
