-- CG-009: the `iVE`-level opening law (bvar / bvar-last / fvar branches).
import GodelQ.ZFC.IVESubstOpen

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVESubstOpen2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.TranslateShiftCompat

/-- `subst ℒₛₑₜ (QvecV (m+1))` fixes `eqAtom ^&x` (fvars are untouched). -/
lemma subst_QvecV_eqAtom_fvar (m x : V) :
    subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (eqAtom (^&x : V)) = eqAtom (^&x : V) := by
  show subst ℒₛₑₜ (QvecV (m+1)) (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&x : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&x : V) ∷ (0 : V))
  rw [substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^&x) (IsUTerm.fvar x))]
  congr 1
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.fvar x)]
  congr 1
  · rw [termSubst_bvar, nth_QvecV_lt (m + 1) 0 (by simp)]
  · rw [termSubst_fvar]

/-- **bvar branch** (`z < m`): the opening vector is the identity on this slot. -/
lemma iVE_open_bvar_lt {m z : V} (hz : z < m) :
    iVE (m + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) m) (^#z : V)) =
      subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (iVE (m + 1) (^#z : V)) := by
  rw [termSubst_bvar, nth_QvecVOr_lt m z hz, iVE_bvar]
  exact (subst_QvecV_eqAtom_bvar_lt (m := m) (z := z + 1) (by
    have h := add_lt_add_right hz 1
    have e : z + 1 = z + 1 := rfl
    simpa [add_assoc] using h)).symm

/-- **bvar branch, last slot** (`z = m`): here the opening actually happens. -/
lemma iVE_open_bvar_last (m : V) :
    iVE (m + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) m) (^#m : V)) =
      subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (iVE (m + 1) (^#m : V)) := by
  rw [termSubst_bvar, nth_QvecVOr_last m, iVE_bvar]
  simp only [iVE_fvar]
  exact (subst_QvecV_eqAtom_bvar_last (m := m)).symm

/-- **fvar branch**: fvars are untouched by both `termSubst` and the opening vector. -/
lemma iVE_open_fvar (m x : V) :
    iVE (m + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) m) (^&x : V)) =
      subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (iVE (m + 1) (^&x : V)) := by
  rw [termSubst_fvar, iVE_fvar]
  exact (subst_QvecV_eqAtom_fvar m x).symm

end GodelQ.IVESubstOpen2

#print axioms GodelQ.IVESubstOpen2.subst_QvecV_eqAtom_fvar
#print axioms GodelQ.IVESubstOpen2.iVE_open_bvar_lt
#print axioms GodelQ.IVESubstOpen2.iVE_open_bvar_last
#print axioms GodelQ.IVESubstOpen2.iVE_open_fvar
