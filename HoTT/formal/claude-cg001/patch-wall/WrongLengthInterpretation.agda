{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-28 (MP-CG001-PATCH-WALL-NEG-001).
  Expected result: KERNEL_REJECTED.

  Claim tested: the length interpretation cannot be written as a family on
  the context HIT.  Defining F (doc n) = File n and sending the path add n
  to the constant path at File n leaves the end of the path at the wrong
  type, and the kernel must refuse it.
-}
module WrongLengthInterpretation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Bool using (Bool)
open import Cubical.Data.Unit using (Unit)
open import Cubical.Data.Sigma using (_×_)

File : ℕ → Type
File zero = Unit
File (suc n) = Bool × File n

data R : Type where
  doc : ℕ → R
  add : (n : ℕ) → doc n ≡ doc (suc n)

F : R → Type
F (doc n) = File n
F (add n i) = File n
