{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-71 (expected KERNEL_REJECTED).
  proof id : MP-CG001-HSET-UNIVERSE-NEG-001

  If the loop flipSet of hSet were trivial, transporting true along its
  first component would give true.  The kernel computes false.
-}
module WrongFlipSetTrivial where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool ; true)
open import HSetNotSet

flipKeepsTrue : transport (cong fst flipSet) true ≡ true
flipKeepsTrue = refl
