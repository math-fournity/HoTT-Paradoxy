import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeQV
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **Q1**：`qVec ?[^&0] = ?[^#0, ^&0]`（fvar 不动）。 -/
lemma qVec_one : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
  rw [show (1:V) = 0 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
    termBShift_fvar, termBShiftVec_nil]

/-- **Q2**：`qVec² ?[^&0] = ?[^#0, ^#1, ^&0]` —— 末分量是 `^&0`（`termBShift` 不动 fvar）。 -/
lemma qVec_two : (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) := by
  rw [Function.iterate_succ_apply', Function.iterate_one, qVec_one]
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^&0] : V) = (2:V) from by simp [len_adjoin, len_nil]; norm_num]
  rw [show (2:V) = 0 + 1 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
      (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
    termBShift_bvar, show (0:V) + 1 = 1 by norm_num,
    termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]

end GodelQ.ProbeQV
