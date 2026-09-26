{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-70 (expected KERNEL_REJECTED).
  proof id : MP-CG001-WILD-SST-LEVELS-NEG-001

  groupoidsCohere₃ gives Coh₃ only when every level is a groupoid.  Using it
  for the flat shape over the 2-sphere, with the circle's groupoid proof in
  place of the missing one for S², must be rejected.
-}
module WrongS2Groupoid where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (zero ; suc)
open import Cubical.Data.Unit.Properties using (isOfHLevelUnit)
open import Cubical.HITs.S1.Properties using (isGroupoidS¹)
open import WildSSTP4
open import WildSSTP4Flat using (flatSurfᵢ)
open import WildSSTP4Levels using (groupoidsCohere₃)

surfCoherent : Coh₃ flatSurfᵢ
surfCoherent = groupoidsCohere₃ flatSurfᵢ λ { zero → isGroupoidS¹ ; (suc n) → isOfHLevelUnit 3 }
