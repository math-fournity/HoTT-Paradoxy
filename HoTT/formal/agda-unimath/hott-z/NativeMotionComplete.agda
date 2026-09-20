{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeMotionComplete where

-- One record for the declared clauses on the unchanged geometric maps.
-- Weak-puncture coverage remains explicit; no physical or whole-theory verdict.
open import hott-z.NativeClosedSpatialBounds
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionContinuity
open import hott-z.NativeClosedMotionInterior
open import hott-z.NativeClosedMotionEndpoints
open import hott-z.NativeEndpointSeparation
open import hott-z.NativeCompletionFibers
open import hott-z.NativeMotion
open import hott-z.NativeMotionEndpoints
open import hott-z.NativeMotionEmbedding
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import hott-z.WeakLiftPrinciple
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.propositions
open import foundation.subtypes
open import foundation.existential-quantification
open import foundation.logical-equivalences
open import metric-spaces.metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.apartness-real-numbers

WeakFinalCoverage : UU (lsuc lzero)
WeakFinalCoverage = (w : PuncturedRealCircle) → exists OpenRealInterval
  (λ u → eq-prop-Metric-Space realPlaneMetric (motion one-ℝ u) (pr1 (pr1 w)))

ChosenWeakFinalOutput : UU (lsuc lzero)
ChosenWeakFinalOutput = (w : PuncturedRealCircle) →
  Σ OpenRealInterval (λ u → motion one-ℝ u ＝ pr1 (pr1 w))

liftGivesChosenWeakFinalOutput : Lift → ChosenWeakFinalOutput
liftGivesChosenWeakFinalOutput lift w = u ,
  motionAtOne u ∙ ap (λ z → pr1 (pr1 z)) (PointwiseHomeomorphism.backwardForward h w)
  where
  h = weakCircleUnitHomeomorphism lift
  u = PointwiseHomeomorphism.forward h w

liftGivesWeakFinalCoverage : Lift → WeakFinalCoverage
liftGivesWeakFinalCoverage lift w = intro-exists (pr1 (liftGivesChosenWeakFinalOutput lift w))
  (pr2 (liftGivesChosenWeakFinalOutput lift w))

weakFinalCoverageGivesLift : WeakFinalCoverage → Lift
weakFinalCoverageGivesLift covers p weak = elim-exists (apart-prop-ℝ (xCoord p) one-ℝ)
  (λ u h → tr Strong (eq-type-subtype circleSubtype {a = paramPoint (realParameter u)} {b = p}
    (inv (motionAtOne u) ∙ h))
    (paramStrong (realParameter u)))
  (covers (p , weak))

weakFinalCoverageIffLift : WeakFinalCoverage ↔ Lift
weakFinalCoverageIffLift = weakFinalCoverageGivesLift , liftGivesWeakFinalCoverage

weakFinalCoverageIffRealPrinciple : WeakFinalCoverage ↔ RealNonzeroApartness
weakFinalCoverageIffRealPrinciple =
  (λ covers → liftToRealApartness (weakFinalCoverageGivesLift covers)) ,
  (λ principle → liftGivesWeakFinalCoverage (realApartnessToLift principle))

record NativeMotionEvidence : UU (lsuc lzero) where
  field
    jointOpen : Cont motionDomain realPlaneMetric (λ z → motion (pr1 z) (pr2 z))
    jointClosed : Cont closedSquare realPlaneMetric (λ z → closedMotion (pr1 (pr1 z)) (pr2 z))
    sliceHomeomorphisms : (t : ClosedParameter) →
      PointwiseHomeomorphism intervalMetric (curveImageMetric (pr1 t))
    interiorAgreement : (t : ClosedParameter) (u : OpenRealInterval) →
      closedMotion (pr1 t) (openIntoClosed u) ＝ motion (pr1 t) u
    initialDiagram : (u : ClosedParameter) → closedMotion zero-ℝ u ＝ nCompletion u
    finalDiagram : (u : ClosedParameter) → closedMotion one-ℝ u ＝ pr1 (mCompletion u)
    endpointMeeting : (t : ClosedParameter) →
      (closedMotion (pr1 t) closedZero ＝ closedMotion (pr1 t) closedOne) ↔ (t ＝ closedOne)
    finalFibers : (u v : ClosedParameter) →
      (closedMotion one-ℝ u ＝ closedMotion one-ℝ v) ↔ type-Prop (FullFiberRelation u v)
    closedBounds : (t u : ClosedParameter) → PlaneBound (closedMotion (pr1 t) u)
    openBounds : (t : ClosedParameter) (u : OpenRealInterval) → PlaneBound (motion (pr1 t) u)
    weakCoverageCriterion : WeakFinalCoverage ↔ Lift
    weakChosenOutput : Lift → ChosenWeakFinalOutput

nativeMotionEvidence : NativeMotionEvidence
NativeMotionEvidence.jointOpen nativeMotionEvidence = motionContinuous
NativeMotionEvidence.jointClosed nativeMotionEvidence = closedSquareMotionContinuous
NativeMotionEvidence.sliceHomeomorphisms nativeMotionEvidence = closedTimeSliceHomeomorphism
NativeMotionEvidence.interiorAgreement nativeMotionEvidence t = closedAgreesInterior (pr1 t)
NativeMotionEvidence.initialDiagram nativeMotionEvidence = closedInitialDiagram
NativeMotionEvidence.finalDiagram nativeMotionEvidence = closedFinalDiagram
NativeMotionEvidence.endpointMeeting nativeMotionEvidence = endpointMeetingTime
NativeMotionEvidence.finalFibers nativeMotionEvidence = closedFinalFiberClassification
NativeMotionEvidence.closedBounds nativeMotionEvidence = closedMotionUniformBound
NativeMotionEvidence.openBounds nativeMotionEvidence = motionUniformBound
NativeMotionEvidence.weakCoverageCriterion nativeMotionEvidence = weakFinalCoverageIffLift
NativeMotionEvidence.weakChosenOutput nativeMotionEvidence = liftGivesChosenWeakFinalOutput
