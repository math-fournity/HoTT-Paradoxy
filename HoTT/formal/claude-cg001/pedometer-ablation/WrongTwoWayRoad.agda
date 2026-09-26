{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-49 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-ABLATION-NEG-001

  One road, one path go : west = east, and a carried counter that goes up by
  one along go.  Walking the same road back is sym go.  Claiming by refl that
  walking back also adds one (from 1 to 2) must be rejected: carried back
  along sym go, the counter goes down to 0.
-}
module WrongTwoWayRoad where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (ℤ; pos; sucPathℤ)

data Road : Type where
  west east : Road
  go : west ≡ east

Ped : Road → Type
Ped west   = ℤ
Ped east   = ℤ
Ped (go i) = sucPathℤ i

walkingBackAlsoAddsOne : subst Ped (sym go) (pos 1) ≡ pos 2
walkingBackAlsoAddsOne = refl
