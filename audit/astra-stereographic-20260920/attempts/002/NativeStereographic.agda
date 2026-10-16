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

shuffleDifference : (a b c : Real) → (a -ℝ b) +ℝ c ＝ (a +ℝ c) -ℝ b
shuffleDifference a b c = associative-add-ℝ a (neg-ℝ b) c ∙
  ap (a +ℝ_) (commutative-add-ℝ (neg-ℝ b) c) ∙
  inv (associative-add-ℝ a c (neg-ℝ b))

-- This equation is derived from the actual circle equation, not postulated.
circleDenominatorSquares : (p : RealCircle) →
  square-ℝ (denominator p) +ℝ square-ℝ (yCoord p) ＝ two *ℝ denominator p
circleDenominatorSquares p =
  ap (_+ℝ square-ℝ y) (square-diff-ℝ one-ℝ x ∙ normalize) ∙
  associative-add-ℝ (one-ℝ -ℝ (two *ℝ x)) (square-ℝ x) (square-ℝ y) ∙
  ap ((one-ℝ -ℝ (two *ℝ x)) +ℝ_) (pr2 p) ∙
  shuffleDifference one-ℝ (two *ℝ x) one-ℝ ∙
  ap (_-ℝ (two *ℝ x)) (inv twoAsSum) ∙
  ap (_-ℝ (two *ℝ x)) (inv (right-unit-law-mul-ℝ two)) ∙
  inv (left-distributive-mul-diff-ℝ two one-ℝ x)
  where
  x = xCoord p
  y = yCoord p
  normalize :
    (square-ℝ one-ℝ -ℝ (two *ℝ (one-ℝ *ℝ x))) +ℝ square-ℝ x ＝
    (one-ℝ -ℝ (two *ℝ x)) +ℝ square-ℝ x
  normalize = ap (_+ℝ square-ℝ x)
    (ap (_-ℝ (two *ℝ (one-ℝ *ℝ x))) oneSquared ∙
      ap (λ z → one-ℝ -ℝ (two *ℝ z)) (left-unit-law-mul-ℝ x))

cancelRightFactor : (a b d r : Real) → d *ℝ r ＝ one-ℝ → a *ℝ d ＝ b *ℝ d → a ＝ b
cancelRightFactor a b d r dr e =
  inv (right-unit-law-mul-ℝ a) ∙ ap (a *ℝ_) (inv dr) ∙
  inv (associative-mul-ℝ a d r) ∙ ap (_*ℝ r) e ∙
  associative-mul-ℝ b d r ∙ ap (b *ℝ_) dr ∙ right-unit-law-mul-ℝ b

forwardTimesDenominator : (w : StrongPuncture) →
  stereographicForward w *ℝ denominator (pr1 w) ＝ yCoord (pr1 w)
forwardTimesDenominator (p , a) =
  associative-mul-ℝ (yCoord p) (inverseDenominator p a) (denominator p) ∙
  ap (yCoord p *ℝ_)
    (commutative-mul-ℝ (inverseDenominator p a) (denominator p) ∙ denominatorRightInverse p a) ∙
  right-unit-law-mul-ℝ (yCoord p)

DtimesDenominator : (w : StrongPuncture) →
  D (stereographicForward w) *ℝ denominator (pr1 w) ＝ two
DtimesDenominator w@(p , a) =
  cancelRightFactor (D t *ℝ d) two d (inverseDenominator p a)
    (denominatorRightInverse p a) multiplied
  where
  t = stereographicForward w
  d = denominator p
  multiplied : (D t *ℝ d) *ℝ d ＝ two *ℝ d
  multiplied =
    associative-mul-ℝ (D t) d d ∙
    right-distributive-mul-add-ℝ (square-ℝ t) one-ℝ (square-ℝ d) ∙
    ap-add-ℝ (inv (distributive-square-mul-ℝ t d)) (left-unit-law-mul-ℝ (square-ℝ d)) ∙
    ap (_+ℝ square-ℝ d) (ap square-ℝ (forwardTimesDenominator w)) ∙
    commutative-add-ℝ (square-ℝ (yCoord p)) (square-ℝ d) ∙
    circleDenominatorSquares p

solvedDenominator : (w : StrongPuncture) →
  denominator (pr1 w) ＝ two *ℝ qInv (stereographicForward w)
solvedDenominator w =
  inv (left-unit-law-mul-ℝ d) ∙ ap (_*ℝ d) (inv (qD t)) ∙
  associative-mul-ℝ (qInv t) (D t) d ∙
  ap (qInv t *ℝ_) (DtimesDenominator w) ∙ commutative-mul-ℝ (qInv t) two
  where
  t = stereographicForward w
  d = denominator (pr1 w)

pointParameterForward : (w : StrongPuncture) → paramPoint (stereographicForward w) ＝ pr1 w
pointParameterForward w@(p , a) = inv (eq-type-subtype circleSubtype (eq-pair xEq yEq))
  where
  t = stereographicForward w
  p' = paramPoint t
  dEq : denominator p ＝ denominator p'
  dEq = solvedDenominator w ∙ inv (paramDenominator t)
  xEq : xCoord p ＝ xCoord p'
  xEq = inv (eq-sim-ℝ (right-diff-diff-ℝ one-ℝ (xCoord p))) ∙
    ap (one-ℝ -ℝ_) dEq ∙ eq-sim-ℝ (right-diff-diff-ℝ one-ℝ (xCoord p'))
  yEq : yCoord p ＝ yCoord p'
  yEq = inv (forwardTimesDenominator w) ∙ ap (t *ℝ_) dEq ∙ inv (paramY t)

parameterForward : (w : StrongPuncture) → parameterize (stereographicForward w) ＝ w
parameterForward w = eq-type-subtype (λ p → apart-prop-ℝ (xCoord p) one-ℝ) (pointParameterForward w)

strongCircleEquivReal : StrongPuncture ≃ Real
strongCircleEquivReal = stereographicForward ,
  is-equiv-is-invertible parameterize forwardParameter parameterForward

-- The original weak puncture is retained. Its equivalence is CONDITIONAL on Lift.
liftWeakPoint : Lift → PuncturedRealCircle → StrongPuncture
liftWeakPoint lift (p , w) = p , lift p w

liftForget : (lift : Lift) (s : StrongPuncture) → liftWeakPoint lift (forgetStrong s) ＝ s
liftForget lift (p , a) = eq-type-subtype (λ z → apart-prop-ℝ (xCoord z) one-ℝ) refl

forgetLift : (lift : Lift) (w : PuncturedRealCircle) → forgetStrong (liftWeakPoint lift w) ＝ w
forgetLift lift (p , w) = eq-type-subtype puncturedSubtype refl

weakCircleEquivStrong : Lift → PuncturedRealCircle ≃ StrongPuncture
weakCircleEquivStrong lift = liftWeakPoint lift ,
  is-equiv-is-invertible forgetStrong (liftForget lift) (forgetLift lift)

weakCircleEquivReal : Lift → PuncturedRealCircle ≃ Real
weakCircleEquivReal lift = strongCircleEquivReal ∘e weakCircleEquivStrong lift

classicalWeakCircleEquivReal : ExcludedMiddle0 → PuncturedRealCircle ≃ Real
classicalWeakCircleEquivReal em = weakCircleEquivReal (dneGivesLift (excludedMiddleToDNE em))
