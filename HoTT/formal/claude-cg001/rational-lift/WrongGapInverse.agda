{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-43 (expected KERNEL_REJECTED).
  proof id : MP-CG001-RATIONAL-LIFT-NEG-001

  At the gap itself (x = -1, so 1 + x = 0) there is no parameter: 0 has no
  inverse.  Claiming by refl that 0 times 0 is 1 must be rejected.
-}
module WrongGapInverse where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Algebra.CommRing
open import Cubical.Algebra.CommRing.Instances.Rationals using (ℚCommRing)
open import Cubical.Data.Rationals.MoreRationals.QuoQ using (ℚ)

open CommRingStr (ℚCommRing .snd)

wrongGapInverse : Σ[ p ∈ ℚ ] 0r · p ≡ 1r
wrongGapInverse = 0r , refl
