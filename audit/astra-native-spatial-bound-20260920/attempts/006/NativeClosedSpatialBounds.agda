{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeClosedSpatialBounds where

-- Uniform coordinate bound for the unchanged full closed motion on [0,1]^2.
-- The bound is deliberately explicit; no velocity or material claim is made.
open import hott-z.NativeSpatialInequalities
open import hott-z.NativeClosedSpatialCoefficients
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionInterior
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.NativeCompletion
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.propositions
open import foundation.conjunction
open import foundation.disjunction
open import foundation.unit-type
open import elementary-number-theory.natural-numbers
open import elementary-number-theory.multiplication-natural-numbers
open import order-theory.large-posets
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-nonnegative-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.inequalities-addition-and-subtraction-real-numbers
open import real-numbers.strict-inequality-real-numbers

open inequality-reasoning-Large-Poset ℝ-Large-Poset

remainingHalf : remaining one-half-ℝ ＝ one-half-ℝ
remainingHalf = ap (_-ℝ one-half-ℝ) (inv (inv (twoTimes one-half-ℝ) ∙ twoHalf)) ∙
  eq-sim-ℝ (cancel-right-add-diff-ℝ one-half-ℝ one-half-ℝ)

closingDSquareLeK : (t u : ClosedParameter) →
  leq-ℝ (square-ℝ (closingD (pr1 t) (pr1 u))) (closingK (pr1 t) (pr1 u))
closingDSquareLeK t u = leftLeSum _ _ (is-nonnegative-square-ℝ (pr1 t *ℝ closingN (pr1 t) (pr1 u)))

closingTNSquareLeK : (t u : ClosedParameter) →
  leq-ℝ (square-ℝ (pr1 t *ℝ closingN (pr1 t) (pr1 u))) (closingK (pr1 t) (pr1 u))
closingTNSquareLeK t u = rightLeSum _ _ (is-nonnegative-square-ℝ (closingD (pr1 t) (pr1 u)))

earlyDLower : (t u : ClosedParameter) → le-ℝ (pr1 t) one-half-ℝ → leq-ℝ quarter (closingD (pr1 t) (pr1 u))
earlyDLower t u early = chain-of-inequalities
  quarter ≤ quarter *ℝ (g +ℝ v) by leq-eq-ℝ
    (inv (right-unit-law-mul-ℝ quarter) ∙ ap (quarter *ℝ_) (inv (cancelAdd one-ℝ v)))
  ≤ (quarter *ℝ g) +ℝ (quarter *ℝ v) by leq-eq-ℝ (left-distributive-mul-add-ℝ quarter g v)
  ≤ g +ℝ (square-ℝ (remaining (pr1 t)) *ℝ v) by preserves-leq-add-ℝ
    (tr (leq-ℝ (quarter *ℝ g)) (left-unit-law-mul-ℝ g)
      (preserves-leq-right-mul-ℝ⁰⁺ (g , closedGapNonnegative u) quarterLeOne))
    (preserves-leq-right-mul-ℝ⁰⁺ (v , is-nonnegative-abs-ℝ (center (pr1 u)))
      (preserves-leq-square-ℝ⁰⁺ (one-half-ℝ , leq-le-ℝ (pr2 one-half-ℝ⁺))
        (remaining (pr1 t) , remainingNN t) halfLower))
  where
  g = gap (pr1 u); v = abs-ℝ (center (pr1 u))
  halfLower : leq-ℝ one-half-ℝ (remaining (pr1 t))
  halfLower = tr (λ z → leq-ℝ z (remaining (pr1 t))) remainingHalf
    (preserves-leq-left-add-ℝ one-ℝ (neg-ℝ one-half-ℝ) (neg-ℝ (pr1 t)) (neg-leq-ℝ (leq-le-ℝ early)))

earlyKScale : (t u : ClosedParameter) → le-ℝ (pr1 t) one-half-ℝ →
  leq-ℝ one-ℝ (real-ℕ 16 *ℝ closingK (pr1 t) (pr1 u))
earlyKScale t u early = tr (λ z → leq-ℝ z (real-ℕ 16 *ℝ closingK (pr1 t) (pr1 u))) sixteenSixteenth
  (preserves-leq-left-mul-ℝ⁰⁺ (real-ℕ 16 , natNN 16)
    (transitive-leq-ℝ _ _ _ (closingDSquareLeK t u)
      (preserves-leq-square-ℝ⁰⁺ (quarter , quarterNN)
        (closingD (pr1 t) (pr1 u) , closingDNonnegative (pr1 t) u) (earlyDLower t u early))))

scaleUnitLower : (m : ℕ) (k : Real) → leq-ℝ one-ℝ (real-ℕ 16 *ℝ k) →
  leq-ℝ (real-ℕ m) (real-ℕ (m *ℕ 16) *ℝ k)
scaleUnitLower m k h = chain-of-inequalities
  real-ℕ m ≤ real-ℕ m *ℝ one-ℝ by leq-eq-ℝ (inv (right-unit-law-mul-ℝ (real-ℕ m)))
  ≤ real-ℕ m *ℝ (real-ℕ 16 *ℝ k) by preserves-leq-left-mul-ℝ⁰⁺ (real-ℕ m , natNN m) h
  ≤ real-ℕ (m *ℕ 16) *ℝ k by leq-eq-ℝ
    (inv (associative-mul-ℝ (real-ℕ m) (real-ℕ 16) k) ∙ ap (_*ℝ k) (natMul m 16))

earlyBaseXBound : (t u : ClosedParameter) → le-ℝ (pr1 t) one-half-ℝ →
  leq-ℝ (abs-ℝ (pr1 (closedBase (pr1 t) u))) (real-ℕ 32)
earlyBaseXBound t u early = quotientAbsBound _ _ (real-ℕ 32) (closingKPositive (pr1 t) u)
  (transitive-leq-ℝ _ _ _ (scaleUnitLower 2 (closingK (pr1 t) (pr1 u)) (earlyKScale t u early)) (closingXNumeratorBound t u))

earlyBaseYBound : (t u : ClosedParameter) → le-ℝ (pr1 t) one-half-ℝ →
  leq-ℝ (abs-ℝ (pr2 (closedBase (pr1 t) u))) (real-ℕ 64)
earlyBaseYBound t u early = quotientAbsBound _ _ (real-ℕ 64) (closingKPositive (pr1 t) u)
  (transitive-leq-ℝ _ _ _ (scaleUnitLower 4 (closingK (pr1 t) (pr1 u)) (earlyKScale t u early)) (closingYNumeratorBound t u))

lateNSquareBound : (t u : ClosedParameter) → le-ℝ quarter (pr1 t) →
  leq-ℝ (square-ℝ (closingN (pr1 t) (pr1 u))) (real-ℕ 16 *ℝ closingK (pr1 t) (pr1 u))
lateNSquareBound t u late = chain-of-inequalities
  square-ℝ n ≤ (real-ℕ 16 *ℝ square-ℝ (pr1 t)) *ℝ square-ℝ n by
    tr (λ z → leq-ℝ z ((real-ℕ 16 *ℝ square-ℝ (pr1 t)) *ℝ square-ℝ n)) (left-unit-law-mul-ℝ (square-ℝ n))
      (preserves-leq-right-mul-ℝ⁰⁺ (square-ℝ n , is-nonnegative-square-ℝ n) timeLower)
  ≤ real-ℕ 16 *ℝ square-ℝ (pr1 t *ℝ n) by leq-eq-ℝ
    (associative-mul-ℝ (real-ℕ 16) (square-ℝ (pr1 t)) (square-ℝ n) ∙
      ap (real-ℕ 16 *ℝ_) (inv (distributive-square-mul-ℝ (pr1 t) n)))
  ≤ real-ℕ 16 *ℝ closingK (pr1 t) (pr1 u) by
    preserves-leq-left-mul-ℝ⁰⁺ (real-ℕ 16 , natNN 16) (closingTNSquareLeK t u)
  where
  n = closingN (pr1 t) (pr1 u)
  timeLower : leq-ℝ one-ℝ (real-ℕ 16 *ℝ square-ℝ (pr1 t))
  timeLower = tr (λ z → leq-ℝ z (real-ℕ 16 *ℝ square-ℝ (pr1 t))) sixteenSixteenth
    (preserves-leq-left-mul-ℝ⁰⁺ (real-ℕ 16 , natNN 16)
      (preserves-leq-square-ℝ⁰⁺ (quarter , quarterNN) (pr1 t , timeNN t) (leq-le-ℝ late)))

lateBaseXBound : (t u : ClosedParameter) → le-ℝ quarter (pr1 t) →
  leq-ℝ (abs-ℝ (pr1 (closedBase (pr1 t) u))) (real-ℕ 32)
lateBaseXBound t u late = quotientAbsBound (n *ℝ d) k (real-ℕ 32) (closingKPositive (pr1 t) u)
  (chain-of-inequalities
    abs-ℝ (n *ℝ d) ≤ square-ℝ n +ℝ square-ℝ d by absProductSquares n d
    ≤ (real-ℕ 16 *ℝ k) +ℝ k by preserves-leq-add-ℝ (lateNSquareBound t u late) (closingDSquareLeK t u)
    ≤ (real-ℕ 16 +ℝ one-ℝ) *ℝ k by leq-eq-ℝ
      (inv (right-distributive-mul-add-ℝ (real-ℕ 16) one-ℝ k ∙ ap-add-ℝ refl (left-unit-law-mul-ℝ k)))
    ≤ real-ℕ 17 *ℝ k by leq-eq-ℝ (ap (_*ℝ k) (add-real-ℕ 16 1))
    ≤ real-ℕ 32 *ℝ k by preserves-leq-right-mul-ℝ⁰⁺ (k , leq-le-ℝ (closingKPositive (pr1 t) u)) (natLe 17 32 star))
  where n = closingN (pr1 t) (pr1 u); d = closingD (pr1 t) (pr1 u); k = closingK (pr1 t) (pr1 u)

lateBaseYBound : (t u : ClosedParameter) → le-ℝ quarter (pr1 t) →
  leq-ℝ (abs-ℝ (pr2 (closedBase (pr1 t) u))) (real-ℕ 64)
lateBaseYBound t u late = quotientAbsBound (pr1 t *ℝ square-ℝ n) k (real-ℕ 64) (closingKPositive (pr1 t) u)
  (chain-of-inequalities
    abs-ℝ (pr1 t *ℝ square-ℝ n) ≤ pr1 t *ℝ square-ℝ n by
      leq-eq-ℝ (abs-real-ℝ⁰⁺ (pr1 t *ℝ square-ℝ n , is-nonnegative-mul-ℝ (timeNN t) (is-nonnegative-square-ℝ n)))
    ≤ one-ℝ *ℝ square-ℝ n by preserves-leq-right-mul-ℝ⁰⁺ (square-ℝ n , is-nonnegative-square-ℝ n) (pr2 (pr2 t))
    ≤ square-ℝ n by leq-eq-ℝ (left-unit-law-mul-ℝ (square-ℝ n))
    ≤ real-ℕ 16 *ℝ k by lateNSquareBound t u late
    ≤ real-ℕ 64 *ℝ k by preserves-leq-right-mul-ℝ⁰⁺ (k , leq-le-ℝ (closingKPositive (pr1 t) u)) (natLe 16 64 star))
  where n = closingN (pr1 t) (pr1 u); k = closingK (pr1 t) (pr1 u)

closedBaseBounds : (t u : ClosedParameter) →
  type-Prop (leq-prop-ℝ (abs-ℝ (pr1 (closedBase (pr1 t) u))) (real-ℕ 32) ∧
    leq-prop-ℝ (abs-ℝ (pr2 (closedBase (pr1 t) u))) (real-ℕ 64))
closedBaseBounds t u = elim-disjunction
  (leq-prop-ℝ (abs-ℝ (pr1 (closedBase (pr1 t) u))) (real-ℕ 32) ∧
    leq-prop-ℝ (abs-ℝ (pr2 (closedBase (pr1 t) u))) (real-ℕ 64))
  (λ late → lateBaseXBound t u late , lateBaseYBound t u late)
  (λ early → earlyBaseXBound t u early , earlyBaseYBound t u early)
  (cotransitive-le-ℝ quarter (pr1 t) one-half-ℝ quarterLessHalf)

PlaneBound : RealPlane → UU lzero
PlaneBound p = type-Prop (leq-prop-ℝ (abs-ℝ (pr1 p)) (real-ℕ 256) ∧ leq-prop-ℝ (abs-ℝ (pr2 p)) (real-ℕ 256))

closedMotionUniformBound : (t u : ClosedParameter) → PlaneBound (closedMotion (pr1 t) u)
closedMotionUniformBound t u =
  (chain-of-inequalities
    abs-ℝ (pr1 (closedMotion (pr1 t) u)) ≤ ((one-ℝ *ℝ real-ℕ 32) +ℝ (two *ℝ real-ℕ 64)) +ℝ one-ℝ by xBound
    ≤ real-ℕ 161 by leq-eq-ℝ
      (ap (_+ℝ one-ℝ) (ap-add-ℝ (natMul 1 32) (natMul 2 64) ∙ add-real-ℕ 32 128) ∙ add-real-ℕ 160 1)
    ≤ real-ℕ 256 by natLe 161 256 star) ,
  (chain-of-inequalities
    abs-ℝ (pr2 (closedMotion (pr1 t) u)) ≤ abs-ℝ ((neg-ℝ b *ℝ x) +ℝ (a *ℝ y)) by leq-eq-ℝ (abs-neg-ℝ ((neg-ℝ b *ℝ x) +ℝ (a *ℝ y)))
    ≤ (two *ℝ real-ℕ 32) +ℝ (one-ℝ *ℝ real-ℕ 64) by yBound
    ≤ real-ℕ 128 by leq-eq-ℝ (ap-add-ℝ (natMul 2 32) (natMul 1 64) ∙ add-real-ℕ 64 64)
    ≤ real-ℕ 256 by natLe 128 256 star)
  where
  a = remaining (pr1 t); b = two *ℝ pr1 t
  x = pr1 (closedBase (pr1 t) u); y = pr2 (closedBase (pr1 t) u)
  bx = pr1 (closedBaseBounds t u); by = pr2 (closedBaseBounds t u)
  bb : leq-ℝ (abs-ℝ b) two
  bb = tr (leq-ℝ (abs-ℝ b)) (right-unit-law-mul-ℝ two)
    (absProductBound two (pr1 t) two one-ℝ (natNN 2) (leq-eq-ℝ (abs-real-ℝ⁰⁺ (two , natNN 2))) (timeAbsBound t))
  xBound = absSumBound ((a *ℝ x) +ℝ (b *ℝ y)) (neg-ℝ (pr1 t))
    ((one-ℝ *ℝ real-ℕ 32) +ℝ (two *ℝ real-ℕ 64)) one-ℝ
    (absSumBound (a *ℝ x) (b *ℝ y) (one-ℝ *ℝ real-ℕ 32) (two *ℝ real-ℕ 64)
      (absProductBound a x one-ℝ (real-ℕ 32) (natNN 1) (remainingAbsBound t) bx)
      (absProductBound b y two (real-ℕ 64) (natNN 2) bb by))
    (tr (λ z → leq-ℝ z one-ℝ) (inv (abs-neg-ℝ (pr1 t))) (timeAbsBound t))
  yBound = absSumBound (neg-ℝ b *ℝ x) (a *ℝ y) (two *ℝ real-ℕ 32) (one-ℝ *ℝ real-ℕ 64)
    (absProductBound (neg-ℝ b) x two (real-ℕ 32) (natNN 2) (tr (λ z → leq-ℝ z two) (inv (abs-neg-ℝ b)) bb) bx)
    (absProductBound a y one-ℝ (real-ℕ 64) (natNN 1) (remainingAbsBound t) by)

motionUniformBound : (t : ClosedParameter) (u : OpenRealInterval) → PlaneBound (motion (pr1 t) u)
motionUniformBound t u = tr PlaneBound (closedAgreesInterior (pr1 t) u) (closedMotionUniformBound t (openIntoClosed u))
