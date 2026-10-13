import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `qVec ?[^&0] = ?[^#0, ^&0]`（长度 2）——已在探针里证过。 -/
lemma qVec_one : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
  rw [show (1:V) = 0 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
    termBShift_fvar, termBShiftVec_nil]

/-- **`(qVec)^[2] ?[^&0] = ?[^#0, ^#1, ^#2, ^&0]`**（长度 4，与 `conjunct 2 2 _ _` 的层数 4 同步）。

由 `qVec_one` 起算：`qVec ?[^#0,^&0] = ?[^#0, ^#1, ^&0]`（bvar 加一、fvar 不动），
再 `qVec ?[^#0,^#1,^&0] = ?[^#0, ^#1, ^#2, ^&0]`。 -/
lemma qVec_two_v : (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^#2, ^&0] : V) := by
  rw [Function.iterate_succ_apply', Function.iterate_one, qVec_one]
  -- `qVec ?[^#0,^&0] = ?[^#0, ^#1, ^&0]`（用 cons₂：向量恰是字面二元组）
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^&0] : V) = (2:V) from by simp [len_adjoin, len_nil]; norm_num]
  rw [termBShiftVec_cons₂ (L := ℒₛₑₜ) (V := V)
      ((IsUTerm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num))
      (IsUTerm.fvar (L := ℒₛₑₜ) (V := V) (0:V))]
  rw [termBShift_bvar, termBShift_fvar]
  -- 现在 `qVec ?[^#0,^#1,^&0]`（长度 3）：用 tBV 的 cons 链
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^#1, ^&0] : V) = (3:V) from by simp [len_adjoin, len_nil]; norm_num]
  rw [show (3:V) = (1 + 1) + 1 by norm_num]
  rw [termBShiftVec_cons (L := ℒₛₑₜ) (V := V)
      ((IsUTerm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (0:V))).mpr (by norm_num))
      (IsUTermVec.adjoin (L := ℒₛₑₜ) (V := V) (n := (1:V)) (w := ((^&0 : V) ∷ (0:V)))
        (IsUTermVec.adjoin (L := ℒₛₑₜ) (V := V) (n := (0:V)) (w := (0:V))
          (IsUTermVec.empty (L := ℒₛₑₜ) (V := V) (1:V))
          (IsUTerm.fvar (L := ℒₛₑₜ) (V := V) (0:V)))
        ((IsUTerm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (1:V))).mpr (by norm_num)))]
  rw [termBShift_bvar]
  rw [show (1 + 1 : V) = (0 + 1) + 1 by norm_num]
  rw [termBShiftVec_cons (L := ℒₛₑₜ) (V := V)
      ((IsUTerm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (1:V))).mpr (by norm_num))
      (IsUTermVec.adjoin (L := ℒₛₑₜ) (V := V) (n := (0:V)) (w := (0:V))
        (IsUTermVec.empty (L := ℒₛₑₜ) (V := V) (1:V))
        (IsUTerm.fvar (L := ℒₛₑₜ) (V := V) (0:V)))]
  rw [termBShift_bvar]
  rw [show (0 + 1 : V) = 0 + 1 from rfl,
    termBShiftVec_cons (L := ℒₛₑₜ) (V := V) (IsUTerm.fvar (L := ℒₛₑₜ) (V := V) (0:V))
      (IsUTermVec.empty (L := ℒₛₑₜ) (V := V) (1:V)),
    termBShift_fvar, termBShiftVec_nil]

end GodelQ.ProbeFL
