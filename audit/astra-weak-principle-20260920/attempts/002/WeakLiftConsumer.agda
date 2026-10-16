{-# OPTIONS --without-K --exact-split #-}
module hott-z.WeakLiftConsumer where

open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.StereographicContinuity
open import hott-z.NativeOpenInterval
open import hott-z.WeakLiftPrinciple
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.logical-equivalences
open import foundation.equivalences
open import foundation.univalence

realPrincipleIffSamePointRefinement : RealNonzeroApartness ↔ SamePointRefinement
realPrincipleIffSamePointRefinement =
  (λ principle → liftToRefinement (realApartnessToLift principle)) ,
  (λ refine → liftToRealApartness (refinementToLift refine))

realPrincipleIffCircleInverse : RealNonzeroApartness ↔ UniformInverse
realPrincipleIffCircleInverse =
  (λ principle → liftToUniformInverse (realApartnessToLift principle)) ,
  (λ invert → liftToRealApartness (uniformInverseToLift invert))

refinementPreservesPoint : (principle : RealNonzeroApartness) (w : PuncturedRealCircle) →
  pr1 (liftWeakPoint (realApartnessToLift principle) w) ＝ pr1 w
refinementPreservesPoint principle w = refl

-- The original weak puncture and original open interval, with the principle explicit.
weakIntervalHomeomorphismFromRealPrinciple : RealNonzeroApartness →
  PointwiseHomeomorphism puncturedCircleMetric intervalMetric
weakIntervalHomeomorphismFromRealPrinciple principle =
  weakCircleUnitHomeomorphism (realApartnessToLift principle)

weakIntervalPathFromRealPrinciple : RealNonzeroApartness →
  PuncturedRealCircle ＝ OpenRealInterval
weakIntervalPathFromRealPrinciple principle =
  weakIntervalTypePath (realApartnessToLift principle)

weakIntervalPathActionFromRealPrinciple :
  (principle : RealNonzeroApartness) (w : PuncturedRealCircle) →
  map-equiv (equiv-eq (weakIntervalPathFromRealPrinciple principle)) w ＝
  PointwiseHomeomorphism.forward (weakIntervalHomeomorphismFromRealPrinciple principle) w
weakIntervalPathActionFromRealPrinciple principle w = ap (λ e → map-equiv e w)
  (is-section-eq-equiv (homeomorphismEquiv (weakIntervalHomeomorphismFromRealPrinciple principle)))

-- This sufficiency result does not assert necessity for every possible homeomorphism.
