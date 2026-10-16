{-# OPTIONS --safe --cubical --guardedness #-}

module TruncationDefense where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base
  using (Bool; false; true; if_then_else_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base
  using (∥_∥₁; ∣_∣₁; squash₁)

private
  variable
    ℓ : Level
    A P : Type ℓ

-- C-67: the native squash-HIT eliminator is available for proposition-valued
-- consumers.  This is the protected, information-respecting direction.
protectedRecursor : isProp P → (A → P) → ∥ A ∥₁ → P
protectedRecursor Pprop f ∣ x ∣₁ = f x
protectedRecursor Pprop f (squash₁ x y i) =
  Pprop (protectedRecursor Pprop f x)
        (protectedRecursor Pprop f y) i

-- C-68: a concrete positive control.  Truncating twice can be flattened back
-- to one truncation because the codomain is itself a proposition.
flattenTruncation : ∥ ∥ A ∥₁ ∥₁ → ∥ A ∥₁
flattenTruncation = protectedRecursor squash₁ (λ x → x)

flattenTruncation-β : (a : A) →
  flattenTruncation ∣ ∣ a ∣₁ ∣₁ ≡ ∣ a ∣₁
flattenTruncation-β a = refl

-- C-69: every function out of the truncation maps its two canonical Bool
-- points to path-equal outputs, because squash₁ identifies all inhabitants.
truncatedBoolMapIsConstant :
  (f : ∥ Bool ∥₁ → Bool) → f ∣ false ∣₁ ≡ f ∣ true ∣₁
truncatedBoolMapIsConstant f = congS f (squash₁ ∣ false ∣₁ ∣ true ∣₁)

false≢true : false ≡ true → ⊥
false≢true p = subst (λ b → if b then ⊥ else Bool) p true

-- C-70: therefore no function can both consume ∥ Bool ∥₁ and preserve each
-- point constructor as the original Bool witness.  This is a defense result:
-- the requested untruncation contract conflicts with the HIT path constructor.
noPointPreservingBoolExtraction :
  (extract : ∥ Bool ∥₁ → Bool) →
  ((b : Bool) → extract ∣ b ∣₁ ≡ b) →
  ⊥
noPointPreservingBoolExtraction extract β =
  false≢true
    (sym (β false) ∙ truncatedBoolMapIsConstant extract ∙ β true)
