{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-79 (proof id MP-CG001-QUESTIONING-DELAY-NEG-003).
  Claims that on the catalogue of sets the program stops at step 1, as it
  does on ℕ.  Expected: rejected; with the judge gatheringJudge 1 the kernel
  computes that level 1 is answered no, so fuel 0 gives nothing
  (nothing != just 1).
-}
module WrongSetsStopAtOne where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (hSet)
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (question; gatheringJudge)

wrong : runFor 0 (question (hSet ℓ-zero) (gatheringJudge 1)) ≡ just 1
wrong = refl
