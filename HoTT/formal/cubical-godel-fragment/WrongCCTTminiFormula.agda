{-# OPTIONS --safe --cubical #-}

module WrongCCTTminiFormula where

open import Agda.Builtin.Equality using (_≡_; refl)
open import CCTTminiFormula

-- Expected rejection: the quotation constructor does not collapse to bottom.
wrongQuoteAsBottom : quoteCert closedC ≡ botF
wrongQuoteAsBottom = refl
