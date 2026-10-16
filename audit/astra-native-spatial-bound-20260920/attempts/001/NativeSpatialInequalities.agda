{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeSpatialInequalities where

-- Explicit real inequalities used to bound the unchanged rational motion.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.SignedIntervalHomeomorphism
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.unit-type
open import elementary-number-theory.natural-numbers
open import elementary-number-theory.addition-natural-numbers
open import elementary-number-theory.multiplication-natural-numbers
open import elementary-number-theory.inequality-natural-numbers
open import elementary-number-theory.rational-numbers
open import elementary-number-theory.multiplication-rational-numbers
open import order-theory.large-posets
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-positive-real-numbers
open import real-numbers.multiplication-nonnegative-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.inequalities-addition-and-subtraction-real-numbers
open import real-numbers.strict-inequality-real-numbers

open inequality-reasoning-Large-Poset ℝ-Large-Poset

natLe : (m n : ℕ) → leq-ℕ m n → leq-ℝ (real-ℕ m) (real-ℕ n)
natLe m n = preserves-leq-real-ℕ

natNN : (n : ℕ) → is-nonnegative-ℝ (real-ℕ n)
natNN n = natLe 0 n star

natMul : (m n : ℕ) → real-ℕ m *ℝ real-ℕ n ＝ real-ℕ (m *ℕ n)
natMul m n = mul-real-ℚ (rational-ℕ m) (rational-ℕ n) ∙ ap real-ℚ (mul-rational-ℕ m n)

quarter sixteenth : Real
quarter = square-ℝ one-half-ℝ
sixteenth = square-ℝ quarter

quarterPositive : is-positive-ℝ quarter
quarterPositive = is-positive-square-ℝ⁺ one-half-ℝ⁺

quarterNN : is-nonnegative-ℝ quarter
quarterNN = leq-le-ℝ quarterPositive

quarterLessHalf : le-ℝ quarter one-half-ℝ
quarterLessHalf = tr (le-ℝ quarter) (right-unit-law-mul-ℝ one-half-ℝ)
  (preserves-le-left-mul-ℝ⁺ one-half-ℝ⁺ (pr2 (pr2 intervalHalf)))

quarterLeOne : leq-ℝ quarter one-ℝ
quarterLeOne = leq-le-ℝ (transitive-le-ℝ quarter one-half-ℝ one-ℝ (pr2 (pr2 intervalHalf)) quarterLessHalf)

fourQuarter : real-ℕ 4 *ℝ quarter ＝ one-ℝ
fourQuarter = ap (_*ℝ quarter) (inv (natMul 2 2)) ∙
  interchange-law-mul-mul-ℝ two two one-half-ℝ one-half-ℝ ∙ ap-mul-ℝ twoHalf twoHalf ∙
  left-unit-law-mul-ℝ one-ℝ

sixteenSixteenth : real-ℕ 16 *ℝ sixteenth ＝ one-ℝ
sixteenSixteenth = ap (_*ℝ sixteenth) (inv (natMul 4 4)) ∙
  interchange-law-mul-mul-ℝ (real-ℕ 4) (real-ℕ 4) quarter quarter ∙
  ap-mul-ℝ fourQuarter fourQuarter ∙ left-unit-law-mul-ℝ one-ℝ

leftLeSum : (a b : Real) → is-nonnegative-ℝ b → leq-ℝ a (a +ℝ b)
leftLeSum a b hb = tr (λ z → leq-ℝ z (a +ℝ b)) (right-unit-law-add-ℝ a)
  (preserves-leq-left-add-ℝ a zero-ℝ b hb)

rightLeSum : (a b : Real) → is-nonnegative-ℝ a → leq-ℝ b (a +ℝ b)
rightLeSum a b ha = tr (λ z → leq-ℝ z (a +ℝ b)) (left-unit-law-add-ℝ b)
  (preserves-leq-right-add-ℝ b zero-ℝ a ha)

sumNN : (a b : Real) → is-nonnegative-ℝ a → is-nonnegative-ℝ b → is-nonnegative-ℝ (a +ℝ b)
sumNN a b ha hb = tr (λ z → leq-ℝ z (a +ℝ b)) (left-unit-law-add-ℝ zero-ℝ)
  (preserves-leq-add-ℝ ha hb)

unitSquareBound : (x : Real) → is-nonnegative-ℝ x → leq-ℝ x one-ℝ → leq-ℝ (square-ℝ x) one-ℝ
unitSquareBound x nn bound = tr (leq-ℝ (square-ℝ x)) oneSquared
  (preserves-leq-square-ℝ⁰⁺ (x , nn) (one-ℝ , natNN 1) bound)

absProductBound : (x y a b : Real) → is-nonnegative-ℝ a →
  leq-ℝ (abs-ℝ x) a → leq-ℝ (abs-ℝ y) b → leq-ℝ (abs-ℝ (x *ℝ y)) (a *ℝ b)
absProductBound x y a b nna hx hy = chain-of-inequalities
  abs-ℝ (x *ℝ y)
  ≤ abs-ℝ x *ℝ abs-ℝ y by leq-eq-ℝ (abs-mul-ℝ x y)
  ≤ a *ℝ abs-ℝ y by preserves-leq-right-mul-ℝ⁰⁺ (abs-ℝ y , is-nonnegative-abs-ℝ y) hx
  ≤ a *ℝ b by preserves-leq-left-mul-ℝ⁰⁺ (a , nna) hy

absSumBound : (x y a b : Real) → leq-ℝ (abs-ℝ x) a → leq-ℝ (abs-ℝ y) b →
  leq-ℝ (abs-ℝ (x +ℝ y)) (a +ℝ b)
absSumBound x y a b hx hy = transitive-leq-ℝ _ _ _ (preserves-leq-add-ℝ hx hy)
  (triangle-inequality-abs-ℝ x y)

absProductSquares : (x y : Real) → leq-ℝ (abs-ℝ (x *ℝ y)) (square-ℝ x +ℝ square-ℝ y)
absProductSquares x y = chain-of-inequalities
  abs-ℝ (x *ℝ y)
  ≤ a *ℝ b by leq-eq-ℝ (abs-mul-ℝ x y)
  ≤ two *ℝ (a *ℝ b) by tr (λ z → leq-ℝ z (two *ℝ (a *ℝ b))) (left-unit-law-mul-ℝ (a *ℝ b))
    (preserves-leq-right-mul-ℝ⁰⁺ (a *ℝ b , is-nonnegative-mul-ℝ (is-nonnegative-abs-ℝ x) (is-nonnegative-abs-ℝ y)) (natLe 1 2 star))
  ≤ square-ℝ a +ℝ square-ℝ b by leq-is-nonnegative-diff-ℝ (two *ℝ (a *ℝ b)) (square-ℝ a +ℝ square-ℝ b)
    (tr is-nonnegative-ℝ (square-diff-ℝ a b ∙ shuffleDifference (square-ℝ a) (two *ℝ (a *ℝ b)) (square-ℝ b))
      (is-nonnegative-square-ℝ (a -ℝ b)))
  ≤ square-ℝ x +ℝ square-ℝ y by leq-eq-ℝ (ap-add-ℝ (square-abs-ℝ x) (square-abs-ℝ y))
  where a = abs-ℝ x; b = abs-ℝ y

quotientAbsBound : (n k c : Real) (positive : is-positive-ℝ k) →
  leq-ℝ (abs-ℝ n) (c *ℝ k) → leq-ℝ (abs-ℝ (n *ℝ recip (nonzero-ℝ⁺ (k , positive)))) c
quotientAbsBound n k c positive bound = chain-of-inequalities
  abs-ℝ (n *ℝ q)
  ≤ abs-ℝ n *ℝ q by leq-eq-ℝ (abs-mul-ℝ n q ∙ ap (abs-ℝ n *ℝ_) (abs-real-ℝ⁺ (q , qp)))
  ≤ (c *ℝ k) *ℝ q by preserves-leq-right-mul-ℝ⁺ (q , qp) bound
  ≤ c by leq-eq-ℝ (associative-mul-ℝ c k q ∙ ap (c *ℝ_) (rightInv nz) ∙ right-unit-law-mul-ℝ c)
  where nz = nonzero-ℝ⁺ (k , positive); q = recip nz; qp = positiveRecip (k , positive)
