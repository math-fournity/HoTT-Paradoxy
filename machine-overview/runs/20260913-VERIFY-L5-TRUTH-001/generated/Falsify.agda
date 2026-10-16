{-# OPTIONS --safe #-}

module Falsify where

open import Agda.Builtin.Bool using (true)
open import Agda.Builtin.Equality using (_≡_; refl)
import L5ConsumerSupport as L5

-- Negative control: the false literal does not evaluate to true.
bad : L5.evalB L5.falseFormula ≡ true
bad = refl
