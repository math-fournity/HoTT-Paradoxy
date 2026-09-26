{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-55 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-SEMANTICS-NEG-001

  Under the P-rev specification (return = sym go, the counter carried by
  subst), the stop-at-+2 program is run for one step on the escape HIT.  A
  real walker stops after one round trip; claiming by refl that the program
  has returned 1 after one step must be rejected: the kernel runs it and
  finds nothing.
-}
module WrongPRevHalts where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int using (ℤ; pos; abs)
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor; module PRevProgram; module Escape)
open Escape using (Places; west; go; Ped)

pRevHaltsLikeTheWalker : runFor 1 (PRevProgram.stopProgram go Ped abs (pos 0)) ≡ just 1
pRevHaltsLikeTheWalker = refl
