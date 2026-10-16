{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeCurveTask where

-- A stated ambient-homeomorphism task model, not all physical restoration.
open import hott-z.NativeRealCircleQualification
open import hott-z.StereographicContinuity
open import hott-z.NativeCompletion
open import hott-z.NativeRichCurve
open import hott-z.FiniteTrace
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.negation
open import foundation.empty-types
open import foundation.propositional-truncations

record AmbientStep (r s : RichCurve) : UU (lsuc lzero) where
  field
    motion : PointwiseHomeomorphism realPlaneMetric realPlaneMetric
    commutes : (u : ClosedParameter) → closedImage s u ＝
      PointwiseHomeomorphism.forward motion (closedImage r u)

stepKeepsCoincidence : (r s : RichCurve) → AmbientStep r s → EndCoincidence r → EndCoincidence s
stepKeepsCoincidence r s e h = AmbientStep.commutes e closedZero ∙
  ap (PointwiseHomeomorphism.forward (AmbientStep.motion e)) h ∙
  inv (AmbientStep.commutes e closedOne)

stepReflectsCoincidence : (r s : RichCurve) → AmbientStep r s → EndCoincidence s → EndCoincidence r
stepReflectsCoincidence r s e h =
  inv (PointwiseHomeomorphism.backwardForward (AmbientStep.motion e) (closedImage r closedZero)) ∙
  ap (PointwiseHomeomorphism.backward (AmbientStep.motion e))
    (inv (AmbientStep.commutes e closedZero) ∙ h ∙ AmbientStep.commutes e closedOne) ∙
  PointwiseHomeomorphism.backwardForward (AmbientStep.motion e) (closedImage r closedOne)

stepKeepsSeparation : (r s : RichCurve) → AmbientStep r s → ¬ (EndCoincidence r) → ¬ (EndCoincidence s)
stepKeepsSeparation r s e separate h = separate (stepReflectsCoincidence r s e h)

traceKeepsCoincidence : {r s : RichCurve} → Trace AmbientStep r s → EndCoincidence r → EndCoincidence s
traceKeepsCoincidence = tracePreserves EndCoincidence stepKeepsCoincidence

traceKeepsSeparation : {r s : RichCurve} → Trace AmbientStep r s → ¬ (EndCoincidence r) → ¬ (EndCoincidence s)
traceKeepsSeparation = tracePreserves (λ r → ¬ (EndCoincidence r)) stepKeepsSeparation

noTraceNtoM : ¬ (Trace AmbientStep nRich mRich)
noTraceNtoM p = traceKeepsSeparation p nSeparate mCoincident

noTraceMtoN : ¬ (Trace AmbientStep mRich nRich)
noTraceMtoN p = nSeparate (traceKeepsCoincidence p mCoincident)

CurveTask : UU (lsuc (lsuc lzero))
CurveTask = RichCurve × RichCurve

Done : CurveTask → RichCurve → UU (lsuc (lsuc lzero))
Done task r = r ＝ pr2 task

Success : CurveTask → UU (lsuc (lsuc lzero))
Success task = FiniteSuccess AmbientStep (pr1 task) (Done task)

MereSuccess : CurveTask → UU (lsuc (lsuc lzero))
MereSuccess task = type-trunc-Prop (Success task)

noSuccessNtoM : ¬ (Success (nRich , mRich))
noSuccessNtoM (r , trace , done) = noTraceNtoM (tr (Trace AmbientStep nRich) done trace)

noSuccessMtoN : ¬ (Success (mRich , nRich))
noSuccessMtoN (r , trace , done) = noTraceMtoN (tr (Trace AmbientStep mRich) done trace)

noMereSuccessNtoM : ¬ (MereSuccess (nRich , mRich))
noMereSuccessNtoM t = apply-universal-property-trunc-Prop t empty-Prop noSuccessNtoM

swapStep : AmbientStep nRich swappedN
AmbientStep.motion swapStep = swapHomeomorphism
AmbientStep.commutes swapStep u = refl

swapSuccess : Success (nRich , swappedN)
swapSuccess = swappedN , step swapStep stop , refl

swappedStillSeparate : ¬ (EndCoincidence swappedN)
swappedStillSeparate = stepKeepsSeparation nRich swappedN swapStep nSeparate

mereSwapSuccess : MereSuccess (nRich , swappedN)
mereSwapSuccess = unit-trunc-Prop swapSuccess

-- A different operation: a witnessed equality of intrinsic representations.
BareStep : UU (lsuc lzero) → UU (lsuc lzero) → UU (lsuc (lsuc lzero))
BareStep A B = A ＝ B

bareTrace : Trace BareStep (Bare mRich) (Bare nRich)
bareTrace = step barePath stop

bareSuccess : FiniteSuccess BareStep (Bare mRich) (λ A → A ＝ Bare nRich)
bareSuccess = Bare nRich , bareTrace , refl

noUniversalTraceLift :
  ¬ ((r s : RichCurve) → Trace BareStep (Bare r) (Bare s) → Trace AmbientStep r s)
noUniversalTraceLift lift = noTraceMtoN (lift mRich nRich bareTrace)
