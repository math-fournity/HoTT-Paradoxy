{-# OPTIONS --safe --cubical #-}

module WrongCCTTminiFormulaCode where

open import Agda.Builtin.Equality using (_≡_; refl)
open import CCTTminiFormulaCode

-- Expected rejection: self substitution of the template is a prov₁ formula.
wrongSelfInstanceIsBottom : selfInstance template ≡ bot₁
wrongSelfInstanceIsBottom = refl
