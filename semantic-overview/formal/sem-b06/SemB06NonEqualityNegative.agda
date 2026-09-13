{-# OPTIONS --safe --cubical --guardedness #-}

module SemB06NonEqualityNegative where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

private
  variable
    ℓ : Level

module _ (R : CommRing ℓ) where

  -- Expected rejection: the solver accepts an equality goal, not a ring value.
  not-an-equality : fst R
  not-an-equality = solve! R
