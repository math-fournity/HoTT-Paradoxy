{-# OPTIONS --safe --cubical #-}
module Positive where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
check : true ≡ true
check = refl
