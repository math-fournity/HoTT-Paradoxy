{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control MP-CG001-TWO-CHOICES-CUBICAL-NEG-001 (CG-010 R4).

  Rejected claim: the universe's questioning gets an answer at stage 1, i.e.
  the answer stream of the univalent universe (with the judge judgeU of C-78)
  reads "yes" at stage 1, as it would if the universe were a set.  Expected:
  the kernel computes false != true.  Positive counterparts:
  UniverseAnswers.allNo and universeRun100.
-}
module WrongUniverseSettles where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (true)
open import QuestioningDelay using (judgeU)
open import SameQ using (module FromJudge)

universeAnswersYesAtOne : FromJudge.answers (Type ℓ-zero) judgeU 1 ≡ true
universeAnswersYesAtOne = refl
