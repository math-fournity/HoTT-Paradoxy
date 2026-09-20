{-# OPTIONS --without-K --exact-split #-}
module hott-z.ReciprocalContinuity where

-- Actual reciprocal on the subspace of apart-from-zero Dedekind reals.
-- The local rational modulus below is constructed without a choice axiom.
open import hott-z.NativeRealCircleQualification using (Real)
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.existential-quantification
open import foundation.propositional-truncations
open import foundation.propositions
open import elementary-number-theory.positive-rational-numbers
open import elementary-number-theory.multiplication-positive-rational-numbers
open import elementary-number-theory.multiplicative-group-of-positive-rational-numbers
open import elementary-number-theory.minimum-positive-rational-numbers
open import elementary-number-theory.unit-fractions-rational-numbers
open import metric-spaces.metric-spaces
open import metric-spaces.subspaces-metric-spaces
open import metric-spaces.continuity-of-maps-at-points-metric-spaces
open import metric-spaces.pointwise-continuous-maps-metric-spaces
open import order-theory.large-posets
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.positive-real-numbers
open import real-numbers.nonnegative-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.multiplication-nonnegative-real-numbers
open import real-numbers.multiplicative-inverses-positive-real-numbers
open import real-numbers.multiplicative-inverses-nonzero-real-numbers
open import real-numbers.absolute-value-real-numbers
open import real-numbers.distance-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.inequalities-addition-and-subtraction-real-numbers
open import real-numbers.metric-space-of-real-numbers

open inequality-reasoning-Large-Poset ℝ-Large-Poset

NonzeroReal : UU (lsuc lzero)
NonzeroReal = nonzero-ℝ lzero

val recip : NonzeroReal → Real
val = real-nonzero-ℝ
recip = real-inv-nonzero-ℝ

realMetric : Metric-Space (lsuc lzero) lzero
realMetric = metric-space-ℝ lzero

nonzeroMetric : Metric-Space (lsuc lzero) lzero
nonzeroMetric = subspace-Metric-Space realMetric is-nonzero-prop-ℝ

rightInv : (x : NonzeroReal) → val x *ℝ recip x ＝ one-ℝ
rightInv x = eq-sim-ℝ (right-inverse-law-mul-nonzero-ℝ x)

leftInv : (x : NonzeroReal) → recip x *ℝ val x ＝ one-ℝ
leftInv x = eq-sim-ℝ (left-inverse-law-mul-nonzero-ℝ x)

positiveAbs : NonzeroReal → ℝ⁺ lzero
positiveAbs x = abs-ℝ (val x) , is-positive-abs-is-nonzero-ℝ (val x) (pr2 x)

absReciprocal : (x : NonzeroReal) → abs-ℝ (recip x) ＝ real-inv-ℝ⁺ (positiveAbs x)
absReciprocal x = eq-sim-ℝ
  (unique-right-inv-ℝ⁺ (positiveAbs x) (positiveAbs (inv-nonzero-ℝ x))
    (sim-eq-ℝ (inv (abs-mul-ℝ (val x) (recip x)) ∙
      ap abs-ℝ (rightInv x) ∙ abs-real-ℝ⁺ one-ℝ⁺)))

reciprocalDifference : (x y : NonzeroReal) →
  recip x -ℝ recip y ＝ (recip x *ℝ (val y -ℝ val x)) *ℝ recip y
reciprocalDifference x y =
  ap (_-ℝ recip y) (inv (ap (recip x *ℝ_) (rightInv y) ∙ right-unit-law-mul-ℝ (recip x))) ∙
  ap ((recip x *ℝ (val y *ℝ recip y)) -ℝ_)
    (inv (ap (_*ℝ recip y) (leftInv x) ∙ left-unit-law-mul-ℝ (recip y))) ∙
  ap (_-ℝ ((recip x *ℝ val x) *ℝ recip y)) (inv (associative-mul-ℝ (recip x) (val y) (recip y))) ∙
  inv (right-distributive-mul-diff-ℝ (recip x *ℝ val y) (recip x *ℝ val x) (recip y)) ∙
  ap (_*ℝ recip y) (inv (left-distributive-mul-diff-ℝ (recip x) (val y) (val x)))

reciprocalDistance : (x y : NonzeroReal) →
  dist-ℝ (recip x) (recip y) ＝
  (abs-ℝ (recip x) *ℝ abs-ℝ (recip y)) *ℝ dist-ℝ (val y) (val x)
reciprocalDistance x y =
  ap abs-ℝ (reciprocalDifference x y) ∙
  abs-mul-ℝ (recip x *ℝ (val y -ℝ val x)) (recip y) ∙
  ap (_*ℝ abs-ℝ (recip y)) (abs-mul-ℝ (recip x) (val y -ℝ val x)) ∙
  right-swap-mul-ℝ (abs-ℝ (recip x)) (dist-ℝ (val y) (val x)) (abs-ℝ (recip y))

inverseBound : (r : ℚ⁺) (x : NonzeroReal) →
  leq-ℝ (real-ℚ⁺ r) (abs-ℝ (val x)) → leq-ℝ (abs-ℝ (recip x)) (real-ℚ⁺ (inv-ℚ⁺ r))
inverseBound r x lower = chain-of-inequalities
  abs-ℝ (recip x)
  ≤ real-inv-ℝ⁺ (positiveAbs x) by leq-eq-ℝ (absReciprocal x)
  ≤ real-inv-ℝ⁺ (positive-real-ℚ⁺ r) by inv-leq-ℝ⁺ (positive-real-ℚ⁺ r) (positiveAbs x) lower
  ≤ real-ℚ⁺ (inv-ℚ⁺ r) by leq-eq-ℝ (real-inv-positive-real-ℚ⁺ r)

radiusLeDouble : (r : ℚ⁺) → leq-ℝ (real-ℚ⁺ r) (real-ℚ⁺ r +ℝ real-ℚ⁺ r)
radiusLeDouble r = tr (λ a → leq-ℝ a (real-ℚ⁺ r +ℝ real-ℚ⁺ r))
  (right-unit-law-add-ℝ (real-ℚ⁺ r))
  (preserves-leq-left-add-ℝ (real-ℚ⁺ r) zero-ℝ (real-ℚ⁺ r) (leq-le-ℝ (is-positive-real-ℚ⁺ r)))

nearbyLower : (r : ℚ⁺) (x y : Real) →
  leq-ℝ (real-ℚ⁺ r +ℝ real-ℚ⁺ r) (abs-ℝ x) →
  leq-ℝ (dist-ℝ y x) (real-ℚ⁺ r) → leq-ℝ (real-ℚ⁺ r) (abs-ℝ y)
nearbyLower r x y center near = reflects-leq-right-add-ℝ (real-ℚ⁺ r) (real-ℚ⁺ r) (abs-ℝ y)
  (chain-of-inequalities
    real-ℚ⁺ r +ℝ real-ℚ⁺ r
    ≤ abs-ℝ x by center
    ≤ abs-ℝ y +ℝ dist-ℝ y x by leq-abs-add-abs-dist-ℝ x y
    ≤ abs-ℝ y +ℝ real-ℚ⁺ r by preserves-leq-left-add-ℝ (abs-ℝ y) _ _ near)

coefficient : ℚ⁺ → ℚ⁺
coefficient r = inv-ℚ⁺ r *ℚ⁺ inv-ℚ⁺ r

budget : ℚ⁺ → ℚ⁺ → ℚ⁺
budget r ε = inv-ℚ⁺ (coefficient r) *ℚ⁺ ε

modulus : ℚ⁺ → ℚ⁺ → ℚ⁺
modulus r ε = min-ℚ⁺ r (budget r ε)

budgetIdentity : (r ε : ℚ⁺) → coefficient r *ℚ⁺ budget r ε ＝ ε
budgetIdentity r ε = inv (associative-mul-ℚ⁺ (coefficient r) (inv-ℚ⁺ (coefficient r)) ε) ∙
  ap (_*ℚ⁺ ε) (right-inverse-law-mul-ℚ⁺ (coefficient r)) ∙ left-unit-law-mul-ℚ⁺ ε

localEstimate : (r ε : ℚ⁺) (x y : NonzeroReal) →
  leq-ℝ (real-ℚ⁺ r +ℝ real-ℚ⁺ r) (abs-ℝ (val x)) →
  neighborhood-ℝ lzero (modulus r ε) (val x) (val y) →
  leq-ℝ (dist-ℝ (recip x) (recip y)) (real-ℚ⁺ ε)
localEstimate r ε x y center near = chain-of-inequalities
  dist-ℝ (recip x) (recip y)
  ≤ (abs-ℝ (recip x) *ℝ abs-ℝ (recip y)) *ℝ dist-ℝ (val y) (val x)
    by leq-eq-ℝ (reciprocalDistance x y)
  ≤ real-ℚ⁺ (coefficient r) *ℝ dist-ℝ (val y) (val x)
    by preserves-leq-right-mul-ℝ⁰⁺ (nonnegative-dist-ℝ (val y) (val x)) productBound
  ≤ real-ℚ⁺ (coefficient r) *ℝ real-ℚ⁺ (modulus r ε)
    by preserves-leq-left-mul-ℝ⁰⁺ (nonnegative-real-ℚ⁺ (coefficient r)) distanceBound
  ≤ real-ℚ⁺ (coefficient r) *ℝ real-ℚ⁺ (budget r ε)
    by preserves-leq-left-mul-ℝ⁰⁺ (nonnegative-real-ℚ⁺ (coefficient r))
      (preserves-leq-real-ℚ (leq-right-min-ℚ⁺ r (budget r ε)))
  ≤ real-ℚ⁺ (coefficient r *ℚ⁺ budget r ε)
    by leq-eq-ℝ (mul-real-ℚ _ _)
  ≤ real-ℚ⁺ ε by leq-eq-ℝ (ap real-ℚ⁺ (budgetIdentity r ε))
  where
  distanceBound : leq-ℝ (dist-ℝ (val y) (val x)) (real-ℚ⁺ (modulus r ε))
  distanceBound = leq-dist-neighborhood-ℝ (modulus r ε) (val y) (val x)
    (is-symmetric-neighborhood-ℝ (modulus r ε) (val x) (val y) near)
  nearRadius : leq-ℝ (dist-ℝ (val y) (val x)) (real-ℚ⁺ r)
  nearRadius = transitive-leq-ℝ _ _ _
    (preserves-leq-real-ℚ (leq-left-min-ℚ⁺ r (budget r ε))) distanceBound
  lowerX : leq-ℝ (real-ℚ⁺ r) (abs-ℝ (val x))
  lowerX = transitive-leq-ℝ _ _ _ center (radiusLeDouble r)
  lowerY : leq-ℝ (real-ℚ⁺ r) (abs-ℝ (val y))
  lowerY = nearbyLower r (val x) (val y) center nearRadius
  productBound : leq-ℝ (abs-ℝ (recip x) *ℝ abs-ℝ (recip y)) (real-ℚ⁺ (coefficient r))
  productBound = chain-of-inequalities
    abs-ℝ (recip x) *ℝ abs-ℝ (recip y)
    ≤ real-ℚ⁺ (inv-ℚ⁺ r) *ℝ real-ℚ⁺ (inv-ℚ⁺ r)
      by preserves-leq-mul-ℝ⁰⁺
        (nonnegative-abs-ℝ (recip x)) (nonnegative-real-ℚ⁺ (inv-ℚ⁺ r))
        (nonnegative-abs-ℝ (recip y)) (nonnegative-real-ℚ⁺ (inv-ℚ⁺ r))
        (inverseBound r x lowerX) (inverseBound r y lowerY)
    ≤ real-ℚ⁺ (coefficient r) by leq-eq-ℝ (mul-real-ℚ _ _)

halfDouble : (γ : ℚ⁺) →
  real-ℚ⁺ (one-half-ℚ⁺ *ℚ⁺ γ) +ℝ real-ℚ⁺ (one-half-ℚ⁺ *ℚ⁺ γ) ＝ real-ℚ⁺ γ
halfDouble γ =
  ap-add-ℝ (inv (mul-real-ℚ _ _)) (inv (mul-real-ℚ _ _)) ∙
  twice-left-mul-one-half-ℝ (real-ℚ⁺ γ)

reciprocalContinuous : is-pointwise-continuous-map-Metric-Space nonzeroMetric realMetric recip
reciprocalContinuous x =
  let open do-syntax-trunc-Prop
        (is-continuous-at-point-prop-map-Metric-Space nonzeroMetric realMetric recip x)
  in do
    (γ , γBelow) ← exists-ℚ⁺-in-lower-cut-ℝ⁺ (positiveAbs x)
    let
      r = one-half-ℚ⁺ *ℚ⁺ γ
      center : leq-ℝ (real-ℚ⁺ r +ℝ real-ℚ⁺ r) (abs-ℝ (val x))
      center = transitive-leq-ℝ _ _ _
        (leq-le-ℝ (le-real-is-in-lower-cut-ℝ (abs-ℝ (val x)) γBelow))
        (leq-eq-ℝ (halfDouble γ))
    intro-exists (modulus r) (λ ε y near →
      neighborhood-dist-ℝ ε (recip x) (recip y) (localEstimate r ε x y center near))
