{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-82 (proof id MP-CG001-PRODUCT-QUESTIONING-NEG-003).
  Claims that the same program, run on the bounded product Bounded 0 =
  (n : ℕ) → K 0 with the judge judgeBounded 0, is still silent at fuel 1,
  as it is on the product of unbounded height.  Expected: rejected; the
  judge answers no at stage 1 and yes at stage 2, and the kernel computes
  just 2 (just 2 != nothing).
-}
module WrongBoundedSilent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (nothing)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question)
open import ProductQuestioning using (Bounded; judgeBounded)

wrong : runFor 1 (question (Bounded 0) (judgeBounded 0)) ≡ nothing
wrong = refl
