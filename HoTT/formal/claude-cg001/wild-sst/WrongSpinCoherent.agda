{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-64 (expected KERNEL_REJECTED).
  proof id : MP-CG001-WILD-SST-NEG-001

  In the instance spin, route A winds once around the circle at base and
  route B twice.  Claiming by refl that route A also winds twice must be
  rejected: the kernel computes the winding number of route A as 1.
-}
module WrongSpinCoherent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (pos)
open import Cubical.HITs.S1.Base using (winding)
open import WildSST

routeAAlsoTwice : winding routeA-spin ≡ pos 2
routeAAlsoTwice = refl
