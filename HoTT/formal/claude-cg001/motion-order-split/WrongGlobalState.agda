{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-18 (MP-CG001-MOTION-ORDER-SPLIT-NEG-001).
  Expected result: KERNEL_REJECTED.

  Claim tested: across the road the counter cannot stay at 0 in the global
  state; the only identification the family allows is the pre-written shift
  (start , 0) = (finish , 1).  Asking for (start , 0) = (finish , 0) must fail.
-}
module WrongGlobalState where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Int using (ℤ; pos; sucPathℤ)
open import Cubical.HITs.Interval using (Interval; seg)
  renaming (zero to start; one to finish)

Counter : Interval → Type
Counter start = ℤ
Counter finish = ℤ
Counter (seg i) = sucPathℤ i

wrongState : Path (Σ Interval Counter) (start , pos 0) (finish , pos 0)
wrongState = ΣPathP (seg , toPathP {A = λ j → sucPathℤ j} {x = pos 0} {y = pos 0} refl)
