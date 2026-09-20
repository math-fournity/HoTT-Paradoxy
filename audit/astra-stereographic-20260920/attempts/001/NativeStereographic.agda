{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeStereographic where

-- Actual Dedekind point-set parameterization; topology is a separate obligation.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.equality-cartesian-product-types
open import foundation.subtypes
open import foundation.equivalences
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.apartness-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.strict-inequalities-addition-and-subtraction-real-numbers
open import real-numbers.multiplicative-inverses-nonzero-real-numbers

two : Real
two = real-ℕ 2

twoTimes : (x : Real) → two *ℝ x ＝ x +ℝ x
twoTimes = left-mul-real-ℕ 2

twoAsSum : two ＝ one-ℝ +ℝ one-ℝ
twoAsSum = inv (right-unit-law-mul-ℝ two) ∙ twoTimes one-ℝ

twoHalf : two *ℝ one-half-ℝ ＝ one-ℝ
twoHalf = twoTimes one-half-ℝ ∙
  inv (ap-add-ℝ (right-unit-law-mul-ℝ one-half-ℝ) (right-unit-law-mul-ℝ one-half-ℝ)) ∙
  twice-left-mul-one-half-ℝ one-ℝ

cancelAdd : (a b : Real) → (a -ℝ b) +ℝ b ＝ a
cancelAdd a b = eq-sim-ℝ (cancel-right-diff-add-ℝ a b)

-- The additive cancellation needed by the difference-of-squares identity.
cancelMiddle : (a b c : Real) → ((a -ℝ b) +ℝ c) +ℝ (b +ℝ b) ＝ (a +ℝ b) +ℝ c
cancelMiddle a b c =
  associative-add-ℝ (a -ℝ b) c (b +ℝ b) ∙
  ap ((a -ℝ b) +ℝ_) (commutative-add-ℝ c (b +ℝ b)) ∙
  inv (associative-add-ℝ (a -ℝ b) (b +ℝ b) c) ∙
  ap (_+ℝ c) (inv (associative-add-ℝ (a -ℝ b) b b)) ∙
  ap (_+ℝ c) (ap (_+ℝ b) (cancelAdd a b))

squareDiffPlusFour : (a b : Real) →
  square-ℝ (a -ℝ b) +ℝ ((two *ℝ (a *ℝ b)) +ℝ (two *ℝ (a *ℝ b))) ＝ square-ℝ (a +ℝ b)
squareDiffPlusFour a b =
  ap (_+ℝ ((two *ℝ (a *ℝ b)) +ℝ (two *ℝ (a *ℝ b)))) (square-diff-ℝ a b) ∙
  cancelMiddle (square-ℝ a) (two *ℝ (a *ℝ b)) (square-ℝ b) ∙
  inv (square-add-ℝ a b)

squareDouble : (t : Real) →
  square-ℝ (t +ℝ t) ＝ (square-ℝ t +ℝ square-ℝ t) +ℝ (square-ℝ t +ℝ square-ℝ t)
squareDouble t = left-distributive-mul-add-ℝ (t +ℝ t) t t ∙
  ap-add-ℝ (right-distributive-mul-add-ℝ t t t) (right-distributive-mul-add-ℝ t t t)

pythagoreanNumerators : (t : Real) →
  square-ℝ (square-ℝ t -ℝ one-ℝ) +ℝ square-ℝ (t +ℝ t) ＝ square-ℝ (square-ℝ t +ℝ one-ℝ)
pythagoreanNumerators t =
  ap (square-ℝ (square-ℝ t -ℝ one-ℝ) +ℝ_)
    (squareDouble t ∙ inv (ap-add-ℝ kEq kEq)) ∙
  squareDiffPlusFour (square-ℝ t) one-ℝ
  where
  kEq : two *ℝ (square-ℝ t *ℝ one-ℝ) ＝ square-ℝ t +ℝ square-ℝ t
  kEq = ap (two *ℝ_) (right-unit-law-mul-ℝ (square-ℝ t)) ∙ twoTimes (square-ℝ t)

scaledSquares : (a b q : Real) →
  square-ℝ (a *ℝ q) +ℝ square-ℝ (b *ℝ q) ＝ (square-ℝ a +ℝ square-ℝ b) *ℝ square-ℝ q
scaledSquares a b q =
  ap-add-ℝ (distributive-square-mul-ℝ a q) (distributive-square-mul-ℝ b q) ∙
  inv (right-distributive-mul-add-ℝ (square-ℝ a) (square-ℝ b) (square-ℝ q))

D : Real → Real
D t = square-ℝ t +ℝ one-ℝ

positiveD : (t : Real) → le-ℝ zero-ℝ (D t)
positiveD t = concatenate-leq-le-ℝ zero-ℝ (square-ℝ t) (D t)
  (is-nonnegative-square-ℝ t)
  (tr (λ z → le-ℝ z (D t)) (right-unit-law-add-ℝ (square-ℝ t))
    (preserves-le-left-add-ℝ (square-ℝ t) zero-ℝ one-ℝ le-zero-one-ℝ))

qInv : Real → Real
qInv t = real-inv-nonzero-ℝ (D t , is-nonzero-is-positive-ℝ (positiveD t))

Dq : (t : Real) → D t *ℝ qInv t ＝ one-ℝ
Dq t = eq-sim-ℝ
  (right-inverse-law-mul-nonzero-ℝ (D t , is-nonzero-is-positive-ℝ (positiveD t)))

qD : (t : Real) → qInv t *ℝ D t ＝ one-ℝ
qD t = commutative-mul-ℝ (qInv t) (D t) ∙ Dq t

numeratorX numeratorY : Real → Real
numeratorX t = square-ℝ t -ℝ one-ℝ
numeratorY t = t +ℝ t

paramPlane : Real → RealPlane
paramPlane t = (numeratorX t *ℝ qInv t) , (numeratorY t *ℝ qInv t)

paramEquation : (t : Real) → circleEquation (paramPlane t) ＝ one-ℝ
paramEquation t =
  scaledSquares (numeratorX t) (numeratorY t) (qInv t) ∙
  ap (_*ℝ square-ℝ (qInv t)) (pythagoreanNumerators t) ∙
  inv (distributive-square-mul-ℝ (D t) (qInv t)) ∙
  ap square-ℝ (Dq t) ∙ oneSquared

paramPoint : Real → RealCircle
paramPoint t = paramPlane t , paramEquation t

sumMinusDiff : (s : Real) → (s +ℝ one-ℝ) -ℝ (s -ℝ one-ℝ) ＝ two
sumMinusDiff s =
  ap (_-ℝ (s -ℝ one-ℝ)) (commutative-add-ℝ s one-ℝ) ∙
  ap ((one-ℝ +ℝ s) -ℝ_) (commutative-add-ℝ s (neg-ℝ one-ℝ)) ∙
  eq-sim-ℝ (diff-add-ℝ one-ℝ (neg-ℝ one-ℝ) s) ∙
  ap (one-ℝ +ℝ_) (neg-neg-ℝ one-ℝ) ∙ inv twoAsSum

paramDenominator : (t : Real) → denominator (paramPoint t) ＝ two *ℝ qInv t
paramDenominator t =
  ap (_-ℝ (numeratorX t *ℝ qInv t)) (inv (Dq t)) ∙
  inv (right-distributive-mul-diff-ℝ (D t) (numeratorX t) (qInv t)) ∙
  ap (_*ℝ qInv t) (sumMinusDiff (square-ℝ t))

paramInverseEquation : (t : Real) →
  denominator (paramPoint t) *ℝ (one-half-ℝ *ℝ D t) ＝ one-ℝ
paramInverseEquation t =
  ap (_*ℝ (one-half-ℝ *ℝ D t)) (paramDenominator t) ∙
  interchange-law-mul-mul-ℝ two (qInv t) one-half-ℝ (D t) ∙
  ap-mul-ℝ twoHalf (qD t) ∙ left-unit-law-mul-ℝ one-ℝ

paramStrong : (t : Real) → Strong (paramPoint t)
paramStrong t = rawInverseToStrong (paramPoint t)
  ((one-half-ℝ *ℝ D t) , paramInverseEquation t)

parameterize : Real → StrongPuncture
parameterize t = paramPoint t , paramStrong t

paramY : (t : Real) → yCoord (paramPoint t) ＝ t *ℝ denominator (paramPoint t)
paramY t =
  ap (_*ℝ qInv t) (inv (twoTimes t) ∙ commutative-mul-ℝ two t) ∙
  associative-mul-ℝ t two (qInv t) ∙
  ap (t *ℝ_) (inv (paramDenominator t))

forwardParameter : (t : Real) → stereographicForward (parameterize t) ＝ t
forwardParameter t =
  ap (_*ℝ inverseDenominator (paramPoint t) (paramStrong t)) (paramY t) ∙
  associative-mul-ℝ t (denominator (paramPoint t)) (inverseDenominator (paramPoint t) (paramStrong t)) ∙
  ap (t *ℝ_) (denominatorRightInverse (paramPoint t) (paramStrong t)) ∙
  right-unit-law-mul-ℝ t
