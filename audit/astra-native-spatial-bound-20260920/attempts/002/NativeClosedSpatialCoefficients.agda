{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeClosedSpatialCoefficients where

-- Bounds for the coefficients and numerators of the original closed formula.
open import hott-z.NativeSpatialInequalities
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeMotion
open import hott-z.NativeStretchInverse
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.NativeCompletion
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.unit-type
open import order-theory.large-posets
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-nonnegative-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.inequalities-addition-and-subtraction-real-numbers
open import real-numbers.strict-inequality-real-numbers

open inequality-reasoning-Large-Poset ℝ-Large-Poset

timeNN : (t : ClosedParameter) → is-nonnegative-ℝ (pr1 t)
timeNN t = pr1 (pr2 t)

timeAbsBound : (t : ClosedParameter) → leq-ℝ (abs-ℝ (pr1 t)) one-ℝ
timeAbsBound t = chain-of-inequalities
  abs-ℝ (pr1 t) ≤ pr1 t by leq-eq-ℝ (abs-real-ℝ⁰⁺ (pr1 t , timeNN t))
  ≤ one-ℝ by pr2 (pr2 t)

remainingNN : (t : ClosedParameter) → is-nonnegative-ℝ (remaining (pr1 t))
remainingNN t = is-nonnegative-diff-leq-ℝ (pr2 (pr2 t))

remainingUpper : (t : ClosedParameter) → leq-ℝ (remaining (pr1 t)) one-ℝ
remainingUpper t = tr (leq-ℝ (remaining (pr1 t))) (right-unit-law-add-ℝ one-ℝ)
  (preserves-leq-left-add-ℝ one-ℝ (neg-ℝ (pr1 t)) zero-ℝ
    (tr (leq-ℝ (neg-ℝ (pr1 t))) neg-zero-ℝ (neg-leq-ℝ (timeNN t))))

remainingAbsBound : (t : ClosedParameter) → leq-ℝ (abs-ℝ (remaining (pr1 t))) one-ℝ
remainingAbsBound t = chain-of-inequalities
  abs-ℝ (remaining (pr1 t)) ≤ remaining (pr1 t) by leq-eq-ℝ (abs-real-ℝ⁰⁺ (remaining (pr1 t) , remainingNN t))
  ≤ one-ℝ by remainingUpper t

scaleUpper : (t : ClosedParameter) → leq-ℝ (scale (pr1 t)) one-ℝ
scaleUpper t = chain-of-inequalities
  scale (pr1 t)
  ≤ one-half-ℝ *ℝ two by preserves-leq-left-mul-ℝ⁰⁺ (one-half-ℝ , leq-le-ℝ (pr2 one-half-ℝ⁺))
    (tr (leq-ℝ (D (pr1 t))) (inv twoAsSum)
      (preserves-leq-add-ℝ (unitSquareBound (pr1 t) (timeNN t) (pr2 (pr2 t))) (refl-leq-ℝ one-ℝ)))
  ≤ one-ℝ by leq-eq-ℝ (commutative-mul-ℝ one-half-ℝ two ∙ twoHalf)

scaleAbsBound : (t : ClosedParameter) → leq-ℝ (abs-ℝ (scale (pr1 t))) one-ℝ
scaleAbsBound t = chain-of-inequalities
  abs-ℝ (scale (pr1 t)) ≤ scale (pr1 t) by leq-eq-ℝ (abs-real-ℝ⁺ (scale (pr1 t) , scalePositive (pr1 t)))
  ≤ one-ℝ by scaleUpper t

offsetNN : (t : ClosedParameter) → is-nonnegative-ℝ (offset (pr1 t))
offsetNN t = is-nonnegative-mul-ℝ (leq-le-ℝ (pr2 one-half-ℝ⁺)) (remainingNN t)

offsetAbsBound : (t : ClosedParameter) → leq-ℝ (abs-ℝ (offset (pr1 t))) one-ℝ
offsetAbsBound t = chain-of-inequalities
  abs-ℝ (offset (pr1 t)) ≤ offset (pr1 t) by leq-eq-ℝ (abs-real-ℝ⁰⁺ (offset (pr1 t) , offsetNN t))
  ≤ one-half-ℝ *ℝ one-ℝ by preserves-leq-left-mul-ℝ⁰⁺ (one-half-ℝ , leq-le-ℝ (pr2 one-half-ℝ⁺)) (remainingUpper t)
  ≤ one-half-ℝ by leq-eq-ℝ (right-unit-law-mul-ℝ one-half-ℝ)
  ≤ one-ℝ by leq-le-ℝ (pr2 (pr2 intervalHalf))

closingDUpper : (t u : ClosedParameter) → leq-ℝ (closingD (pr1 t) (pr1 u)) one-ℝ
closingDUpper t u = chain-of-inequalities
  closingD (pr1 t) (pr1 u)
  ≤ gap (pr1 u) +ℝ (one-ℝ *ℝ abs-ℝ (center (pr1 u))) by
    preserves-leq-left-add-ℝ (gap (pr1 u)) _ _
      (preserves-leq-right-mul-ℝ⁰⁺ (abs-ℝ (center (pr1 u)) , is-nonnegative-abs-ℝ (center (pr1 u)))
        (unitSquareBound (remaining (pr1 t)) (remainingNN t) (remainingUpper t)))
  ≤ gap (pr1 u) +ℝ abs-ℝ (center (pr1 u)) by leq-eq-ℝ
    (ap (gap (pr1 u) +ℝ_) (left-unit-law-mul-ℝ (abs-ℝ (center (pr1 u)))))
  ≤ one-ℝ by leq-eq-ℝ (cancelAdd one-ℝ (abs-ℝ (center (pr1 u))))

closingDAbsBound : (t u : ClosedParameter) → leq-ℝ (abs-ℝ (closingD (pr1 t) (pr1 u))) one-ℝ
closingDAbsBound t u = chain-of-inequalities
  abs-ℝ (closingD (pr1 t) (pr1 u)) ≤ closingD (pr1 t) (pr1 u) by
    leq-eq-ℝ (abs-real-ℝ⁰⁺ (closingD (pr1 t) (pr1 u) , closingDNonnegative (pr1 t) u))
  ≤ one-ℝ by closingDUpper t u

unitProductAbs : (x y : Real) → leq-ℝ (abs-ℝ x) one-ℝ → leq-ℝ (abs-ℝ y) one-ℝ → leq-ℝ (abs-ℝ (x *ℝ y)) one-ℝ
unitProductAbs x y hx hy = tr (leq-ℝ (abs-ℝ (x *ℝ y))) (left-unit-law-mul-ℝ one-ℝ)
  (absProductBound x y one-ℝ one-ℝ (natNN 1) hx hy)

closingNAbsBound : (t u : ClosedParameter) → leq-ℝ (abs-ℝ (closingN (pr1 t) (pr1 u))) two
closingNAbsBound t u = tr (leq-ℝ (abs-ℝ (closingN (pr1 t) (pr1 u)))) (inv twoAsSum)
  (absSumBound (scale (pr1 t) *ℝ center (pr1 u)) (offset (pr1 t) *ℝ closingD (pr1 t) (pr1 u)) one-ℝ one-ℝ
    (unitProductAbs (scale (pr1 t)) (center (pr1 u)) (scaleAbsBound t) (closedCenterAbsBound u))
    (unitProductAbs (offset (pr1 t)) (closingD (pr1 t) (pr1 u)) (offsetAbsBound t) (closingDAbsBound t u)))

closingNSquareBound : (t u : ClosedParameter) → leq-ℝ (square-ℝ (closingN (pr1 t) (pr1 u))) (real-ℕ 4)
closingNSquareBound t u = chain-of-inequalities
  square-ℝ n ≤ square-ℝ (abs-ℝ n) by leq-eq-ℝ (inv (square-abs-ℝ n))
  ≤ square-ℝ two by preserves-leq-square-ℝ⁰⁺ (abs-ℝ n , is-nonnegative-abs-ℝ n) (two , natNN 2) (closingNAbsBound t u)
  ≤ real-ℕ 4 by leq-eq-ℝ (natMul 2 2)
  where n = closingN (pr1 t) (pr1 u)

closingXNumeratorBound : (t u : ClosedParameter) →
  leq-ℝ (abs-ℝ (closingN (pr1 t) (pr1 u) *ℝ closingD (pr1 t) (pr1 u))) two
closingXNumeratorBound t u = tr (leq-ℝ (abs-ℝ (closingN (pr1 t) (pr1 u) *ℝ closingD (pr1 t) (pr1 u))))
  (right-unit-law-mul-ℝ two)
  (absProductBound _ _ two one-ℝ (natNN 2) (closingNAbsBound t u) (closingDAbsBound t u))

closingYNumeratorBound : (t u : ClosedParameter) →
  leq-ℝ (abs-ℝ (pr1 t *ℝ square-ℝ (closingN (pr1 t) (pr1 u))))) (real-ℕ 4)
closingYNumeratorBound t u = tr (leq-ℝ (abs-ℝ (pr1 t *ℝ square-ℝ n))) (left-unit-law-mul-ℝ (real-ℕ 4))
  (absProductBound (pr1 t) (square-ℝ n) one-ℝ (real-ℕ 4) (natNN 1) (timeAbsBound t)
    (tr (λ z → leq-ℝ z (real-ℕ 4)) (inv (abs-real-ℝ⁰⁺ (square-ℝ n , is-nonnegative-square-ℝ n))) (closingNSquareBound t u)))
  where n = closingN (pr1 t) (pr1 u)
