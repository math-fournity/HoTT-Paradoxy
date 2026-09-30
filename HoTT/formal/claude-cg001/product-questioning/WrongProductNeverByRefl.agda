{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-81 (proof id MP-CG001-PRODUCT-QUESTIONING-NEG-002).
  Claims by refl that the questioning of the product is never.  Expected:
  rejected; computation alone never shows that a program does not halt
  (coinductive records have no eta, and the two sides are different
  programs), so C-81 (c) needs the corecursive proof imported from C-77.
-}
module WrongProductNeverByRefl where

open import Cubical.Foundations.Prelude
open import PedometerSemantics using (never)
open import QuestioningDelay using (question)
open import ProductQuestioning using (Prod; judgeProd)

wrong : question Prod judgeProd ≡ never
wrong = refl
