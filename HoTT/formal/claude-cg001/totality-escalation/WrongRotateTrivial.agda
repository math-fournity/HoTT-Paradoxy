{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-73 (expected KERNEL_REJECTED).
  proof id : MP-CG001-TOTALITY-ESCALATION-NEG-001

  If rotating the circle once were the trivial loop of self-equivalences,
  the base point would travel a loop of winding number 0.  The kernel
  computes winding number 1.
-}
module WrongRotateTrivial where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (equivFun)
open import Cubical.Data.Int using (pos)
open import Cubical.HITs.S1.Base using (base ; winding)
open import TotalityEscalates

rotateOnceStill : winding (cong (λ e → equivFun e base) rotateOnce) ≡ pos 0
rotateOnceStill = refl
