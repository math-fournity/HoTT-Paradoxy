{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A direct completion-reflection control for ZFC-HoTT-Q2.

  This module does not judge whether replacing the original universe by its
  set truncation is the same user task.  It makes one narrower, formal point:
  the observed stage-one completion of the truncated question does not imply
  a finite halt of the original universe question.
-}
module CompletionReflectionFailure where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import Cubical.Relation.Nullary using (¬_)

open import PedometerSemantics using (runFor)
open import QuestioningDelay using
  (Judge; question; judgeU; universeQuestioningNeverAnswers; module Questioning)
open import TruncationQuestioning using (TU; judgeTU; truncUniverseStopsAtOne)

------------------------------------------------------------------------
-- C-358

-- A completion-reflecting observer would be allowed to infer a finite halt
-- of the original Q from the stage-one success of its set-truncated version.
-- The implication is written explicitly so that it cannot be silently
-- substituted for the result of a different task.
CompletionReflectsOriginalHalting : Type
CompletionReflectsOriginalHalting =
  runFor 0 (question TU judgeTU) ≡ just 1
  → Questioning.Halts (Type ℓ-zero) judgeU

coarseCompletionDoesNotReflectOriginalHalting :
  ¬ CompletionReflectsOriginalHalting
coarseCompletionDoesNotReflectOriginalHalting reflects =
  universeQuestioningNeverAnswers judgeU
    (reflects (truncUniverseStopsAtOne judgeTU))
