import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeSV
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `shiftVec` 与 `qVec` 的组合律

目标：`subst (^#0 ∷ shiftVec 2 0) X = subst W (subst (^#0 ∷ shiftVec 2 1) X)`，`W = ?[^#0,^#1,^&0]`。

先算 `shiftVec 2 n` 的形状。 -/

-- `shiftVec 2 0 = ?[^#1,^#2]`
example : shiftVec (V := V) 2 0 = (?[^#1, ^#2] : V) := by
  rw [show (2 : V) = 1 + 1 by norm_num, shiftVec_succ, shiftVec_succ, shiftVec_zero]
  rfl

-- `shiftVec 2 1 = ?[^#2,^#3]`
example : shiftVec (V := V) 2 1 = (?[^#2, ^#3] : V) := by
  rw [show (2 : V) = 1 + 1 by norm_num, shiftVec_succ, shiftVec_succ, shiftVec_zero]
  rfl

-- `qVec ?[^&0] = ?[^#0,^&1]`；`qVec² ?[^&0] = ?[^#0,^#1,^&0]`（已证）
-- 关键：`subst (qVec W) (subst (qVec W) X) = subst W (subst W X)`（幂等）

end GodelQ.ProbeSV
