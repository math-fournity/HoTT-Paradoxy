{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (zero)
open import L3M4Support

check-start : phase start ≡ false
check-start = phase-start

check-finish : phase finish ≡ true
check-finish = phase-finish

check-apart : (phase start ≡ phase finish) → ⊥
check-apart = phase-apart
