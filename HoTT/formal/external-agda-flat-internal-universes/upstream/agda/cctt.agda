{-# OPTIONS --without-K #-}

module agda.cctt where

open import agda.fibration
open import agda.prelude
open import agda.postulates
open import agda.exp-path

----------------------------------------------------------------------
-- The composition structure from "Cartesian Cubical Type Theory"
-- by Angiuli et al
----------------------------------------------------------------------
CCTT :
    {l : Level}
    (P : ℘ (Set l))
    → -------------
    Set (ℓ₁ ⊔ l)
CCTT P =
   (φ : Set)
   (_ : cof φ)
   (p : (i : 𝕀) → φ → P i)
   (i : 𝕀)
   (a : P i)
   (_ : p i ↗ a)
   → -----------------------------------------
   Σ f ∶ (Π 𝕀 P) , (f i ≡ a) × ∀ j → p j ↗ f j 

