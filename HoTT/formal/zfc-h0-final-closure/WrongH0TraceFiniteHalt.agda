{-# OPTIONS --safe --cubical --guardedness #-}
-- Expected negative control for M1: the exact H0 trace cannot be made to
-- report a finite answer merely by changing the target-level description.
module WrongH0TraceFiniteHalt where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)

open import H0TraceObservation using (trace)
open import QuestioningDelay using (judgeU; question)

wrong-h0-trace-halt :
  trace (question (Type ℓ-zero) judgeU) 0 ≡ just 1
wrong-h0-trace-halt = refl
