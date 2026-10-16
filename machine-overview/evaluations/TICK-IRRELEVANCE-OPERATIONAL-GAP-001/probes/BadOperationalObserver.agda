{-# OPTIONS --safe --cubical #-}
module BadOperationalObserver where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)

data ExtTick : Type₀ where
  forcing ordinary : ExtTick
  tirr : forcing ≡ ordinary

isForcing : ExtTick → Bool
isForcing forcing = true
isForcing ordinary = false
