{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeClosedMotionInterior where

-- Exact agreement of the closed formula with the already checked motion.
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionContinuity
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.equality-cartesian-product-types
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers

closingDPositiveInterior : (t : Real) (u : OpenRealInterval) → is-positive-ℝ (closingD t (pr1 u))
closingDPositiveInterior t u = closingDPositiveSmall t (pr1 u) (pr2 (fromUnit u))

parameterTimesGap : (u : OpenRealInterval) → realParameter u *ℝ gap (pr1 u) ＝ center (pr1 u)
parameterTimesGap u = associative-mul-ℝ (center (pr1 u)) (minusInverse (fromUnit u)) (gap (pr1 u)) ∙
  ap (center (pr1 u) *ℝ_) (leftInv (minusNZ (fromUnit u))) ∙ right-unit-law-mul-ℝ (center (pr1 u))

absParameterTimesGap : (u : OpenRealInterval) → abs-ℝ (realParameter u) *ℝ gap (pr1 u) ＝ abs-ℝ (center (pr1 u))
absParameterTimesGap u = ap (_*ℝ gap (pr1 u)) (absUnsquash (fromUnit u)) ∙
  associative-mul-ℝ (abs-ℝ (center (pr1 u))) (minusInverse (fromUnit u)) (gap (pr1 u)) ∙
  ap (abs-ℝ (center (pr1 u)) *ℝ_) (leftInv (minusNZ (fromUnit u))) ∙
  right-unit-law-mul-ℝ (abs-ℝ (center (pr1 u)))

stretchDenTimesGap : (t : Real) (u : OpenRealInterval) →
  stretchDen t (realParameter u) *ℝ gap (pr1 u) ＝ closingD t (pr1 u)
stretchDenTimesGap t u = right-distributive-mul-add-ℝ one-ℝ (c *ℝ abs-ℝ (realParameter u)) g ∙
  ap-add-ℝ (left-unit-law-mul-ℝ g)
    (associative-mul-ℝ c (abs-ℝ (realParameter u)) g ∙ ap (c *ℝ_) (absParameterTimesGap u))
  where c = square-ℝ (remaining t); g = gap (pr1 u)

compressedTimesClosingD : (t : Real) (u : OpenRealInterval) →
  (realParameter u *ℝ stretchInv t (realParameter u)) *ℝ closingD t (pr1 u) ＝ center (pr1 u)
compressedTimesClosingD t u = associative-mul-ℝ r q d ∙
  ap (r *ℝ_) (ap (q *ℝ_) (inv (stretchDenTimesGap t u)) ∙
    inv (associative-mul-ℝ q (stretchDen t r) g) ∙
    ap (_*ℝ g) (leftInv (stretchNZ t r)) ∙ left-unit-law-mul-ℝ g) ∙ parameterTimesGap u
  where
  r = realParameter u; q = stretchInv t r; d = closingD t (pr1 u); g = gap (pr1 u)

stretchTimesClosingD : (t : Real) (u : OpenRealInterval) →
  stretch t (realParameter u) *ℝ closingD t (pr1 u) ＝ closingN t (pr1 u)
stretchTimesClosingD t u = right-distributive-mul-add-ℝ
  (scale t *ℝ (realParameter u *ℝ stretchInv t (realParameter u))) (offset t) (closingD t (pr1 u)) ∙
  ap-add-ℝ
    (associative-mul-ℝ (scale t) (realParameter u *ℝ stretchInv t (realParameter u)) (closingD t (pr1 u)) ∙
      ap (scale t *ℝ_) (compressedTimesClosingD t u)) refl

interiorDNZ : Real → OpenRealInterval → NonzeroReal
interiorDNZ t u = nonzero-ℝ⁺ (closingD t (pr1 u) , closingDPositiveInterior t u)

stretchAsClosingFraction : (t : Real) (u : OpenRealInterval) →
  stretch t (realParameter u) ＝ closingN t (pr1 u) *ℝ recip (interiorDNZ t u)
stretchAsClosingFraction t u = inv (right-unit-law-mul-ℝ s) ∙
  ap (s *ℝ_) (inv (rightInv (interiorDNZ t u))) ∙
  inv (associative-mul-ℝ s (closingD t (pr1 u)) (recip (interiorDNZ t u))) ∙
  ap (_*ℝ recip (interiorDNZ t u)) (stretchTimesClosingD t u)
  where s = stretch t (realParameter u)

rightInverseUnique : (d q x : Real) → d *ℝ q ＝ one-ℝ → d *ℝ x ＝ one-ℝ → q ＝ x
rightInverseUnique d q x dq dx = inv (right-unit-law-mul-ℝ q) ∙ ap (q *ℝ_) (inv dx) ∙
  inv (associative-mul-ℝ q d x) ∙ ap (_*ℝ x) (commutative-mul-ℝ q d ∙ dq) ∙ left-unit-law-mul-ℝ x

closedBaseMatchesBend : (t : Real) (u : ClosedParameter) (hd : is-positive-ℝ (closingD t (pr1 u))) →
  closedBase t u ＝ bend t (closingN t (pr1 u) *ℝ recip (nonzero-ℝ⁺ (closingD t (pr1 u) , hd)))
closedBaseMatchesBend t u hd = inv (eq-pair xEq yEq)
  where
  d = closingD t (pr1 u); n = closingN t (pr1 u)
  nz = nonzero-ℝ⁺ (d , hd); s = n *ℝ recip nz; q = closingInverse t u
  d² = square-ℝ d
  sd : s *ℝ d ＝ n
  sd = associative-mul-ℝ n (recip nz) d ∙ ap (n *ℝ_) (leftInv nz) ∙ right-unit-law-mul-ℝ n
  tsd : (t *ℝ s) *ℝ d ＝ t *ℝ n
  tsd = associative-mul-ℝ t s d ∙ ap (t *ℝ_) sd
  denominatorScale : D (t *ℝ s) *ℝ d² ＝ closingK t (pr1 u)
  denominatorScale = right-distributive-mul-add-ℝ (square-ℝ (t *ℝ s)) one-ℝ d² ∙
    ap-add-ℝ (inv (distributive-square-mul-ℝ (t *ℝ s) d) ∙ ap square-ℝ tsd) (left-unit-law-mul-ℝ d²) ∙
    commutative-add-ℝ (square-ℝ (t *ℝ n)) d²
  candidateInverse : D (t *ℝ s) *ℝ (d² *ℝ q) ＝ one-ℝ
  candidateInverse = inv (associative-mul-ℝ (D (t *ℝ s)) d² q) ∙
    ap (_*ℝ q) denominatorScale ∙ rightInv (closingNZ t u)
  inverseScale : qInv (t *ℝ s) ＝ d² *ℝ q
  inverseScale = rightInverseUnique (D (t *ℝ s)) (qInv (t *ℝ s)) (d² *ℝ q) (Dq (t *ℝ s)) candidateInverse
  xEq : s *ℝ qInv (t *ℝ s) ＝ (n *ℝ d) *ℝ q
  xEq = ap (s *ℝ_) inverseScale ∙ inv (associative-mul-ℝ s d² q) ∙
    ap (_*ℝ q) (inv (associative-mul-ℝ s d d) ∙ ap (_*ℝ d) sd)
  yEq : (t *ℝ square-ℝ s) *ℝ qInv (t *ℝ s) ＝ (t *ℝ square-ℝ n) *ℝ q
  yEq = ap ((t *ℝ square-ℝ s) *ℝ_) inverseScale ∙
    inv (associative-mul-ℝ (t *ℝ square-ℝ s) d² q) ∙
    ap (_*ℝ q) (associative-mul-ℝ t (square-ℝ s) d² ∙
      ap (t *ℝ_) (inv (distributive-square-mul-ℝ s d) ∙ ap square-ℝ sd))

closedAgreesInterior : (t : Real) (u : OpenRealInterval) →
  closedMotion t (openIntoClosed u) ＝ motion t u
closedAgreesInterior t u = ap (λ v → reflectY (turn t v))
  (closedBaseMatchesBend t (openIntoClosed u) (closingDPositiveInterior t u)) ∙
  ap (λ s → reflectY (turn t (bend t s))) (inv (stretchAsClosingFraction t u))
