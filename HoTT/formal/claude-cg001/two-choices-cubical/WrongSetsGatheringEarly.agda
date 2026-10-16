{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control MP-CG001-TWO-CHOICES-CUBICAL-NEG-002 (CG-010 R4).

  Rejected claim: the gathering of the sets (TypeOfHLevel ℓ-zero 2) answers
  the questioning already at stage 1, as it would if it were a set.  By
  univalence it is not a set (C-76), so stage 1 answers "no" and the answer
  comes at stage 2.  Expected: the kernel computes nothing, not just 1.
  Positive counterparts: setsGatheringRun, Stage.stopsAtStage.
-}
module WrongSetsGatheringEarly where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question)
open import TwoChoicesCubical using (stageJudge)

setsAnswerAtOne : runFor 0 (question (TypeOfHLevel ℓ-zero 2) (stageJudge 1)) ≡ just 1
setsAnswerAtOne = refl
