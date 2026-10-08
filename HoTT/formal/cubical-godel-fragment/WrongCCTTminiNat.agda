{-# OPTIONS --safe --cubical #-}

module WrongCCTTminiNat where

open import Agda.Builtin.Equality using (_≡_; refl)
open import CCTTmini
open import CCTTminiNat

-- Expected rejection: `decode (code positiveC)` normalizes to positiveC, not
-- zeroC.  This tests the coded round trip rather than a parser/import error.
wrong-coded-positive : decode (code positiveC) ≡ zeroC
wrong-coded-positive = refl
