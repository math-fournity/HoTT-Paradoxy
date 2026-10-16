{-# OPTIONS --safe --cubical #-}

module WrongCCTTmini where

open import Agda.Builtin.Bool using (false)
open import Agda.Builtin.Equality using (_≡_; refl)
open import CCTTmini

-- Expected negative control: the main module reduces this expression to true.
wrong-positive-rejection : accepts Γ₁ positiveC ≡ false
wrong-positive-rejection = refl
