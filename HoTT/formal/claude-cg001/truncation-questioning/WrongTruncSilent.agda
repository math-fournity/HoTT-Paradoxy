{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-83 (proof id MP-CG001-TRUNCATION-QUESTIONING-NEG-001).

  Claims by refl that the questioning of the set truncation of the universe,
  with judgeTU, is still silent at fuel 0.  Expected rejection: the kernel
  runs the program, the judge answers yes at stage 1, and the run returns
  just 1, so just 1 != nothing.
-}
module WrongTruncSilent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (Maybe; nothing; just)

open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question)
open import TruncationQuestioning using (TU; judgeTU)

truncStillSilent : runFor 0 (question TU judgeTU) ≡ nothing
truncStillSilent = refl
