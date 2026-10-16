{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-24 (MP-CG001-TIME-DIRECTION-NEG-001).
  Expected result: KERNEL_REJECTED.

  Claim tested: in (ℕ, ≤) a step down is not an arrow.  Offering the witness
  (0 , refl) for 1 ≤ 0 must fail, since 0 + 1 is 1, not 0.
-}
module WrongDownStep where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Order using (_≤_)

downStep : 1 ≤ 0
downStep = 0 , refl
