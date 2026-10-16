{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-68 (expected KERNEL_REJECTED).
  proof id : MP-CG001-WILD-SST-P4-NEG-001

  The proof of notCoh₃ rests on one move of the first hemisphere carrying the
  non-trivial filler σr.  Claiming that this move is trivial in the same way
  as the other thirteen (its face refl) must be rejected: the face is sym σr.
-}
module WrongSurfMoveTrivial where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (zero)
open import Cubical.Data.Unit using (tt)
open import Cubical.HITs.S2.Base using (S²) renaming (base to north)
open import WildSST using (fzero ; fsuc)
open import WildSSTP4
open import WildSSTP4Flat

firstMoveTrivial : P4.hem₁-1 flatSurfᵢ zero fzero fzero fzero (fsuc fzero) tt tt tt tt ≡ refl
firstMoveTrivial = mv3-triv (λ (z : north ≡ north) → z) (refl {x = north} ∙ refl ∙ refl ∙ refl) refl
