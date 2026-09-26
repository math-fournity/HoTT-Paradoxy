{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-47 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-HALTING-NEG-001

  Carried around the circle and back, the helix counter returns to its start.
  Claiming by refl that one round trip has advanced it by two must be rejected.
-}
module WrongHelixRoundTrip where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (ℤ; pos)
open import Cubical.HITs.S1 using (S¹; base; loop; helix)

roundTripAdvancedByTwo : subst helix (loop ∙ sym loop) (pos 0) ≡ pos 2
roundTripAdvancedByTwo = refl
