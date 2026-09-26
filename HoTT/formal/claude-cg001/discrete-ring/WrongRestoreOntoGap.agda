{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-42 (expected KERNEL_REJECTED).
  proof id : MP-CG001-DISCRETE-RING-NEG-001

  The first point of the unfolded segment is restored next to the gap, not
  onto the removed point: claiming by refl that it lands on fzero must be
  rejected (1 != 0).  Self-contained.
-}
module WrongRestoreOntoGap where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Nat.Order using (suc-≤-suc; zero-≤)
open import Cubical.Data.Fin using (Fin; fzero; fsuc)

firstPoint : Fin 3
firstPoint = (0 , suc-≤-suc zero-≤)

wrongRestoreOntoGap : Path (Fin 4) (fsuc firstPoint) fzero
wrongRestoreOntoGap = refl
