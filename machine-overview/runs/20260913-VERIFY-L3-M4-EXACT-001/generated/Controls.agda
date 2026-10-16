{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (zero)
open import L3M4Support

check-finite : FiniteApproximation
check-finite = approximate zero

check-exact-empty : ExactArrival → ⊥
check-exact-empty = exact-elim
