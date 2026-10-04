{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Native Cubical Agda certificate for the B side of the ZFC-1 policy model.

  The fixed HoTT question has a stage-one completion on its set truncation,
  while the original universe question has no finite halt witness.  Therefore
  the policy P “this coarse completion promotes to original finite halting” is
  rejected by the native HoTT proof.

  This does not formalize ZFC, IEP, an actual source policy, or the claim that
  the truncation and original question are the same user task.
-}
module HoTTCounterexample where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Relation.Nullary using (¬_)

open import PedometerSemantics using (runFor)
open import QuestioningDelay using
  (judgeU; question; universeQuestioningNeverAnswers; module Questioning)
open import TruncationQuestioning using (TU; judgeTU; truncUniverseStopsAtOne)
open import CompletionReflectionFailure using
  (CompletionReflectsOriginalHalting; coarseCompletionDoesNotReflectOriginalHalting)

------------------------------------------------------------------------
-- C-360: the fixed HoTT B certificate

-- This names the exact policy P rejected by C-358.
MathematicalIllusionP : Type
MathematicalIllusionP = CompletionReflectsOriginalHalting

-- The source-side formal completion exists at stage one.
coarseCompletion : runFor 0 (question TU judgeTU) ≡ just 1
coarseCompletion = truncUniverseStopsAtOne judgeTU

-- The original fixed Q has no finite halt witness.
originalCompletionFails : ¬ Questioning.Halts (Type ℓ-zero) judgeU
originalCompletionFails = universeQuestioningNeverAnswers judgeU

-- Therefore the fixed HoTT Q supplies a native counterexample to P.
hottCounterexampleToMathematicalIllusionP : ¬ MathematicalIllusionP
hottCounterexampleToMathematicalIllusionP =
  coarseCompletionDoesNotReflectOriginalHalting

-- The same result, expanded instead of imported, makes the A/B shape visible.
hottCounterexampleExpanded : MathematicalIllusionP → ⊥
hottCounterexampleExpanded p = originalCompletionFails (p coarseCompletion)
