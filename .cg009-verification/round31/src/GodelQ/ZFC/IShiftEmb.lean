-- CG-009: Rew-level identity — shift composed with emb is emb.
-- emb's free-variable action is h.elim (Empty domain), so bumping fvars has no effect.
import GodelQ.ZFC.IShiftAtom

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.IShiftEmb

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- Rew-level: shift ∘ emb = emb (fvar domain is Empty). -/
lemma shift_comp_emb {n : ℕ} :
    (Rew.shift : Rew ℒₛₑₜ ℕ n ℕ n).comp (Rew.emb : Rew ℒₛₑₜ Empty n ℕ n) =
      (Rew.emb : Rew ℒₛₑₜ Empty n ℕ n) := by
  ext x
  · rfl
  · exact isEmptyElim x

/-- Formula-level: shift fixes the emb of a Semisentence. -/
lemma shift_emb_app {n : ℕ} (φ : Semisentence ℒₛₑₜ n) :
    Rewriting.shift ((Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n)) =
      (Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n) := by
  have h := TransitiveRewriting.comp_app (L := ℒₛₑₜ)
    (ξ₁ := ℕ) (F₁ := Semiformula ℒₛₑₜ ℕ) (ξ₂ := ℕ) (F₂ := Semiformula ℒₛₑₜ ℕ)
    (ξ₃ := ℕ) (F₃ := Semiformula ℒₛₑₜ ℕ) (n₁ := n) (n₂ := n) (n₃ := n)
    (ω₁₂ := (Rew.emb : Rew ℒₛₑₜ Empty n ℕ n)) (ω₂₃ := (Rew.shift : Rew ℒₛₑₜ ℕ n ℕ n)) φ
  rw [show (Rew.shift : Rew ℒₛₑₜ ℕ n ℕ n).comp (Rew.emb : Rew ℒₛₑₜ Empty n ℕ n) =
    (Rew.emb : Rew ℒₛₑₜ Empty n ℕ n) from shift_comp_emb (n := n)] at h
  exact h

end GodelQ.IShiftEmb
