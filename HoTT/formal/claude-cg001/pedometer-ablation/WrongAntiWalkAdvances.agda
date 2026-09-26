{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-50 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-ABLATION-NEG-003

  In the escape of C-50, going back is a second path, and the counter goes up
  along both go and back.  The theory still supplies sym go, a walk from east
  to west.  Claiming by refl that this walk also adds a step (from 0 to 1)
  must be rejected: the kernel computes negsuc 0, that is -1.
-}
module WrongAntiWalkAdvances where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (ℤ; pos)
open import PedometerAblation using (module Escape)
open Escape using (Ped; go)

theReverseOfGoAddsAStep : subst Ped (sym go) (pos 0) ≡ pos 1
theReverseOfGoAddsAStep = refl
