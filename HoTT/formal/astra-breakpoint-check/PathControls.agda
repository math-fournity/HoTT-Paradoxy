{-# OPTIONS --safe --cubical --guardedness #-}
module PathControls where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool
open import Cubical.Data.Empty as Empty

-- BP-C01: a missing intermediate bridge is not supplied by concatenation.
compose : {A : Type} {a b c : A} → a ≡ b → b ≡ c → a ≡ c
compose p q = p ∙ q

restore : {A : Type} {a b c d : A} → a ≡ b → b ≡ c → c ≡ d → a ≡ d
restore p r q = p ∙ r ∙ q

noFreeBridge :
  ((A : Type) (a b c d : A) → a ≡ b → c ≡ d → a ≡ d) → ⊥
noFreeBridge f = true≢false (f Bool true true false false refl refl)

-- BP-C02/C05: the concrete consumer receives the transported endpoint.
flipThenCompose : transport (ua notEquiv) true ≡ false
flipThenCompose = uaβ notEquiv true ∙ refl

roundTripValue : not (transport (ua notEquiv) true) ≡ true
roundTripValue = cong not (uaβ notEquiv true)

positiveInstance : true ≡ true
positiveInstance = restore refl refl refl
