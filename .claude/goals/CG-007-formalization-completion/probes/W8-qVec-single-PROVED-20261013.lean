import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`qVec ?[t']` 的实际值**：`?[^#0, termShift t']`（长度 2）。

`qVec w = ^#0 ∷ termBShiftVec (len w) w`，而 `w = ?[t']` 长度 1，
故 `termBShiftVec 1 ?[t'] = ?[termBShift t']`——**`t'` 被 `termBShift` 加一**。 -/
lemma qVec_single (t' : V) (ht : IsUTerm ℒₛₑₜ t') :
    qVec ℒₛₑₜ (?[t'] : V) = ((^#0 : V) ∷ (termBShift ℒₛₑₜ t' ∷ (0:V))) := by
  rw [Bootstrapping.qVec, show len (?[t'] : V) = (1:V) from by simp]
  rw [show (1:V) = 0 + 1 by norm_num,
    termBShiftVec_cons ht IsUTermVec.empty, termBShiftVec_nil]

/-- **推论**：`(qVec ?[t']).[2] = 0`（越界补零）。 -/
lemma qVec_single_idx2 (t' : V) (ht : IsUTerm ℒₛₑₜ t') :
    (qVec ℒₛₑₜ (?[t'] : V)).[2] = (0:V) := by
  rw [qVec_single t' ht]
  rw [show ((^#0 : V) ∷ (termBShift ℒₛₑₜ t' ∷ (0:V))) = (^#0 : V) ∷ (termBShift ℒₛₑₜ t' ∷ (0:V)) from rfl]
  rw [show (2:V) = 1 + 1 by norm_num, nth_adjoin_succ]
  rw [show ((termBShift ℒₛₑₜ t' : V) ∷ (0:V)).[1] = (0:V).[0] from nth_adjoin_one _ _]
  rw [show (0:V).[0] = (0:V) from by rw [nth_zero]; simp [fstIdx, pi₁_zero]]

end GodelQ.ProbeFL
