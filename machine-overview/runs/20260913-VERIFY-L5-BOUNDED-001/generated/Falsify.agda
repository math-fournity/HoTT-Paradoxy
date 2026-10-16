{-# OPTIONS --safe #-}

module Falsify where

open import Agda.Builtin.Bool using (true)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Nat using (zero)
import L5ConsumerSupport as L5

-- Negative control: zero fuel does not report success.
bad : L5.searchK zero ≡ true
bad = refl
