{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-69 (expected KERNEL_REJECTED).
  proof id : MP-CG001-WINDING-COCYCLE-NEG-001

  The winding pattern of spin does not satisfy the cocycle equation at
  m = 0, i = j = k = 0: the routes meet windings adding up to 1 and 2.
  Claiming the equation there by computation must be rejected.
-}
module WrongSpinWCocycle where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (zero)
open import Cubical.Data.Unit using (tt)
open import WildSST using (fzero)
open import WindingCocycle

open import Cubical.Data.Int using (_+_)
open import WildSST using (fsuc ; weaken)

spinWAt000 : spinW 1 (fsuc fzero) (fsuc fzero) + (spinW 0 fzero fzero + spinW 1 (weaken fzero) (weaken fzero))
           ≡ spinW 0 fzero fzero + (spinW 1 (weaken fzero) (fsuc fzero) + spinW 0 fzero fzero)
spinWAt000 = refl
