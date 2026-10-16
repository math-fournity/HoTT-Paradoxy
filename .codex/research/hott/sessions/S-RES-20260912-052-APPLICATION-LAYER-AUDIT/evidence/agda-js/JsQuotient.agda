{-# OPTIONS --cubical --guardedness #-}

-- N10 probe A4: delivery of a computation that eliminates a set quotient.
-- The relation identifies true and false; the eliminator is constant, as the
-- quotient requires.  Both representatives must deliver the same result.
module JsQuotient where

open import Agda.Builtin.IO
open import Agda.Builtin.Unit
open import Agda.Builtin.String
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Bool
open import Cubical.Data.Unit
open import Cubical.HITs.SetQuotients renaming (rec to SQ-rec)

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

_~_ : Bool → Bool → Type
_~_ _ _ = Unit

_++_ : String → String → String
_++_ = primStringAppend

infixr 5 _++_

Q : Type
Q = Bool / _~_

g : Q → Bool
g = SQ-rec isSetBool (λ _ → true) (λ _ _ _ → refl)

render : Bool → String
render true = "TRUE"
render false = "FALSE"

main : IO ⊤
main = putStrLn ("QUOTIENT_ELIM_RESULT=" ++ render (g [ true ]) ++ "/" ++ render (g [ false ]))
