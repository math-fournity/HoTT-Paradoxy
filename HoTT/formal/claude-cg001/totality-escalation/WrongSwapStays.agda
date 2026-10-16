{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-74 (expected KERNEL_REJECTED).
  proof id : MP-CG001-COPIES-OF-BOOL-NEG-001

  If the gathering of two-element sets settled into one point, its loop
  swapLoop would carry true to true.  The kernel computes false.
-}
module WrongSwapStays where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (true)
open import CopiesOfBool

swapKeepsTrue : transport (cong fst swapLoop) true ≡ true
swapKeepsTrue = refl
