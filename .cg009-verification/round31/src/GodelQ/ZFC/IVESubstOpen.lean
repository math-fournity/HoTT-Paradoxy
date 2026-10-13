-- CG-009: the term-level core of the opening law.
--
-- `iVE n t = eqAtom (t with bvar z ↦ ^#(z+1), fvar x ↦ ^&x)`.
-- The opening substitution acts on the *terms* of the source language, so the
-- term-level statement is:
--     iVE (m+1) (termSubst ℒₒᵣ (QvecVOr m) t) = subst ℒₛₑₜ (QvecV (m+1)) (iVE (m+1) t)
-- for `t : IsSemiterm ℒₒᵣ (m+1) t`.
--
-- Mechanism: `iVE (m+1) ^#z = eqAtom ^#(z+1)`, and `QvecV (m+1)`'s entry at
-- index `z+1` is `^#(z+1)` for `z+1 < m+1` (i.e. `z < m`) — the identity — while at
-- `z+1 = m+1` (i.e. `z = m`) it is `^&0`, which is exactly what `termSubst` with
-- `QvecVOr m` puts there (since `QvecVOr m`'s last entry is `^&0`).
import GodelQ.ZFC.ITRSubstOpen

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVESubstOpen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.TranslateShiftCompat

end GodelQ.IVESubstOpen

namespace GodelQ.ITRSubstOpen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen

/-- `QvecV m`'s `i`-th entry for `i < m` is `^#i`. -/
lemma nth_QvecV_lt (m : V) : ∀ i < m, (QvecV (V := V) m).[i] = ^#i := by
  induction m using ISigma1.sigma1_succ_induction
  · definability
  case zero => intro i hi; exact absurd hi (by simp)
  case succ m ih =>
    intro i hi
    rw [QvecV_succ]
    rcases zero_or_succ i with rfl | ⟨j, rfl⟩
    · simp [qVec]
    · have hj : j < m := by simpa using hi
      have hj' : j < m + 1 := lt_of_lt_of_le hj (by rw [add_comm m 1]; exact le_add_self)
      rw [qVec, nth_adjoin_succ, len_QvecV,
        nth_termBShiftVec (isSemitermVec_QvecV m).isUTerm hj', ih j hj, termBShift_bvar]

/-- `QvecV m`'s last entry (index `m`) is `^&0`. -/
lemma nth_QvecV_last (m : V) : (QvecV (V := V) m).[m] = ^&0 := by
  induction m using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp [QvecV_zero]
  case succ m ih =>
    rw [QvecV_succ, qVec, nth_adjoin_succ, len_QvecV,
      nth_termBShiftVec (isSemitermVec_QvecV m).isUTerm (by simp), ih, termBShift_fvar]

end GodelQ.ITRSubstOpen

namespace GodelQ.IVESubstOpen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.TranslateShiftCompat

/-- `subst ℒₛₑₜ (QvecV (m+1))` applied to `eqAtom (^#z)` for `z < m`: identity,
    because `QvecV (m+1)`'s entry at index `z` is `^#z`. -/
lemma subst_QvecV_eqAtom_bvar_lt {m z : V} (hz : z < m + 1) :
    subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (eqAtom (^#z : V)) = eqAtom (^#z : V) := by
  show subst ℒₛₑₜ (QvecV (m+1)) (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V))
  rw [substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^#z) (IsUTerm.bvar (z := z)))]
  congr 1
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := z))]
  congr 1
  · rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) 0 (by simp)]
  · rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) z (by simpa using hz)]

/-- `subst ℒₛₑₜ (QvecV (m+1))` applied to `eqAtom (^#(m+1))` lands the `^&0`:
    `QvecV (m+1)`'s entry at index `m+1` is `^&0`. -/
lemma subst_QvecV_eqAtom_bvar_last (m : V) :
    subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (eqAtom (^#(m + 1) : V)) = eqAtom (^&0 : V) := by
  show subst ℒₛₑₜ (QvecV (m+1)) (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#(m+1) : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V))
  rw [substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^#(m+1)) (IsUTerm.bvar (z := m + 1)))]
  congr 1
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := m + 1))]
  congr 1
  · rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) 0 (by simp)]
  · rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_last (m + 1)]

end GodelQ.IVESubstOpen

#print axioms GodelQ.ITRSubstOpen.nth_QvecV_lt
#print axioms GodelQ.ITRSubstOpen.nth_QvecV_last
#print axioms GodelQ.IVESubstOpen.subst_QvecV_eqAtom_bvar_lt
#print axioms GodelQ.IVESubstOpen.subst_QvecV_eqAtom_bvar_last
