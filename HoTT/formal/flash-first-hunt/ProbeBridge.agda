{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module flash-first-hunt.ProbeBridge where
open import Cubical.Foundations.Prelude using (sym; Level; Type; Σ-syntax; _≡_)
open import Cubical.Data.Int.Base using (ℤ; pos)
open import Cubical.Data.Int.Properties using (discreteℤ; injPos)
open import Cubical.Data.Nat.Properties using (znots)
open import Cubical.Data.Nat.Base using (ℕ; suc; zero)
open import Cubical.Data.Empty.Base using (⊥)

private
  ¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
  ¬ A = A → ⊥

ExcludedCarrier : {ℓ : Level} (C : Type ℓ) (r : C) → Type ℓ
ExcludedCarrier C r = Σ[ q ∈ C ] (¬ (q ≡ r))

0z : ℤ
0z = pos 0

p1 : ¬ (pos 1 ≡ pos 0)
p1 h = znots (sym (congℕ (injPos h)))
  where
  congℕ : suc zero ≡ zero → zero ≡ suc zero
  congℕ q = sym q

w : ExcludedCarrier ℤ 0z
w = pos 1 , p1
