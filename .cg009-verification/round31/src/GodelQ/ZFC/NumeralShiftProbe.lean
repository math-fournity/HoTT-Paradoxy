import GodelQ.ZFC.ShiftDomZeroProbe
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.NumeralShiftProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- shift fixes numerals (they are closed terms)
example (m : ℕ) : shift (L := ℒₛₑₜ) ((m : V)) = (m : V) := by
  sorry

-- shift fixes the quote of a sentence (from ShiftDomZero's rew_shift_emb route)
example (φ : Semisentence ℒₛₑₜ 1) :
    shift (L := ℒₛₑₜ) ((⌜φ⌝ : V)) = (⌜φ⌝ : V) := by
  rw [Sentence.quote_def]
  rw [← Semiformula.quote_shift (V := V) (L := ℒₛₑₜ)
    (φ := (Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ 1))]
  congr 1
  apply Semiformula.rew_eq_self_of
  · intro x; rfl
  · intro x hx
    have h0 : ((Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ 1)).fvSup = 0 :=
      Semiformula.fvSup_sentence φ
    have : x < 0 := by
      rw [← h0]
      exact Semiformula.lt_fvSup_of_fvar? hx
    exact absurd this (by simp)

end GodelQ.NumeralShiftProbe
