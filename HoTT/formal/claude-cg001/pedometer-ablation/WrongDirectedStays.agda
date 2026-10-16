{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-51 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-ABLATION-NEG-002

  In the directed model a round trip is two arrows, not an arrow and its
  inverse.  Claiming by refl that the pedometer is unchanged after one round
  trip must be rejected: the kernel computes 2, not 0.
-}
module WrongDirectedStays where

open import Cubical.Foundations.Prelude
open import PedometerAblation using (module Directed)
open Directed using (carry; roundTrip)

roundTripLeavesThePedometer : carry roundTrip 0 ≡ 0
roundTripLeavesThePedometer = refl
