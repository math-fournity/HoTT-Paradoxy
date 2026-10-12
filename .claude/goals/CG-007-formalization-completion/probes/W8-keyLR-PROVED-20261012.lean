import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeJ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma shiftVec_2_1 : shiftVec (V := V) 2 1 = (?[^#2] : V) := by
  rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero, termBShiftVec_nil]

lemma shiftVec_2_0 : shiftVec (V := V) 2 0 = (0 : V) := shiftVec_zero 2

-- **keyL**：`subst (^#0 ∷ shiftVec 2 1) (iVE 1 ^#0) = ^rel 2 cEqN ?[^#0, ^#2]`
lemma keyL : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^#2] : V) : V) := by
  rw [iVE_bvar, eqAtom, shiftVec_2_1]
  rw [show ((^#(0:V) : V) ∷ (?[^#2] : V)) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) from rfl]
  rw [show (0 : V) + 1 = 1 by norm_num]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  have hR1 : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]
    exact codeIn_rel_quote _
  have hv1 : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V))
        (IsUTerm.bvar (L := ℒₛₑₜ) (z := (1:V))))
      (IsUTerm.bvar (L := ℒₛₑₜ) (z := (0:V)))
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (k := (0 + 1 + 1 : V))
    (v := ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))))
    hR1 hv1]
  congr 1
  rw [termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (1:V)))),
      termSubstVec_cons (IsUTerm.bvar (z := (1:V))) IsUTermVec.empty,
      termSubstVec_nil, termSubst_bvar, termSubst_bvar]
  simp only [nth_adjoin_zero, nth_adjoin_one]

-- **keyR**：`subst (^#0 ∷ shiftVec 2 0) (iVE 0 ^&0) = ^rel 2 cEqN ?[^#0, ^&0]`
lemma keyR : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  rw [iVE_fvar, eqAtom, shiftVec_2_0]
  rw [show ((^#(0:V) : V) ∷ (0 : V)) = (?[^#0] : V) from rfl]
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  have hR2 : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]
    exact codeIn_rel_quote _
  have hv2 : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V))
        (IsUTerm.fvar (L := ℒₛₑₜ) (x := (0:V))))
      (IsUTerm.bvar (L := ℒₛₑₜ) (z := (0:V)))
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (k := (0 + 1 + 1 : V))
    (v := ((^#(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V))))
    hR2 hv2]
  congr 1
  rw [termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
      termSubstVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termSubstVec_nil, termSubst_bvar, termSubst_fvar]
  simp only [nth_adjoin_zero, nth_adjoin_one]

end GodelQ.ProbeJ
