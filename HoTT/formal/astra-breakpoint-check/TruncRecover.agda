{-# OPTIONS --safe --cubical --guardedness #-}
module TruncRecover where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.HITs.PropositionalTruncation
bad : ∥ Bool ∥₁ → Bool
bad ∣ b ∣₁ = b
bad (squash₁ x y i) = bad x
