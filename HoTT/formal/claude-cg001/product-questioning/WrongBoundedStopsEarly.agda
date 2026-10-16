{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-82 (proof id MP-CG001-PRODUCT-QUESTIONING-NEG-004).
  Claims that on the bounded product Bounded 0 = (n : ℕ) → K 0 the program
  stops at stage 1, as it does on ℕ.  Expected: rejected; with the judge
  judgeBounded 0 the kernel computes that stage 1 is answered no (the
  product is not a set), so fuel 0 gives nothing (nothing != just 1).
-}
module WrongBoundedStopsEarly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question)
open import ProductQuestioning using (Bounded; judgeBounded)

wrong : runFor 0 (question (Bounded 0) (judgeBounded 0)) ≡ just 1
wrong = refl
