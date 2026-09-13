{-# OPTIONS --erased-cubical --guardedness --erasure #-}

-- N10 probe A7: the same escape hatch with a *computational* use of the
-- cubical feature.  The erasure checker must reject this, not deliver a
-- representative-dependent or erased result.
module ErasedCubicalNegative where

open import Agda.Builtin.IO
open import Agda.Builtin.Unit
open import Agda.Builtin.String
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool

postulate
  putStrLn : String → IO ⊤

{-# COMPILE JS putStrLn =
  function (s) {
    return function () {
      console.log(s);
      return null;
    };
  }
  #-}

not' : Bool → Bool
not' true = false
not' false = true

@0 notnot' : ∀ b → not' (not' b) ≡ b
notnot' true = refl
notnot' false = refl

@0 notEquivLocal : Bool ≃ Bool
notEquivLocal = isoToEquiv (iso not' not' notnot' notnot')

render : Bool → String
render true = "TRUE"
render false = "FALSE"

_++_ : String → String → String
_++_ = primStringAppend

infixr 5 _++_

computed : Bool
computed = transport (ua notEquivLocal) true

main : IO ⊤
main = putStrLn ("COMPUTED=" ++ render computed)
