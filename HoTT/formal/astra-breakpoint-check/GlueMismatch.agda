{-# OPTIONS --safe --cubical --guardedness #-}
module GlueMismatch where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.Core.Glue
G : Type
G = Glue Bool {φ = i1} (λ _ → Bool , notEquiv)
bad : G
bad = glue {A = Bool} {φ = i1} {T = λ _ → Bool} {e = λ _ → notEquiv}
  (λ _ → true) true
