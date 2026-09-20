{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeMotionBridge where

-- Restrict the actual time family to [0,1], retaining the original open
-- parameter and the exact pre-existing n/m closed-curve interior diagrams.
-- This is not yet a proof that every intermediate slice is an embedding.
open import hott-z.NativeMotion
open import hott-z.NativeMotionEndpoints
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.equality-cartesian-product-types
open import foundation.transport-along-identifications
open import metric-spaces.metric-spaces
open import metric-spaces.cartesian-products-metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.negation-real-numbers

closedTimeDomain : Space
closedTimeDomain = product-Metric-Space closedMetric intervalMetric

closedTimeMotion : ClosedParameter → OpenRealInterval → RealPlane
closedTimeMotion t u = motion (pr1 t) u

closedTimeInclusion : Cont closedTimeDomain motionDomain (λ z → pr1 (pr1 z) , pr2 z)
closedTimeInclusion = pairContinuous closedTimeDomain realMetric intervalMetric
  (λ z → pr1 (pr1 z)) pr2
  (composeContinuous closedTimeDomain closedMetric realMetric pr1 pr1 closedInclusionContinuous
    (firstContinuous closedMetric intervalMetric))
  (secondContinuous closedMetric intervalMetric)

closedTimeMotionContinuous : Cont closedTimeDomain realPlaneMetric (λ z → closedTimeMotion (pr1 z) (pr2 z))
closedTimeMotionContinuous = composeContinuous closedTimeDomain motionDomain realPlaneMetric
  (λ z → motion (pr1 z) (pr2 z)) (λ z → pr1 (pr1 z) , pr2 z)
  motionContinuous closedTimeInclusion

initialOriginalDiagram : (u : OpenRealInterval) →
  closedTimeMotion closedZero u ＝ nCompletion (openIntoClosed u)
initialOriginalDiagram = motionAtZero

finalOriginalDiagram : (u : OpenRealInterval) →
  closedTimeMotion closedOne u ＝ pr1 (mCompletion (openIntoClosed u))
finalOriginalDiagram u = motionAtOneOriginal u ∙ inv (ap pr1 (mInterior u))

finalStrongPoint : (u : OpenRealInterval) →
  closedTimeMotion closedOne u ＝ pr1 (paramPoint (realParameter u))
finalStrongPoint = motionAtOne

reflectionInvolution : (v : RealPlane) → reflectY (reflectY v) ＝ v
reflectionInvolution v = eq-pair refl (neg-neg-ℝ (pr2 v))

reflectionFixesLine : (r : Real) → reflectY (r , zero-ℝ) ＝ (r , zero-ℝ)
reflectionFixesLine r = eq-pair refl neg-zero-ℝ

rawIsReflectedMotion : (t : Real) (u : OpenRealInterval) →
  motionRaw t u ＝ reflectY (motion t u)
rawIsReflectedMotion t u = inv (reflectionInvolution (motionRaw t u))

-- No change to the parameter and no replacement of the final Rich diagram.
rawFinalOrientation : (u : OpenRealInterval) →
  motionRaw one-ℝ u ＝ reflectY (pr1 (mCompletion (openIntoClosed u)))
rawFinalOrientation u = rawIsReflectedMotion one-ℝ u ∙ ap reflectY (finalOriginalDiagram u)
