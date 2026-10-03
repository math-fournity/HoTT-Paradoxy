{-# OPTIONS --safe --cubical --guardedness #-}
-- Negative control for CG001-C-84: a constant attempted decoder cannot supply
-- the required identity of every original universe element.
module WrongObservationCompletionBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.HITs.SetTruncation as ST using (∣_∣₂)
open import TruncationQuestioning using (TU)

wrongUniformRestore :
  Σ[ g ∈ (TU → Type ℓ-zero) ] ((A : Type ℓ-zero) → g ∣ A ∣₂ ≡ A)
wrongUniformRestore = (λ _ → Type ℓ-zero) , λ A → refl
