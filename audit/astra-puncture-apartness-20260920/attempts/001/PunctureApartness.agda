{-# OPTIONS --without-K --exact-split #-}
module hott-z.PunctureApartness where

-- Actual Dedekind circle from C281, under the pinned no-erasure derivative.
-- No excluded-middle or double-negation principle is assumed globally.
open import hott-z.NativeRealCircleQualification
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.equality-cartesian-product-types
open import foundation.subtypes
open import foundation.propositions
open import foundation.logical-equivalences
open import foundation.negation
open import foundation.negated-equality
open import foundation.empty-types
open import foundation.coproduct-types
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.zero-real-numbers
open import real-numbers.apartness-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplicative-inverses-nonzero-real-numbers
open import real-numbers.strict-inequality-real-numbers

xCoord yCoord : RealCircle → Real
xCoord p = pr1 (pr1 p)
yCoord p = pr2 (pr1 p)

firstCoordinateOneIsEast : (p : RealCircle) → xCoord p ＝ one-ℝ → p ＝ east
firstCoordinateOneIsEast p h = eq-type-subtype circleSubtype (eq-pair h yZero)
  where
  xSquaredOne : square-ℝ (xCoord p) ＝ one-ℝ
  xSquaredOne = ap square-ℝ h ∙ oneSquared

  onePlusYSquared : one-ℝ +ℝ square-ℝ (yCoord p) ＝ one-ℝ
  onePlusYSquared = inv (ap-add-ℝ xSquaredOne refl) ∙ pr2 p

  ySquaredZero : square-ℝ (yCoord p) ＝ zero-ℝ
  ySquaredZero = eq-sim-ℝ
    (reflects-sim-left-add-ℝ one-ℝ (square-ℝ (yCoord p)) zero-ℝ
      (sim-eq-ℝ (onePlusYSquared ∙ inv (right-unit-law-add-ℝ one-ℝ))))

  yZero : yCoord p ＝ zero-ℝ
  yZero = eq-sim-ℝ (is-zero-is-zero-square-ℝ (sim-eq-ℝ ySquaredZero))

Weak : RealCircle → UU (lsuc lzero)
Weak p = p ≠ east

Strong : RealCircle → UU lzero
Strong p = apart-ℝ (xCoord p) one-ℝ

strongToWeak : (p : RealCircle) → Strong p → Weak p
strongToWeak p a h = nonequal-apart-ℝ (xCoord p) one-ℝ a (ap xCoord h)

weakToDoubleNegStrong : (p : RealCircle) → Weak p → ¬ (¬ (Strong p))
weakToDoubleNegStrong p w noApart =
  w (firstCoordinateOneIsEast p (eq-sim-ℝ (sim-nonapart-ℝ (xCoord p) one-ℝ noApart)))

doubleNegStrongToWeak : (p : RealCircle) → ¬ (¬ (Strong p)) → Weak p
doubleNegStrongToWeak p nn h = nn (λ a → strongToWeak p a h)

weakIffDoubleNegStrong : (p : RealCircle) → Weak p ↔ ¬ (¬ (Strong p))
weakIffDoubleNegStrong p = weakToDoubleNegStrong p , doubleNegStrongToWeak p

StrongPuncture : UU (lsuc lzero)
StrongPuncture = Σ RealCircle Strong

forgetStrong : StrongPuncture → PuncturedRealCircle
forgetStrong (p , a) = p , strongToWeak p a

Lift : UU (lsuc lzero)
Lift = (p : RealCircle) → Weak p → Strong p

LocalStability : UU (lsuc lzero)
LocalStability = (p : RealCircle) → ¬ (¬ (Strong p)) → Strong p

liftToStability : Lift → LocalStability
liftToStability lift p nn = lift p (doubleNegStrongToWeak p nn)

stabilityToLift : LocalStability → Lift
stabilityToLift stable p w = stable p (weakToDoubleNegStrong p w)

liftIffLocalStability : Lift ↔ LocalStability
liftIffLocalStability = liftToStability , stabilityToLift

-- A refinement must retain the actual point, not silently move to another one.
SamePointRefinement : UU (lsuc lzero)
SamePointRefinement = (w : PuncturedRealCircle) →
  Σ StrongPuncture (λ s → pr1 s ＝ pr1 w)

liftToRefinement : Lift → SamePointRefinement
liftToRefinement lift (p , w) = (p , lift p w) , refl

refinementToLift : SamePointRefinement → Lift
refinementToLift refine p w =
  tr Strong (pr2 (refine (p , w))) (pr2 (pr1 (refine (p , w))))

refinementIffLift : SamePointRefinement ↔ Lift
refinementIffLift = refinementToLift , liftToRefinement

-- Optional sufficiency control; NOT an unconditional instance of Lift.
DoubleNegationElimination0 : UU (lsuc lzero)
DoubleNegationElimination0 = (P : Prop lzero) → ¬ (¬ (type-Prop P)) → type-Prop P

ExcludedMiddle0 : UU (lsuc lzero)
ExcludedMiddle0 = (P : Prop lzero) → type-Prop P + ¬ (type-Prop P)

excludedMiddleToDNE : ExcludedMiddle0 → DoubleNegationElimination0
excludedMiddleToDNE em P nn =
  rec-coproduct (λ p → p) (λ np → ex-falso (nn np)) (em P)

dneGivesLift : DoubleNegationElimination0 → Lift
dneGivesLift dne p w = dne (apart-prop-ℝ (xCoord p) one-ℝ) (weakToDoubleNegStrong p w)

denominator : RealCircle → Real
denominator p = one-ℝ -ℝ xCoord p

denominatorNonzero : (p : RealCircle) → Strong p → is-nonzero-ℝ (denominator p)
denominatorNonzero p a = is-nonzero-diff-is-apart-ℝ one-ℝ (xCoord p) (symmetric-apart-ℝ a)

inverseDenominator : (p : RealCircle) → Strong p → Real
inverseDenominator p a = real-inv-nonzero-ℝ (denominator p , denominatorNonzero p a)

denominatorRightInverse : (p : RealCircle) (a : Strong p) →
  denominator p *ℝ inverseDenominator p a ＝ one-ℝ
denominatorRightInverse p a = eq-sim-ℝ
  (right-inverse-law-mul-nonzero-ℝ (denominator p , denominatorNonzero p a))

-- A forward coordinate only: continuity, inverse map and roundtrips remain open.
stereographicForward : StrongPuncture → Real
stereographicForward (p , a) = yCoord p *ℝ inverseDenominator p a

northStrong : Strong north
northStrong = apart-le-ℝ le-zero-one-ℝ

northForwardOne : stereographicForward (north , northStrong) ＝ one-ℝ
northForwardOne =
  inv (ap (λ d → d *ℝ inverseDenominator north northStrong) (right-unit-law-diff-ℝ one-ℝ)) ∙
  denominatorRightInverse north northStrong

eastNotStrong : ¬ (Strong east)
eastNotStrong = antireflexive-apart-ℝ one-ℝ
