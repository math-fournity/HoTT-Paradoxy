{-# OPTIONS --safe --cubical --guardedness #-}
module RawNumeratorQuotient where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Int.Base using (ℤ)
import Cubical.Data.Int.Properties as Z
open import Cubical.Data.Rationals.Base using (ℚ)
import Cubical.HITs.SetQuotients.Properties as SQ
open import QuotientConsumer using (Frac)

-- Controlled incorrect relation proof for the actual rational quotient.
bad : ℚ → ℤ
bad = SQ.rec Z.isSetℤ fst (λ a b relation → refl)
