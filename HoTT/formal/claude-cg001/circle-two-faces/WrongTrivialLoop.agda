{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-22 (MP-CG001-CIRCLE-TWO-FACES-NEG-001).
  Expected result: KERNEL_REJECTED.

  Claim tested: the loop of the synthetic circle is not the trivial loop.
  Asserting loop ≡ refl by reflexivity must fail.
-}
module WrongTrivialLoop where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.S1 using (S¹; base; loop)

loopIsTrivial : loop ≡ refl
loopIsTrivial = refl
