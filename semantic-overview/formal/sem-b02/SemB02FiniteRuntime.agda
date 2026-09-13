module SemB02FiniteRuntime where

open import Agda.Builtin.IO
open import SemB02Kernel
open import foundation.unit-type
open import foundation-core.booleans

postulate
  printBool : bool → IO unit

{-# COMPILE JS printBool =
  function (b) {
    return function () {
      console.log(b({ "true": () => "TRUE", "false": () => "FALSE" }));
      return null;
    };
  }
  #-}

main : IO unit
main = printBool finiteTag
