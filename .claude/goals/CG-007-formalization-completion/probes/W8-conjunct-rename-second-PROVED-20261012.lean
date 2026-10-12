import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeA6
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma lt_two_cases {i : V} (hi : i < 2) : i = 0 ∨ i = 1 := by
  have h : i < 1 + 1 := by norm_num at hi ⊢; exact hi
  rcases lt_succ_iff_eq_or_succ.mp h with h1 | h1
  · exact Or.inr h1
  · exact Or.inl (lt_one_iff_eq_zero.mp h1)

/-- **第二分量**：`subst W (subst (^#i ∷ ?[^#2]) (iVE 1 ^#0)) = subst (^#i ∷ 0) (iVE 0 ^&0)`。

左内层给 `^rel 2 cEqN ?[^#i, ^#2]`，外层 W 把 `#2 ↦ ^&0`；
右给 `^rel 2 cEqN ?[^#i, ^&0]`。两侧相等。 -/
lemma conjunct_rename_second {i : V} (hi : i < 2) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V)))
      = subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&0 : V)) := by
  have hR : (ℒₛₑₜ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  -- 左内层
  have hL : subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#0 : V))
      = (^rel 2 (↑cEqN) (?[^#i, ^#2] : V) : V) := by
    rw [show shiftVec (V := V) 2 1 = (?[^#2] : V) from by
      rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero, termBShiftVec_nil]]
    rw [iVE_bvar, eqAtom, show (^#(0+1) : V) = (^#1 : V) by norm_num]
    rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
    rw [show (^#i ∷ (?[^#2] : V) : V) = (^#i : V) ∷ ((^#2 : V) ∷ (0 : V)) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (1:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (^#i ∷ (^#2 : V) ∷ (0:V) : V) = (?[^#i, ^#2] : V) from rfl,
      show (^#0 ∷ (^#1 : V) ∷ (0:V) : V) = (?[^#0, ^#1] : V) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
      termSubst_bvar, termSubst_bvar]
    simp
  -- 右
  have hRr : subst ℒₛₑₜ (^#i ∷ shiftVec (V := V) 2 0) (iVE (0:V) (^&0 : V))
      = (^rel 2 (↑cEqN) (?[^#i, ^&0] : V) : V) := by
    rw [show shiftVec (V := V) 2 0 = (0 : V) from shiftVec_zero 2]
    rw [iVE_fvar, eqAtom]
    rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl]
    rw [show (^#i ∷ (0:V) : V) = (^#i : V) ∷ (0 : V) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.fvar (x := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (2:V) = 0 + 1 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
      termSubstVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty, termSubstVec_nil,
      termSubst_bvar, termSubst_fvar]
    simp
  -- 左外层
  have hout : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (^rel 2 (↑cEqN) (?[^#i, ^#2] : V))
      = (^rel 2 (↑cEqN) (?[^#i, ^&0] : V) : V) := by
    rw [show (?[^#i, ^#2] : V) = (^#i : V) ∷ ((^#2 : V) ∷ (0 : V)) from rfl]
    rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (2:V)))) (IsUTerm.bvar (z := (0:V)))))]
    congr 1
    rw [show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V))) from rfl]
    rw [show (^#i ∷ (^#2 : V) ∷ (0:V) : V) = (?[^#i, ^#2] : V) from rfl,
      show (^#0 ∷ (^#1 : V) ∷ ((^&0 : V) ∷ (0:V)) : V) = (?[^#0, ^#1, ^&0] : V) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := (2:V))),
      termSubst_bvar, termSubst_bvar]
    rw [show (^#i ∷ (^&0 : V) ∷ (0:V) : V) = (?[^#i, ^&0] : V) from rfl]
    rcases lt_two_cases hi with rfl | rfl <;> simp
  rw [hL, hout, hRr]

end GodelQ.ProbeA6
