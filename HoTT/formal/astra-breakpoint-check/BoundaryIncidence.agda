{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryIncidence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool
open import Cubical.Data.Empty

-- Boundary maps are actual maps into ambient types, not extra truth-value tags.
-- Both ambient coordinates and the labels of the two ends may change.
noBoundaryPreservingEquivalence : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (n : Bool → A) (m : Bool → B)
  → (n false ≡ n true → ⊥)
  → ((u v : Bool) → m u ≡ m v)
  → (e : A ≃ B) (labels : Bool ≃ Bool)
  → ((b : Bool) → equivFun e (n b) ≡ m (equivFun labels b))
  → ⊥
noBoundaryPreservingEquivalence n m distinct collapsed e labels commute =
  distinct (sym (retEq e (n false))
    ∙ cong (invEq e) (commute false
       ∙ collapsed (equivFun labels false) (equivFun labels true)
       ∙ sym (commute true))
    ∙ retEq e (n true))

-- Calibration only: a geometric circle/interval must supply its own boundary maps.
finiteBoundaryInstance : (e labels : Bool ≃ Bool)
  → ((b : Bool) → equivFun e b ≡ false) → ⊥
finiteBoundaryInstance = noBoundaryPreservingEquivalence
  (λ b → b) (λ _ → false) false≢true (λ _ _ → refl)
