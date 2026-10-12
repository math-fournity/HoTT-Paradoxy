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
