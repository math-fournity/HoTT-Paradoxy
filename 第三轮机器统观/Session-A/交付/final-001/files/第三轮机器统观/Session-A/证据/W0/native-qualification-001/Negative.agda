{-# OPTIONS --safe --cubical --guardedness #-}
module Negative where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
check : true ≡ false
check = refl
