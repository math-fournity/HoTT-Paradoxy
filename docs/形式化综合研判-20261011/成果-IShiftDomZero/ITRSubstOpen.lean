-- CG-009: the atomic layer of the opening law — `iTR` under the opening substitution.
--
-- ## The shape of the problem
--
-- `iTR n 2 R v = qqAlls (imp ℒₛₑₜ (A₀ ⋏ (A₁ ⋏ ⊤)) (subst ℒₛₑₜ ?[^#0,^#1] (cRel R))) 2`
-- with `Aⱼ = conjunct 2 n j (iVE n v.[j])`.
--
-- The opening substitution `subst ℒₒᵣ (QvecVOr m) ·` at layer `m` acts on
-- `iTR m 2 R v`, i.e. on a code whose layer is `m`.  Pushing it inside the two
-- `qqAlls` binders uses `substs_all`/`substs_ex` twice, so the vector becomes
-- `qVec (qVec (QvecVOr m)) = QvecVOr (m + 2)` (length `m + 3`).
--
-- `QvecVOr (m+2) = [#0, #1, …, #(m+1), &0]`, so:
--   * index `i` for `i ≤ m+1` maps to `^#i` — the identity on bvars;
--   * index `m+2` maps to `^&0` — this is the slot that `iVE (m+2) ^#(m+2)` uses.
--
-- That is exactly why `iT (m+2)` of the shifted code equals `subst` of `iT (m+3)`:
-- the substitution is the identity on everything `iT` produces except the one
-- variable slot, where it correctly installs `^&0`.
import GodelQ.ZFC.ITSubstOpen

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITRSubstOpen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen

/-- `QvecVOr m`'s `i`-th entry for `i < m` is `^#i`. -/
lemma nth_QvecVOr_lt (m : V) : ∀ i < m, (QvecVOr (V := V) m).[i] = ^#i := by
  induction m using ISigma1.sigma1_succ_induction
  · definability
  case zero => intro i hi; exact absurd hi (by simp)
  case succ m ih =>
    intro i hi
    rw [QvecVOr_succ]
    rcases zero_or_succ i with rfl | ⟨j, rfl⟩
    · simp [qVec]
    · have hj : j < m := by simpa using hi
      have hj' : j < m + 1 := lt_of_lt_of_le hj (by
        rw [add_comm m 1]; exact le_add_self)
      rw [qVec, nth_adjoin_succ, len_QvecVOr,
        nth_termBShiftVec (isSemitermVec_QvecVOr m).isUTerm hj', ih j hj, termBShift_bvar]

/-- `QvecVOr m`'s last entry (index `m`) is `^&0`. -/
lemma nth_QvecVOr_last (m : V) : (QvecVOr (V := V) m).[m] = ^&0 := by
  induction m using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp [QvecVOr_zero]
  case succ m ih =>
    rw [QvecVOr_succ, qVec, nth_adjoin_succ, len_QvecVOr,
      nth_termBShiftVec (isSemitermVec_QvecVOr m).isUTerm (by simp), ih, termBShift_fvar]

end GodelQ.ITRSubstOpen

#print axioms GodelQ.ITRSubstOpen.nth_QvecVOr_lt
#print axioms GodelQ.ITRSubstOpen.nth_QvecVOr_last
