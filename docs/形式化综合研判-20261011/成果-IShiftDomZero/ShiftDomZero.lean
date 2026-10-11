-- CG-009 round 31: shift fixes domZero — the pivot for ishift's quantifier branches.
-- Route: Semisentence L n = Semiformula L Empty n has no free variables;
-- Rewriting.shift only bumps fvars, so it is identity on the quote of an emb'd sentence.
import GodelQ.ZFC.GateBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ShiftDomZeroProbe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `Rewriting.shift` fixes the quote of an `emb`'d sentence: `emb σ` has no fvars. -/
lemma rew_shift_emb {n : ℕ} (σ : Semisentence ℒₛₑₜ n) :
    Rewriting.shift ((Rewriting.emb (ξ := ℕ) σ : Semiproposition ℒₛₑₜ n)) =
      (Rewriting.emb (ξ := ℕ) σ : Semiproposition ℒₛₑₜ n) := by
  apply Semiformula.rew_eq_self_of
  · intro x; rfl
  · intro x hx
    -- fvSup (emb σ) = 0, so no fvar is present
    have h0 : ((Rewriting.emb (ξ := ℕ) σ : Semiproposition ℒₛₑₜ n)).fvSup = 0 :=
      Semiformula.fvSup_sentence σ
    have : x < 0 := by
      rw [← h0]
      exact Semiformula.lt_fvSup_of_fvar? hx
    exact absurd this (by simp)

/-- The pivot: shift fixes domZero. -/
lemma shift_domZero : shift (L := ℒₛₑₜ) (domZero (V := V)) = domZero (V := V) := by
  have h : domZero (V := V) = (⌜(arithTrln.domain/[#0] : Semisentence ℒₛₑₜ (0 + 1))⌝ : V) := by
    rw [← quote_domain_zero (V := V) (n := 0), emb_app_self]
  rw [h, Sentence.quote_def]
  rw [← Semiformula.quote_shift (V := V) (L := ℒₛₑₜ)
    (φ := (Rewriting.emb (ξ := ℕ) (arithTrln.domain/[#0]) : Semiproposition ℒₛₑₜ (0 + 1)))]
  rw [rew_shift_emb]

end GodelQ.ShiftDomZeroProbe

#print axioms GodelQ.ShiftDomZeroProbe.shift_domZero
