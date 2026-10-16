{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeStretchInverse where

-- Explicit continuous left inverse for the actual stretch map on its chart.
open import hott-z.NativeMotion
open import hott-z.NativeMotionEndpoints
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
open import real-numbers.multiplication-positive-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers

squeezed unsqueezeDen : Real → Real → Real
squeezed t r = r *ℝ stretchInv t r
unsqueezeDen t z = one-ℝ -ℝ (square-ℝ (remaining t) *ℝ abs-ℝ z)

absSqueezed : (t r : Real) → abs-ℝ (squeezed t r) ＝ abs-ℝ r *ℝ stretchInv t r
absSqueezed t r = abs-mul-ℝ r (stretchInv t r) ∙
  ap (abs-ℝ r *ℝ_) (abs-real-ℝ⁺ (stretchInv t r , positiveRecip (stretchDen t r , stretchDenPositive t r)))

squeezedInverseSum : (t r : Real) →
  stretchInv t r +ℝ (square-ℝ (remaining t) *ℝ abs-ℝ (squeezed t r)) ＝ one-ℝ
squeezedInverseSum t r =
  ap (q +ℝ_) (ap (c *ℝ_) (absSqueezed t r) ∙ inv (associative-mul-ℝ c (abs-ℝ r) q)) ∙
  inv (right-distributive-mul-add-ℝ one-ℝ (c *ℝ abs-ℝ r) q ∙
    ap-add-ℝ (left-unit-law-mul-ℝ q) refl) ∙ rightInv (stretchNZ t r)
  where q = stretchInv t r; c = square-ℝ (remaining t)

squeezedInverseDen : (t r : Real) → unsqueezeDen t (squeezed t r) ＝ stretchInv t r
squeezedInverseDen t r =
  ap (_-ℝ (square-ℝ (remaining t) *ℝ abs-ℝ (squeezed t r))) (inv (squeezedInverseSum t r)) ∙
  eq-sim-ℝ (cancel-right-add-diff-ℝ (stretchInv t r) (square-ℝ (remaining t) *ℝ abs-ℝ (squeezed t r)))

scalePositive : (t : Real) → is-positive-ℝ (scale t)
scalePositive t = is-positive-mul-ℝ (pr2 one-half-ℝ⁺) (positiveD t)

scaleNZ : Real → NonzeroReal
scaleNZ t = nonzero-ℝ⁺ (scale t , scalePositive t)

affineUndo : Real → Real → Real
affineUndo t w = (w -ℝ offset t) *ℝ recip (scaleNZ t)

affineStretch : (t r : Real) → affineUndo t (stretch t r) ＝ squeezed t r
affineStretch t r =
  ap (_*ℝ recip (scaleNZ t)) (eq-sim-ℝ (cancel-right-add-diff-ℝ (scale t *ℝ squeezed t r) (offset t))) ∙
  ap (_*ℝ recip (scaleNZ t)) (commutative-mul-ℝ (scale t) (squeezed t r)) ∙
  associative-mul-ℝ (squeezed t r) (scale t) (recip (scaleNZ t)) ∙
  ap (squeezed t r *ℝ_) (rightInv (scaleNZ t)) ∙ right-unit-law-mul-ℝ (squeezed t r)

affineContinuous : (t : Real) (X : Space) (f : type-Metric-Space X → Real) →
  Cont X realMetric f → Cont X realMetric (λ x → affineUndo t (f x))
affineContinuous t X f cf = mulContinuous X (λ x → f x -ℝ offset t) (λ _ → recip (scaleNZ t))
  (addContinuous X f (λ _ → neg-ℝ (offset t)) cf (constantContinuous X (neg-ℝ (offset t))))
  (constantContinuous X (recip (scaleNZ t)))

unsqueezeDenContinuous : (t : Real) (X : Space) (f : type-Metric-Space X → Real) →
  Cont X realMetric f → Cont X realMetric (λ x → unsqueezeDen t (f x))
unsqueezeDenContinuous t X f cf = addContinuous X (λ _ → one-ℝ)
  (λ x → neg-ℝ (square-ℝ (remaining t) *ℝ abs-ℝ (f x))) (constantContinuous X one-ℝ)
  (negContinuous X (λ x → square-ℝ (remaining t) *ℝ abs-ℝ (f x))
    (mulContinuous X (λ _ → square-ℝ (remaining t)) (λ x → abs-ℝ (f x))
      (constantContinuous X (square-ℝ (remaining t))) (absContinuous X f cf)))

stretchChartSubtype : Real → subtype lzero Real
stretchChartSubtype t w = is-positive-prop-ℝ (unsqueezeDen t (affineUndo t w))

stretchChartMetric : Real → Space
stretchChartMetric t = subspace-Metric-Space realMetric (stretchChartSubtype t)

StretchChart : Real → UU (lsuc lzero)
StretchChart t = type-Metric-Space (stretchChartMetric t)

stretchChartDen : (t : Real) → StretchChart t → NonzeroReal
stretchChartDen t w = nonzero-ℝ⁺ (unsqueezeDen t (affineUndo t (pr1 w)) , pr2 w)

stretchChartPoint : (t r : Real) → StretchChart t
stretchChartPoint t r = stretch t r , tr is-positive-ℝ
  (inv (ap (unsqueezeDen t) (affineStretch t r) ∙ squeezedInverseDen t r))
  (positiveRecip (stretchDen t r , stretchDenPositive t r))

stretchInverse : (t : Real) → StretchChart t → Real
stretchInverse t w = affineUndo t (pr1 w) *ℝ recip (stretchChartDen t w)

stretchLeftInverse : (t r : Real) → stretchInverse t (stretchChartPoint t r) ＝ r
stretchLeftInverse t r =
  ap (_*ℝ recip nz) (affineStretch t r) ∙
  associative-mul-ℝ r (stretchInv t r) (recip nz) ∙
  ap (r *ℝ_) (ap (_*ℝ recip nz) (inv denEq) ∙ rightInv nz) ∙ right-unit-law-mul-ℝ r
  where
  nz = stretchChartDen t (stretchChartPoint t r)
  denEq = ap (unsqueezeDen t) (affineStretch t r) ∙ squeezedInverseDen t r

stretchChartInclusionContinuous : (t : Real) → Cont (stretchChartMetric t) realMetric pr1
stretchChartInclusionContinuous t x = intro-exists (λ ε → ε) (λ ε y near → near)

stretchInverseContinuous : (t : Real) → Cont (stretchChartMetric t) realMetric (stretchInverse t)
stretchInverseContinuous t = mulContinuous X (λ w → affineUndo t (pr1 w))
  (λ w → recip (stretchChartDen t w)) ca
  (composeContinuous X nonzeroMetric realMetric recip (stretchChartDen t) reciprocalContinuous
    (unsqueezeDenContinuous t X (λ w → affineUndo t (pr1 w)) ca))
  where
  X = stretchChartMetric t
  ca = affineContinuous t X pr1 (stretchChartInclusionContinuous t)
