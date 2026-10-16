{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-59 (expected KERNEL_REJECTED).
  proof id : MP-CG001-DELAY-MONAD-NEG-001

  DelayMonad.neverBind proves bind never f ≡ never by a coinductive path.
  The two programs are not definitionally equal: unfolding bind never f gives
  later (bind never f), unfolding never gives later never, and coinductive
  records have no eta rule that would close the gap.  Claiming the equation
  by refl must therefore be rejected.
-}
module WrongNeverBindRefl where

open import Cubical.Foundations.Prelude
open import PedometerSemantics using (Delay; never)
open import DelayMonad using (bind)

wrong : {A B : Type} (f : A → Delay B) → bind never f ≡ never
wrong f = refl
