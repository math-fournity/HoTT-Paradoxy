{-# OPTIONS --safe --cubical --guardedness #-}
-- Expected negative control for C-360.  The fake original halt witness must
-- be rejected at the original universe run, not merely at a missing import.
module WrongHoTTCounterexample where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)

open import PedometerSemantics using (runFor)
open import QuestioningDelay using (judgeU; question; module Questioning)
open import TruncationQuestioning using (TU; judgeTU)
open import HoTTCounterexample using (MathematicalIllusionP)

wrongP : MathematicalIllusionP
wrongP _ = 0 , 1 , refl
