{-# OPTIONS --erased-cubical --guardedness #-}

-- N10 probe A8: a delivery program that only *uses* data defined in the
-- cubical library (Bool) without any cubical feature of its own.  This
-- distinguishes "no cubical computation" from "cubical provenance".
module ErasedCubicalImport where

open import Agda.Builtin.IO
open import Agda.Builtin.Unit
open import Agda.Builtin.String
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

render : Bool → String
render true = "TRUE"
render false = "FALSE"

myNot : Bool → Bool
myNot true = false
myNot false = true

_++_ : String → String → String
_++_ = primStringAppend

infixr 5 _++_

main : IO ⊤
main = putStrLn ("LOCAL_NOT_TRUE=" ++ render (myNot true) ++ ";LIB_CONSTRUCTOR=" ++ render true)
