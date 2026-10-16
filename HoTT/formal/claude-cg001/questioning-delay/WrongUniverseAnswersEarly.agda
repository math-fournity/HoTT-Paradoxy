{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-78 (proof id MP-CG001-QUESTIONING-DELAY-NEG-001).
  Claims that the questioning of the universe, run with the judge judgeU for
  one step, returns level 1.  Expected: rejected; the kernel runs the program,
  the judge answers no at levels 1 and 2, and the run gets nothing
  (nothing != just 1).
-}
module WrongUniverseAnswersEarly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question; judgeU)

wrong : runFor 1 (question (Type ℓ-zero) judgeU) ≡ just 1
wrong = refl
