-- CG-009: shift fixes the quote of any Semisentence — a general tool.
import GodelQ.ZFC.ShiftDomZeroProbe

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ShiftQuote

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `Rewriting.shift` fixes the quote of any sentence (Empty fvar domain). -/
lemma rew_shift_quote {n : ℕ} (φ : Semisentence ℒₛₑₜ n) :
    Rewriting.shift ((Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n)) =
      (Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n) := by
  apply Semiformula.rew_eq_self_of
  · intro x; rfl
  · intro x hx
    have h0 : ((Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n)).fvSup = 0 :=
      Semiformula.fvSup_sentence φ
    have : x < 0 := by
      rw [← h0]
      exact Semiformula.lt_fvSup_of_fvar? hx
    exact absurd this (by simp)

/-- **shift fixes the quote of any Semisentence** (V level). -/
lemma shift_quote {n : ℕ} (φ : Semisentence ℒₛₑₜ n) :
    shift (L := ℒₛₑₜ) ((⌜φ⌝ : V)) = (⌜φ⌝ : V) := by
  rw [Sentence.quote_def]
  rw [← Semiformula.quote_shift (V := V) (L := ℒₛₑₜ)
    (φ := (Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n))]
  rw [rew_shift_quote]

end GodelQ.ShiftQuote

#print axioms GodelQ.ShiftQuote.shift_quote
