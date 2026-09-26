{-# OPTIONS --safe --cubical --guardedness #-}
module OverlapMismatch where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
bad : (i j : I) → Partial (i ∨ j) Bool
bad i j = λ { (i = i1) → true ; (j = i1) → false }
