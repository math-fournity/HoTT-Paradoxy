{-# OPTIONS --safe --cubical --guardedness #-}
-- Negative control for CG001-C-113: on the univalent universe the same search does
-- not answer at the first stage (it never answers, C-78).  The kernel computes
-- `nothing`, so this claim must be rejected.
module WrongH0Settles where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import PedometerSemantics using (runFor)
open import QuestioningDelay using (judgeU)
open import SameQ

wrongH0Settles : runFor 0 (askQ (FromJudge.answers (Type ℓ-zero) judgeU) 1) ≡ just 1
wrongH0Settles = refl
