import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeH
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- `shiftVec 2 1 = ?[^#2]`
lemma shiftVec_2_1 : shiftVec (V := V) 2 1 = (?[^#2] : V) := by
  rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero]
  rfl

-- `shiftVec 2 0 = 0`
lemma shiftVec_2_0 : shiftVec (V := V) 2 0 = (0 : V) := shiftVec_zero 2

-- 关键：`subst (^#0 ∷ shiftVec 2 1) (iVE 1 ^#0) = ^rel 2 cEqN ?[^#0, ^#2]`
lemma keyL : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^#2] : V) : V) := by
  rw [iVE_bvar, eqAtom, shiftVec_2_1]
  rw [show ((^#(0:V) : V) ∷ (?[^#2] : V)) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) from rfl]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (2:V))))
      (IsUTerm.bvar (z := (0:V))))]
  congr 1
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
    termSubst_bvar, termSubst_bvar]
  rw [show (0 : V) + 1 = 1 by norm_num]
  rfl

-- 关键：`subst (^#0 ∷ shiftVec 2 0) (iVE 0 ^&0) = ^rel 2 cEqN ?[^#0, ^&0]`
lemma keyR : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  rw [iVE_fvar, eqAtom, shiftVec_2_0]
  rw [show ((^#(0:V) : V) ∷ (0 : V)) = (?[^#0] : V) from rfl]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))]
  congr 1
  rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.fvar (x := (0:V))),
    termSubst_bvar, termSubst_fvar]
  rfl

end GodelQ.ProbeH
