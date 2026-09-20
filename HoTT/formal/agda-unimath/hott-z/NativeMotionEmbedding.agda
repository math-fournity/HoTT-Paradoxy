{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeMotionEmbedding where

-- Each actual time slice is a homeomorphism onto its image equipped with the
-- ambient plane subspace metric. This is stronger than set-level injectivity.
open import hott-z.NativeMotion
open import hott-z.NativeMotionBridge
open import hott-z.NativeStretchInverse
open import hott-z.NativeBendInverse
open import hott-z.NativeTurnInverse
open import hott-z.NativeRealCircleQualification
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.propositions
open import foundation.propositional-truncations
open import foundation.existential-quantification
open import foundation.images
open import metric-spaces.metric-spaces
open import metric-spaces.images-metric-spaces
open import real-numbers.positive-real-numbers

curveImageMetric : Real → Space
curveImageMetric t = im-Metric-Space intervalMetric realPlaneMetric (motion t)

CurveImage : Real → UU (lsuc lzero)
CurveImage t = type-Metric-Space (curveImageMetric t)

imageInduction : {l : Level} (t : Real) (P : CurveImage t → Prop l) →
  ((u : OpenRealInterval) → type-Prop (P (map-unit-im (motion t) u))) →
  (v : CurveImage t) → type-Prop (P v)
imageInduction t P step v = apply-universal-property-trunc-Prop (pr2 v) (P v)
  (λ (u , h) → tr (λ z → type-Prop (P z))
    (eq-Eq-im (motion t) (map-unit-im (motion t) u) v h) (step u))

reflectYContinuous : Cont realPlaneMetric realPlaneMetric reflectY
reflectYContinuous = pairContinuous realPlaneMetric realMetric realMetric pr1
  (λ v → pr2 (reflectY v)) (firstContinuous realMetric realMetric)
  (negContinuous realPlaneMetric pr2 (secondContinuous realMetric realMetric))

reverseTurn : Real → RealPlane → RealPlane
reverseTurn t v = turnUndo t (reflectY v)

reverseTurnContinuous : (t : Real) → Cont realPlaneMetric realPlaneMetric (reverseTurn t)
reverseTurnContinuous t = composeContinuous realPlaneMetric realPlaneMetric realPlaneMetric
  (turnUndo t) reflectY (turnUndoContinuous t) reflectYContinuous

reverseTurnOnCurve : (t : Real) (u : OpenRealInterval) →
  reverseTurn t (motion t u) ＝ bend t (stretch t (realParameter u))
reverseTurnOnCurve t u = ap (turnUndo t) (reflectionInvolution (motionRaw t u)) ∙
  turnLeftInverse t (bend t (stretch t (realParameter u)))

imageInclusionContinuous : (t : Real) → Cont (curveImageMetric t) realPlaneMetric pr1
imageInclusionContinuous t v = intro-exists (λ ε → ε) (λ ε w near → near)

imageBendPositive : (t : Real) (v : CurveImage t) →
  is-positive-ℝ (bendInverseDen t (reverseTurn t (pr1 v)))
imageBendPositive t = imageInduction t
  (λ v → is-positive-prop-ℝ (bendInverseDen t (reverseTurn t (pr1 v))))
  (λ u → tr is-positive-ℝ (inv (ap (bendInverseDen t) (reverseTurnOnCurve t u)))
    (pr2 (bendChartPoint t (stretch t (realParameter u)))))

imageBendPoint : (t : Real) → CurveImage t → BendChart t
imageBendPoint t v = reverseTurn t (pr1 v) , imageBendPositive t v

imageBendPointOnCurve : (t : Real) (u : OpenRealInterval) →
  imageBendPoint t (map-unit-im (motion t) u) ＝ bendChartPoint t (stretch t (realParameter u))
imageBendPointOnCurve t u = eq-type-subtype (bendChartSubtype t) (reverseTurnOnCurve t u)

imageBendValue : (t : Real) → CurveImage t → Real
imageBendValue t v = bendInverse t (imageBendPoint t v)

imageBendOnCurve : (t : Real) (u : OpenRealInterval) →
  imageBendValue t (map-unit-im (motion t) u) ＝ stretch t (realParameter u)
imageBendOnCurve t u = ap (bendInverse t) (imageBendPointOnCurve t u) ∙
  bendLeftInverse t (stretch t (realParameter u))

imageBendPointContinuous : (t : Real) → Cont (curveImageMetric t) (bendChartMetric t) (imageBendPoint t)
imageBendPointContinuous t = composeContinuous (curveImageMetric t) realPlaneMetric realPlaneMetric
  (reverseTurn t) pr1 (reverseTurnContinuous t) (imageInclusionContinuous t)

imageBendValueContinuous : (t : Real) → Cont (curveImageMetric t) realMetric (imageBendValue t)
imageBendValueContinuous t = composeContinuous (curveImageMetric t) (bendChartMetric t) realMetric
  (bendInverse t) (imageBendPoint t) (bendInverseContinuous t) (imageBendPointContinuous t)

imageStretchPositive : (t : Real) (v : CurveImage t) →
  is-positive-ℝ (unsqueezeDen t (affineUndo t (imageBendValue t v)))
imageStretchPositive t = imageInduction t
  (λ v → is-positive-prop-ℝ (unsqueezeDen t (affineUndo t (imageBendValue t v))))
  (λ u → tr is-positive-ℝ (inv (ap (λ r → unsqueezeDen t (affineUndo t r)) (imageBendOnCurve t u)))
    (pr2 (stretchChartPoint t (realParameter u))))

imageStretchPoint : (t : Real) → CurveImage t → StretchChart t
imageStretchPoint t v = imageBendValue t v , imageStretchPositive t v

imageStretchOnCurve : (t : Real) (u : OpenRealInterval) →
  imageStretchPoint t (map-unit-im (motion t) u) ＝ stretchChartPoint t (realParameter u)
imageStretchOnCurve t u = eq-type-subtype (stretchChartSubtype t) (imageBendOnCurve t u)

recoverReal : (t : Real) → CurveImage t → Real
recoverReal t v = stretchInverse t (imageStretchPoint t v)

recoverRealOnCurve : (t : Real) (u : OpenRealInterval) →
  recoverReal t (map-unit-im (motion t) u) ＝ realParameter u
recoverRealOnCurve t u = ap (stretchInverse t) (imageStretchOnCurve t u) ∙
  stretchLeftInverse t (realParameter u)

recoverRealContinuous : (t : Real) → Cont (curveImageMetric t) realMetric (recoverReal t)
recoverRealContinuous t = composeContinuous (curveImageMetric t) (stretchChartMetric t) realMetric
  (stretchInverse t) (imageStretchPoint t) (stretchInverseContinuous t) (imageBendValueContinuous t)

recoverInterval : (t : Real) → CurveImage t → OpenRealInterval
recoverInterval t v = PointwiseHomeomorphism.forward realUnitHomeomorphism (recoverReal t v)

recoverIntervalContinuous : (t : Real) → Cont (curveImageMetric t) intervalMetric (recoverInterval t)
recoverIntervalContinuous t = composeContinuous (curveImageMetric t) realMetric intervalMetric
  (PointwiseHomeomorphism.forward realUnitHomeomorphism) (recoverReal t)
  (PointwiseHomeomorphism.forwardContinuous realUnitHomeomorphism) (recoverRealContinuous t)

recoverIntervalLeft : (t : Real) (u : OpenRealInterval) →
  recoverInterval t (map-unit-im (motion t) u) ＝ u
recoverIntervalLeft t u = ap (PointwiseHomeomorphism.forward realUnitHomeomorphism) (recoverRealOnCurve t u) ∙
  PointwiseHomeomorphism.forwardBackward realUnitHomeomorphism u

recoverIntervalRight : (t : Real) (v : CurveImage t) →
  map-unit-im (motion t) (recoverInterval t v) ＝ v
recoverIntervalRight t = imageInduction t
  (λ v → eq-prop-Metric-Space (curveImageMetric t) (map-unit-im (motion t) (recoverInterval t v)) v)
  (λ u → ap (map-unit-im (motion t)) (recoverIntervalLeft t u))

motionSliceContinuous : (t : Real) → Cont intervalMetric realPlaneMetric (motion t)
motionSliceContinuous t = composeContinuous intervalMetric motionDomain realPlaneMetric
  (λ z → motion (pr1 z) (pr2 z)) (λ u → t , u) motionContinuous
  (pairContinuous intervalMetric realMetric intervalMetric (λ _ → t) (λ u → u)
    (constantContinuous intervalMetric t) (λ u → intro-exists (λ ε → ε) (λ ε v near → near)))

motionSliceHomeomorphism : (t : Real) → PointwiseHomeomorphism intervalMetric (curveImageMetric t)
PointwiseHomeomorphism.forward (motionSliceHomeomorphism t) = map-unit-im (motion t)
PointwiseHomeomorphism.backward (motionSliceHomeomorphism t) = recoverInterval t
PointwiseHomeomorphism.forwardContinuous (motionSliceHomeomorphism t) = motionSliceContinuous t
PointwiseHomeomorphism.backwardContinuous (motionSliceHomeomorphism t) = recoverIntervalContinuous t
PointwiseHomeomorphism.forwardBackward (motionSliceHomeomorphism t) = recoverIntervalRight t
PointwiseHomeomorphism.backwardForward (motionSliceHomeomorphism t) = recoverIntervalLeft t

motionSliceInjective : (t : Real) (u v : OpenRealInterval) → motion t u ＝ motion t v → u ＝ v
motionSliceInjective t u v h = inv (recoverIntervalLeft t u) ∙
  ap (recoverInterval t) (eq-Eq-im (motion t) (map-unit-im (motion t) u) (map-unit-im (motion t) v) h) ∙
  recoverIntervalLeft t v

closedTimeSliceHomeomorphism : (t : ClosedParameter) →
  PointwiseHomeomorphism intervalMetric (curveImageMetric (pr1 t))
closedTimeSliceHomeomorphism t = motionSliceHomeomorphism (pr1 t)
