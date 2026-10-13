-- CG-009: substitution versions of the cDomN/conjunct/cFunc pieces.
import GodelQ.ZFC.IVEOpenFunc6

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc8
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6

/-- `QvecV (mm+2)`'s entry `i` is `^#i` for `i < mm+2`. -/
lemma nth_QvecV_two_lt {mm i : V} (hi : i < mm + 2) :
    (QvecV (V := V) (mm + 2)).[i] = ^#i :=
  nth_QvecV_lt (mm + 2) i hi

/-- `termSubstVec ℒₛₑₜ 1 (QvecV (mm+2)) ?[^#i] = ?[^#i]` for `i < mm+2`. -/
lemma termSubstVec_one_QvecV_single {mm i : V} (hi : i < mm + 2) :
    termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (mm + 2)) (?[^#i] : V) = (?[^#i] : V) := by
  rw [show (?[^#i] : V) = (^#i : V) ∷ (0 : V) from rfl]
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := i))]
  rw [termSubst_bvar, nth_QvecV_two_lt hi]

end GodelQ.IVEOpenFunc8

#print axioms GodelQ.IVEOpenFunc8.termSubstVec_one_QvecV_single

namespace GodelQ.IVEOpenFunc8
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6

/-- **The `cDomN` piece**: `QvecV (mm+2)` fixes `subst ℒₛₑₜ ?[^#i] cDomN` for `i < mm+2`. -/
lemma subst_QvecV_cDomN_subst {mm i : V} (hi : i < mm + 2) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 2)) (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V)) =
      subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V) := by
  have hQ : IsSemitermVec ℒₛₑₜ (mm + 3) (mm + 3) (QvecV (V := V) (mm + 2)) := by
    have h := isSemitermVec_QvecV (V := V) (mm + 2)
    have e : (mm + 2 : V) + 1 = mm + 3 := by ring
    rwa [e] at h
  have hw : IsSemitermVec ℒₛₑₜ 1 (mm + 3) (?[^#i] : V) :=
    isSemitermVec_single_bvar (n := mm + 3) (by
      have hlt : (mm + 2 : V) < (mm + 2) + 1 := lt_add_one (mm + 2)
      have h2 : i < (mm + 2) + 1 := lt_trans hi hlt
      have e : (mm + 2 : V) + 1 = mm + 3 := by ring
      rwa [e] at h2)
  rw [show subst ℒₛₑₜ (QvecV (V := V) (mm + 2))
        (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (mm + 2)) (?[^#i] : V))
        ((cDomN : ℕ) : V) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) (n := mm + 3) (m := mm + 3)
      (p := ((cDomN : ℕ) : V)) isSemiformula_cDomN hQ hw]
  rw [termSubstVec_one_QvecV_single hi]

end GodelQ.IVEOpenFunc8

#print axioms GodelQ.IVEOpenFunc8.subst_QvecV_cDomN_subst
