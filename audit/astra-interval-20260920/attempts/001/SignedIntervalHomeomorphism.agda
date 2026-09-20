{-# OPTIONS --without-K --exact-split #-}
module hott-z.SignedIntervalHomeomorphism where

-- Actual Real ↔ {z : Real | |z| < 1}, with inherited subspace metric.
open import hott-z.NativeRealCircleQualification
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.existential-quantification
open import metric-spaces.metric-spaces
open import metric-spaces.subspaces-metric-spaces
open import metric-spaces.pointwise-continuous-maps-metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.multiplication-positive-real-numbers
open import real-numbers.multiplicative-inverses-positive-real-numbers
open import real-numbers.multiplicative-inverses-nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.inequalities-addition-and-subtraction-real-numbers
open import real-numbers.strict-inequalities-addition-and-subtraction-real-numbers

positiveRecip : (x : ℝ⁺ lzero) → is-positive-ℝ (recip (nonzero-ℝ⁺ x))
positiveRecip x = tr is-positive-ℝ
  (eq-sim-ℝ (unique-right-inv-nonzero-ℝ (nonzero-ℝ⁺ x)
    (nonzero-ℝ⁺ (inv-ℝ⁺ x)) (right-inverse-law-mul-ℝ⁺ x)))
  (is-positive-real-inv-ℝ⁺ x)

signedSubtype = λ z → le-prop-ℝ (abs-ℝ z) one-ℝ

signedMetric : Space
signedMetric = subspace-Metric-Space realMetric signedSubtype

SignedInterval : UU (lsuc lzero)
SignedInterval = type-Metric-Space signedMetric

plusDenominator : Real → Real
plusDenominator t = one-ℝ +ℝ abs-ℝ t

positivePlus : (t : Real) → is-positive-ℝ (plusDenominator t)
positivePlus t = concatenate-le-leq-ℝ zero-ℝ one-ℝ (plusDenominator t) le-zero-one-ℝ
  (tr (λ a → leq-ℝ a (plusDenominator t)) (right-unit-law-add-ℝ one-ℝ)
    (preserves-leq-left-add-ℝ one-ℝ zero-ℝ (abs-ℝ t) (is-nonnegative-abs-ℝ t)))

plusNZ : Real → NonzeroReal
plusNZ t = nonzero-ℝ⁺ (plusDenominator t , positivePlus t)

plusInverse : Real → Real
plusInverse t = recip (plusNZ t)

positivePlusInverse : (t : Real) → is-positive-ℝ (plusInverse t)
positivePlusInverse t = positiveRecip (plusDenominator t , positivePlus t)

squashValue : Real → Real
squashValue t = t *ℝ plusInverse t

absSquash : (t : Real) → abs-ℝ (squashValue t) ＝ abs-ℝ t *ℝ plusInverse t
absSquash t = abs-mul-ℝ t (plusInverse t) ∙
  ap (abs-ℝ t *ℝ_) (abs-real-ℝ⁺ (plusInverse t , positivePlusInverse t))

squashBound : (t : Real) → le-ℝ (abs-ℝ (squashValue t)) one-ℝ
squashBound t = tr (λ a → le-ℝ a one-ℝ) (inv (absSquash t))
  (tr (le-ℝ (abs-ℝ t *ℝ plusInverse t)) (rightInv (plusNZ t))
    (preserves-le-right-mul-ℝ⁺ (plusInverse t , positivePlusInverse t)
      (tr (λ a → le-ℝ a (plusDenominator t)) (left-unit-law-add-ℝ (abs-ℝ t))
        (preserves-le-right-add-ℝ (abs-ℝ t) zero-ℝ one-ℝ le-zero-one-ℝ))))

squash : Real → SignedInterval
squash t = squashValue t , squashBound t

minusDenominator : SignedInterval → Real
minusDenominator z = one-ℝ -ℝ abs-ℝ (pr1 z)

positiveMinus : (z : SignedInterval) → is-positive-ℝ (minusDenominator z)
positiveMinus z = is-positive-diff-le-ℝ (pr2 z)

minusNZ : SignedInterval → NonzeroReal
minusNZ z = nonzero-ℝ⁺ (minusDenominator z , positiveMinus z)

minusInverse : SignedInterval → Real
minusInverse z = recip (minusNZ z)

positiveMinusInverse : (z : SignedInterval) → is-positive-ℝ (minusInverse z)
positiveMinusInverse z = positiveRecip (minusDenominator z , positiveMinus z)

unsquash : SignedInterval → Real
unsquash z = pr1 z *ℝ minusInverse z

plusInvAndAbs : (t : Real) → plusInverse t +ℝ abs-ℝ (squashValue t) ＝ one-ℝ
plusInvAndAbs t =
  ap (plusInverse t +ℝ_) (absSquash t) ∙
  inv (right-distributive-mul-add-ℝ one-ℝ (abs-ℝ t) (plusInverse t) ∙
    ap-add-ℝ (left-unit-law-mul-ℝ (plusInverse t)) refl) ∙ rightInv (plusNZ t)

minusSquash : (t : Real) → minusDenominator (squash t) ＝ plusInverse t
minusSquash t =
  ap (_-ℝ abs-ℝ (squashValue t)) (inv (plusInvAndAbs t)) ∙
  eq-sim-ℝ (cancel-right-add-diff-ℝ (plusInverse t) (abs-ℝ (squashValue t)))

unsquashSquash : (t : Real) → unsquash (squash t) ＝ t
unsquashSquash t =
  associative-mul-ℝ t (plusInverse t) (minusInverse (squash t)) ∙
  ap (t *ℝ_)
    (inv (ap (_*ℝ minusInverse (squash t)) (minusSquash t)) ∙ rightInv (minusNZ (squash t))) ∙
  right-unit-law-mul-ℝ t

absUnsquash : (z : SignedInterval) → abs-ℝ (unsquash z) ＝ abs-ℝ (pr1 z) *ℝ minusInverse z
absUnsquash z = abs-mul-ℝ (pr1 z) (minusInverse z) ∙
  ap (abs-ℝ (pr1 z) *ℝ_) (abs-real-ℝ⁺ (minusInverse z , positiveMinusInverse z))

plusUnsquashTimesMinus : (z : SignedInterval) →
  plusDenominator (unsquash z) *ℝ minusDenominator z ＝ one-ℝ
plusUnsquashTimesMinus z =
  right-distributive-mul-add-ℝ one-ℝ (abs-ℝ (unsquash z)) (minusDenominator z) ∙
  ap-add-ℝ (left-unit-law-mul-ℝ (minusDenominator z))
    (ap (_*ℝ minusDenominator z) (absUnsquash z) ∙
      associative-mul-ℝ (abs-ℝ (pr1 z)) (minusInverse z) (minusDenominator z) ∙
      ap (abs-ℝ (pr1 z) *ℝ_) (leftInv (minusNZ z)) ∙ right-unit-law-mul-ℝ (abs-ℝ (pr1 z))) ∙
  eq-sim-ℝ (cancel-right-diff-add-ℝ one-ℝ (abs-ℝ (pr1 z)))

inversePlusUnsquash : (z : SignedInterval) → plusInverse (unsquash z) ＝ minusDenominator z
inversePlusUnsquash z = inv (eq-sim-ℝ
  (unique-right-inv-nonzero-ℝ (plusNZ (unsquash z)) (minusNZ z)
    (sim-eq-ℝ (plusUnsquashTimesMinus z))))

squashUnsquashValue : (z : SignedInterval) → squashValue (unsquash z) ＝ pr1 z
squashUnsquashValue z =
  ap ((pr1 z *ℝ minusInverse z) *ℝ_) (inversePlusUnsquash z) ∙
  associative-mul-ℝ (pr1 z) (minusInverse z) (minusDenominator z) ∙
  ap (pr1 z *ℝ_) (leftInv (minusNZ z)) ∙ right-unit-law-mul-ℝ (pr1 z)

squashUnsquash : (z : SignedInterval) → squash (unsquash z) ＝ z
squashUnsquash z = eq-type-subtype signedSubtype (squashUnsquashValue z)

absContinuous : (X : Space) (f : type-Metric-Space X → Real) →
  Cont X realMetric f → Cont X realMetric (λ x → abs-ℝ (f x))
absContinuous X f cf = composeContinuous X realMetric realMetric abs-ℝ f
  (pr2 (pointwise-continuous-map-short-map-Metric-Space realMetric realMetric (short-map-abs-ℝ {lzero}))) cf

plusContinuous : Cont realMetric realMetric plusDenominator
plusContinuous = addContinuous realMetric (λ _ → one-ℝ) abs-ℝ
  (constantContinuous realMetric one-ℝ) (absContinuous realMetric (λ t → t) identityContinuous)

plusNZContinuous : Cont realMetric nonzeroMetric plusNZ
plusNZContinuous = plusContinuous

plusInverseContinuous : Cont realMetric realMetric plusInverse
plusInverseContinuous = composeContinuous realMetric nonzeroMetric realMetric recip plusNZ
  reciprocalContinuous plusNZContinuous

squashContinuous : Cont realMetric signedMetric squash
squashContinuous = mulContinuous realMetric (λ t → t) plusInverse identityContinuous plusInverseContinuous

signedInclusionContinuous : Cont signedMetric realMetric pr1
signedInclusionContinuous z = intro-exists (λ ε → ε) (λ ε z' near → near)

minusContinuous : Cont signedMetric realMetric minusDenominator
minusContinuous = addContinuous signedMetric (λ _ → one-ℝ) (λ z → neg-ℝ (abs-ℝ (pr1 z)))
  (constantContinuous signedMetric one-ℝ)
  (negContinuous signedMetric (λ z → abs-ℝ (pr1 z)) (absContinuous signedMetric pr1 signedInclusionContinuous))

minusNZContinuous : Cont signedMetric nonzeroMetric minusNZ
minusNZContinuous = minusContinuous

minusInverseContinuous : Cont signedMetric realMetric minusInverse
minusInverseContinuous = composeContinuous signedMetric nonzeroMetric realMetric recip minusNZ
  reciprocalContinuous minusNZContinuous

unsquashContinuous : Cont signedMetric realMetric unsquash
unsquashContinuous = mulContinuous signedMetric pr1 minusInverse signedInclusionContinuous minusInverseContinuous

realSignedHomeomorphism : PointwiseHomeomorphism realMetric signedMetric
PointwiseHomeomorphism.forward realSignedHomeomorphism = squash
PointwiseHomeomorphism.backward realSignedHomeomorphism = unsquash
PointwiseHomeomorphism.forwardContinuous realSignedHomeomorphism = squashContinuous
PointwiseHomeomorphism.backwardContinuous realSignedHomeomorphism = unsquashContinuous
PointwiseHomeomorphism.forwardBackward realSignedHomeomorphism = squashUnsquash
PointwiseHomeomorphism.backwardForward realSignedHomeomorphism = unsquashSquash
