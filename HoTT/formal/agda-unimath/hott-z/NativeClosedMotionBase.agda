{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeClosedMotionBase where

-- The original rational closed-parameter formula. Positivity uses located order
-- and apartness cotransitivity, without deciding whether a real time equals 1.
open import hott-z.NativeMotion
open import hott-z.NativeStretchInverse
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.NativeCompletion
open import hott-z.HomogeneousCircle
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.disjunction
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.addition-positive-and-negative-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-positive-real-numbers
open import real-numbers.multiplication-nonnegative-real-numbers
open import real-numbers.multiplication-nonzero-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.inequalities-addition-and-subtraction-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.strict-inequalities-addition-and-subtraction-real-numbers
open import real-numbers.apartness-real-numbers

closingD closingN closingK : Real → Real → Real
closingD t u = gap u +ℝ (square-ℝ (remaining t) *ℝ abs-ℝ (center u))
closingN t u = (scale t *ℝ center u) +ℝ (offset t *ℝ closingD t u)
closingK t u = K (closingD t u) (t *ℝ closingN t u)

closedCenterUpper : (u : ClosedParameter) → leq-ℝ (center (pr1 u)) one-ℝ
closedCenterUpper u = tr (leq-ℝ (center (pr1 u)))
  (eq-sim-ℝ (cancel-right-add-diff-ℝ one-ℝ one-ℝ))
  (preserves-leq-right-add-ℝ (neg-ℝ one-ℝ) (pr1 u +ℝ pr1 u) (one-ℝ +ℝ one-ℝ)
    (preserves-leq-add-ℝ (pr2 (pr2 u)) (pr2 (pr2 u))))

closedCenterNegativeUpper : (u : ClosedParameter) → leq-ℝ (neg-ℝ (center (pr1 u))) one-ℝ
closedCenterNegativeUpper u = tr (λ a → leq-ℝ a one-ℝ)
  (inv (distributive-neg-diff-ℝ (pr1 u +ℝ pr1 u) one-ℝ))
  (tr (leq-ℝ (one-ℝ -ℝ (pr1 u +ℝ pr1 u))) (right-unit-law-add-ℝ one-ℝ)
    (preserves-leq-left-add-ℝ one-ℝ (neg-ℝ (pr1 u +ℝ pr1 u)) zero-ℝ
      (tr (leq-ℝ (neg-ℝ (pr1 u +ℝ pr1 u))) neg-zero-ℝ
        (neg-leq-ℝ (tr (λ z → leq-ℝ z (pr1 u +ℝ pr1 u)) (left-unit-law-add-ℝ zero-ℝ)
          (preserves-leq-add-ℝ (pr1 (pr2 u)) (pr1 (pr2 u))))))))

closedCenterAbsBound : (u : ClosedParameter) → leq-ℝ (abs-ℝ (center (pr1 u))) one-ℝ
closedCenterAbsBound u = leq-abs-leq-leq-neg-ℝ (closedCenterUpper u) (closedCenterNegativeUpper u)

closedGapNonnegative : (u : ClosedParameter) → is-nonnegative-ℝ (gap (pr1 u))
closedGapNonnegative u = is-nonnegative-diff-leq-ℝ (closedCenterAbsBound u)

closingTermNonnegative : (t u : Real) → is-nonnegative-ℝ (square-ℝ (remaining t) *ℝ abs-ℝ (center u))
closingTermNonnegative t u = is-nonnegative-mul-ℝ
  (is-nonnegative-square-ℝ (remaining t)) (is-nonnegative-abs-ℝ (center u))

closingDNonnegative : (t : Real) (u : ClosedParameter) → is-nonnegative-ℝ (closingD t (pr1 u))
closingDNonnegative t u = tr (λ z → leq-ℝ z (closingD t (pr1 u))) (left-unit-law-add-ℝ zero-ℝ)
  (preserves-leq-add-ℝ (closedGapNonnegative u) (closingTermNonnegative t (pr1 u)))

closingDPositiveSmall : (t u : Real) → le-ℝ (abs-ℝ (center u)) one-ℝ → is-positive-ℝ (closingD t u)
closingDPositiveSmall t u small = tr is-positive-ℝ
  (commutative-add-ℝ (square-ℝ (remaining t) *ℝ abs-ℝ (center u)) (gap u))
  (is-positive-add-nonnegative-positive-ℝ (closingTermNonnegative t u) (is-positive-diff-le-ℝ small))

closingDPositiveBefore : (t : Real) (u : ClosedParameter) → le-ℝ t one-ℝ → is-positive-ℝ (closingD t (pr1 u))
closingDPositiveBefore t u before = elim-disjunction (is-positive-prop-ℝ (closingD t (pr1 u)))
  (λ positiveAbs → is-positive-add-nonnegative-positive-ℝ (closedGapNonnegative u)
    (is-positive-mul-ℝ (is-positive-square-ℝ⁺ (remaining t , is-positive-diff-le-ℝ before)) positiveAbs))
  (closingDPositiveSmall t (pr1 u))
  (cotransitive-le-ℝ zero-ℝ (abs-ℝ (center (pr1 u))) one-ℝ le-zero-one-ℝ)

closingKFromNonzeroD : (t u : Real) → is-nonzero-ℝ (closingD t u) → is-positive-ℝ (closingK t u)
closingKFromNonzeroD t u hd = tr is-positive-ℝ
  (commutative-add-ℝ (square-ℝ (t *ℝ closingN t u)) (square-ℝ (closingD t u)))
  (is-positive-add-nonnegative-positive-ℝ (is-nonnegative-square-ℝ (t *ℝ closingN t u))
    (is-positive-square-is-nonzero-ℝ (closingD t u) hd))

closingKFromNonzeroN : (t u : Real) → is-positive-ℝ t → is-nonzero-ℝ (closingN t u) → is-positive-ℝ (closingK t u)
closingKFromNonzeroN t u ht hn = is-positive-add-nonnegative-positive-ℝ
  (is-nonnegative-square-ℝ (closingD t u))
  (is-positive-square-is-nonzero-ℝ (t *ℝ closingN t u)
    (is-nonzero-mul-ℝ (is-nonzero-is-positive-ℝ ht) hn))

closingNOffsetDifference : (t u : Real) →
  closingN t u -ℝ (offset t *ℝ closingD t u) ＝ scale t *ℝ center u
closingNOffsetDifference t u = eq-sim-ℝ
  (cancel-right-add-diff-ℝ (scale t *ℝ center u) (offset t *ℝ closingD t u))

closingKFromNonzeroCenter : (t u : Real) → is-positive-ℝ t → is-nonzero-ℝ (center u) → is-positive-ℝ (closingK t u)
closingKFromNonzeroCenter t u ht hc = elim-disjunction (is-positive-prop-ℝ (closingK t u))
  (closingKFromNonzeroN t u ht)
  (λ h → closingKFromNonzeroD t u
    (pr2 (is-nonzero-factors-is-nonzero-mul-ℝ (offset t) (closingD t u) (symmetric-apart-ℝ h))))
  (cotransitive-apart-ℝ (closingN t u) zero-ℝ (offset t *ℝ closingD t u)
    (apart-is-nonzero-diff-ℝ (closingN t u) (offset t *ℝ closingD t u)
      (tr is-nonzero-ℝ (inv (closingNOffsetDifference t u))
        (is-nonzero-mul-ℝ (is-nonzero-is-positive-ℝ (scalePositive t)) hc))))

closingKPositiveAtPositiveTime : (t : Real) (u : ClosedParameter) → is-positive-ℝ t → is-positive-ℝ (closingK t (pr1 u))
closingKPositiveAtPositiveTime t u ht = elim-disjunction (is-positive-prop-ℝ (closingK t (pr1 u)))
  (λ ha → closingKFromNonzeroCenter t (pr1 u) ht (is-nonzero-is-positive-abs-ℝ (center (pr1 u)) ha))
  (λ small → closingKFromNonzeroD t (pr1 u) (is-nonzero-is-positive-ℝ (closingDPositiveSmall t (pr1 u) small)))
  (cotransitive-le-ℝ zero-ℝ (abs-ℝ (center (pr1 u))) one-ℝ le-zero-one-ℝ)

closingKPositive : (t : Real) (u : ClosedParameter) → is-positive-ℝ (closingK t (pr1 u))
closingKPositive t u = elim-disjunction (is-positive-prop-ℝ (closingK t (pr1 u)))
  (closingKPositiveAtPositiveTime t u)
  (λ before → closingKFromNonzeroD t (pr1 u) (is-nonzero-is-positive-ℝ (closingDPositiveBefore t u before)))
  (cotransitive-le-ℝ zero-ℝ t one-ℝ le-zero-one-ℝ)

closingNZ : Real → ClosedParameter → NonzeroReal
closingNZ t u = nonzero-ℝ⁺ (closingK t (pr1 u) , closingKPositive t u)

closingInverse : Real → ClosedParameter → Real
closingInverse t u = recip (closingNZ t u)

closedBase : Real → ClosedParameter → RealPlane
closedBase t u = ((closingN t (pr1 u) *ℝ closingD t (pr1 u)) *ℝ closingInverse t u) ,
  ((t *ℝ square-ℝ (closingN t (pr1 u))) *ℝ closingInverse t u)

closedMotion : Real → ClosedParameter → RealPlane
closedMotion t u = reflectY (turn t (closedBase t u))
