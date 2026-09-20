{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeEndpointSeparation where

-- Exact separation of the two closed-parameter images at every real t < 1.
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionInterior
open import hott-z.NativeClosedMotionEndpoints
open import hott-z.NativeMotion
open import hott-z.NativeMotionEndpoints
open import hott-z.NativeMotionBridge
open import hott-z.NativeMotionEmbedding
open import hott-z.NativeStretchInverse
open import hott-z.NativeBendInverse
open import hott-z.NativeTurnInverse
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.NativeCompletion
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.negation
open import foundation.logical-equivalences
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.apartness-real-numbers

reverseClosedBase : (t : Real) (u : ClosedParameter) → reverseTurn t (closedMotion t u) ＝ closedBase t u
reverseClosedBase t u = ap (turnUndo t) (reflectionInvolution (turn t (closedBase t u))) ∙
  turnLeftInverse t (closedBase t u)

closedFractionEquality : (t : Real) (u v : ClosedParameter)
  (hu : is-positive-ℝ (closingD t (pr1 u))) (hv : is-positive-ℝ (closingD t (pr1 v))) →
  closedMotion t u ＝ closedMotion t v →
  closingN t (pr1 u) *ℝ recip (nonzero-ℝ⁺ (closingD t (pr1 u) , hu)) ＝
  closingN t (pr1 v) *ℝ recip (nonzero-ℝ⁺ (closingD t (pr1 v) , hv))
closedFractionEquality t u v hu hv h = inv (bendLeftInverse t ru) ∙
  ap (bendInverse t) (eq-type-subtype (bendChartSubtype t)
    (inv (closedBaseMatchesBend t u hu) ∙
      inv (reverseClosedBase t u) ∙ ap (reverseTurn t) h ∙ reverseClosedBase t v ∙
      closedBaseMatchesBend t v hv)) ∙ bendLeftInverse t rv
  where
  ru = closingN t (pr1 u) *ℝ recip (nonzero-ℝ⁺ (closingD t (pr1 u) , hu))
  rv = closingN t (pr1 v) *ℝ recip (nonzero-ℝ⁺ (closingD t (pr1 v) , hv))

endpointDZero : (t : Real) → closingD t zero-ℝ ＝ square-ℝ (remaining t)
endpointDZero t = ap-add-ℝ gapZero
  (ap (square-ℝ (remaining t) *ℝ_) (ap abs-ℝ centerZero ∙ abs-neg-ℝ one-ℝ ∙ abs-real-ℝ⁺ one-ℝ⁺) ∙
    right-unit-law-mul-ℝ (square-ℝ (remaining t))) ∙ left-unit-law-add-ℝ (square-ℝ (remaining t))

endpointDOne : (t : Real) → closingD t one-ℝ ＝ square-ℝ (remaining t)
endpointDOne t = ap-add-ℝ gapOne
  (ap (square-ℝ (remaining t) *ℝ_) (ap abs-ℝ centerOne ∙ abs-real-ℝ⁺ one-ℝ⁺) ∙
    right-unit-law-mul-ℝ (square-ℝ (remaining t))) ∙ left-unit-law-add-ℝ (square-ℝ (remaining t))

endpointNZero : (t : Real) → closingN t zero-ℝ ＝
  neg-ℝ (scale t) +ℝ (offset t *ℝ square-ℝ (remaining t))
endpointNZero t = ap-add-ℝ
  (ap (scale t *ℝ_) centerZero ∙ right-negative-law-mul-ℝ (scale t) one-ℝ ∙
    ap neg-ℝ (right-unit-law-mul-ℝ (scale t)))
  (ap (offset t *ℝ_) (endpointDZero t))

endpointNOne : (t : Real) → closingN t one-ℝ ＝
  scale t +ℝ (offset t *ℝ square-ℝ (remaining t))
endpointNOne t = ap-add-ℝ (ap (scale t *ℝ_) centerOne ∙ right-unit-law-mul-ℝ (scale t))
  (ap (offset t *ℝ_) (endpointDOne t))

fractionTimesDenominator : (n : Real) (d : NonzeroReal) → (n *ℝ recip d) *ℝ val d ＝ n
fractionTimesDenominator n d = associative-mul-ℝ n (recip d) (val d) ∙
  ap (n *ℝ_) (leftInv d) ∙ right-unit-law-mul-ℝ n

closedEndpointsDistinctBefore : (t : Real) → le-ℝ t one-ℝ →
  ¬ (closedMotion t closedZero ＝ closedMotion t closedOne)
closedEndpointsDistinctBefore t before h =
  nonequal-apart-ℝ (neg-ℝ (scale t)) (scale t)
    (apart-le-ℝ (transitive-le-ℝ (neg-ℝ (scale t)) zero-ℝ (scale t) (scalePositive t)
      (tr (le-ℝ (neg-ℝ (scale t))) neg-zero-ℝ (neg-le-ℝ (scalePositive t))))) negativeEqualsPositive
  where
  hu = closingDPositiveBefore t closedZero before
  hv = closingDPositiveBefore t closedOne before
  du = nonzero-ℝ⁺ (closingD t zero-ℝ , hu)
  dv = nonzero-ℝ⁺ (closingD t one-ℝ , hv)
  nu = closingN t zero-ℝ; nv = closingN t one-ℝ
  denominatorEquality = endpointDZero t ∙ inv (endpointDOne t)
  numeratorEquality : nu ＝ nv
  numeratorEquality = inv (fractionTimesDenominator nu du) ∙
    ap (_*ℝ val du) (closedFractionEquality t closedZero closedOne hu hv h) ∙
    ap ((nv *ℝ recip dv) *ℝ_) denominatorEquality ∙ fractionTimesDenominator nv dv
  c = offset t *ℝ square-ℝ (remaining t)
  negativeEqualsPositive : neg-ℝ (scale t) ＝ scale t
  negativeEqualsPositive = inv (eq-sim-ℝ (cancel-right-add-diff-ℝ (neg-ℝ (scale t)) c)) ∙
    ap (_-ℝ c) (inv (endpointNZero t) ∙ numeratorEquality ∙ endpointNOne t) ∙
    eq-sim-ℝ (cancel-right-add-diff-ℝ (scale t) c)

endpointMeetingTime : (t : ClosedParameter) →
  (closedMotion (pr1 t) closedZero ＝ closedMotion (pr1 t) closedOne) ↔ (t ＝ closedOne)
endpointMeetingTime t =
  (λ same → eq-type-subtype closedSubtype
    (antisymmetric-leq-ℝ (pr1 t) one-ℝ (pr2 (pr2 t))
      (leq-not-le-ℝ (pr1 t) one-ℝ (λ before → closedEndpointsDistinctBefore (pr1 t) before same)))) ,
  (λ atEnd → tr (λ s → closedMotion (pr1 s) closedZero ＝ closedMotion (pr1 s) closedOne)
    (inv atEnd) closedFinalEndsCoincide)
