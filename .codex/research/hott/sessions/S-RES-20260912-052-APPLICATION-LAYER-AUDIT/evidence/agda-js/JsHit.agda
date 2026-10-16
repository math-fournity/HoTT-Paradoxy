{-# OPTIONS --cubical --guardedness #-}

-- N10 probe A3: delivery of a computation that eliminates a higher inductive
-- type with a non-trivial path constructor.  The elimination must be constant
-- on the identified points; the observed value is the constant result.
module JsHit where

open import Agda.Builtin.IO
open import Agda.Builtin.Unit
open import Agda.Builtin.String
open import Cubical.Foundations.Prelude
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

data Two : Type where
  a : Two
  b : Two
  sq : a ≡ b

_++_ : String → String → String
_++_ = primStringAppend

infixr 5 _++_

f : Two → Bool
f a = true
f b = true
f (sq i) = true

render : Bool → String
render true = "TRUE"
render false = "FALSE"

main : IO ⊤
main = putStrLn ("HIT_ELIM_RESULT=" ++ render (f a) ++ "/" ++ render (f b))
