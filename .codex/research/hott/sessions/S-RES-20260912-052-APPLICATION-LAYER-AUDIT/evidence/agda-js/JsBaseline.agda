-- N10 probe A1: baseline delivery through the Agda JS backend (no cubical
-- content).  If this runs, the pipeline (type check -> JS -> node) works.
module JsBaseline where

open import Agda.Builtin.IO
open import Agda.Builtin.Unit
open import Agda.Builtin.String

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

main : IO ⊤
main = putStrLn "BASELINE_OK"
