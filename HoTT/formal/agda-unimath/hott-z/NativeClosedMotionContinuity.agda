{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeClosedMotionContinuity where

-- Joint continuity of the same rational formula including the closed parameter.
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import hott-z.NativeCompletion
open import foundation.dependent-pair-types
open import metric-spaces.metric-spaces
open import metric-spaces.cartesian-products-metric-spaces
open import real-numbers.addition-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.negation-real-numbers

extendedDomain : Space
extendedDomain = product-Metric-Space realMetric closedMetric

closedParameterContinuous : Cont extendedDomain realMetric (λ z → pr1 (pr2 z))
closedParameterContinuous = composeContinuous extendedDomain closedMetric realMetric pr1 pr2
  closedInclusionContinuous (secondContinuous realMetric closedMetric)

closedTimeContinuous : Cont extendedDomain realMetric pr1
closedTimeContinuous = firstContinuous realMetric closedMetric

closedCenterContinuous : Cont extendedDomain realMetric (λ z → center (pr1 (pr2 z)))
closedCenterContinuous = composeContinuous extendedDomain realMetric realMetric center
  (λ z → pr1 (pr2 z)) centerContinuous closedParameterContinuous

closedGapContinuous : Cont extendedDomain realMetric (λ z → gap (pr1 (pr2 z)))
closedGapContinuous = composeContinuous extendedDomain realMetric realMetric gap
  (λ z → pr1 (pr2 z)) gapContinuous closedParameterContinuous

closedRemainingContinuous : Cont extendedDomain realMetric (λ z → remaining (pr1 z))
closedRemainingContinuous = composeContinuous extendedDomain realMetric realMetric remaining pr1
  remainingContinuous closedTimeContinuous

closingDContinuous : Cont extendedDomain realMetric (λ z → closingD (pr1 z) (pr1 (pr2 z)))
closingDContinuous = addContinuous X (λ z → gap (pr1 (pr2 z)))
  (λ z → square-ℝ (remaining (pr1 z)) *ℝ abs-ℝ (center (pr1 (pr2 z)))) closedGapContinuous
  (mulContinuous X (λ z → square-ℝ (remaining (pr1 z))) (λ z → abs-ℝ (center (pr1 (pr2 z))))
    (mulContinuous X (λ z → remaining (pr1 z)) (λ z → remaining (pr1 z)) closedRemainingContinuous closedRemainingContinuous)
    (absContinuous X (λ z → center (pr1 (pr2 z))) closedCenterContinuous))
  where X = extendedDomain

closingNContinuous : Cont extendedDomain realMetric (λ z → closingN (pr1 z) (pr1 (pr2 z)))
closingNContinuous = addContinuous X (λ z → scale (pr1 z) *ℝ center (pr1 (pr2 z)))
  (λ z → offset (pr1 z) *ℝ closingD (pr1 z) (pr1 (pr2 z)))
  (mulContinuous X (λ z → scale (pr1 z)) (λ z → center (pr1 (pr2 z)))
    (composeContinuous X realMetric realMetric scale pr1 scaleContinuous closedTimeContinuous) closedCenterContinuous)
  (mulContinuous X (λ z → offset (pr1 z)) (λ z → closingD (pr1 z) (pr1 (pr2 z)))
    (composeContinuous X realMetric realMetric offset pr1 offsetContinuous closedTimeContinuous) closingDContinuous)
  where X = extendedDomain

closingKContinuous : Cont extendedDomain realMetric (λ z → closingK (pr1 z) (pr1 (pr2 z)))
closingKContinuous = addContinuous X (λ z → square-ℝ (closingD (pr1 z) (pr1 (pr2 z))))
  (λ z → square-ℝ (pr1 z *ℝ closingN (pr1 z) (pr1 (pr2 z))))
  (mulContinuous X d d closingDContinuous closingDContinuous)
  (mulContinuous X tn tn ctn ctn)
  where
  X = extendedDomain
  d = λ z → closingD (pr1 z) (pr1 (pr2 z))
  tn = λ z → pr1 z *ℝ closingN (pr1 z) (pr1 (pr2 z))
  ctn = mulContinuous X pr1 (λ z → closingN (pr1 z) (pr1 (pr2 z))) closedTimeContinuous closingNContinuous

closingInverseContinuous : Cont extendedDomain realMetric (λ z → closingInverse (pr1 z) (pr2 z))
closingInverseContinuous = composeContinuous extendedDomain nonzeroMetric realMetric recip
  (λ z → closingNZ (pr1 z) (pr2 z)) reciprocalContinuous closingKContinuous

closedBaseXContinuous : Cont extendedDomain realMetric (λ z → pr1 (closedBase (pr1 z) (pr2 z)))
closedBaseXContinuous = mulContinuous X (λ z → n z *ℝ d z)
  (λ z → closingInverse (pr1 z) (pr2 z))
  (mulContinuous X n d closingNContinuous closingDContinuous) closingInverseContinuous
  where
  X = extendedDomain
  n = λ z → closingN (pr1 z) (pr1 (pr2 z))
  d = λ z → closingD (pr1 z) (pr1 (pr2 z))

closedBaseYContinuous : Cont extendedDomain realMetric (λ z → pr2 (closedBase (pr1 z) (pr2 z)))
closedBaseYContinuous = mulContinuous X (λ z → pr1 z *ℝ square-ℝ (n z))
  (λ z → closingInverse (pr1 z) (pr2 z))
  (mulContinuous X pr1 (λ z → square-ℝ (n z)) closedTimeContinuous
    (mulContinuous X n n closingNContinuous closingNContinuous)) closingInverseContinuous
  where
  X = extendedDomain
  n = λ z → closingN (pr1 z) (pr1 (pr2 z))

private
  module C = TurnContinuity extendedDomain pr1
    (λ z → pr1 (closedBase (pr1 z) (pr2 z))) (λ z → pr2 (closedBase (pr1 z) (pr2 z)))
    closedTimeContinuous closedBaseXContinuous closedBaseYContinuous

closedMotionContinuous : Cont extendedDomain realPlaneMetric (λ z → closedMotion (pr1 z) (pr2 z))
closedMotionContinuous = pairContinuous extendedDomain realMetric realMetric
  (λ z → pr1 (turn (pr1 z) (closedBase (pr1 z) (pr2 z))))
  (λ z → neg-ℝ (pr2 (turn (pr1 z) (closedBase (pr1 z) (pr2 z)))))
  C.cxturn (negContinuous extendedDomain (λ z → pr2 (turn (pr1 z) (closedBase (pr1 z) (pr2 z)))) C.cyturn)

closedSquare : Space
closedSquare = product-Metric-Space closedMetric closedMetric

closedSquareInclusion : Cont closedSquare extendedDomain (λ z → pr1 (pr1 z) , pr2 z)
closedSquareInclusion = pairContinuous closedSquare realMetric closedMetric
  (λ z → pr1 (pr1 z)) pr2
  (composeContinuous closedSquare closedMetric realMetric pr1 pr1 closedInclusionContinuous (firstContinuous closedMetric closedMetric))
  (secondContinuous closedMetric closedMetric)

closedSquareMotionContinuous : Cont closedSquare realPlaneMetric (λ z → closedMotion (pr1 (pr1 z)) (pr2 z))
closedSquareMotionContinuous = composeContinuous closedSquare extendedDomain realPlaneMetric
  (λ z → closedMotion (pr1 z) (pr2 z)) (λ z → pr1 (pr1 z) , pr2 z)
  closedMotionContinuous closedSquareInclusion
