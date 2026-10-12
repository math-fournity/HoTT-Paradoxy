-- CG-009: the `conjunct` piece of the func branch.
--
-- ## Which layer acts here
--
-- `A_i = conjunct 3 n i y_i` sits inside `ve2`'s `qqAlls … 2`, so a `subst`
-- arriving from outside carries
--     qVec²(QvecV n) = QvecV (n+3)          (two `QvecV_succ` steps)
-- of length `n+4`.
--
-- `A_i`'s own substitution vector is `W_i := ^#i ∷ shiftVec 3 n`
-- (length `n+1`, layer `3+n`), whose entries read only indices
--     {i} ∪ {3, 4, …, n+2}
-- and `QvecV (n+3)` is the identity on all of them (`i ≤ 2 < n+3`, `n+2 < n+3`).
-- Hence both components of `conjunct` are fixed by the outer `subst`.
import GodelQ.ZFC.IVEOpenFunc10

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc11
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10

/-- `n + 2 < n + 3`. -/
lemma lt_add_two_three (n : V) : n + 2 < n + 3 := by
  have h := lt_add_self_add_one (n + 2) 0
  have e : (0 : V) + (n + 2) + 1 = n + 3 := by ring
  rwa [e] at h

/-- **Component ①**: `QvecV (n+3)` fixes the domain part's vector `?[^#i]` for `i < n+3`. -/
lemma termSubstVec_one_QvecV_three {n i : V} (hi : i < n + 3) :
    termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (n + 3)) (?[^#i] : V) = (?[^#i] : V) := by
  rw [termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar,
    nth_QvecV_lt (n + 3) i hi]

end GodelQ.IVEOpenFunc11

#print axioms GodelQ.IVEOpenFunc11.termSubstVec_one_QvecV_three

namespace GodelQ.IVEOpenFunc11
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10

/-- `3 + j < n + 3` when `j < n`. -/
lemma lt_three_add_three {n j : V} (hj : j < n) : 3 + j < n + 3 := by
  have h : 3 + j < 3 + n := add_lt_add_right hj 3
  have e : 3 + n = n + 3 := by ring
  rwa [e] at h

/-- `len (shiftVec 3 n) = n`. -/
lemma len_shiftVec_three (n : V) : len (shiftVec 3 n) = n := by
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp [shiftVec_zero]
  case succ n ih =>
    rw [shiftVec_succ, len_adjoin,
      len_termBShiftVec (isSemitermVec_shiftVec_V 3 n).isUTerm]

/-- **Component ②**: `QvecV (n+3)` fixes `^#i ∷ shiftVec 3 n` for `i < n+3`. -/
lemma termSubstVec_cons_QvecV_three {n i : V} (hi : i < n + 3) :
    termSubstVec ℒₛₑₜ (n + 1) (QvecV (V := V) (n + 3))
        ((^#i : V) ∷ shiftVec 3 n) =
      ((^#i : V) ∷ shiftVec 3 n) := by
  have hb : (i : V) < 3 + n := by
    have e : (n : V) + 3 = 3 + n := by ring
    rwa [e] at hi
  have hsemi : IsSemitermVec ℒₛₑₜ (n + 1) (3 + n) ((^#i : V) ∷ shiftVec 3 n) :=
    isSemitermVec_shiftVec_cons hb
  have hv : IsUTermVec ℒₛₑₜ n (shiftVec 3 n) := (isSemitermVec_shiftVec_V 3 n).isUTerm
  have hib : IsUTerm ℒₛₑₜ (^#i : V) := IsUTerm.bvar
  rw [termSubstVec_cons hib hv]
  congr 1
  · rw [termSubst_bvar, nth_QvecV_lt (n + 3) i hi]
  · -- `termSubstVec n (QvecV (n+3)) (shiftVec 3 n) = shiftVec 3 n`
    have hlen1 : len (shiftVec 3 n) = n := len_shiftVec_three n
    have hlen2 : len (termSubstVec ℒₛₑₜ n (QvecV (V := V) (n + 3)) (shiftVec 3 n)) = n := by
      rw [len_termSubstVec (hts := hv)]
    refine nth_ext' n hlen2 hlen1 ?_
    intro j hj
    have hj3' : (3 + j) < (n + 3 : V) + 1 := by
      have h1 : (3 + j) < (3 + n : V) + 1 := lt_of_lt_of_le
        (add_lt_add_right hj 3) (le_of_lt (lt_add_one (3 + n)))
      have e : (3 + n : V) + 1 = (n + 3 : V) + 1 := by ring
      exact e ▸ h1
    have hnth : (termSubstVec ℒₛₑₜ n (QvecV (V := V) (n + 3)) (shiftVec 3 n)).[j]
        = termSubst ℒₛₑₜ (QvecV (V := V) (n + 3)) (shiftVec 3 n).[j] :=
      nth_termSubstVec (L := ℒₛₑₜ) (k := n) (ts := shiftVec 3 n) hv hj
    rw [hnth, nth_shiftVec 3 n j hj, termSubst_bvar,
      nth_QvecV_lt (n + 3) (3 + j) (lt_three_add_three hj)]

end GodelQ.IVEOpenFunc11

#print axioms GodelQ.IVEOpenFunc11.termSubstVec_cons_QvecV_three
