import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 探针：`iT_rename` 的 `rel` 支 —— 逐项核对

仿 `shift_iTR`（`TranslateShiftCompat.lean:482`）。目标（`k = 0`）：
`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`，`p = ^rel 2 R ?[^#0,^#0]`。

先测最关键的**内层换名**：`subst (qVec ?[^&0]) (eqAtom ^#1) = eqAtom ^&0`。 -/

lemma qVec_single_fvar : qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) := by
  rw [qVec, show len (?[^&0] : V) = 1 from by simp]
  rw [show termBShiftVec ℒₛₑₜ 1 (?[^&0] : V) = (?[^&0] : V) from by
    rw [show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty, termBShift_fvar,
      termBShiftVec_nil]]

lemma subst_vec_two : termSubstVec ℒₛₑₜ 2 (?[^#0, ^&0] : V) (?[^#0, ^#1] : V)
    = (?[^#0, ^&0] : V) := by
  rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl,
    show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
    termSubst_bvar, termSubst_bvar]
  simp

-- 内层换名：`subst (qVec ?[^&0]) (eqAtom ^#1) = eqAtom ^&0`
lemma subst_qVec_eqAtom : subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (eqAtom (^#(1:V) : V))
    = eqAtom (^&(0:V) : V) := by
  have hv2 : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (z := (1:V))))
      (IsUTerm.bvar (z := (0:V)))
  rw [qVec_single_fvar, eqAtom, eqAtom]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (by simpa using hv2)]
  congr 1
  exact subst_vec_two

end GodelQ.ProbeRen3
