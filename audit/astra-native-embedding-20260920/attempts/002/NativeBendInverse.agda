{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeBendInverse where

-- Continuous inverse of bend on its actual positive-denominator plane chart.
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.existential-quantification
open import metric-spaces.metric-spaces
open import metric-spaces.subspaces-metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonzero-real-numbers

bendInverseDen : Real → RealPlane → Real
bendInverseDen t v = one-ℝ -ℝ (t *ℝ pr2 v)

bendDenIdentity : (t r : Real) → bendInverseDen t (bend t r) ＝ qInv (t *ℝ r)
bendDenIdentity t r = ap-add-ℝ (inv (Dq (t *ℝ r))) (ap neg-ℝ term) ∙
  inv (right-distributive-mul-diff-ℝ (D (t *ℝ r)) (square-ℝ (t *ℝ r)) q) ∙
  ap (_*ℝ q) (ap (_-ℝ square-ℝ (t *ℝ r))
    (commutative-add-ℝ (square-ℝ (t *ℝ r)) one-ℝ) ∙
    eq-sim-ℝ (cancel-right-add-diff-ℝ one-ℝ (square-ℝ (t *ℝ r)))) ∙
  left-unit-law-mul-ℝ q
  where
  q = qInv (t *ℝ r)
  term : t *ℝ ((t *ℝ square-ℝ r) *ℝ q) ＝ square-ℝ (t *ℝ r) *ℝ q
  term = inv (associative-mul-ℝ t (t *ℝ square-ℝ r) q) ∙
    ap (_*ℝ q) (inv (associative-mul-ℝ t t (square-ℝ r)) ∙
      inv (distributive-square-mul-ℝ t r))

bendChartSubtype : Real → subtype lzero RealPlane
bendChartSubtype t v = is-positive-prop-ℝ (bendInverseDen t v)

bendChartMetric : Real → Space
bendChartMetric t = subspace-Metric-Space realPlaneMetric (bendChartSubtype t)

BendChart : Real → UU (lsuc lzero)
BendChart t = type-Metric-Space (bendChartMetric t)

bendChartPoint : (t r : Real) → BendChart t
bendChartPoint t r = bend t r , tr is-positive-ℝ (inv (bendDenIdentity t r))
  (positiveRecip (D (t *ℝ r) , positiveD (t *ℝ r)))

bendChartDen : (t : Real) → BendChart t → NonzeroReal
bendChartDen t v = nonzero-ℝ⁺ (bendInverseDen t (pr1 v) , pr2 v)

bendInverse : (t : Real) → BendChart t → Real
bendInverse t v = pr1 (pr1 v) *ℝ recip (bendChartDen t v)

bendLeftInverse : (t r : Real) → bendInverse t (bendChartPoint t r) ＝ r
bendLeftInverse t r = associative-mul-ℝ r (qInv (t *ℝ r)) (recip nz) ∙
  ap (r *ℝ_) (ap (_*ℝ recip nz) (inv (bendDenIdentity t r)) ∙ rightInv nz) ∙
  right-unit-law-mul-ℝ r
  where nz = bendChartDen t (bendChartPoint t r)

bendChartXContinuous : (t : Real) → Cont (bendChartMetric t) realMetric (λ v → pr1 (pr1 v))
bendChartXContinuous t v = intro-exists (λ ε → ε) (λ ε w near → pr1 near)

bendChartYContinuous : (t : Real) → Cont (bendChartMetric t) realMetric (λ v → pr2 (pr1 v))
bendChartYContinuous t v = intro-exists (λ ε → ε) (λ ε w near → pr2 near)

bendChartDenContinuous : (t : Real) → Cont (bendChartMetric t) nonzeroMetric (bendChartDen t)
bendChartDenContinuous t = addContinuous X (λ _ → one-ℝ)
  (λ v → neg-ℝ (t *ℝ pr2 (pr1 v))) (constantContinuous X one-ℝ)
  (negContinuous X (λ v → t *ℝ pr2 (pr1 v))
    (mulContinuous X (λ _ → t) (λ v → pr2 (pr1 v)) (constantContinuous X t) (bendChartYContinuous t)))
  where X = bendChartMetric t

bendInverseContinuous : (t : Real) → Cont (bendChartMetric t) realMetric (bendInverse t)
bendInverseContinuous t = mulContinuous (bendChartMetric t) (λ v → pr1 (pr1 v))
  (λ v → recip (bendChartDen t v)) (bendChartXContinuous t)
  (composeContinuous (bendChartMetric t) nonzeroMetric realMetric recip (bendChartDen t)
    reciprocalContinuous (bendChartDenContinuous t))
