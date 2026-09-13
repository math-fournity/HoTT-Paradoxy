{-# OPTIONS --cubical --guardedness #-}

-- N10 probe A2: delivery of a computation whose value is produced by
-- transport along a ua path.  uabeta makes transport (ua e) x reduce to
-- equivFun e x, so `true` must travel to `false`.  The delivered program
-- prints FALSE for the transported value and TRUE for its negation.
module JsUaTransport where

open import Agda.Builtin.IO
open import Agda.Builtin.Unit
open import Agda.Builtin.String
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
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

_++_ : String → String → String
_++_ = primStringAppend

infixr 5 _++_

render : Bool → String
render true = "TRUE"
render false = "FALSE"

transported : Bool
transported = transport (ua notEquiv) true

main : IO ⊤
main = putStrLn ("UA_TRANSPORT_RESULT=" ++ render transported ++ ";DIRECT_NOT=" ++ render (not true))
