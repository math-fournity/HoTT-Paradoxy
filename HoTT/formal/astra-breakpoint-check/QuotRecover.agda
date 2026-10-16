{-# OPTIONS --safe --cubical --guardedness #-}
module QuotRecover where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.Data.Unit
import Cubical.HITs.SetQuotients as SQ
bad : Bool SQ./ (λ _ _ → Unit) → Bool
bad = SQ.rec isSetBool (λ x → x) (λ a b r → refl)
