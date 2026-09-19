{-# OPTIONS --safe --cubical --guardedness #-}
module MixedRecovery where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool
open import Cubical.Data.Unit
import Cubical.HITs.SetQuotients as SQ
-- The same quotient consumer obligation, after a valid native equivalence.
bad : Bool SQ./ (λ _ _ → Unit) → Bool
bad = SQ.rec isSetBool (transport (ua notEquiv)) (λ a b r → refl)
