-- CG-009: NEGATIVE RESULT — the naive term-level iVE/subst law is FALSE.
-- Documented to prevent repeated attempts (mine and 9276's).
import GodelQ.ZFC.ITShiftFull

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstCounter
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst ?[^&0]` replaces **bvar 0** of its argument. `eqAtom t = ^rel 2 cEqN [#0, t]`
    has its own bound variable at position 0, so `subst ?[^&0] (eqAtom ^&x)` becomes
    `^rel 2 cEqN [^&0, ^&x]` — NOT `eqAtom ^&x`. -/
lemma subst_eqAtom_fvar_neq (x : V) :
    subst ℒₛₑₜ ?[^&0] (eqAtom (^&x : V)) =
      (^rel 2 (↑cEqN) ((^&0 : V) ∷ (^&x : V) ∷ (0 : V)) : V) := by
  show subst ℒₛₑₜ ?[^&0] (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&x : V) ∷ (0 : V)))
      = ^rel 2 (↑cEqN) ((^&0 : V) ∷ (^&x : V) ∷ (0 : V))
  rw [substs_rel (by rw [cEqN]; exact codeIn_rel_quote _)
    (GodelQ.TranslateShiftCompat.isUTermVec_eqAtom_vec (^&x) (IsUTerm.fvar x))]
  congr 1
  rw [show (2 : V) = 1 + 1 by norm_num,
    termSubstVec_cons (IsUTerm.bvar (z := 0))
      (by simpa using (IsUTermVec.adjoin (L := ℒₛₑₜ) (n := (0 : V)) IsUTermVec.empty
        (IsUTerm.fvar x) : IsUTermVec ℒₛₑₜ (0 + 1) ((^&x : V) ∷ (0 : V))))]
  rw [show (1 : V) = 0 + 1 by norm_num,
    termSubstVec_cons (IsUTerm.fvar x) IsUTermVec.empty]
  rw [termSubst_bvar, termSubst_fvar, termSubstVec_nil]
  simp

/-- The LHS of the naive law at `t = ^&x` equals `eqAtom ^&x` (termSubst leaves fvars alone). -/
lemma naive_lhs (x : V) :
    iVE (0 : V) (termSubst ℒₒᵣ ?[^&0] (^&x : V)) = eqAtom (^&x : V) := by
  rw [termSubst_fvar, iVE_fvar]

/-- **The naive term-level law fails**: `iVE 0 (termSubst ?[^&0] ^&x) = eqAtom ^&x`
    but `subst ?[^&0] (iVE 1 ^&x) = ^rel 2 cEqN [^&0, ^&x]`. They differ because
    the substitution hits `eqAtom`'s own bound variable.
    **Consequence**: `hAll`'s remaining obligation is an *implication* (Σ1 range),
    not an equality — matching 9276's final position. -/
theorem naive_law_is_false_shape (x : V) :
    subst ℒₛₑₜ ?[^&0] (iVE (1 : V) (^&x : V)) =
      (^rel 2 (↑cEqN) ((^&0 : V) ∷ (^&x : V) ∷ (0 : V)) : V) := by
  rw [iVE_fvar]
  exact subst_eqAtom_fvar_neq x

end GodelQ.ITSubstCounter

#print axioms GodelQ.ITSubstCounter.subst_eqAtom_fvar_neq
#print axioms GodelQ.ITSubstCounter.naive_lhs
#print axioms GodelQ.ITSubstCounter.naive_law_is_false_shape
