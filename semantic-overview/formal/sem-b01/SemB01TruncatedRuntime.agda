module SemB01TruncatedRuntime where

open import Agda.Builtin.IO
open import SemB01Kernel
open import foundation.unit-type
open import foundation-core.booleans

postulate
  printBool : bool → IO unit

{-# COMPILE JS printBool =
  function (b) {
    return function () {
      console.log(b ? "TRUE" : "FALSE");
      return null;
    };
  }
  #-}

main : IO unit
main = printBool truncatedResult
