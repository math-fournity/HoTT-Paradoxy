{-# OPTIONS --safe --cubical --guardedness #-}
module HITMismatch where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import LocalCoherence using (Joined; left; right; join)
bad : Joined → Bool
bad left = true
bad right = false
bad (join i) = true
