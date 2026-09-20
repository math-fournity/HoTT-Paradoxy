{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeCompletionFibers where

-- Complete fibers of the actual closed final diagram. Logical disjunctions are
-- propositions, not a decision procedure for equality of arbitrary real inputs.
open import hott-z.NativeClosedMotionBase
open import hott-z.NativeClosedMotionEndpoints
open import hott-z.NativeEndpointSeparation
open import hott-z.NativeMotion
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import hott-z.NativeOpenInterval
open import hott-z.NativeCompletion
open import hott-z.HomogeneousCircle
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.propositions
open import foundation.conjunction
open import foundation.disjunction
open import foundation.logical-equivalences
open import foundation.negation
open import foundation.empty-types
open import metric-spaces.metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-nonzero-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.apartness-real-numbers

sumMinusDifference : (a b : Real) → (a +ℝ b) -ℝ (a -ℝ b) ＝ two *ℝ b
sumMinusDifference a b = ap (_-ℝ (a -ℝ b)) (commutative-add-ℝ a b) ∙
  ap ((b +ℝ a) -ℝ_) (commutative-add-ℝ a (neg-ℝ b)) ∙
  eq-sim-ℝ (diff-add-ℝ b (neg-ℝ b) a) ∙ ap (b +ℝ_) (neg-neg-ℝ b) ∙ inv (twoTimes b)

completionDenominator : (u : ClosedParameter) → denominator (mCompletion u) ＝
  (two *ℝ square-ℝ (gap (pr1 u))) *ℝ Kinv (center (pr1 u)) (gap (pr1 u)) (completionPositive (pr1 u))
completionDenominator u = ap (_-ℝ (AX a b *ℝ q)) (inv (rightInv nz)) ∙
  inv (right-distributive-mul-diff-ℝ (K a b) (AX a b) q) ∙
  ap (_*ℝ q) (sumMinusDifference (square-ℝ a) (square-ℝ b))
  where
  a = center (pr1 u); b = gap (pr1 u)
  nz = Knonzero a b (completionPositive (pr1 u)); q = recip nz

gapNonzeroFromStrong : (u : ClosedParameter) → Strong (mCompletion u) → is-nonzero-ℝ (gap (pr1 u))
gapNonzeroFromStrong u strong = pr1 (is-nonzero-factors-is-nonzero-mul-ℝ b b
  (pr2 (is-nonzero-factors-is-nonzero-mul-ℝ two (square-ℝ b)
    (pr1 (is-nonzero-factors-is-nonzero-mul-ℝ (two *ℝ square-ℝ b) q
      (tr is-nonzero-ℝ (completionDenominator u) (denominatorNonzero (mCompletion u) strong)))))))
  where
  b = gap (pr1 u); q = Kinv (center (pr1 u)) b (completionPositive (pr1 u))

gapPositiveFromStrong : (u : ClosedParameter) → Strong (mCompletion u) → is-positive-ℝ (gap (pr1 u))
gapPositiveFromStrong u strong = elim-disjunction (is-positive-prop-ℝ (gap (pr1 u)))
  (λ negative → ex-falso (not-leq-le-ℝ (gap (pr1 u)) zero-ℝ negative (closedGapNonnegative u)))
  (λ positive → positive) (gapNonzeroFromStrong u strong)

closedSignedToUnit : (u : ClosedParameter) (small : le-ℝ (abs-ℝ (center (pr1 u))) one-ℝ) →
  toUnitValue (center (pr1 u) , small) ＝ pr1 u
closedSignedToUnit u small =
  ap (one-half-ℝ *ℝ_) (eq-sim-ℝ (add-right-diff-ℝ one-ℝ (pr1 u +ℝ pr1 u))) ∙
  left-distributive-mul-add-ℝ one-half-ℝ (pr1 u) (pr1 u) ∙ twice-left-mul-one-half-ℝ (pr1 u)

gapInterior : (u : ClosedParameter) → is-positive-ℝ (gap (pr1 u)) → OpenRealInterval
gapInterior u positive = pr1 u , tr (le-ℝ zero-ℝ) valueEq (toUnitPositive z) ,
  tr (λ x → le-ℝ x one-ℝ) valueEq (toUnitUpper z)
  where
  small = le-is-positive-diff-ℝ positive
  z = center (pr1 u) , small
  valueEq = closedSignedToUnit u small

fiberAtInterior : (u : OpenRealInterval) (v : ClosedParameter) →
  mCompletion (openIntoClosed u) ＝ mCompletion v → openIntoClosed u ＝ v
fiberAtInterior u v h = ap openIntoClosed
  (interiorInjective u vi (h ∙ inv (ap mCompletion included))) ∙ included
  where
  vi = gapInterior v (gapPositiveFromStrong v (tr Strong h (interiorStrong u)))
  included : openIntoClosed vi ＝ v
  included = eq-type-subtype closedSubtype refl

closedInteriorUnique : (u v : ClosedParameter) → le-ℝ zero-ℝ (pr1 u) → le-ℝ (pr1 u) one-ℝ →
  mCompletion u ＝ mCompletion v → u ＝ v
closedInteriorUnique u v lower upper h = inv included ∙
  fiberAtInterior (pr1 u , lower , upper) v (ap mCompletion included ∙ h)
  where
  included : openIntoClosed (pr1 u , lower , upper) ＝ u
  included = eq-type-subtype closedSubtype refl

orderedFiberEndpoints : (u v : ClosedParameter) → le-ℝ (pr1 u) (pr1 v) →
  mCompletion u ＝ mCompletion v → (u ＝ closedZero) × (v ＝ closedOne)
orderedFiberEndpoints u v less h =
  eq-type-subtype closedSubtype
    (antisymmetric-leq-ℝ (pr1 u) zero-ℝ (leq-not-le-ℝ zero-ℝ (pr1 u) notPositiveU) (pr1 (pr2 u))) ,
  eq-type-subtype closedSubtype
    (antisymmetric-leq-ℝ (pr1 v) one-ℝ (pr2 (pr2 v)) (leq-not-le-ℝ (pr1 v) one-ℝ notBelowOneV))
  where
  notPositiveU : ¬ (le-ℝ zero-ℝ (pr1 u))
  notPositiveU positive = nonequal-apart-ℝ (pr1 u) (pr1 v) (apart-le-ℝ less)
    (ap pr1 (closedInteriorUnique u v positive
      (concatenate-le-leq-ℝ (pr1 u) (pr1 v) one-ℝ less (pr2 (pr2 v))) h))
  notBelowOneV : ¬ (le-ℝ (pr1 v) one-ℝ)
  notBelowOneV upper = nonequal-apart-ℝ (pr1 u) (pr1 v) (apart-le-ℝ less)
    (inv (ap pr1 (closedInteriorUnique v u
      (concatenate-leq-le-ℝ zero-ℝ (pr1 u) (pr1 v) (pr1 (pr2 u)) less) upper (inv h))))

EndpointPair FullFiberRelation : ClosedParameter → ClosedParameter → Prop (lsuc lzero)
EndpointPair u v =
  (eq-prop-Metric-Space closedMetric u closedZero ∧ eq-prop-Metric-Space closedMetric v closedOne) ∨
  (eq-prop-Metric-Space closedMetric u closedOne ∧ eq-prop-Metric-Space closedMetric v closedZero)
FullFiberRelation u v = eq-prop-Metric-Space closedMetric u v ∨ EndpointPair u v

apartFiberEndpoints : (u v : ClosedParameter) → mCompletion u ＝ mCompletion v →
  apart-ℝ (pr1 u) (pr1 v) → type-Prop (EndpointPair u v)
apartFiberEndpoints u v h = elim-disjunction (EndpointPair u v)
  (λ less → inl-disjunction (orderedFiberEndpoints u v less h))
  (λ less → let ends = orderedFiberEndpoints v u less (inv h) in inr-disjunction (pr2 ends , pr1 ends))

parameterGap : ClosedParameter → ClosedParameter → Real
parameterGap u v = abs-ℝ (pr1 u -ℝ pr1 v)

endpointPairGapOne : (u v : ClosedParameter) → type-Prop (EndpointPair u v) → parameterGap u v ＝ one-ℝ
endpointPairGapOne u v = elim-disjunction
  (eq-prop-Metric-Space realMetric (parameterGap u v) one-ℝ)
  (λ (hu , hv) → ap abs-ℝ (ap-add-ℝ (ap pr1 hu) (ap neg-ℝ (ap pr1 hv)) ∙
    left-unit-law-add-ℝ (neg-ℝ one-ℝ)) ∙ abs-neg-ℝ one-ℝ ∙ abs-real-ℝ⁺ one-ℝ⁺)
  (λ (hu , hv) → ap abs-ℝ (ap-add-ℝ (ap pr1 hu) (ap neg-ℝ (ap pr1 hv)) ∙
    right-unit-law-diff-ℝ one-ℝ) ∙ abs-real-ℝ⁺ one-ℝ⁺)

pointEqualityToFiberRelation : (u v : ClosedParameter) →
  mCompletion u ＝ mCompletion v → type-Prop (FullFiberRelation u v)
pointEqualityToFiberRelation u v h = elim-disjunction (FullFiberRelation u v)
  (λ positiveGap → inr-disjunction (apartFiberEndpoints u v h
    (apart-is-nonzero-diff-ℝ (pr1 u) (pr1 v)
      (is-nonzero-is-positive-abs-ℝ (pr1 u -ℝ pr1 v) positiveGap))))
  (λ smallGap → inl-disjunction (eq-type-subtype closedSubtype
    (pr2 (eq-iff-nonapart-ℝ (pr1 u) (pr1 v))
      (λ apart → irreflexive-le-ℝ one-ℝ
        (tr (λ x → le-ℝ x one-ℝ) (endpointPairGapOne u v (apartFiberEndpoints u v h apart)) smallGap)))))
  (cotransitive-le-ℝ zero-ℝ (parameterGap u v) one-ℝ le-zero-one-ℝ)

fiberRelationToPointEquality : (u v : ClosedParameter) →
  type-Prop (FullFiberRelation u v) → mCompletion u ＝ mCompletion v
fiberRelationToPointEquality u v = elim-disjunction eqP (ap mCompletion)
  (elim-disjunction eqP
    (λ (hu , hv) → ap mCompletion hu ∙ mEndsCoincide ∙ inv (ap mCompletion hv))
    (λ (hu , hv) → ap mCompletion hu ∙ inv mEndsCoincide ∙ inv (ap mCompletion hv)))
  where eqP = eq-prop-Metric-Space circleMetric (mCompletion u) (mCompletion v)

completionFiberClassification : (u v : ClosedParameter) →
  (mCompletion u ＝ mCompletion v) ↔ type-Prop (FullFiberRelation u v)
completionFiberClassification u v = pointEqualityToFiberRelation u v , fiberRelationToPointEquality u v

closedFinalFiberClassification : (u v : ClosedParameter) →
  (closedMotion one-ℝ u ＝ closedMotion one-ℝ v) ↔ type-Prop (FullFiberRelation u v)
closedFinalFiberClassification u v =
  (λ h → pointEqualityToFiberRelation u v
    (eq-type-subtype circleSubtype (inv (closedFinalDiagram u) ∙ h ∙ closedFinalDiagram v))) ,
  (λ h → closedFinalDiagram u ∙ ap pr1 (fiberRelationToPointEquality u v h) ∙ inv (closedFinalDiagram v))
