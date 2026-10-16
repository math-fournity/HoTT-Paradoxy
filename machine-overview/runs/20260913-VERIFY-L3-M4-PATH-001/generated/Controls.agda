{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (zero)
open import L3M4Support

check-segment-path : left ≡ right
check-segment-path = segment-path

check-stage-apart : (phase start ≡ phase finish) → ⊥
check-stage-apart = phase-apart
