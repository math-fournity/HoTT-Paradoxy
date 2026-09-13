module SemB02ExplicitRuntime where

open import Agda.Builtin.IO
open import foundation.decidable-types
open import foundation.unit-type
open import foundation.universe-levels
open import foundation-core.booleans
open import foundation-core.coproduct-types
open import foundation-core.identity-types

explicitDecision : is-decidable (true ＝ false)
explicitDecision = inr neq-true-false-bool

decisionTag : {l : Level} {A : UU l} → is-decidable A → bool
decisionTag (inl _) = true
decisionTag (inr _) = false

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
main = printBool (decisionTag explicitDecision)
