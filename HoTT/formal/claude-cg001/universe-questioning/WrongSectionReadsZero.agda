{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-75 (proof id MP-CG001-UNIVERSE-QUESTIONING-NEG-001).
  Claims that the non-trivial section of UniverseHasNoLevel reads back as 0 at
  the base point.  Expected: rejected, the kernel computes 1 (1 != 0).
-}
module WrongSectionReadsZero where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Pointed
open import Cubical.Data.Int using (pos)
open import Cubical.Algebra.AbGroup.Instances.Int using (ℤAbGroup)
open import Cubical.Homotopy.EilenbergMacLane.Base using (0ₖ)
open import UniverseHasNoLevel

wrong : transport (cong typ (ΩⁿK 0 (0ₖ {G = ℤAbGroup} 1))) (sec 0 (0ₖ {G = ℤAbGroup} 1)) ≡ pos 0
wrong = refl
