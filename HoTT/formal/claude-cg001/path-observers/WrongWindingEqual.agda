{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-46 (a) (expected KERNEL_REJECTED).
  proof id : MP-CG001-PATH-OBSERVERS-NEG-001

  The winding number of loop is 1 and of refl is 0.  Claiming by refl that a
  fixed-endpoint observer cannot tell them apart must be rejected.
-}
module WrongWindingEqual where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.S1 using (S¹; base; loop; winding)

windingBlindToLoop : winding loop ≡ winding refl
windingBlindToLoop = refl
