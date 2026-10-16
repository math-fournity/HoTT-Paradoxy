{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeTurnInverse where

-- The actual affine turn has a positive determinant and continuous left inverse.
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.HomogeneousCircle
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.equality-cartesian-product-types
open import foundation.disjunction
open import metric-spaces.metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.addition-positive-real-numbers
open import real-numbers.addition-positive-and-negative-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-positive-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.strict-inequality-real-numbers

turnDet : Real → Real
turnDet t = K (remaining t) (two *ℝ t)

twoPositive : is-positive-ℝ two
twoPositive = tr is-positive-ℝ (inv twoAsSum) (is-positive-add-ℝ (pr2 one-ℝ⁺) (pr2 one-ℝ⁺))

turnDetPositive : (t : Real) → is-positive-ℝ (turnDet t)
turnDetPositive t = elim-disjunction (is-positive-prop-ℝ (turnDet t))
  (λ ht → is-positive-add-nonnegative-positive-ℝ (is-nonnegative-square-ℝ (remaining t))
    (is-positive-square-ℝ⁺ ((two *ℝ t) , is-positive-mul-ℝ twoPositive ht)))
  (λ ht → tr is-positive-ℝ (commutative-add-ℝ (square-ℝ (two *ℝ t)) (square-ℝ (remaining t)))
    (is-positive-add-nonnegative-positive-ℝ (is-nonnegative-square-ℝ (two *ℝ t))
      (is-positive-square-ℝ⁺ (remaining t , is-positive-diff-le-ℝ
        (transitive-le-ℝ t one-half-ℝ one-ℝ (pr2 (pr2 intervalHalf)) ht)))))
  (cotransitive-le-ℝ zero-ℝ t one-half-ℝ (pr1 (pr2 intervalHalf)))

-- Matrix identities are proved by ring laws, not postulated or externally solved.
firstMatrixProduct : (a b x y : Real) →
  (a *ℝ ((a *ℝ x) +ℝ (b *ℝ y))) -ℝ (b *ℝ ((neg-ℝ b *ℝ x) +ℝ (a *ℝ y))) ＝ K a b *ℝ x
firstMatrixProduct a b x y = ap-add-ℝ
  (left-distributive-mul-add-ℝ a (a *ℝ x) (b *ℝ y) ∙ ap-add-ℝ
    (inv (associative-mul-ℝ a a x)) (inv (associative-mul-ℝ a b y)))
  (ap neg-ℝ (left-distributive-mul-add-ℝ b (neg-ℝ b *ℝ x) (a *ℝ y) ∙ ap-add-ℝ
    (inv (associative-mul-ℝ b (neg-ℝ b) x) ∙ ap (_*ℝ x) (right-negative-law-mul-ℝ b b) ∙
      left-negative-law-mul-ℝ (square-ℝ b) x)
    (inv (associative-mul-ℝ b a y) ∙ ap (_*ℝ y) (commutative-mul-ℝ b a)))) ∙
  eq-sim-ℝ (diff-add-ℝ (square-ℝ a *ℝ x) (neg-ℝ (square-ℝ b *ℝ x)) ((a *ℝ b) *ℝ y)) ∙
  ap ((square-ℝ a *ℝ x) +ℝ_) (neg-neg-ℝ (square-ℝ b *ℝ x)) ∙
  inv (right-distributive-mul-add-ℝ (square-ℝ a) (square-ℝ b) x)

secondMatrixProduct : (a b x y : Real) →
  (b *ℝ ((a *ℝ x) +ℝ (b *ℝ y))) +ℝ (a *ℝ ((neg-ℝ b *ℝ x) +ℝ (a *ℝ y))) ＝ K a b *ℝ y
secondMatrixProduct a b x y = ap-add-ℝ
  (left-distributive-mul-add-ℝ b (a *ℝ x) (b *ℝ y) ∙ ap-add-ℝ
    (inv (associative-mul-ℝ b a x) ∙ ap (_*ℝ x) (commutative-mul-ℝ b a))
    (inv (associative-mul-ℝ b b y)))
  (left-distributive-mul-add-ℝ a (neg-ℝ b *ℝ x) (a *ℝ y) ∙ ap-add-ℝ
    (inv (associative-mul-ℝ a (neg-ℝ b) x) ∙ ap (_*ℝ x) (right-negative-law-mul-ℝ a b) ∙
      left-negative-law-mul-ℝ (a *ℝ b) x)
    (inv (associative-mul-ℝ a a y))) ∙
  interchange-law-add-add-ℝ ((a *ℝ b) *ℝ x) (square-ℝ b *ℝ y) (neg-ℝ ((a *ℝ b) *ℝ x)) (square-ℝ a *ℝ y) ∙
  ap (_+ℝ ((square-ℝ b *ℝ y) +ℝ (square-ℝ a *ℝ y)))
    (eq-sim-ℝ (right-inverse-law-add-ℝ ((a *ℝ b) *ℝ x))) ∙
  left-unit-law-add-ℝ ((square-ℝ b *ℝ y) +ℝ (square-ℝ a *ℝ y)) ∙
  commutative-add-ℝ (square-ℝ b *ℝ y) (square-ℝ a *ℝ y) ∙
  inv (right-distributive-mul-add-ℝ (square-ℝ a) (square-ℝ b) y)

turnRecip : Real → Real
turnRecip t = Kinv (remaining t) (two *ℝ t) (turnDetPositive t)

turnUndo : Real → RealPlane → RealPlane
turnUndo t w =
  (((remaining t *ℝ (pr1 w +ℝ t)) -ℝ ((two *ℝ t) *ℝ pr2 w)) *ℝ turnRecip t) ,
  ((((two *ℝ t) *ℝ (pr1 w +ℝ t)) +ℝ (remaining t *ℝ pr2 w)) *ℝ turnRecip t)

turnCancelScale : (t x : Real) → (turnDet t *ℝ x) *ℝ turnRecip t ＝ x
turnCancelScale t x = ap (_*ℝ turnRecip t) (commutative-mul-ℝ (turnDet t) x) ∙
  associative-mul-ℝ x (turnDet t) (turnRecip t) ∙
  ap (x *ℝ_) (rightInv (Knonzero (remaining t) (two *ℝ t) (turnDetPositive t))) ∙
  right-unit-law-mul-ℝ x

turnLeftInverse : (t : Real) (v : RealPlane) → turnUndo t (turn t v) ＝ v
turnLeftInverse t (x , y) = eq-pair
  (ap (λ z → ((a *ℝ z) -ℝ (b *ℝ yy)) *ℝ turnRecip t) cancel ∙
    ap (_*ℝ turnRecip t) (firstMatrixProduct a b x y) ∙ turnCancelScale t x)
  (ap (λ z → ((b *ℝ z) +ℝ (a *ℝ yy)) *ℝ turnRecip t) cancel ∙
    ap (_*ℝ turnRecip t) (secondMatrixProduct a b x y) ∙ turnCancelScale t y)
  where
  a = remaining t; b = two *ℝ t
  yy = (neg-ℝ b *ℝ x) +ℝ (a *ℝ y)
  cancel = cancelAdd ((a *ℝ x) +ℝ (b *ℝ y)) t

turnUndoContinuous : (t : Real) → Cont realPlaneMetric realPlaneMetric (turnUndo t)
turnUndoContinuous t = pairContinuous X realMetric realMetric
  (λ w → pr1 (turnUndo t w)) (λ w → pr2 (turnUndo t w))
  (mulContinuous X (λ w → (a *ℝ (pr1 w +ℝ t)) -ℝ (b *ℝ pr2 w)) (λ _ → turnRecip t)
    (addContinuous X (λ w → a *ℝ (pr1 w +ℝ t)) (λ w → neg-ℝ (b *ℝ pr2 w))
      (mulContinuous X (λ _ → a) (λ w → pr1 w +ℝ t) (constantContinuous X a) cshift)
      (negContinuous X (λ w → b *ℝ pr2 w)
        (mulContinuous X (λ _ → b) pr2 (constantContinuous X b) cy)))
    (constantContinuous X (turnRecip t)))
  (mulContinuous X (λ w → (b *ℝ (pr1 w +ℝ t)) +ℝ (a *ℝ pr2 w)) (λ _ → turnRecip t)
    (addContinuous X (λ w → b *ℝ (pr1 w +ℝ t)) (λ w → a *ℝ pr2 w)
      (mulContinuous X (λ _ → b) (λ w → pr1 w +ℝ t) (constantContinuous X b) cshift)
      (mulContinuous X (λ _ → a) pr2 (constantContinuous X a) cy))
    (constantContinuous X (turnRecip t)))
  where
  X = realPlaneMetric; a = remaining t; b = two *ℝ t
  cx = firstContinuous realMetric realMetric
  cy = secondContinuous realMetric realMetric
  cshift = addContinuous X pr1 (λ _ → t) cx (constantContinuous X t)
