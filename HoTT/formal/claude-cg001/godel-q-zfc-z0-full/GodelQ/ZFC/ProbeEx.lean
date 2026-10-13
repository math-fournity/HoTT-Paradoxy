import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeEx
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 先算 termSubst ?[^&0] ^#0
example : termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V) = (^&(0:V) : V) := by
  rw [show ((?[^&0] : V) = ((^&(0:V) : V) ∷ (0:V))) from rfl,
    show ((^#(0:V) : V) = ((^#(0:V) : V) ∷ 0)) from rfl,
    show (0:V) = ((0:ℕ):V) by norm_num,
    termSubstVec_cons₂ (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
    termSubstVec_nil, termSubst_fvar, termSubst_bvar]
  rfl

end GodelQ.ProbeEx
