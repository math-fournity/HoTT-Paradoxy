{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeRealCircleQualification where

-- Actual Dedekind real coordinates in the isolated no-erasure derivative.
-- Imported foundation axioms are recorded separately; this is not --safe Cubical Agda.
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.propositions
open import foundation.sets
open import foundation.subtypes
open import foundation.negation
open import foundation.negated-equality
open import foundation.empty-types
open import foundation.conjunction

open import elementary-number-theory.rational-numbers
open import elementary-number-theory.multiplication-rational-numbers
open import elementary-number-theory.positive-rational-numbers
open import elementary-number-theory.unit-fractions-rational-numbers
open import real-numbers.dedekind-real-numbers
open import real-numbers.rational-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.metric-space-of-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import metric-spaces.metric-spaces
open import metric-spaces.cartesian-products-metric-spaces
open import metric-spaces.subspaces-metric-spaces

Real : UU (lsuc lzero)
Real = ℝ lzero

RealPlane : UU (lsuc lzero)
RealPlane = Real × Real

realPlaneMetric : Metric-Space (lsuc lzero) lzero
realPlaneMetric = product-Metric-Space (metric-space-ℝ lzero) (metric-space-ℝ lzero)

circleEquation : RealPlane → Real
circleEquation (x , y) = (x *ℝ x) +ℝ (y *ℝ y)

circleSubtype : subtype (lsuc lzero) RealPlane
circleSubtype p = (circleEquation p ＝ one-ℝ) , is-set-ℝ lzero (circleEquation p) one-ℝ

circleMetric : Metric-Space (lsuc lzero) lzero
circleMetric = subspace-Metric-Space realPlaneMetric circleSubtype

RealCircle : UU (lsuc lzero)
RealCircle = type-Metric-Space circleMetric

zeroSquared : zero-ℝ *ℝ zero-ℝ ＝ zero-ℝ
zeroSquared = mul-real-ℚ zero-ℚ zero-ℚ ∙ ap real-ℚ (left-zero-law-mul-ℚ zero-ℚ)

oneSquared : one-ℝ *ℝ one-ℝ ＝ one-ℝ
oneSquared = left-unit-law-mul-ℝ one-ℝ

eastEquation : circleEquation (one-ℝ , zero-ℝ) ＝ one-ℝ
eastEquation = ap-add-ℝ oneSquared zeroSquared ∙ right-unit-law-add-ℝ one-ℝ

northEquation : circleEquation (zero-ℝ , one-ℝ) ＝ one-ℝ
northEquation = ap-add-ℝ zeroSquared oneSquared ∙ left-unit-law-add-ℝ one-ℝ

east north : RealCircle
east = (one-ℝ , zero-ℝ) , eastEquation
north = (zero-ℝ , one-ℝ) , northEquation

northNotEast : north ≠ east
northNotEast p = neq-zero-one-ℝ (ap (λ z → pr1 (pr1 z)) p)

puncturedSubtype : subtype (lsuc lzero) RealCircle
puncturedSubtype p = neg-type-Prop (p ＝ east)

puncturedCircleMetric : Metric-Space (lsuc lzero) lzero
puncturedCircleMetric = subspace-Metric-Space circleMetric puncturedSubtype

PuncturedRealCircle : UU (lsuc lzero)
PuncturedRealCircle = type-Metric-Space puncturedCircleMetric

puncturedNorth : PuncturedRealCircle
puncturedNorth = north , northNotEast

intervalSubtype : subtype lzero Real
intervalSubtype x = le-prop-ℝ zero-ℝ x ∧ le-prop-ℝ x one-ℝ

intervalMetric : Metric-Space (lsuc lzero) lzero
intervalMetric = subspace-Metric-Space (metric-space-ℝ lzero) intervalSubtype

OpenRealInterval : UU (lsuc lzero)
OpenRealInterval = type-Metric-Space intervalMetric

intervalHalf : OpenRealInterval
intervalHalf = one-half-ℝ ,
  preserves-le-real-ℚ (le-zero-is-positive-ℚ (is-positive-rational-ℚ⁺ one-half-ℚ⁺)) ,
  preserves-le-real-ℚ le-one-half-one-ℚ
