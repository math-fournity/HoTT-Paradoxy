{-# OPTIONS --safe --cubical --guardedness #-}
module MissingBridge where
open import Cubical.Foundations.Prelude

-- Expected failure at q: its source c is not the required intermediate b.
bad : {A : Type} {a b c d : A} → a ≡ b → c ≡ d → a ≡ d
bad p q = p ∙ q
