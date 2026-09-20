{-# OPTIONS --without-K --exact-split #-}
module hott-z.NativeMotion where

-- The rational stretch/bend/turn family over the original native Real and (0,1).
-- Reflection of the second coordinate aligns the final parametrization with
-- NativeStereographic.paramPlane. Embeddings and the closed square are separate
-- obligations; this module does not assert their completion.
open import hott-z.NativeRealCircleQualification
open import hott-z.NativeStereographic
open import hott-z.ReciprocalContinuity
open import hott-z.StereographicContinuity
open import hott-z.SignedIntervalHomeomorphism
open import hott-z.NativeOpenInterval
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.equality-cartesian-product-types
open import foundation.existential-quantification
open import metric-spaces.metric-spaces
open import metric-spaces.cartesian-products-metric-spaces
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
open import real-numbers.multiplication-nonnegative-real-numbers
open import real-numbers.absolute-value-real-numbers

remaining scale offset : Real → Real
remaining t = one-ℝ -ℝ t
scale t = one-half-ℝ *ℝ D t
offset t = one-half-ℝ *ℝ remaining t

stretchDen : Real → Real → Real
stretchDen t r = one-ℝ +ℝ (square-ℝ (remaining t) *ℝ abs-ℝ r)

stretchDenPositive : (t r : Real) → is-positive-ℝ (stretchDen t r)
stretchDenPositive t r = tr is-positive-ℝ
  (commutative-add-ℝ (square-ℝ (remaining t) *ℝ abs-ℝ r) one-ℝ)
  (is-positive-add-nonnegative-positive-ℝ
    (is-nonnegative-mul-ℝ (is-nonnegative-square-ℝ (remaining t)) (is-nonnegative-abs-ℝ r))
    (pr2 one-ℝ⁺))

stretchNZ : Real → Real → NonzeroReal
stretchNZ t r = nonzero-ℝ⁺ (stretchDen t r , stretchDenPositive t r)

stretchInv stretch : Real → Real → Real
stretchInv t r = recip (stretchNZ t r)
stretch t r = (scale t *ℝ (r *ℝ stretchInv t r)) +ℝ offset t

bend : Real → Real → RealPlane
bend t r = (r *ℝ qInv (t *ℝ r)) , ((t *ℝ square-ℝ r) *ℝ qInv (t *ℝ r))

turn : Real → RealPlane → RealPlane
turn t v =
  (((remaining t *ℝ pr1 v) +ℝ ((two *ℝ t) *ℝ pr2 v)) -ℝ t) ,
  ((neg-ℝ (two *ℝ t) *ℝ pr1 v) +ℝ (remaining t *ℝ pr2 v))

reflectY : RealPlane → RealPlane
reflectY v = pr1 v , neg-ℝ (pr2 v)

realParameter : OpenRealInterval → Real
realParameter u = unsquash (fromUnit u)

motionRaw motion : Real → OpenRealInterval → RealPlane
motionRaw t u = turn t (bend t (stretch t (realParameter u)))
motion t u = reflectY (motionRaw t u)

remainingContinuous : Cont realMetric realMetric remaining
remainingContinuous = addContinuous realMetric (λ _ → one-ℝ) neg-ℝ
  (constantContinuous realMetric one-ℝ)
  (negContinuous realMetric (λ t → t) identityContinuous)

scaleContinuous : Cont realMetric realMetric scale
scaleContinuous = mulContinuous realMetric (λ _ → one-half-ℝ) D
  (constantContinuous realMetric one-half-ℝ) DContinuous

offsetContinuous : Cont realMetric realMetric offset
offsetContinuous = mulContinuous realMetric (λ _ → one-half-ℝ) remaining
  (constantContinuous realMetric one-half-ℝ) remainingContinuous

-- These two projections are continuous for every product used below.
firstContinuous : (X Y : Space) → Cont (product-Metric-Space X Y) X pr1
firstContinuous X Y x = intro-exists (λ ε → ε) (λ ε y near → pr1 near)

secondContinuous : (X Y : Space) → Cont (product-Metric-Space X Y) Y pr2
secondContinuous X Y x = intro-exists (λ ε → ε) (λ ε y near → pr2 near)

-- The same formulas can be composed with any already continuous t and r.
module FormulaContinuity (X : Space) (t r : type-Metric-Space X → Real)
  (ct : Cont X realMetric t) (cr : Cont X realMetric r) where

  crem : Cont X realMetric (λ x → remaining (t x))
  crem = composeContinuous X realMetric realMetric remaining t remainingContinuous ct

  cscale : Cont X realMetric (λ x → scale (t x))
  cscale = composeContinuous X realMetric realMetric scale t scaleContinuous ct

  coffset : Cont X realMetric (λ x → offset (t x))
  coffset = composeContinuous X realMetric realMetric offset t offsetContinuous ct

  cden : Cont X realMetric (λ x → stretchDen (t x) (r x))
  cden = addContinuous X (λ _ → one-ℝ)
    (λ x → square-ℝ (remaining (t x)) *ℝ abs-ℝ (r x))
    (constantContinuous X one-ℝ)
    (mulContinuous X (λ x → square-ℝ (remaining (t x))) (λ x → abs-ℝ (r x))
      (mulContinuous X (λ x → remaining (t x)) (λ x → remaining (t x)) crem crem)
      (absContinuous X r cr))

  cinv : Cont X realMetric (λ x → stretchInv (t x) (r x))
  cinv = composeContinuous X nonzeroMetric realMetric recip
    (λ x → stretchNZ (t x) (r x)) reciprocalContinuous cden

  cstretch : Cont X realMetric (λ x → stretch (t x) (r x))
  cstretch = addContinuous X (λ x → scale (t x) *ℝ (r x *ℝ stretchInv (t x) (r x)))
    (λ x → offset (t x))
    (mulContinuous X (λ x → scale (t x)) (λ x → r x *ℝ stretchInv (t x) (r x))
      cscale (mulContinuous X r (λ x → stretchInv (t x) (r x)) cr cinv)) coffset

  cbendInv : Cont X realMetric (λ x → qInv (t x *ℝ r x))
  cbendInv = composeContinuous X realMetric realMetric qInv (λ x → t x *ℝ r x)
    qContinuous (mulContinuous X t r ct cr)

  cbendX : Cont X realMetric (λ x → pr1 (bend (t x) (r x)))
  cbendX = mulContinuous X r (λ x → qInv (t x *ℝ r x)) cr cbendInv

  cbendY : Cont X realMetric (λ x → pr2 (bend (t x) (r x)))
  cbendY = mulContinuous X (λ x → t x *ℝ square-ℝ (r x)) (λ x → qInv (t x *ℝ r x))
    (mulContinuous X t (λ x → square-ℝ (r x)) ct (mulContinuous X r r cr cr)) cbendInv

module TurnContinuity (X : Space) (t x y : type-Metric-Space X → Real)
  (ct : Cont X realMetric t) (cx : Cont X realMetric x) (cy : Cont X realMetric y) where

  crem : Cont X realMetric (λ z → remaining (t z))
  crem = composeContinuous X realMetric realMetric remaining t remainingContinuous ct

  ctwot : Cont X realMetric (λ z → two *ℝ t z)
  ctwot = mulContinuous X (λ _ → two) t (constantContinuous X two) ct

  cxturn : Cont X realMetric (λ z → pr1 (turn (t z) (x z , y z)))
  cxturn = addContinuous X
    (λ z → (remaining (t z) *ℝ x z) +ℝ ((two *ℝ t z) *ℝ y z)) (λ z → neg-ℝ (t z))
    (addContinuous X (λ z → remaining (t z) *ℝ x z) (λ z → (two *ℝ t z) *ℝ y z)
      (mulContinuous X (λ z → remaining (t z)) x crem cx)
      (mulContinuous X (λ z → two *ℝ t z) y ctwot cy))
    (negContinuous X t ct)

  cyturn : Cont X realMetric (λ z → pr2 (turn (t z) (x z , y z)))
  cyturn = addContinuous X (λ z → neg-ℝ (two *ℝ t z) *ℝ x z) (λ z → remaining (t z) *ℝ y z)
    (mulContinuous X (λ z → neg-ℝ (two *ℝ t z)) x (negContinuous X (λ z → two *ℝ t z) ctwot) cx)
    (mulContinuous X (λ z → remaining (t z)) y crem cy)

motionDomain : Space
motionDomain = product-Metric-Space realMetric intervalMetric

realParameterContinuous : Cont intervalMetric realMetric realParameter
realParameterContinuous = composeContinuous intervalMetric signedMetric realMetric unsquash fromUnit
  unsquashContinuous fromUnitContinuous

private
  timeContinuous = firstContinuous realMetric intervalMetric
  parameterContinuous = composeContinuous motionDomain intervalMetric realMetric realParameter pr2
    realParameterContinuous (secondContinuous realMetric intervalMetric)
  module StretchC = FormulaContinuity motionDomain pr1 (λ z → realParameter (pr2 z))
    timeContinuous parameterContinuous
  module BendC = FormulaContinuity motionDomain pr1 (λ z → stretch (pr1 z) (realParameter (pr2 z)))
    timeContinuous StretchC.cstretch
  module TurnC = TurnContinuity motionDomain pr1
    (λ z → pr1 (bend (pr1 z) (stretch (pr1 z) (realParameter (pr2 z)))))
    (λ z → pr2 (bend (pr1 z) (stretch (pr1 z) (realParameter (pr2 z)))))
    timeContinuous BendC.cbendX BendC.cbendY

motionRawContinuous : Cont motionDomain realPlaneMetric (λ z → motionRaw (pr1 z) (pr2 z))
motionRawContinuous = pairContinuous motionDomain realMetric realMetric
  (λ z → pr1 (motionRaw (pr1 z) (pr2 z))) (λ z → pr2 (motionRaw (pr1 z) (pr2 z)))
  TurnC.cxturn TurnC.cyturn

motionContinuous : Cont motionDomain realPlaneMetric (λ z → motion (pr1 z) (pr2 z))
motionContinuous = pairContinuous motionDomain realMetric realMetric
  (λ z → pr1 (motionRaw (pr1 z) (pr2 z))) (λ z → neg-ℝ (pr2 (motionRaw (pr1 z) (pr2 z))))
  TurnC.cxturn (negContinuous motionDomain (λ z → pr2 (motionRaw (pr1 z) (pr2 z))) TurnC.cyturn)
