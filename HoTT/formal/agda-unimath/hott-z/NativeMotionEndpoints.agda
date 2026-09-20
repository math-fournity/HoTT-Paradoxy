{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeMotionEndpoints where

-- Exact initial line and final native circle parametrization of the time family.
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import hott-z.NativeOpenInterval
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
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers

remainingZero : remaining zero-ℝ ＝ one-ℝ
remainingZero = right-unit-law-diff-ℝ one-ℝ

remainingOne : remaining one-ℝ ＝ zero-ℝ
remainingOne = eq-sim-ℝ (right-inverse-law-add-ℝ one-ℝ)

Dzero : D zero-ℝ ＝ one-ℝ
Dzero = ap (_+ℝ one-ℝ) square-zero-ℝ ∙ left-unit-law-add-ℝ one-ℝ

Done : D one-ℝ ＝ two
Done = ap (_+ℝ one-ℝ) oneSquared ∙ inv twoAsSum

inverseOfOne : (x : NonzeroReal) → val x ＝ one-ℝ → recip x ＝ one-ℝ
inverseOfOne x h = inv (left-unit-law-mul-ℝ (recip x)) ∙
  inv (ap (_*ℝ recip x) h) ∙ rightInv x

recipCongruence : (x y : NonzeroReal) → val x ＝ val y → recip x ＝ recip y
recipCongruence x y h = ap recip (eq-type-subtype is-nonzero-prop-ℝ h)

qZero : qInv zero-ℝ ＝ one-ℝ
qZero = inverseOfOne (paramNonzeroD zero-ℝ) Dzero

scaleZero : scale zero-ℝ ＝ one-half-ℝ
scaleZero = ap (one-half-ℝ *ℝ_) Dzero ∙ right-unit-law-mul-ℝ one-half-ℝ

scaleOne : scale one-ℝ ＝ one-ℝ
scaleOne = ap (one-half-ℝ *ℝ_) Done ∙ commutative-mul-ℝ one-half-ℝ two ∙ twoHalf

offsetZero : offset zero-ℝ ＝ one-half-ℝ
offsetZero = ap (one-half-ℝ *ℝ_) remainingZero ∙ right-unit-law-mul-ℝ one-half-ℝ

offsetOne : offset one-ℝ ＝ zero-ℝ
offsetOne = ap (one-half-ℝ *ℝ_) remainingOne ∙ eq-sim-ℝ (right-zero-law-mul-ℝ one-half-ℝ)

stretchDenZero : (r : Real) → stretchDen zero-ℝ r ＝ plusDenominator r
stretchDenZero r = ap (λ a → one-ℝ +ℝ (a *ℝ abs-ℝ r))
  (ap square-ℝ remainingZero ∙ oneSquared) ∙
  ap (one-ℝ +ℝ_) (left-unit-law-mul-ℝ (abs-ℝ r))

stretchInvZero : (r : Real) → stretchInv zero-ℝ r ＝ plusInverse r
stretchInvZero r = recipCongruence (stretchNZ zero-ℝ r) (plusNZ r) (stretchDenZero r)

stretchDenOne : (r : Real) → stretchDen one-ℝ r ＝ one-ℝ
stretchDenOne r = ap (λ a → one-ℝ +ℝ (a *ℝ abs-ℝ r))
  (ap square-ℝ remainingOne ∙ square-zero-ℝ) ∙
  ap (one-ℝ +ℝ_) (eq-sim-ℝ (left-zero-law-mul-ℝ (abs-ℝ r))) ∙
  right-unit-law-add-ℝ one-ℝ

stretchInvOne : (r : Real) → stretchInv one-ℝ r ＝ one-ℝ
stretchInvOne r = inverseOfOne (stretchNZ one-ℝ r) (stretchDenOne r)

stretchZero : (u : OpenRealInterval) → stretch zero-ℝ (realParameter u) ＝ pr1 u
stretchZero u =
  ap-add-ℝ (ap-mul-ℝ scaleZero (ap (r *ℝ_) (stretchInvZero r))) offsetZero ∙
  commutative-add-ℝ (one-half-ℝ *ℝ squashValue r) one-half-ℝ ∙
  ap (_+ℝ (one-half-ℝ *ℝ squashValue r)) (inv (right-unit-law-mul-ℝ one-half-ℝ)) ∙
  inv (left-distributive-mul-add-ℝ one-half-ℝ one-ℝ (squashValue r)) ∙
  ap toUnitValue (squashUnsquash (fromUnit u)) ∙ toFromValue u
  where r = realParameter u

stretchOne : (r : Real) → stretch one-ℝ r ＝ r
stretchOne r = ap-add-ℝ
  (ap-mul-ℝ scaleOne (ap (r *ℝ_) (stretchInvOne r) ∙ right-unit-law-mul-ℝ r) ∙
    left-unit-law-mul-ℝ r) offsetOne ∙ right-unit-law-add-ℝ r

bendZero : (r : Real) → bend zero-ℝ r ＝ (r , zero-ℝ)
bendZero r = eq-pair
  (ap (r *ℝ_) q ∙ right-unit-law-mul-ℝ r)
  (ap-mul-ℝ (eq-sim-ℝ (left-zero-law-mul-ℝ (square-ℝ r))) q ∙
    eq-sim-ℝ (left-zero-law-mul-ℝ one-ℝ))
  where
  q : qInv (zero-ℝ *ℝ r) ＝ one-ℝ
  q = ap qInv (eq-sim-ℝ (left-zero-law-mul-ℝ r)) ∙ qZero

bendOne : (r : Real) → bend one-ℝ r ＝ ((r *ℝ qInv r) , (square-ℝ r *ℝ qInv r))
bendOne r = eq-pair (ap (r *ℝ_) (ap qInv (left-unit-law-mul-ℝ r)))
  (ap-mul-ℝ (left-unit-law-mul-ℝ (square-ℝ r)) (ap qInv (left-unit-law-mul-ℝ r)))

turnZero : (v : RealPlane) → turn zero-ℝ v ＝ v
turnZero (x , y) = eq-pair
  (ap (_-ℝ zero-ℝ) (ap-add-ℝ (ap (_*ℝ x) remainingZero ∙ left-unit-law-mul-ℝ x)
    (ap (_*ℝ y) z ∙ eq-sim-ℝ (left-zero-law-mul-ℝ y)) ∙ right-unit-law-add-ℝ x) ∙
    right-unit-law-diff-ℝ x)
  (ap-add-ℝ (ap (λ a → neg-ℝ a *ℝ x) z ∙ ap (_*ℝ x) neg-zero-ℝ ∙
    eq-sim-ℝ (left-zero-law-mul-ℝ x))
    (ap (_*ℝ y) remainingZero ∙ left-unit-law-mul-ℝ y) ∙ left-unit-law-add-ℝ y)
  where z = eq-sim-ℝ (right-zero-law-mul-ℝ two)

reflectedTurnOne : (v : RealPlane) → reflectY (turn one-ℝ v) ＝ ((two *ℝ pr2 v -ℝ one-ℝ) , (two *ℝ pr1 v))
reflectedTurnOne (x , y) = eq-pair
  (ap (_-ℝ one-ℝ) (ap-add-ℝ
    (ap (_*ℝ x) remainingOne ∙ eq-sim-ℝ (left-zero-law-mul-ℝ x))
    (ap (_*ℝ y) (right-unit-law-mul-ℝ two)) ∙ left-unit-law-add-ℝ (two *ℝ y)))
  (ap neg-ℝ (ap-add-ℝ (ap (λ a → neg-ℝ a *ℝ x) (right-unit-law-mul-ℝ two))
    (ap (_*ℝ y) remainingOne ∙ eq-sim-ℝ (left-zero-law-mul-ℝ y)) ∙
    right-unit-law-add-ℝ (neg-ℝ two *ℝ x) ∙ left-negative-law-mul-ℝ two x) ∙
    neg-neg-ℝ (two *ℝ x))

motionAtZero : (u : OpenRealInterval) → motion zero-ℝ u ＝ (pr1 u , zero-ℝ)
motionAtZero u = ap reflectY (turnZero (bend zero-ℝ (stretch zero-ℝ (realParameter u))) ∙
  ap (bend zero-ℝ) (stretchZero u) ∙ bendZero (pr1 u)) ∙ eq-pair refl neg-zero-ℝ

twiceSquareMinusD : (r : Real) → (two *ℝ square-ℝ r) -ℝ D r ＝ numeratorX r
twiceSquareMinusD r = ap-add-ℝ (twoTimes (square-ℝ r))
  (ap neg-ℝ (commutative-add-ℝ (square-ℝ r) one-ℝ)) ∙
  eq-sim-ℝ (diff-add-ℝ (square-ℝ r) one-ℝ (square-ℝ r))

reflectedBendTurn : (r : Real) → reflectY (turn one-ℝ (bend one-ℝ r)) ＝ paramPlane r
reflectedBendTurn r = ap (λ v → reflectY (turn one-ℝ v)) (bendOne r) ∙
  reflectedTurnOne ((r *ℝ qInv r) , (square-ℝ r *ℝ qInv r)) ∙ eq-pair
    (ap-add-ℝ (inv (associative-mul-ℝ two (square-ℝ r) (qInv r))) (ap neg-ℝ (inv (Dq r))) ∙
      inv (right-distributive-mul-diff-ℝ (two *ℝ square-ℝ r) (D r) (qInv r)) ∙
      ap (_*ℝ qInv r) (twiceSquareMinusD r))
    (inv (associative-mul-ℝ two r (qInv r)) ∙ ap (_*ℝ qInv r) (twoTimes r))

motionAtOne : (u : OpenRealInterval) → motion one-ℝ u ＝ paramPlane (realParameter u)
motionAtOne u = ap (λ r → reflectY (turn one-ℝ (bend one-ℝ r))) (stretchOne (realParameter u)) ∙
  reflectedBendTurn (realParameter u)

motionAtOneOriginal : (u : OpenRealInterval) →
  motion one-ℝ u ＝ pr1 (pr1 (PointwiseHomeomorphism.backward strongCircleUnitHomeomorphism u))
motionAtOneOriginal = motionAtOne
