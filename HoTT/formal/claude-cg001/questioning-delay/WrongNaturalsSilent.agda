{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-79 (proof id MP-CG001-QUESTIONING-DELAY-NEG-002).
  Claims that the same program, run on ℕ with the judge judgeℕ, is silent at
  fuel 0, as it is on the universe.  Expected: rejected; the judge answers
  yes at level 1 and the kernel computes just 1 (just 1 != nothing).
-}
module WrongNaturalsSilent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Maybe using (nothing)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question; judgeℕ)

wrong : runFor 0 (question ℕ judgeℕ) ≡ nothing
wrong = refl
