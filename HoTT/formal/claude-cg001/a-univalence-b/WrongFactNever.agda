{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control MP-CG001-A-UNIVALENCE-B-NEG-001 (CG001-C-430).

  Claim to be refused: A alone gives B.  The numbered collection hands over
  every height at once (codes ℕ, members EM ℤ (1+n)), but the sameness of its
  codes is a fact.  The claim says its questioning is still silent at the
  first question.  Expected: rejected; the kernel runs the program, the first
  question answers yes, and the run is `just 1`, not `nothing`.
-}
module WrongFactNever where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (nothing)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question; judgeℕ)
open import AUnivalenceB using (Collection; numbered)

open Collection

aloneKeepsSilent : runFor 0 (question (Code numbered) judgeℕ) ≡ nothing
aloneKeepsSilent = refl
