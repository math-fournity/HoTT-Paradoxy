{-# OPTIONS --safe --cubical --guardedness #-}

module SemB06FalseEqualityNegative where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

private
  variable
    ℓ : Level

module _ (R : CommRing ℓ) (x y : fst R) where

  -- Expected rejection: commutative-ring laws do not identify two variables.
  arbitrary-elements-equal : x ≡ y
  arbitrary-elements-equal = solve! R
