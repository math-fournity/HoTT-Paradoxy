{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A formal control for the ZFC-HoTT observation investigation.

  It does not formalize ZFC, a simplicial model, model acceptance, or a
  reality/UR verdict.  It only packages three already independent facts about
  one fixed Cubical Agda universe:

    * the original h-level questioning process is `never`;
    * the same question on its set truncation returns at stage one; and
    * the truncation has no uniform section back to the original universe.

  The point is proof-level: a completion-changing observation can be a genuine
  construction while failing to preserve the original object.  A later source
  must still show that a real model or foundational acceptance contract uses
  this observation before any conclusion about ZFC is possible.
-}
module ObservationCompletionBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import Cubical.Data.Sigma
open import Cubical.HITs.SetTruncation as ST using (∣_∣₂)
open import Cubical.Relation.Nullary using (¬_)

open import PedometerSemantics using (never; runFor)
open import QuestioningDelay using (Judge; question; judgeU)
open import TruncationQuestioning using
  (TU; judgeTU; universeSideBySide; noDecoding)

------------------------------------------------------------------------
-- CG001-C-84

-- The conjunction uses the original universe, its set truncation, and the
-- fixed judges supplied by the existing C-78/C-83 packages.  It is a compact
-- bridge-control theorem, not a claim that either representation is wrong.
coarseCompletionCreatesNoRestoration :
  (question (Type ℓ-zero) judgeU ≡ never)
  × (runFor 0 (question TU judgeTU) ≡ just 1)
  × ¬ (Σ[ g ∈ (TU → Type ℓ-zero) ] ((A : Type ℓ-zero) → g ∣ A ∣₂ ≡ A))
coarseCompletionCreatesNoRestoration =
  fst (universeSideBySide judgeU judgeTU) ,
  snd (universeSideBySide judgeU judgeTU) ,
  noDecoding
