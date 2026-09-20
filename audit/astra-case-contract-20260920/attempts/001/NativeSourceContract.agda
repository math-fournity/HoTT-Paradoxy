{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeSourceContract where

-- Supplied source data and a precise diagram denotation; no physical provenance oracle.
open import hott-z.NativeRealCircleQualification
open import hott-z.StereographicContinuity
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import hott-z.NativeRichCurve
open import hott-z.NativeCurveTask using (AmbientStep; EndCoincidence; Success; noSuccessMtoN)
open import hott-z.NativeCurveTaskControls
open import hott-z.FiniteTrace
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.identity-types
open import foundation.transport-along-identifications
open import foundation.equivalences
open import foundation.univalence
open import foundation.negation
open import foundation.empty-types

record Input : UU (lsuc (lsuc lzero)) where
  field
    source : RichCurve
    targetCarrier : UU (lsuc lzero)
    encoding : Bare source ≃ targetCarrier

State Output : Input → UU (lsuc (lsuc lzero))
State i = RichCurve
Output i = RichCurve

initial : (i : Input) → State i
initial = Input.source

Step : (i : Input) → State i → State i → UU (lsuc lzero)
Step i = AmbientStep

Observation : Input → UU (lsuc lzero)
Observation i = ClosedParameter → RealPlane

observe : (i : Input) → State i → Observation i
observe i = closedImage

Denotes : (i : Input) → State i → UU (lsuc lzero)
Denotes i r = (u : ClosedParameter) → observe i r u ＝ observe i (Input.source i) u

Satisfies : (i : Input) → Output i → UU (lsuc (lsuc lzero))
Satisfies i r = (Bare r ＝ Input.targetCarrier i) × Denotes i r

carrierPath : (i : Input) → Bare (Input.source i) ＝ Input.targetCarrier i
carrierPath i = eq-equiv (Input.encoding i)

reexpressed : (i : Input) → Output i
reexpressed i = Input.targetCarrier i , tr CurveData (carrierPath i) (pr2 (Input.source i))

reexpressionPath : (i : Input) → Input.source i ＝ reexpressed i
reexpressionPath i = packTransport (carrierPath i) (pr2 (Input.source i))

denotesReexpression : (i : Input) → Denotes i (reexpressed i)
denotesReexpression i = transportKeepsClosedImage (carrierPath i) (pr2 (Input.source i))

satisfiesReexpression : (i : Input) → Satisfies i (reexpressed i)
satisfiesReexpression i = refl , denotesReexpression i

Done : (i : Input) → State i → UU (lsuc (lsuc lzero))
Done i r = r ＝ reexpressed i

Run : Input → UU (lsuc (lsuc lzero))
Run i = FiniteSuccess (Step i) (initial i) (Done i)

runReexpression : (i : Input) → Run i
runReexpression i = reexpressed i , step (richPathStep (reexpressionPath i)) stop , refl

doneIsSound : (i : Input) (r : State i) → Done i r → Satisfies i r
doneIsSound i r done = tr (Satisfies i) (inv done) (satisfiesReexpression i)

checkedOutput : (i : Input) → Run i → Σ (Output i) (Satisfies i)
checkedOutput i (r , trace , done) = r , doneIsSound i r done

actualInput : Input
Input.source actualInput = mRich
Input.targetCarrier actualInput = OpenRealInterval
Input.encoding actualInput = homeomorphismEquiv strongCircleUnitHomeomorphism

actualOutputIsTransported : reexpressed actualInput ＝ transportedRich
actualOutputIsTransported = refl

actualRun : Run actualInput
actualRun = runReexpression actualInput

actualCheckedOutput : Σ (Output actualInput) (Satisfies actualInput)
actualCheckedOutput = checkedOutput actualInput actualRun

plainNBareAccepted : Bare nRich ＝ Input.targetCarrier actualInput
plainNBareAccepted = refl

plainNDoesNotDenote : ¬ (Denotes actualInput nRich)
plainNDoesNotDenote h = nSeparate (h closedZero ∙ mCoincident ∙ inv (h closedOne))

plainNNotSatisfied : ¬ (Satisfies actualInput nRich)
plainNNotSatisfied h = plainNDoesNotDenote (pr2 h)

bareCheckIsInsufficient : ¬ ((r : Output actualInput) →
  Bare r ＝ Input.targetCarrier actualInput → Denotes actualInput r)
bareCheckIsInsufficient sound = plainNDoesNotDenote (sound nRich plainNBareAccepted)

actualOutputNotPlainN : ¬ (reexpressed actualInput ＝ nRich)
actualOutputNotPlainN h = plainNDoesNotDenote
  (tr (Denotes actualInput) h (denotesReexpression actualInput))

straightTargetStillFails : ¬ (Success (initial actualInput , nRich))
straightTargetStillFails = noSuccessMtoN
