{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-83 (proof id MP-CG001-TRUNCATION-QUESTIONING-NEG-002).

  Claims by refl that transport along notEq leaves true where it is, that is,
  that the second self-identification of Bool acts like refl before any
  truncation.  Expected rejection: the kernel computes the transport to
  false, so false != true.
-}
module WrongNotEqTrivial where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEq)

notEqActsTrivially : transport notEq true ≡ true
notEqActsTrivially = refl
