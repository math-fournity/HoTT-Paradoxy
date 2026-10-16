{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeCompletion where

-- Closed-parameter extension of the exact C290 inverse, not a physical trace.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import hott-z.NativeOpenInterval
open import hott-z.HomogeneousCircle
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.subtypes
open import foundation.conjunction
open import foundation.disjunction
open import foundation.negation
open import foundation.existential-quantification
open import metric-spaces.metric-spaces
open import metric-spaces.subspaces-metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.addition-positive-and-negative-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.apartness-real-numbers

center gap : Real → Real
center u = (u +ℝ u) -ℝ one-ℝ
gap u = one-ℝ -ℝ abs-ℝ (center u)

completionPositive : (u : Real) → is-positive-ℝ (K (center u) (gap u))
completionPositive u = elim-disjunction (is-positive-prop-ℝ (K (center u) (gap u)))
  (λ positiveAbsCenter →
    tr is-positive-ℝ (commutative-add-ℝ (square-ℝ (gap u)) (square-ℝ (center u)))
      (is-positive-add-nonnegative-positive-ℝ (is-nonnegative-square-ℝ (gap u))
        (is-positive-square-is-nonzero-ℝ (center u)
          (is-nonzero-is-positive-abs-ℝ (center u) positiveAbsCenter))))
  (λ smallAbsCenter →
    is-positive-add-nonnegative-positive-ℝ (is-nonnegative-square-ℝ (center u))
      (is-positive-square-ℝ⁺ (gap u , is-positive-diff-le-ℝ
        (transitive-le-ℝ (abs-ℝ (center u)) one-half-ℝ one-ℝ
          (pr2 (pr2 intervalHalf)) smallAbsCenter))))
  (cotransitive-le-ℝ zero-ℝ (abs-ℝ (center u)) one-half-ℝ (pr1 (pr2 intervalHalf)))

completionCircle : Real → RealCircle
completionCircle u = homogeneousPoint (center u) (gap u) (completionPositive u)

completionPlane : Real → RealPlane
completionPlane u = pr1 (completionCircle u)

centerContinuous : Cont realMetric realMetric center
centerContinuous = addContinuous realMetric (λ u → u +ℝ u) (λ _ → neg-ℝ one-ℝ)
  (addContinuous realMetric (λ u → u) (λ u → u) identityContinuous identityContinuous)
  (constantContinuous realMetric (neg-ℝ one-ℝ))

gapContinuous : Cont realMetric realMetric gap
gapContinuous = addContinuous realMetric (λ _ → one-ℝ) (λ u → neg-ℝ (abs-ℝ (center u)))
  (constantContinuous realMetric one-ℝ)
  (negContinuous realMetric (λ u → abs-ℝ (center u)) (absContinuous realMetric center centerContinuous))

centerSquareContinuous : Cont realMetric realMetric (λ u → square-ℝ (center u))
centerSquareContinuous = mulContinuous realMetric center center centerContinuous centerContinuous

gapSquareContinuous : Cont realMetric realMetric (λ u → square-ℝ (gap u))
gapSquareContinuous = mulContinuous realMetric gap gap gapContinuous gapContinuous

completionKContinuous : Cont realMetric realMetric (λ u → K (center u) (gap u))
completionKContinuous = addContinuous realMetric (λ u → square-ℝ (center u)) (λ u → square-ℝ (gap u))
  centerSquareContinuous gapSquareContinuous

completionNZ : Real → NonzeroReal
completionNZ u = Knonzero (center u) (gap u) (completionPositive u)

completionNZContinuous : Cont realMetric nonzeroMetric completionNZ
completionNZContinuous = completionKContinuous

completionInvContinuous : Cont realMetric realMetric (λ u → Kinv (center u) (gap u) (completionPositive u))
completionInvContinuous = composeContinuous realMetric nonzeroMetric realMetric recip completionNZ
  reciprocalContinuous completionNZContinuous

completionXContinuous : Cont realMetric realMetric (λ u → AX (center u) (gap u))
completionXContinuous = addContinuous realMetric (λ u → square-ℝ (center u))
  (λ u → neg-ℝ (square-ℝ (gap u))) centerSquareContinuous
  (negContinuous realMetric (λ u → square-ℝ (gap u)) gapSquareContinuous)

completionYContinuous : Cont realMetric realMetric (λ u → AY (center u) (gap u))
completionYContinuous = mulContinuous realMetric (λ u → center u +ℝ center u) gap
  (addContinuous realMetric center center centerContinuous centerContinuous) gapContinuous

completionPlaneContinuous : Cont realMetric realPlaneMetric completionPlane
completionPlaneContinuous = pairContinuous realMetric realMetric realMetric
  (λ u → AX (center u) (gap u) *ℝ Kinv (center u) (gap u) (completionPositive u))
  (λ u → AY (center u) (gap u) *ℝ Kinv (center u) (gap u) (completionPositive u))
  (mulContinuous realMetric (λ u → AX (center u) (gap u))
    (λ u → Kinv (center u) (gap u) (completionPositive u)) completionXContinuous completionInvContinuous)
  (mulContinuous realMetric (λ u → AY (center u) (gap u))
    (λ u → Kinv (center u) (gap u) (completionPositive u)) completionYContinuous completionInvContinuous)

completionCircleContinuous : Cont realMetric circleMetric completionCircle
completionCircleContinuous = completionPlaneContinuous

closedSubtype : subtype lzero Real
closedSubtype u = leq-prop-ℝ zero-ℝ u ∧ leq-prop-ℝ u one-ℝ

closedMetric : Space
closedMetric = subspace-Metric-Space realMetric closedSubtype

ClosedParameter : UU (lsuc lzero)
ClosedParameter = type-Metric-Space closedMetric

closedZero closedOne : ClosedParameter
closedZero = zero-ℝ , refl-leq-ℝ zero-ℝ , leq-zero-one-ℝ
closedOne = one-ℝ , leq-zero-one-ℝ , refl-leq-ℝ one-ℝ

openIntoClosed : OpenRealInterval → ClosedParameter
openIntoClosed u = pr1 u , leq-le-ℝ (pr1 (pr2 u)) , leq-le-ℝ (pr2 (pr2 u))

closedInclusionContinuous : Cont closedMetric realMetric pr1
closedInclusionContinuous u = intro-exists (λ ε → ε) (λ ε u' near → near)

mCompletion : ClosedParameter → RealCircle
mCompletion u = completionCircle (pr1 u)

mCompletionContinuous : Cont closedMetric circleMetric mCompletion
mCompletionContinuous = composeContinuous closedMetric realMetric circleMetric completionCircle pr1
  completionCircleContinuous closedInclusionContinuous

nCompletion : ClosedParameter → RealPlane
nCompletion u = pr1 u , zero-ℝ

nCompletionContinuous : Cont closedMetric realPlaneMetric nCompletion
nCompletionContinuous = pairContinuous closedMetric realMetric realMetric pr1 (λ _ → zero-ℝ)
  closedInclusionContinuous (constantContinuous closedMetric zero-ℝ)

mInterior : (u : OpenRealInterval) →
  mCompletion (openIntoClosed u) ＝ pr1 (PointwiseHomeomorphism.backward strongCircleUnitHomeomorphism u)
mInterior u = homogeneousMatchesParam (center (pr1 u)) (gap (pr1 u))
  (positiveMinus (fromUnit u)) (completionPositive (pr1 u))

interiorStrong : (u : OpenRealInterval) → Strong (mCompletion (openIntoClosed u))
interiorStrong u = tr Strong (inv (mInterior u))
  (pr2 (PointwiseHomeomorphism.backward strongCircleUnitHomeomorphism u))

interiorNotEast : (u : OpenRealInterval) → Weak (mCompletion (openIntoClosed u))
interiorNotEast u = strongToWeak (mCompletion (openIntoClosed u)) (interiorStrong u)

centerZero : center zero-ℝ ＝ neg-ℝ one-ℝ
centerZero = ap (_-ℝ one-ℝ) (left-unit-law-add-ℝ zero-ℝ) ∙ left-unit-law-add-ℝ (neg-ℝ one-ℝ)

centerOne : center one-ℝ ＝ one-ℝ
centerOne = eq-sim-ℝ (cancel-right-add-diff-ℝ one-ℝ one-ℝ)

gapZero : gap zero-ℝ ＝ zero-ℝ
gapZero = ap (one-ℝ -ℝ_)
  (ap abs-ℝ centerZero ∙ abs-neg-ℝ one-ℝ ∙ abs-real-ℝ⁺ one-ℝ⁺) ∙
  eq-sim-ℝ (right-inverse-law-add-ℝ one-ℝ)

gapOne : gap one-ℝ ＝ zero-ℝ
gapOne = ap (one-ℝ -ℝ_) (ap abs-ℝ centerOne ∙ abs-real-ℝ⁺ one-ℝ⁺) ∙
  eq-sim-ℝ (right-inverse-law-add-ℝ one-ℝ)

mAtZero : mCompletion closedZero ＝ east
mAtZero = homogeneousEast (center zero-ℝ) (gap zero-ℝ) (completionPositive zero-ℝ)
  (ap square-ℝ centerZero ∙ square-neg-ℝ one-ℝ ∙ oneSquared) gapZero

mAtOne : mCompletion closedOne ＝ east
mAtOne = homogeneousEast (center one-ℝ) (gap one-ℝ) (completionPositive one-ℝ)
  (ap square-ℝ centerOne ∙ oneSquared) gapOne

mEndsCoincide : mCompletion closedZero ＝ mCompletion closedOne
mEndsCoincide = mAtZero ∙ inv mAtOne

nEndsDistinct : ¬ (nCompletion closedZero ＝ nCompletion closedOne)
nEndsDistinct h = neq-zero-one-ℝ (ap pr1 h)

closedEndpointsDistinct : ¬ (closedZero ＝ closedOne)
closedEndpointsDistinct h = neq-zero-one-ℝ (ap pr1 h)

completionNotInjective : ¬ ((u v : ClosedParameter) → mCompletion u ＝ mCompletion v → u ＝ v)
completionNotInjective injective = closedEndpointsDistinct (injective closedZero closedOne mEndsCoincide)

interiorInjective : (u v : OpenRealInterval) →
  mCompletion (openIntoClosed u) ＝ mCompletion (openIntoClosed v) → u ＝ v
interiorInjective u v h =
  inv (PointwiseHomeomorphism.forwardBackward strongCircleUnitHomeomorphism u) ∙
  ap (PointwiseHomeomorphism.forward strongCircleUnitHomeomorphism)
    (eq-type-subtype (λ p → apart-prop-ℝ (xCoord p) one-ℝ)
      (inv (mInterior u) ∙ h ∙ mInterior v)) ∙
  PointwiseHomeomorphism.forwardBackward strongCircleUnitHomeomorphism v
