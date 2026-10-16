{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control MP-CG001-A-UNIVALENCE-B-NEG-002 (CG001-C-430).

  Claim to be refused: univalence alone gives B.  The gathering of the sets
  is univalent, but its members' heights are bounded.  The claim says its
  questioning is still silent after the second question.  Expected:
  rejected; the kernel runs the program, the second question answers yes,
  and the run is `just 2`, not `nothing`.
-}
module WrongBoundedNever where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (nothing)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question; gatheringJudge)
open import AUnivalenceB using (Collection; gathering)

open Collection

aloneKeepsSilent : runFor 1 (question (Code (gathering 1)) (gatheringJudge 1)) ≡ nothing
aloneKeepsSilent = refl
