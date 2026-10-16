{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-41 (expected KERNEL_REJECTED).
  proof id : MP-CG001-STEP-COUNT-NEG-001

  With journeys kept as data, "there and back" has two steps and staying put
  has none; the kernel tells them apart.  Claiming by refl that the two step
  counts are equal must be rejected.  (Realized as loops, the same two
  journeys are equal as paths, C-41.)  Self-contained.
-}
module WrongStepCount where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.List using (List; []; _∷_; length)

data Step : Type where
  fwd back : Step

wrongStepCount : Path ℕ (length (fwd ∷ back ∷ [])) (length {A = Step} [])
wrongStepCount = refl
