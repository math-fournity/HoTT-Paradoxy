-- N10 probe A9: a compilation-eligible module (no cubical options) that
-- imports data defined in the cubical library.  This distinguishes "uses a
-- cubical feature" from "depends on a cubical-provenance module".
module PlainCubicalImport where

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
main = putStrLn (render true)
