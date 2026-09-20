{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeRichCurve where

-- Intrinsic carriers with their actual parametrization and closed-plane diagram.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.StereographicContinuity
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.equivalences
open import foundation.negation
open import foundation.existential-quantification
open import real-numbers.rational-real-numbers

record CurveData (A : UU (lsuc lzero)) : UU (lsuc lzero) where
  field
    parametrization : OpenRealInterval ≃ A
    realize : A → RealPlane
    close : ClosedParameter → RealPlane
    closeContinuous : Cont closedMetric realPlaneMetric close
    agrees : (u : OpenRealInterval) →
      close (openIntoClosed u) ＝ realize (map-equiv parametrization u)

RichCurve : UU (lsuc (lsuc lzero))
RichCurve = Σ (UU (lsuc lzero)) CurveData

Bare : RichCurve → UU (lsuc lzero)
Bare = pr1

closedImage : RichCurve → ClosedParameter → RealPlane
closedImage r = CurveData.close (pr2 r)

mData : CurveData StrongPuncture
CurveData.parametrization mData =
  PointwiseHomeomorphism.backward strongCircleUnitHomeomorphism ,
  is-equiv-is-invertible (PointwiseHomeomorphism.forward strongCircleUnitHomeomorphism)
    (PointwiseHomeomorphism.backwardForward strongCircleUnitHomeomorphism)
    (PointwiseHomeomorphism.forwardBackward strongCircleUnitHomeomorphism)
CurveData.realize mData w = pr1 (pr1 w)
CurveData.close mData u = pr1 (mCompletion u)
CurveData.closeContinuous mData = mCompletionContinuous
CurveData.agrees mData u = ap pr1 (mInterior u)

nData : CurveData OpenRealInterval
CurveData.parametrization nData = (λ u → u) ,
  is-equiv-is-invertible (λ u → u) (λ _ → refl) (λ _ → refl)
CurveData.realize nData u = pr1 u , zero-ℝ
CurveData.close nData = nCompletion
CurveData.closeContinuous nData = nCompletionContinuous
CurveData.agrees nData u = refl

mRich nRich : RichCurve
mRich = StrongPuncture , mData
nRich = OpenRealInterval , nData

barePath : Bare mRich ＝ Bare nRich
barePath = strongIntervalTypePath

EndCoincidence : RichCurve → UU (lsuc lzero)
EndCoincidence r = closedImage r closedZero ＝ closedImage r closedOne

mCoincident : EndCoincidence mRich
mCoincident = ap pr1 mEndsCoincide

nSeparate : ¬ (EndCoincidence nRich)
nSeparate = nEndsDistinct

noRichPath : ¬ (mRich ＝ nRich)
noRichPath p = nSeparate (tr EndCoincidence p mCoincident)

packTransport : {A B : UU (lsuc lzero)} (p : A ＝ B) (d : CurveData A) →
  (A , d) ＝ (B , tr CurveData p d)
packTransport refl d = refl

transportedM : CurveData OpenRealInterval
transportedM = tr CurveData barePath mData

transportedRich : RichCurve
transportedRich = OpenRealInterval , transportedM

fullTransportPath : mRich ＝ transportedRich
fullTransportPath = packTransport barePath mData

fullTransportKeepsEnds : EndCoincidence transportedRich
fullTransportKeepsEnds = tr EndCoincidence fullTransportPath mCoincident

transportKeepsClosedImage : {A B : UU (lsuc lzero)} (p : A ＝ B)
  (d : CurveData A) (u : ClosedParameter) →
  CurveData.close (tr CurveData p d) u ＝ CurveData.close d u
transportKeepsClosedImage refl d u = refl

noAnyBarePathLift : (p : StrongPuncture ＝ OpenRealInterval) →
  ¬ (tr CurveData p mData ＝ nData)
noAnyBarePathLift p h = noRichPath (packTransport p mData ∙ ap (λ d → OpenRealInterval , d) h)

noUniformBareRecovery : (recover : UU (lsuc lzero) → RichCurve) →
  recover StrongPuncture ＝ mRich → recover OpenRealInterval ＝ nRich → empty
noUniformBareRecovery recover hm hn = noRichPath (inv hm ∙ ap recover barePath ∙ hn)

postCompose : {A : UU (lsuc lzero)} →
  PointwiseHomeomorphism realPlaneMetric realPlaneMetric → CurveData A → CurveData A
CurveData.parametrization (postCompose h d) = CurveData.parametrization d
CurveData.realize (postCompose h d) x = PointwiseHomeomorphism.forward h (CurveData.realize d x)
CurveData.close (postCompose h d) u = PointwiseHomeomorphism.forward h (CurveData.close d u)
CurveData.closeContinuous (postCompose h d) =
  composeContinuous closedMetric realPlaneMetric realPlaneMetric
    (PointwiseHomeomorphism.forward h) (CurveData.close d)
    (PointwiseHomeomorphism.forwardContinuous h) (CurveData.closeContinuous d)
CurveData.agrees (postCompose h d) u = ap (PointwiseHomeomorphism.forward h) (CurveData.agrees d u)

swapPlane : RealPlane → RealPlane
swapPlane p = pr2 p , pr1 p

firstPlaneContinuous : Cont realPlaneMetric realMetric pr1
firstPlaneContinuous p = intro-exists (λ ε → ε) (λ ε q near → pr1 near)

secondPlaneContinuous : Cont realPlaneMetric realMetric pr2
secondPlaneContinuous p = intro-exists (λ ε → ε) (λ ε q near → pr2 near)

swapContinuous : Cont realPlaneMetric realPlaneMetric swapPlane
swapContinuous = pairContinuous realPlaneMetric realMetric realMetric pr2 pr1
  secondPlaneContinuous firstPlaneContinuous

swapHomeomorphism : PointwiseHomeomorphism realPlaneMetric realPlaneMetric
PointwiseHomeomorphism.forward swapHomeomorphism = swapPlane
PointwiseHomeomorphism.backward swapHomeomorphism = swapPlane
PointwiseHomeomorphism.forwardContinuous swapHomeomorphism = swapContinuous
PointwiseHomeomorphism.backwardContinuous swapHomeomorphism = swapContinuous
PointwiseHomeomorphism.forwardBackward swapHomeomorphism p = refl
PointwiseHomeomorphism.backwardForward swapHomeomorphism p = refl

swappedN : RichCurve
swappedN = OpenRealInterval , postCompose swapHomeomorphism nData

swappedEnd : closedImage swappedN closedOne ＝ (zero-ℝ , one-ℝ)
swappedEnd = refl

swapActuallyChangesCurve : ¬ (nRich ＝ swappedN)
swapActuallyChangesCurve p = neq-zero-one-ℝ (ap (λ r → pr2 (closedImage r closedOne)) p)
