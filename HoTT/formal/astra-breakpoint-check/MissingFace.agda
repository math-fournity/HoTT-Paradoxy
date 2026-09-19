{-# OPTIONS --safe --cubical --guardedness #-}
module MissingFace where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
bad : (φ : I) → Partial φ Bool → Bool
bad φ u = u 1=1
