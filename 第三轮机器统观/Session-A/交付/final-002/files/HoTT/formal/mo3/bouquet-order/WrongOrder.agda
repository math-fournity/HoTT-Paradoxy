{-# OPTIONS --safe --cubical --guardedness #-}
module WrongOrder where

open import Cubical.Foundations.Prelude
open import BouquetOrder

-- Expected type-boundary control: identical base endpoints do not supply
-- this claimed equality between the two fiber observations.
wrong : act (α ∙ β) a ≡ act (β ∙ α) a
wrong = refl
