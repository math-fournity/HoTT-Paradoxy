{-# OPTIONS --without-K --exact-split #-}
module hott-z.HomogeneousCircle where

-- Algebra for the exact closed-parameter extension; denominator evidence explicit.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.equality-cartesian-product-types
open import foundation.subtypes
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.multiplicative-inverses-nonzero-real-numbers
open import real-numbers.multiplication-nonzero-real-numbers

K AX AY : Real → Real → Real
K a b = square-ℝ a +ℝ square-ℝ b
AX a b = square-ℝ a -ℝ square-ℝ b
AY a b = (a +ℝ a) *ℝ b

homogeneousNumerators : (a b : Real) →
  square-ℝ (AX a b) +ℝ square-ℝ (AY a b) ＝ square-ℝ (K a b)
homogeneousNumerators a b =
  ap (square-ℝ (AX a b) +ℝ_) four ∙ squareDiffPlusFour (square-ℝ a) (square-ℝ b)
  where
  s = square-ℝ a
  r = square-ℝ b
  four : square-ℝ (AY a b) ＝ (two *ℝ (s *ℝ r)) +ℝ (two *ℝ (s *ℝ r))
  four = distributive-square-mul-ℝ (a +ℝ a) b ∙
    ap (_*ℝ r) (squareDouble a) ∙
    right-distributive-mul-add-ℝ (s +ℝ s) (s +ℝ s) r ∙
    ap-add-ℝ (right-distributive-mul-add-ℝ s s r) (right-distributive-mul-add-ℝ s s r) ∙
    ap-add-ℝ (inv (twoTimes (s *ℝ r))) (inv (twoTimes (s *ℝ r)))

Knonzero : (a b : Real) → is-positive-ℝ (K a b) → NonzeroReal
Knonzero a b h = K a b , is-nonzero-is-positive-ℝ h

Kinv : (a b : Real) → is-positive-ℝ (K a b) → Real
Kinv a b h = recip (Knonzero a b h)

homogeneousPlane : (a b : Real) → is-positive-ℝ (K a b) → RealPlane
homogeneousPlane a b h = (AX a b *ℝ Kinv a b h) , (AY a b *ℝ Kinv a b h)

homogeneousEquation : (a b : Real) (h : is-positive-ℝ (K a b)) →
  circleEquation (homogeneousPlane a b h) ＝ one-ℝ
homogeneousEquation a b h =
  scaledSquares (AX a b) (AY a b) (Kinv a b h) ∙
  ap (_*ℝ square-ℝ (Kinv a b h)) (homogeneousNumerators a b) ∙
  inv (distributive-square-mul-ℝ (K a b) (Kinv a b h)) ∙
  ap square-ℝ (rightInv (Knonzero a b h)) ∙ oneSquared

homogeneousPoint : (a b : Real) → is-positive-ℝ (K a b) → RealCircle
homogeneousPoint a b h = homogeneousPlane a b h , homogeneousEquation a b h

homogeneousMatchesParam : (a b : Real) (hb : is-positive-ℝ b) (hk : is-positive-ℝ (K a b)) →
  homogeneousPoint a b hk ＝ paramPoint (a *ℝ recip (nonzero-ℝ⁺ (b , hb)))
homogeneousMatchesParam a b hb hk =
  inv (eq-type-subtype circleSubtype (eq-pair xEq yEq))
  where
  t = a *ℝ recip (nonzero-ℝ⁺ (b , hb))
  q = Kinv a b hk
  b² = square-ℝ b
  tb : t *ℝ b ＝ a
  tb = associative-mul-ℝ a (recip (nonzero-ℝ⁺ (b , hb))) b ∙
    ap (a *ℝ_) (leftInv (nonzero-ℝ⁺ (b , hb))) ∙ right-unit-law-mul-ℝ a
  t²b² : square-ℝ t *ℝ b² ＝ square-ℝ a
  t²b² = inv (distributive-square-mul-ℝ t b) ∙ ap square-ℝ tb
  Db² : D t *ℝ b² ＝ K a b
  Db² = right-distributive-mul-add-ℝ (square-ℝ t) one-ℝ b² ∙
    ap-add-ℝ t²b² (left-unit-law-mul-ℝ b²)
  candidateInv : D t *ℝ (b² *ℝ q) ＝ one-ℝ
  candidateInv = inv (associative-mul-ℝ (D t) b² q) ∙
    ap (_*ℝ q) Db² ∙ rightInv (Knonzero a b hk)
  qRel : qInv t ＝ b² *ℝ q
  qRel = inv (eq-sim-ℝ
    (unique-right-inv-nonzero-ℝ (D t , is-nonzero-is-positive-ℝ (positiveD t))
      ((b² *ℝ q) , is-nonzero-has-left-inverse-mul-ℝ (D t) (b² *ℝ q) (sim-eq-ℝ candidateInv))
      (sim-eq-ℝ candidateInv)))
  xScaled : numeratorX t *ℝ b² ＝ AX a b
  xScaled = right-distributive-mul-diff-ℝ (square-ℝ t) one-ℝ b² ∙
    ap-add-ℝ t²b² (ap neg-ℝ (left-unit-law-mul-ℝ b²))
  xEq : numeratorX t *ℝ qInv t ＝ AX a b *ℝ q
  xEq = ap (numeratorX t *ℝ_) qRel ∙
    inv (associative-mul-ℝ (numeratorX t) b² q) ∙ ap (_*ℝ q) xScaled
  yScaled : numeratorY t *ℝ b² ＝ AY a b
  yScaled = inv (associative-mul-ℝ (t +ℝ t) b b) ∙
    ap (_*ℝ b) (right-distributive-mul-add-ℝ t t b ∙ ap-add-ℝ tb tb)
  yEq : numeratorY t *ℝ qInv t ＝ AY a b *ℝ q
  yEq = ap (numeratorY t *ℝ_) qRel ∙
    inv (associative-mul-ℝ (numeratorY t) b² q) ∙ ap (_*ℝ q) yScaled

homogeneousEast : (a b : Real) (hk : is-positive-ℝ (K a b)) →
  square-ℝ a ＝ one-ℝ → b ＝ zero-ℝ → homogeneousPoint a b hk ＝ east
homogeneousEast a b hk ha hb = eq-type-subtype circleSubtype (eq-pair xOne yZero)
  where
  q = Kinv a b hk
  bSquareZero : square-ℝ b ＝ zero-ℝ
  bSquareZero = ap square-ℝ hb ∙ square-zero-ℝ
  Kone : K a b ＝ one-ℝ
  Kone = ap-add-ℝ ha bSquareZero ∙ right-unit-law-add-ℝ one-ℝ
  qOne : q ＝ one-ℝ
  qOne = inv (left-unit-law-mul-ℝ q) ∙ inv (ap (_*ℝ q) Kone) ∙ rightInv (Knonzero a b hk)
  axOne : AX a b ＝ one-ℝ
  axOne = ap-add-ℝ ha (ap neg-ℝ bSquareZero) ∙ right-unit-law-diff-ℝ one-ℝ
  xOne : AX a b *ℝ q ＝ one-ℝ
  xOne = ap-mul-ℝ axOne qOne ∙ left-unit-law-mul-ℝ one-ℝ
  yZero : AY a b *ℝ q ＝ zero-ℝ
  yZero = ap (λ z → ((a +ℝ a) *ℝ z) *ℝ q) hb ∙
    ap (_*ℝ q) (eq-sim-ℝ (right-zero-law-mul-ℝ (a +ℝ a))) ∙
    eq-sim-ℝ (left-zero-law-mul-ℝ q)
