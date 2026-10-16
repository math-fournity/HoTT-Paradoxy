{-# OPTIONS --safe --cubical --guardedness #-}
-- Negative control for C-358.  Pretending that the truncated completion
-- witnesses an original finite halt must be rejected at the original run.
module WrongCompletionReflection where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)

open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question; judgeU; module Questioning)
open import TruncationQuestioning using (TU; judgeTU)

CompletionReflectsOriginalHalting : Type
CompletionReflectsOriginalHalting =
  runFor 0 (question TU judgeTU) ≡ just 1
  → Questioning.Halts (Type ℓ-zero) judgeU

wrongCompletionReflection : CompletionReflectsOriginalHalting
wrongCompletionReflection _ = 0 , 1 , refl
