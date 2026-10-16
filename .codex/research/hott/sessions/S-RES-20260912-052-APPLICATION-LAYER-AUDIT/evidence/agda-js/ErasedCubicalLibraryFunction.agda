{-# OPTIONS --erased-cubical --guardedness --erasure #-}

-- N10 probe A10: even the simplest *function* defined in the cubical library
-- (Bool.not) is declared erased for erased-cubical imports, so a compilable
-- program cannot compute with it.  Only the data constructors remain usable.
module ErasedCubicalLibraryFunction where

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

main : IO ⊤
main = putStrLn (render (not true))
