import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeQ2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **结论**：`(qVec)^[2] ?[^&0] = ?[^#0, ^#1, ^&0]`（末分量确实是 ^&0）
example : (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) := by
  show (qVec ℒₛₑₜ)^[1 + 1] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V)
  rw [Function.iterate_succ_apply', Function.iterate_one]
  rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
    rw [qVec, show len (?[^&0] : V) = 1 from by simp,
      termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]]
  rw [qVec, show len (?[^#0, ^&0] : V) = 2 from by rw [len_adjoin, len_adjoin, len_nil]; rfl,
    show (2 : V) = 0 + 1 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
      (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
    termBShift_bvar, show (0 : V) + 1 = 1 by norm_num,
    termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]

end GodelQ.ProbeQ2
