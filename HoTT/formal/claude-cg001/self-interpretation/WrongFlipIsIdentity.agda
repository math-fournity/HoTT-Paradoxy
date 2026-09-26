{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-67 (expected KERNEL_REJECTED).
  proof id : MP-CG001-SELF-INTERPRETATION-NEG-001

  Carrying the function first (first x y = x) along ua flipEquiv gives the
  flipped function (x y ↦ y).  Claiming by refl that it stays first, as it
  would if the flip were the trivial identification, must be rejected: the
  kernel computes the transport.
-}
module WrongFlipIsIdentity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence using (ua)
open import SelfInterpretation

flipLeavesFirst : transport (ua flipEquiv) first ≡ first
flipLeavesFirst = refl
