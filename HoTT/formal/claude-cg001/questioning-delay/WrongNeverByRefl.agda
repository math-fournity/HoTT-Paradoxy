{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-78 (proof id MP-CG001-QUESTIONING-DELAY-NEG-004).
  Claims by refl that the questioning of the universe is never.  Expected:
  rejected; computation alone never shows that a program does not halt
  (coinductive records have no eta, and the two sides are different
  programs), so C-78 (a) needs the corecursive proof of the main file.
-}
module WrongNeverByRefl where

open import Cubical.Foundations.Prelude
open import PedometerSemantics using (never)
open import QuestioningDelay using (question; judgeU)

wrong : question (Type ℓ-zero) judgeU ≡ never
wrong = refl
