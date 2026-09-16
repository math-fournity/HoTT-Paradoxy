{-# OPTIONS --without-K #-}

module agda.cchm where

open import agda.fibration
open import agda.prelude
open import agda.postulates
open import agda.exp-path

----------------------------------------------------------------------
-- The Cohen-Coquand-Huber-Mörtberg composition structure
----------------------------------------------------------------------
CCHM :
    {l : Level}
    (P : ℘ (Set l))
    → -------------
    Set (ℓ₁ ⊔ l)
CCHM P =
  (φ : Set)
  (_ : cof φ)
  (p : (i : 𝕀) → φ → P i)
  → -----------------------------------------------
  (Σ a₀ ∶ P O , p O ↗ a₀) → (Σ a₁ ∶ P I , p I ↗ a₁)

