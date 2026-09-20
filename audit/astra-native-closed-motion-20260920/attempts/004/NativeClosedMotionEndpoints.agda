{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeClosedMotionEndpoints where

-- Full initial and final closed diagrams of the same extended time formula.
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionContinuity
open import hott-z.NativeClosedMotionInterior
open import hott-z.NativeMotion
open import hott-z.NativeMotionEndpoints
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.NativeCompletion
open import hott-z.HomogeneousCircle
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.equality-cartesian-product-types
open import foundation.negation
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.absolute-value-real-numbers

closingDZero : (u : Real) → closingD zero-ℝ u ＝ one-ℝ
closingDZero u = ap (gap u +ℝ_)
  (ap (_*ℝ abs-ℝ (center u)) (ap square-ℝ remainingZero ∙ oneSquared) ∙
    left-unit-law-mul-ℝ (abs-ℝ (center u))) ∙ cancelAdd one-ℝ (abs-ℝ (center u))

halfCenter : (u : Real) → (one-half-ℝ *ℝ center u) +ℝ one-half-ℝ ＝ u
halfCenter u = commutative-add-ℝ (one-half-ℝ *ℝ center u) one-half-ℝ ∙
  ap (_+ℝ (one-half-ℝ *ℝ center u)) (inv (right-unit-law-mul-ℝ one-half-ℝ)) ∙
  inv (left-distributive-mul-add-ℝ one-half-ℝ one-ℝ (center u)) ∙
  ap (one-half-ℝ *ℝ_) (eq-sim-ℝ (add-right-diff-ℝ one-ℝ (u +ℝ u))) ∙
  left-distributive-mul-add-ℝ one-half-ℝ u u ∙ twice-left-mul-one-half-ℝ u

closingNZero : (u : Real) → closingN zero-ℝ u ＝ u
closingNZero u = ap-add-ℝ (ap (_*ℝ center u) scaleZero)
  (ap-mul-ℝ offsetZero (closingDZero u) ∙ right-unit-law-mul-ℝ one-half-ℝ) ∙ halfCenter u

closedInitialDiagram : (u : ClosedParameter) → closedMotion zero-ℝ u ＝ nCompletion u
closedInitialDiagram u =
  ap (λ v → reflectY (turn zero-ℝ v))
    (closedBaseMatchesBend zero-ℝ u (closingDPositiveBefore zero-ℝ u le-zero-one-ℝ)) ∙
  ap (λ r → reflectY (turn zero-ℝ (bend zero-ℝ r))) fraction ∙
  ap reflectY (turnZero (bend zero-ℝ (pr1 u)) ∙ bendZero (pr1 u)) ∙ eq-pair refl neg-zero-ℝ
  where
  nz = nonzero-ℝ⁺ (closingD zero-ℝ (pr1 u) , closingDPositiveBefore zero-ℝ u le-zero-one-ℝ)
  fraction : closingN zero-ℝ (pr1 u) *ℝ recip nz ＝ pr1 u
  fraction = ap-mul-ℝ (closingNZero (pr1 u)) (inverseOfOne nz (closingDZero (pr1 u))) ∙
    right-unit-law-mul-ℝ (pr1 u)

closingDOne : (u : Real) → closingD one-ℝ u ＝ gap u
closingDOne u = ap (gap u +ℝ_)
  (ap (_*ℝ abs-ℝ (center u)) (ap square-ℝ remainingOne ∙ square-zero-ℝ) ∙
    eq-sim-ℝ (left-zero-law-mul-ℝ (abs-ℝ (center u)))) ∙ right-unit-law-add-ℝ (gap u)

closingNOne : (u : Real) → closingN one-ℝ u ＝ center u
closingNOne u = ap-add-ℝ (ap (_*ℝ center u) scaleOne ∙ left-unit-law-mul-ℝ (center u))
  (ap (_*ℝ closingD one-ℝ u) offsetOne ∙ eq-sim-ℝ (left-zero-law-mul-ℝ (closingD one-ℝ u))) ∙
  right-unit-law-add-ℝ (center u)

closingKOne : (u : Real) → closingK one-ℝ u ＝ K (center u) (gap u)
closingKOne u = ap-add-ℝ (ap square-ℝ (closingDOne u))
  (ap square-ℝ (left-unit-law-mul-ℝ (closingN one-ℝ u) ∙ closingNOne u)) ∙
  commutative-add-ℝ (square-ℝ (gap u)) (square-ℝ (center u))

closingInverseOne : (u : ClosedParameter) →
  closingInverse one-ℝ u ＝ Kinv (center (pr1 u)) (gap (pr1 u)) (completionPositive (pr1 u))
closingInverseOne u = recipCongruence (closingNZ one-ℝ u)
  (Knonzero (center (pr1 u)) (gap (pr1 u)) (completionPositive (pr1 u))) (closingKOne (pr1 u))

closedBaseOne : (u : ClosedParameter) → closedBase one-ℝ u ＝
  (((center (pr1 u) *ℝ gap (pr1 u)) *ℝ Kinv (center (pr1 u)) (gap (pr1 u)) (completionPositive (pr1 u))) ,
   (square-ℝ (center (pr1 u)) *ℝ Kinv (center (pr1 u)) (gap (pr1 u)) (completionPositive (pr1 u))))
closedBaseOne u = eq-pair
  (ap-mul-ℝ (ap-mul-ℝ (closingNOne (pr1 u)) (closingDOne (pr1 u))) (closingInverseOne u))
  (ap-mul-ℝ (left-unit-law-mul-ℝ (square-ℝ (closingN one-ℝ (pr1 u))) ∙ ap square-ℝ (closingNOne (pr1 u)))
    (closingInverseOne u))

twiceSquareMinusK : (a b : Real) → two *ℝ square-ℝ a -ℝ K a b ＝ AX a b
twiceSquareMinusK a b = ap-add-ℝ (twoTimes (square-ℝ a))
  (ap neg-ℝ (commutative-add-ℝ (square-ℝ a) (square-ℝ b))) ∙
  eq-sim-ℝ (diff-add-ℝ (square-ℝ a) (square-ℝ b) (square-ℝ a))

closedFinalDiagram : (u : ClosedParameter) → closedMotion one-ℝ u ＝ pr1 (mCompletion u)
closedFinalDiagram u = ap (λ v → reflectY (turn one-ℝ v)) (closedBaseOne u) ∙
  reflectedTurnOne (((a *ℝ b) *ℝ q) , (square-ℝ a *ℝ q)) ∙ eq-pair xEq yEq
  where
  a = center (pr1 u); b = gap (pr1 u)
  nz = Knonzero a b (completionPositive (pr1 u)); q = recip nz
  xEq : two *ℝ (square-ℝ a *ℝ q) -ℝ one-ℝ ＝ AX a b *ℝ q
  xEq = ap-add-ℝ (inv (associative-mul-ℝ two (square-ℝ a) q)) (ap neg-ℝ (inv (rightInv nz))) ∙
    inv (right-distributive-mul-diff-ℝ (two *ℝ square-ℝ a) (K a b) q) ∙
    ap (_*ℝ q) (twiceSquareMinusK a b)
  yEq : two *ℝ ((a *ℝ b) *ℝ q) ＝ AY a b *ℝ q
  yEq = inv (associative-mul-ℝ two (a *ℝ b) q) ∙
    ap (_*ℝ q) (twoTimes (a *ℝ b) ∙ inv (right-distributive-mul-add-ℝ a a b))

closedFinalLeft : closedMotion one-ℝ closedZero ＝ pr1 east
closedFinalLeft = closedFinalDiagram closedZero ∙ ap pr1 mAtZero

closedFinalRight : closedMotion one-ℝ closedOne ＝ pr1 east
closedFinalRight = closedFinalDiagram closedOne ∙ ap pr1 mAtOne

closedFinalEndsCoincide : closedMotion one-ℝ closedZero ＝ closedMotion one-ℝ closedOne
closedFinalEndsCoincide = closedFinalLeft ∙ inv closedFinalRight

closedFinalNotInjective : ¬ ((u v : ClosedParameter) → closedMotion one-ℝ u ＝ closedMotion one-ℝ v → u ＝ v)
closedFinalNotInjective injective = closedEndpointsDistinct (injective closedZero closedOne closedFinalEndsCoincide)
