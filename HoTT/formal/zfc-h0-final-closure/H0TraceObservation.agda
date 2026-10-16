{-# OPTIONS --safe --cubical --guardedness #-}
{-
  M1 fragment for ZFC-H0-FINAL-PROOF-CLOSURE-SOP.

  This source does not construct a model of all Cubical Agda in ZFC or in
  CCHM cubical sets.  It fixes the exact operational fragment used by H0:
  `Delay ℕ`, its finite `runFor` observation, and the universe question from
  QuestioningDelay.  Its target is the set-valued trace ℕ → Maybe ℕ.

  The point is deliberately limited and useful: `question (Type ℓ-zero) judge`
  is mapped to the all-nothing trace for every Judge, while a known bounded
  control maps to a trace with a finite answer.  Any later full H0Map has to
  preserve this already-fixed trace interface.

  This is an H0 operational-fragment theorem, not a semantic interpretation
  of EM1/HIT/univalence or an assertion about bare ZFC.
-}
module H0TraceObservation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isSetΠ)
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.Maybe.Properties using (isOfHLevelMaybe; ¬nothing≡just)
open import Cubical.Relation.Nullary using (¬_)

open import PedometerSemantics using (Delay; never; runFor)
open import DelayMonad using (runForNever)
open import QuestioningDelay using
  (Judge; question; judgeU; universeQuestioningRunsNothing)

------------------------------------------------------------------------
-- The set-valued finite-observation target

Trace : Type₀
Trace = ℕ → Maybe ℕ

trace : Delay ℕ → Trace
trace d fuel = runFor fuel d

silentTrace : Trace
silentTrace _ = nothing

Maybeℕ-isSet : isSet (Maybe ℕ)
Maybeℕ-isSet = isOfHLevelMaybe 0 isSetℕ

Trace-isSet : isSet Trace
Trace-isSet = isSetΠ (λ _ → Maybeℕ-isSet)

------------------------------------------------------------------------
-- The exact H0 observation bridge

trace-never : trace never ≡ silentTrace
trace-never = funExt runForNever

trace-respects-path : (d e : Delay ℕ) → d ≡ e → trace d ≡ trace e
trace-respects-path d e p = cong trace p

trace-universe-question :
  (judge : Judge (Type ℓ-zero)) →
  trace (question (Type ℓ-zero) judge) ≡ silentTrace
trace-universe-question judge =
  funExt (universeQuestioningRunsNothing judge)

universe-trace-has-no-finite-answer :
  (judge : Judge (Type ℓ-zero)) (fuel answer : ℕ) →
  ¬ (trace (question (Type ℓ-zero) judge) fuel ≡ just answer)
universe-trace-has-no-finite-answer judge fuel answer traceAnswer =
  ¬nothing≡just
    ((sym (cong (λ t → t fuel) (trace-universe-question judge)))
      ∙ traceAnswer)

------------------------------------------------------------------------
-- A concrete target-level control: H0 is not silently reclassified as halt.

universe-trace-zero-is-nothing :
  trace (question (Type ℓ-zero) judgeU) 0 ≡ nothing
universe-trace-zero-is-nothing =
  cong (λ t → t 0) (trace-universe-question judgeU)

universe-trace-zero-is-not-one :
  ¬ (trace (question (Type ℓ-zero) judgeU) 0 ≡ just 1)
universe-trace-zero-is-not-one =
  universe-trace-has-no-finite-answer judgeU 0 1
