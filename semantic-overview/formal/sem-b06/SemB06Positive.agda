{-# OPTIONS --safe --cubical --guardedness #-}

module SemB06Positive where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

private
  variable
    ℓ : Level

module _ (R : CommRing ℓ) (x y z : fst R) where
  open CommRingStr (snd R)

  commutative-distributive-normalisation :
    x · (y + z) ≡ z · x + x · y
  commutative-distributive-normalisation = solve! R
