-- CG-009: the opening vector's basic facts (verified), plus the *statement* of the
-- opening law and the reduction of hAB to it.
--
-- ## What hAll needs
--
-- `hAll_uncond` (in `HAllProof.lean`) has one remaining premise `hAB`, which via
-- `HABKey` reduces to the code identity
--     iT 0 (free ℒₒᵣ p) = subst ℒₛₑₜ ?[^&0] (iT 1 (shift ℒₒᵣ p))          (p : IsSemiformula ℒₒᵣ 1 p)
-- (`free_imp_domZero` turns `B` into `imp (subst ?[^&0] domZero) (free (iT 1 p))`, and
-- `iT_shift` turns `free (iT 1 p)` into `subst ?[^&0] (iT 1 (shift p))`; then `A → B`
-- is the propositional tautology `A → (C → A)`).
--
-- ## The general law
--
-- The identity is the `m = 0` instance of
--     iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m + 1) q)   (q : IsSemiformula ℒₒᵣ (m+1) q)
-- where `QvecVOr m = QvecV m = [#0, #1, …, #(m-1), &0]` (length `m+1`) — the `qVec`
-- iterated `m` times on `?[^&0]`.
--
-- **Why it is TRUE** (the qVec mechanism): `subst` descends under a binder by
-- replacing its vector `W` with `qVec W = ^#0 ∷ termBShiftVec W`, i.e. it prepends a
-- fresh `^#0` and bumps every index by one.  Inside `iTR`'s two `qqAlls` binders the
-- opening vector has therefore grown to `[#0, …, #(m+1), &0]`, and `iVE` places the
-- source variable `z` at index `z+1` — so the substitution lands exactly on the
-- variable slot and misses `eqAtom`'s own value slot at index 0.  (The naive
-- "`iT` commutes with `subst` at the same index" form is FALSE; the machine-checked
-- counterexample is `ITSubstCounter.naive_law_is_false_shape`.)
--
-- ## The two remaining inductions
--
-- (A) `IsSemiformula ℒₒᵣ m (subst ℒₒᵣ (QvecVOr m) q)` for `q` at layer `m+1`.
--     True because every entry of `QvecVOr m` has bvar `< m`, so the substituted
--     code again has bvars `< m`; needed to make `iT m` applicable.
-- (B) The law itself, by `UformulaRec1.Construction.semiformula_result_induction`
--     on `q`.  The `all` branch needs the pivot `subst ℒₛₑₜ (QvecV (m+1)) domZero = domZero`
--     (already proven as `ShiftDomZeroProbe.shift_domZero`'s `subst` analogue — see
--     `TranslateShiftCompat.shift_imp_domZero` for the `shift` version), because
--     `subst (QvecV (m+1))` fixes `domZero`'s own free bvar `#0` at index 0.
import GodelQ.ZFC.QvecV

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

open GodelQ.QvecVDefs

/-- `QvecVOr m` is a SemitermVec over `ℒₒᵣ` of length `m+1` at layer `m+1`. -/
lemma isSemitermVec_QvecVOr : ∀ m : V,
    IsSemitermVec ℒₒᵣ (m + 1) (m + 1) (QvecVOr (V := V) m) := by
  intro m
  induction m using ISigma1.sigma1_succ_induction
  · definability
  case zero =>
    rw [QvecVOr_zero]
    simpa using (IsSemitermVec.singleton (L := ℒₒᵣ) (n := (1 : V))).mpr
      (IsSemiterm.fvar (L := ℒₒᵣ) (1 : V) 0)
  case succ m ih =>
    rw [QvecVOr_succ]
    exact ih.qVec

/-- `QvecV m` is a SemitermVec over `ℒₛₑₜ` of length `m+1` at layer `m+1`. -/
lemma isSemitermVec_QvecV : ∀ m : V,
    IsSemitermVec ℒₛₑₜ (m + 1) (m + 1) (QvecV (V := V) m) := by
  intro m
  induction m using ISigma1.sigma1_succ_induction
  · definability
  case zero =>
    rw [QvecV_zero]
    simpa using (IsSemitermVec.singleton (L := ℒₛₑₜ) (n := (1 : V))).mpr
      (IsSemiterm.fvar (L := ℒₛₑₜ) (1 : V) 0)
  case succ m ih =>
    rw [QvecV_succ]
    exact ih.qVec

lemma len_QvecVOr (m : V) : len (QvecVOr (V := V) m) = m + 1 :=
  (isSemitermVec_QvecVOr m).lh

lemma len_QvecV (m : V) : len (QvecV (V := V) m) = m + 1 :=
  (isSemitermVec_QvecV m).lh

end GodelQ.ITSubstOpen

#print axioms GodelQ.ITSubstOpen.isSemitermVec_QvecVOr
#print axioms GodelQ.ITSubstOpen.isSemitermVec_QvecV
