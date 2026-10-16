{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeTaskIntegration where

-- The same nRich/mRich pair under two explicitly different operation contracts.
-- CurveRun uses continuous embedding families and the complete closed diagram;
-- Success uses the existing finite ambient-homeomorphism steps.
open import hott-z.NativeMotionComplete
open import hott-z.NativeClosedSpatialBounds
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionContinuity
open import hott-z.NativeClosedMotionInterior
open import hott-z.NativeClosedMotionEndpoints
open import hott-z.NativeMotion
open import hott-z.NativeMotionEmbedding
open import hott-z.NativeRealCircleQualification
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.NativeCompletion
open import hott-z.NativeRichCurve
open import hott-z.NativeCurveTask using (Success; noSuccessNtoM; AmbientStep; swapSuccess)
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.identity-types
open import foundation.negation
open import foundation.equivalences
open import foundation.images
open import metric-spaces.metric-spaces
open import metric-spaces.images-metric-spaces

record CurveRun (r s : RichCurve) : UU (lsuc lzero) where
  field
    at : ClosedParameter → OpenRealInterval → RealPlane
    closedAt : ClosedParameter → ClosedParameter → RealPlane
    jointlyContinuous : Cont closedSquare realPlaneMetric (λ z → closedAt (pr1 z) (pr2 z))
    agreesInterior : (t : ClosedParameter) (u : OpenRealInterval) → closedAt t (openIntoClosed u) ＝ at t u
    slice : (t : ClosedParameter) → PointwiseHomeomorphism intervalMetric
      (im-Metric-Space intervalMetric realPlaneMetric (at t))
    sliceIsActualMap : (t : ClosedParameter) (u : OpenRealInterval) →
      PointwiseHomeomorphism.forward (slice t) u ＝ map-unit-im (at t) u
    initial : (u : ClosedParameter) → closedAt closedZero u ＝ closedImage r u
    final : (u : ClosedParameter) → closedAt closedOne u ＝ closedImage s u
    spaceBound : (t u : ClosedParameter) → PlaneBound (closedAt t u)

actualCurveRun : CurveRun nRich mRich
CurveRun.at actualCurveRun t = motion (pr1 t)
CurveRun.closedAt actualCurveRun t = closedMotion (pr1 t)
CurveRun.jointlyContinuous actualCurveRun = closedSquareMotionContinuous
CurveRun.agreesInterior actualCurveRun t = closedAgreesInterior (pr1 t)
CurveRun.slice actualCurveRun = closedTimeSliceHomeomorphism
CurveRun.sliceIsActualMap actualCurveRun t u = refl
CurveRun.initial actualCurveRun = closedInitialDiagram
CurveRun.final actualCurveRun = closedFinalDiagram
CurveRun.spaceBound actualCurveRun = closedMotionUniformBound

samePairDifferentOperations : CurveRun nRich mRich × ¬ (Success (nRich , mRich))
samePairDifferentOperations = actualCurveRun , noSuccessNtoM

noCurveToAmbientAtActualPair : ¬ (CurveRun nRich mRich → Success (nRich , mRich))
noCurveToAmbientAtActualPair convert = noSuccessNtoM (convert actualCurveRun)

noUniformCurveToAmbient : ¬ ((r s : RichCurve) → CurveRun r s → Success (r , s))
noUniformCurveToAmbient convert = noCurveToAmbientAtActualPair (convert nRich mRich)

noCurveAmbientEquivalence : ¬ (CurveRun nRich mRich ≃ Success (nRich , mRich))
noCurveAmbientEquivalence e = noCurveToAmbientAtActualPair (map-equiv e)

-- The negative ambient result is not caused by declaring every ambient task empty.
nontrivialAmbientControl : Success (nRich , swappedN)
nontrivialAmbientControl = swapSuccess

-- The positive curve run does not manufacture an identity of the Rich inputs.
samePairStillRichDistinct : ¬ (mRich ＝ nRich)
samePairStillRichDistinct = noRichPath
