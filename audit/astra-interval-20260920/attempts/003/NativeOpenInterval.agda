{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeOpenInterval where

-- The original C281 (0,1) subtype and metric, not a replacement closed interval.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.existential-quantification
open import foundation.equivalences
open import foundation.univalence
open import metric-spaces.metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.addition-positive-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.multiplication-positive-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.strict-inequalities-addition-and-subtraction-real-numbers

signedUpper : (z : SignedInterval) → le-ℝ (pr1 z) one-ℝ
signedUpper z = concatenate-leq-le-ℝ (pr1 z) (abs-ℝ (pr1 z)) one-ℝ (leq-abs-ℝ (pr1 z)) (pr2 z)

signedNegativeUpper : (z : SignedInterval) → le-ℝ (neg-ℝ (pr1 z)) one-ℝ
signedNegativeUpper z = concatenate-leq-le-ℝ (neg-ℝ (pr1 z)) (abs-ℝ (pr1 z)) one-ℝ
  (neg-leq-abs-ℝ (pr1 z)) (pr2 z)

onePlusPositive : (z : SignedInterval) → is-positive-ℝ (one-ℝ +ℝ pr1 z)
onePlusPositive z = tr (λ a → le-ℝ a (one-ℝ +ℝ pr1 z))
  (commutative-add-ℝ (neg-ℝ (pr1 z)) (pr1 z) ∙ eq-sim-ℝ (right-inverse-law-add-ℝ (pr1 z)))
  (preserves-le-right-add-ℝ (pr1 z) (neg-ℝ (pr1 z)) one-ℝ (signedNegativeUpper z))

toUnitValue unitGap : SignedInterval → Real
toUnitValue z = one-half-ℝ *ℝ (one-ℝ +ℝ pr1 z)
unitGap z = one-half-ℝ *ℝ (one-ℝ -ℝ pr1 z)

toUnitPositive : (z : SignedInterval) → is-positive-ℝ (toUnitValue z)
toUnitPositive z = is-positive-mul-ℝ (pr2 one-half-ℝ⁺) (onePlusPositive z)

unitGapPositive : (z : SignedInterval) → is-positive-ℝ (unitGap z)
unitGapPositive z = is-positive-mul-ℝ (pr2 one-half-ℝ⁺) (is-positive-diff-le-ℝ (signedUpper z))

plusMinusTwo : (z : Real) → (one-ℝ +ℝ z) +ℝ (one-ℝ -ℝ z) ＝ two
plusMinusTwo z = associative-add-ℝ one-ℝ z (one-ℝ -ℝ z) ∙
  ap (one-ℝ +ℝ_) (eq-sim-ℝ (add-right-diff-ℝ z one-ℝ)) ∙ inv twoAsSum

unitValuePlusGap : (z : SignedInterval) → toUnitValue z +ℝ unitGap z ＝ one-ℝ
unitValuePlusGap z =
  inv (left-distributive-mul-add-ℝ one-half-ℝ (one-ℝ +ℝ pr1 z) (one-ℝ -ℝ pr1 z)) ∙
  ap (one-half-ℝ *ℝ_) (plusMinusTwo (pr1 z)) ∙ commutative-mul-ℝ one-half-ℝ two ∙ twoHalf

toUnitUpper : (z : SignedInterval) → le-ℝ (toUnitValue z) one-ℝ
toUnitUpper z = tr (le-ℝ (toUnitValue z)) (unitValuePlusGap z)
  (tr (λ a → le-ℝ a (toUnitValue z +ℝ unitGap z)) (right-unit-law-add-ℝ (toUnitValue z))
    (preserves-le-left-add-ℝ (toUnitValue z) zero-ℝ (unitGap z) (unitGapPositive z)))

toUnit : SignedInterval → OpenRealInterval
toUnit z = toUnitValue z , toUnitPositive z , toUnitUpper z

fromUnitValue : OpenRealInterval → Real
fromUnitValue u = (pr1 u +ℝ pr1 u) -ℝ one-ℝ

fromUnitUpper : (u : OpenRealInterval) → le-ℝ (fromUnitValue u) one-ℝ
fromUnitUpper u = tr (le-ℝ (fromUnitValue u))
  (eq-sim-ℝ (cancel-right-add-diff-ℝ one-ℝ one-ℝ))
  (preserves-le-right-add-ℝ (neg-ℝ one-ℝ) (pr1 u +ℝ pr1 u) (one-ℝ +ℝ one-ℝ)
    (preserves-le-add-ℝ (pr2 (pr2 u)) (pr2 (pr2 u))))

fromUnitNegativeUpper : (u : OpenRealInterval) → le-ℝ (neg-ℝ (fromUnitValue u)) one-ℝ
fromUnitNegativeUpper u = tr (λ a → le-ℝ a one-ℝ)
  (inv (distributive-neg-diff-ℝ (pr1 u +ℝ pr1 u) one-ℝ))
  (tr (le-ℝ (one-ℝ -ℝ (pr1 u +ℝ pr1 u))) (right-unit-law-add-ℝ one-ℝ)
    (preserves-le-left-add-ℝ one-ℝ (neg-ℝ (pr1 u +ℝ pr1 u)) zero-ℝ
      (tr (le-ℝ (neg-ℝ (pr1 u +ℝ pr1 u))) neg-zero-ℝ
        (neg-le-ℝ (is-positive-add-ℝ (pr1 (pr2 u)) (pr1 (pr2 u)))))))

fromUnit : OpenRealInterval → SignedInterval
fromUnit u = fromUnitValue u , le-abs-le-le-neg-ℝ (fromUnitUpper u) (fromUnitNegativeUpper u)

toFromValue : (u : OpenRealInterval) → toUnitValue (fromUnit u) ＝ pr1 u
toFromValue u =
  ap (one-half-ℝ *ℝ_) (eq-sim-ℝ (add-right-diff-ℝ one-ℝ (pr1 u +ℝ pr1 u))) ∙
  left-distributive-mul-add-ℝ one-half-ℝ (pr1 u) (pr1 u) ∙
  twice-left-mul-one-half-ℝ (pr1 u)

toFrom : (u : OpenRealInterval) → toUnit (fromUnit u) ＝ u
toFrom u = eq-type-subtype intervalSubtype (toFromValue u)

fromToValue : (z : SignedInterval) → fromUnitValue (toUnit z) ＝ pr1 z
fromToValue z =
  ap (_-ℝ one-ℝ) (twice-left-mul-one-half-ℝ (one-ℝ +ℝ pr1 z)) ∙
  eq-sim-ℝ (cancel-left-conjugation-ℝ one-ℝ (pr1 z))

fromTo : (z : SignedInterval) → fromUnit (toUnit z) ＝ z
fromTo z = eq-type-subtype signedSubtype (fromToValue z)

toUnitContinuous : Cont signedMetric intervalMetric toUnit
toUnitContinuous = mulContinuous signedMetric (λ _ → one-half-ℝ) (λ z → one-ℝ +ℝ pr1 z)
  (constantContinuous signedMetric one-half-ℝ)
  (addContinuous signedMetric (λ _ → one-ℝ) pr1 (constantContinuous signedMetric one-ℝ) signedInclusionContinuous)

unitInclusionContinuous : Cont intervalMetric realMetric pr1
unitInclusionContinuous u = intro-exists (λ ε → ε) (λ ε u' near → near)

fromUnitContinuous : Cont intervalMetric signedMetric fromUnit
fromUnitContinuous = addContinuous intervalMetric (λ u → pr1 u +ℝ pr1 u) (λ _ → neg-ℝ one-ℝ)
  (addContinuous intervalMetric pr1 pr1 unitInclusionContinuous unitInclusionContinuous)
  (constantContinuous intervalMetric (neg-ℝ one-ℝ))

signedUnitHomeomorphism : PointwiseHomeomorphism signedMetric intervalMetric
PointwiseHomeomorphism.forward signedUnitHomeomorphism = toUnit
PointwiseHomeomorphism.backward signedUnitHomeomorphism = fromUnit
PointwiseHomeomorphism.forwardContinuous signedUnitHomeomorphism = toUnitContinuous
PointwiseHomeomorphism.backwardContinuous signedUnitHomeomorphism = fromUnitContinuous
PointwiseHomeomorphism.forwardBackward signedUnitHomeomorphism = toFrom
PointwiseHomeomorphism.backwardForward signedUnitHomeomorphism = fromTo

composeHomeomorphism : (X Y Z : Space) → PointwiseHomeomorphism Y Z →
  PointwiseHomeomorphism X Y → PointwiseHomeomorphism X Z
PointwiseHomeomorphism.forward (composeHomeomorphism X Y Z g f) x =
  PointwiseHomeomorphism.forward g (PointwiseHomeomorphism.forward f x)
PointwiseHomeomorphism.backward (composeHomeomorphism X Y Z g f) z =
  PointwiseHomeomorphism.backward f (PointwiseHomeomorphism.backward g z)
PointwiseHomeomorphism.forwardContinuous (composeHomeomorphism X Y Z g f) =
  composeContinuous X Y Z (PointwiseHomeomorphism.forward g) (PointwiseHomeomorphism.forward f)
    (PointwiseHomeomorphism.forwardContinuous g) (PointwiseHomeomorphism.forwardContinuous f)
PointwiseHomeomorphism.backwardContinuous (composeHomeomorphism X Y Z g f) =
  composeContinuous Z Y X (PointwiseHomeomorphism.backward f) (PointwiseHomeomorphism.backward g)
    (PointwiseHomeomorphism.backwardContinuous f) (PointwiseHomeomorphism.backwardContinuous g)
PointwiseHomeomorphism.forwardBackward (composeHomeomorphism X Y Z g f) z =
  ap (PointwiseHomeomorphism.forward g)
    (PointwiseHomeomorphism.forwardBackward f (PointwiseHomeomorphism.backward g z)) ∙
  PointwiseHomeomorphism.forwardBackward g z
PointwiseHomeomorphism.backwardForward (composeHomeomorphism X Y Z g f) x =
  ap (PointwiseHomeomorphism.backward f)
    (PointwiseHomeomorphism.backwardForward g (PointwiseHomeomorphism.forward f x)) ∙
  PointwiseHomeomorphism.backwardForward f x

realUnitHomeomorphism : PointwiseHomeomorphism realMetric intervalMetric
realUnitHomeomorphism = composeHomeomorphism realMetric signedMetric intervalMetric
  signedUnitHomeomorphism realSignedHomeomorphism

strongCircleUnitHomeomorphism : PointwiseHomeomorphism strongMetric intervalMetric
strongCircleUnitHomeomorphism = composeHomeomorphism strongMetric realMetric intervalMetric
  realUnitHomeomorphism strongHomeomorphism

weakCircleUnitHomeomorphism : Lift → PointwiseHomeomorphism puncturedCircleMetric intervalMetric
weakCircleUnitHomeomorphism lift = composeHomeomorphism puncturedCircleMetric realMetric intervalMetric
  realUnitHomeomorphism (weakHomeomorphism lift)

classicalWeakCircleUnitHomeomorphism : ExcludedMiddle0 → PointwiseHomeomorphism puncturedCircleMetric intervalMetric
classicalWeakCircleUnitHomeomorphism em = weakCircleUnitHomeomorphism (dneGivesLift (excludedMiddleToDNE em))

homeomorphismEquiv : {X Y : Space} → PointwiseHomeomorphism X Y → type-Metric-Space X ≃ type-Metric-Space Y
homeomorphismEquiv h = PointwiseHomeomorphism.forward h ,
  is-equiv-is-invertible (PointwiseHomeomorphism.backward h)
    (PointwiseHomeomorphism.forwardBackward h) (PointwiseHomeomorphism.backwardForward h)

strongIntervalTypePath : StrongPuncture ＝ OpenRealInterval
strongIntervalTypePath = eq-equiv (homeomorphismEquiv strongCircleUnitHomeomorphism)

strongIntervalPathAction : (w : StrongPuncture) →
  map-equiv (equiv-eq strongIntervalTypePath) w ＝ PointwiseHomeomorphism.forward strongCircleUnitHomeomorphism w
strongIntervalPathAction w = ap (λ e → map-equiv e w)
  (is-section-eq-equiv (homeomorphismEquiv strongCircleUnitHomeomorphism))

weakIntervalTypePath : Lift → PuncturedRealCircle ＝ OpenRealInterval
weakIntervalTypePath lift = eq-equiv (homeomorphismEquiv (weakCircleUnitHomeomorphism lift))
