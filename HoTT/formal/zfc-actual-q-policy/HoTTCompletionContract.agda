{-# OPTIONS --safe --cubical --guardedness #-}
{-
  `C-363` packages the fixed Cubical Agda B witness as a completion-contract
  gap.  It proves a shared abstract shape with C-362, not an identity between
  Zeno's action task and the HoTT question.
-}
module HoTTCompletionContract where

open import Cubical.Foundations.Prelude
open import Cubical.Relation.Nullary using (¬_)

open import HoTTCounterexample using
  (coarseCompletion; originalCompletionFails; MathematicalIllusionP)

record CompletionGap : Type₁ where
  field
    RevisedDone  : Type
    OriginalDone : Type
    revisedWitness : RevisedDone
    noOriginal : ¬ OriginalDone

open CompletionGap

noBridge : (gap : CompletionGap) → ¬ (RevisedDone gap → OriginalDone gap)
noBridge gap bridge = noOriginal gap (bridge (revisedWitness gap))

-- The exact fixed HoTT gap used by C-360.
hottCompletionGap : CompletionGap
hottCompletionGap = record
  { RevisedDone = _ ≡ _
  ; OriginalDone = _
  ; revisedWitness = coarseCompletion
  ; noOriginal = originalCompletionFails
  }

hottCompletionGapHasNoBridge : ¬ (RevisedDone hottCompletionGap → OriginalDone hottCompletionGap)
hottCompletionGapHasNoBridge = noBridge hottCompletionGap

-- This restates C-360's policy failure through the generic contract schema.
hottPIsNotABridge : ¬ MathematicalIllusionP
hottPIsNotABridge promotion = originalCompletionFails (promotion coarseCompletion)
