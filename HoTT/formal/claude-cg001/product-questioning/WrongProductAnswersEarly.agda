{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-81 (proof id MP-CG001-PRODUCT-QUESTIONING-NEG-001).
  Claims that the questioning of the product Prod = (n : ℕ) → K n, run with
  the judge judgeProd for one step, returns level 1.  Expected: rejected; the
  kernel runs the program, the judge answers no at stages 1 and 2, and the
  run gets nothing (nothing != just 1).
-}
module WrongProductAnswersEarly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question)
open import ProductQuestioning using (Prod; judgeProd)

wrong : runFor 1 (question Prod judgeProd) ≡ just 1
wrong = refl
