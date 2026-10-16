{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-66 (expected KERNEL_REJECTED).
  proof id : MP-CG001-WILD-SST2-NEG-001

  Carrying base along the Hopf family over surf gives a loop of winding
  number -1.  Claiming by refl that it winds zero times, as it would if surf
  were refl, must be rejected: the kernel computes the winding number.
-}
module WrongSurfTrivial where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (pos)
open import Cubical.HITs.S1.Base using (winding)
open import Cubical.HITs.S2.Base using (surf)
open import WildSST2

surfWindsZero : winding (carry surf) ≡ pos 0
surfWindsZero = refl
