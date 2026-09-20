{-# OPTIONS --without-K --exact-split #-}
module hott-z.StereographicContinuity where

-- Same maps and the original product/subspace metrics; pointwise continuity.
open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.existential-quantification
open import foundation.propositions
open import metric-spaces.metric-spaces
open import metric-spaces.subspaces-metric-spaces
open import metric-spaces.cartesian-products-metric-spaces
open import metric-spaces.pointwise-continuous-maps-metric-spaces
open import metric-spaces.uniformly-continuous-maps-metric-spaces
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.apartness-real-numbers
open import real-numbers.isometry-addition-real-numbers
open import real-numbers.isometry-negation-real-numbers
open import real-numbers.lipschitz-continuity-multiplication-real-numbers

Space : UU (lsuc (lsuc lzero))
Space = Metric-Space (lsuc lzero) lzero

Cont : (X Y : Space) → (type-Metric-Space X → type-Metric-Space Y) → UU (lsuc lzero)
Cont = is-pointwise-continuous-map-Metric-Space

composeContinuous : (X Y Z : Space)
  (g : type-Metric-Space Y → type-Metric-Space Z)
  (f : type-Metric-Space X → type-Metric-Space Y) →
  Cont Y Z g → Cont X Y f → Cont X Z (λ x → g (f x))
composeContinuous X Y Z g f cg cf =
  pr2 (comp-pointwise-continuous-map-Metric-Space X Y Z (g , cg) (f , cf))

diagonalContinuous : (X : Space) → Cont X (product-Metric-Space X X) (λ x → x , x)
diagonalContinuous X x = intro-exists (λ ε → ε) (λ ε y near → near , near)

pairContinuous : (X Y Z : Space)
  (f : type-Metric-Space X → type-Metric-Space Y)
  (g : type-Metric-Space X → type-Metric-Space Z) →
  Cont X Y f → Cont X Z g → Cont X (product-Metric-Space Y Z) (λ x → f x , g x)
pairContinuous X Y Z f g cf cg = composeContinuous X (product-Metric-Space X X)
  (product-Metric-Space Y Z) (λ xy → f (pr1 xy) , g (pr2 xy)) (λ x → x , x)
  (pr2 (product-pointwise-continuous-map-Metric-Space X Y X Z (f , cf) (g , cg)))
  (diagonalContinuous X)

constantContinuous : (X : Space) (c : Real) → Cont X realMetric (λ _ → c)
constantContinuous X c = is-pointwise-continuous-map-const-Metric-Space X realMetric c

identityContinuous : Cont realMetric realMetric (λ x → x)
identityContinuous = is-pointwise-continuous-map-id-Metric-Space realMetric

addContinuous : (X : Space) (f g : type-Metric-Space X → Real) →
  Cont X realMetric f → Cont X realMetric g → Cont X realMetric (λ x → f x +ℝ g x)
addContinuous X f g cf cg = composeContinuous X realPlaneMetric realMetric
  (λ xy → pr1 xy +ℝ pr2 xy) (λ x → f x , g x)
  (pr2 (pointwise-continuous-map-uniformly-continuous-map-Metric-Space realPlaneMetric realMetric
    (uniformly-continuous-map-add-pair-ℝ lzero lzero)))
  (pairContinuous X realMetric realMetric f g cf cg)

mulContinuous : (X : Space) (f g : type-Metric-Space X → Real) →
  Cont X realMetric f → Cont X realMetric g → Cont X realMetric (λ x → f x *ℝ g x)
mulContinuous X f g cf cg = composeContinuous X realPlaneMetric realMetric
  (λ xy → pr1 xy *ℝ pr2 xy) (λ x → f x , g x)
  (pr2 (pointwise-continuous-map-mul-pair-ℝ lzero lzero))
  (pairContinuous X realMetric realMetric f g cf cg)

negContinuous : (X : Space) (f : type-Metric-Space X → Real) →
  Cont X realMetric f → Cont X realMetric (λ x → neg-ℝ (f x))
negContinuous X f cf = composeContinuous X realMetric realMetric neg-ℝ f
  (pr2 (pointwise-continuous-map-isometry-Metric-Space realMetric realMetric (isometry-neg-ℝ lzero))) cf

strongMetric : Space
strongMetric = subspace-Metric-Space circleMetric (λ p → apart-prop-ℝ (xCoord p) one-ℝ)

forwardXContinuous : Cont strongMetric realMetric (λ w → xCoord (pr1 w))
forwardXContinuous w = intro-exists (λ ε → ε) (λ ε w' near → pr1 near)

forwardYContinuous : Cont strongMetric realMetric (λ w → yCoord (pr1 w))
forwardYContinuous w = intro-exists (λ ε → ε) (λ ε w' near → pr2 near)

forwardDenominatorContinuous : Cont strongMetric realMetric (λ w → denominator (pr1 w))
forwardDenominatorContinuous = addContinuous strongMetric (λ _ → one-ℝ)
  (λ w → neg-ℝ (xCoord (pr1 w))) (constantContinuous strongMetric one-ℝ)
  (negContinuous strongMetric (λ w → xCoord (pr1 w)) forwardXContinuous)

forwardNonzeroDenominator : StrongPuncture → NonzeroReal
forwardNonzeroDenominator w = denominator (pr1 w) , denominatorNonzero (pr1 w) (pr2 w)

forwardNonzeroContinuous : Cont strongMetric nonzeroMetric forwardNonzeroDenominator
forwardNonzeroContinuous = forwardDenominatorContinuous

forwardReciprocalContinuous : Cont strongMetric realMetric (λ w → inverseDenominator (pr1 w) (pr2 w))
forwardReciprocalContinuous = composeContinuous strongMetric nonzeroMetric realMetric recip
  forwardNonzeroDenominator reciprocalContinuous forwardNonzeroContinuous

stereographicContinuous : Cont strongMetric realMetric stereographicForward
stereographicContinuous = mulContinuous strongMetric (λ w → yCoord (pr1 w))
  (λ w → inverseDenominator (pr1 w) (pr2 w)) forwardYContinuous forwardReciprocalContinuous

squareContinuous : Cont realMetric realMetric square-ℝ
squareContinuous = mulContinuous realMetric (λ t → t) (λ t → t) identityContinuous identityContinuous

DContinuous : Cont realMetric realMetric D
DContinuous = addContinuous realMetric square-ℝ (λ _ → one-ℝ) squareContinuous (constantContinuous realMetric one-ℝ)

paramNonzeroD : Real → NonzeroReal
paramNonzeroD t = D t , is-nonzero-is-positive-ℝ (positiveD t)

paramNonzeroDContinuous : Cont realMetric nonzeroMetric paramNonzeroD
paramNonzeroDContinuous = DContinuous

qContinuous : Cont realMetric realMetric qInv
qContinuous = composeContinuous realMetric nonzeroMetric realMetric recip paramNonzeroD
  reciprocalContinuous paramNonzeroDContinuous

numeratorXContinuous : Cont realMetric realMetric numeratorX
numeratorXContinuous = addContinuous realMetric square-ℝ (λ _ → neg-ℝ one-ℝ)
  squareContinuous (constantContinuous realMetric (neg-ℝ one-ℝ))

numeratorYContinuous : Cont realMetric realMetric numeratorY
numeratorYContinuous = addContinuous realMetric (λ t → t) (λ t → t) identityContinuous identityContinuous

paramPlaneContinuous : Cont realMetric realPlaneMetric paramPlane
paramPlaneContinuous = pairContinuous realMetric realMetric realMetric
  (λ t → numeratorX t *ℝ qInv t) (λ t → numeratorY t *ℝ qInv t)
  (mulContinuous realMetric numeratorX qInv numeratorXContinuous qContinuous)
  (mulContinuous realMetric numeratorY qInv numeratorYContinuous qContinuous)

parameterizeContinuous : Cont realMetric strongMetric parameterize
parameterizeContinuous = paramPlaneContinuous

-- Explicit inverse maps with the library's pointwise modulus-based continuity.
record PointwiseHomeomorphism (X Y : Space) : UU (lsuc lzero) where
  field
    forward : type-Metric-Space X → type-Metric-Space Y
    backward : type-Metric-Space Y → type-Metric-Space X
    forwardContinuous : Cont X Y forward
    backwardContinuous : Cont Y X backward
    forwardBackward : (y : type-Metric-Space Y) → forward (backward y) ＝ y
    backwardForward : (x : type-Metric-Space X) → backward (forward x) ＝ x

strongHomeomorphism : PointwiseHomeomorphism strongMetric realMetric
PointwiseHomeomorphism.forward strongHomeomorphism = stereographicForward
PointwiseHomeomorphism.backward strongHomeomorphism = parameterize
PointwiseHomeomorphism.forwardContinuous strongHomeomorphism = stereographicContinuous
PointwiseHomeomorphism.backwardContinuous strongHomeomorphism = parameterizeContinuous
PointwiseHomeomorphism.forwardBackward strongHomeomorphism = forwardParameter
PointwiseHomeomorphism.backwardForward strongHomeomorphism = parameterForward

liftContinuous : (lift : Lift) → Cont puncturedCircleMetric strongMetric (liftWeakPoint lift)
liftContinuous lift w = intro-exists (λ ε → ε) (λ ε w' near → near)

forgetContinuous : Cont strongMetric puncturedCircleMetric forgetStrong
forgetContinuous w = intro-exists (λ ε → ε) (λ ε w' near → near)

weakHomeomorphism : Lift → PointwiseHomeomorphism puncturedCircleMetric realMetric
PointwiseHomeomorphism.forward (weakHomeomorphism lift) w = stereographicForward (liftWeakPoint lift w)
PointwiseHomeomorphism.backward (weakHomeomorphism lift) t = forgetStrong (parameterize t)
PointwiseHomeomorphism.forwardContinuous (weakHomeomorphism lift) =
  composeContinuous puncturedCircleMetric strongMetric realMetric stereographicForward (liftWeakPoint lift)
    stereographicContinuous (liftContinuous lift)
PointwiseHomeomorphism.backwardContinuous (weakHomeomorphism lift) =
  composeContinuous realMetric strongMetric puncturedCircleMetric forgetStrong parameterize
    forgetContinuous parameterizeContinuous
PointwiseHomeomorphism.forwardBackward (weakHomeomorphism lift) t =
  ap stereographicForward (liftForget lift (parameterize t)) ∙ forwardParameter t
PointwiseHomeomorphism.backwardForward (weakHomeomorphism lift) w =
  ap forgetStrong (parameterForward (liftWeakPoint lift w)) ∙ forgetLift lift w

classicalWeakHomeomorphism : ExcludedMiddle0 → PointwiseHomeomorphism puncturedCircleMetric realMetric
classicalWeakHomeomorphism em = weakHomeomorphism (dneGivesLift (excludedMiddleToDNE em))
