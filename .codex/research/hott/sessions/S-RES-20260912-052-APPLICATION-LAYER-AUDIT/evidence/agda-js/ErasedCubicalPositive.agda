{-# OPTIONS --erased-cubical --guardedness --erasure #-}

-- N10 probe A6: the documented escape hatch.  Under --erased-cubical, cubical
-- features may be used in erased positions; the delivered program must still
-- type check, compile and run, with the cubical content erased.
module ErasedCubicalPositive where

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

@0 erasedUaPath : Bool ≡ Bool
erasedUaPath = ua (idEquiv Bool)

main : IO ⊤
main = putStrLn "ERASED_CUBICAL_OK"
