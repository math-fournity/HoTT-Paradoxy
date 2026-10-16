{-# OPTIONS --without-K --exact-split #-}
module hott-z.WeakLiftPrinciple where

open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.NativeStereographic
open import foundation.universe-levels
open import foundation.identity-types
open import foundation.negated-equality
open import foundation.negation
open import foundation.empty-types
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.logical-equivalences
open import real-numbers.rational-real-numbers
open import real-numbers.zero-real-numbers
open import real-numbers.addition-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.negation-real-numbers
open import real-numbers.multiplication-real-numbers
open import real-numbers.squares-real-numbers
open import real-numbers.similarity-real-numbers
open import real-numbers.nonzero-real-numbers
open import real-numbers.apartness-real-numbers
open import real-numbers.multiplication-nonzero-real-numbers
open import real-numbers.multiplicative-inverses-nonzero-real-numbers

RealNonzeroApartness : UU (lsuc lzero)
RealNonzeroApartness = (r : Real) → r ≠ zero-ℝ → apart-ℝ r zero-ℝ

denominatorZeroIsEast : (p : RealCircle) → denominator p ＝ zero-ℝ → p ＝ east
denominatorZeroIsEast p d0 = firstCoordinateOneIsEast p
  (inv (transpose-eq-right-diff-ℝ one-ℝ (xCoord p) zero-ℝ d0) ∙
   right-unit-law-diff-ℝ one-ℝ)

realApartnessToLift : RealNonzeroApartness → Lift
realApartnessToLift principle p weak = symmetric-apart-ℝ
  (apart-is-nonzero-diff-ℝ one-ℝ (xCoord p)
    (principle (denominator p) (λ d0 → weak (denominatorZeroIsEast p d0))))

-- A reflection inside the original Dedekind point-set circle.
reflectFirst : RealCircle → RealCircle
reflectFirst p =
  (neg-ℝ (xCoord p) , yCoord p) ,
  (ap (_+ℝ square-ℝ (yCoord p)) (square-neg-ℝ (xCoord p)) ∙ pr2 p)

encodeReal : Real → RealCircle
encodeReal r = reflectFirst (paramPoint r)

encodedWeak : (r : Real) → r ≠ zero-ℝ → Weak (encodeReal r)
encodedWeak r nonzero atEast = nonzero
  (inv (forwardParameter r) ∙
   ap (_*ℝ inverseDenominator (paramPoint r) (paramStrong r)) (ap yCoord atEast) ∙
   eq-sim-ℝ (left-zero-law-mul-ℝ (inverseDenominator (paramPoint r) (paramStrong r))))

numeratorSum : (r : Real) → D r +ℝ numeratorX r ＝ two *ℝ square-ℝ r
numeratorSum r =
  associative-add-ℝ (square-ℝ r) one-ℝ (square-ℝ r -ℝ one-ℝ) ∙
  ap (square-ℝ r +ℝ_) (commutative-add-ℝ one-ℝ (square-ℝ r -ℝ one-ℝ)) ∙
  ap (square-ℝ r +ℝ_) (cancelAdd (square-ℝ r) one-ℝ) ∙
  inv (twoTimes (square-ℝ r))

encodedDenominator : (r : Real) →
  denominator (encodeReal r) ＝ (two *ℝ square-ℝ r) *ℝ qInv r
encodedDenominator r =
  ap (one-ℝ +ℝ_) (neg-neg-ℝ (xCoord (paramPoint r))) ∙
  ap (_+ℝ xCoord (paramPoint r)) (inv (Dq r)) ∙
  inv (right-distributive-mul-add-ℝ (D r) (numeratorX r) (qInv r)) ∙
  ap (_*ℝ qInv r) (numeratorSum r)

encodedStrongToApartness : (r : Real) → Strong (encodeReal r) → apart-ℝ r zero-ℝ
encodedStrongToApartness r strong = pr1
  (is-nonzero-factors-is-nonzero-mul-ℝ r r
    (pr2 (is-nonzero-factors-is-nonzero-mul-ℝ two (square-ℝ r)
      (pr1 (is-nonzero-factors-is-nonzero-mul-ℝ (two *ℝ square-ℝ r) (qInv r)
        (tr is-nonzero-ℝ (encodedDenominator r)
          (denominatorNonzero (encodeReal r) strong)))))))

liftToRealApartness : Lift → RealNonzeroApartness
liftToRealApartness lift r nonzero =
  encodedStrongToApartness r (lift (encodeReal r) (encodedWeak r nonzero))

realApartnessIffLift : RealNonzeroApartness ↔ Lift
realApartnessIffLift = realApartnessToLift , liftToRealApartness

encodedZeroDenominator : denominator (encodeReal zero-ℝ) ＝ zero-ℝ
encodedZeroDenominator = encodedDenominator zero-ℝ ∙
  ap (λ s → (two *ℝ s) *ℝ qInv zero-ℝ) square-zero-ℝ ∙
  ap (_*ℝ qInv zero-ℝ) (eq-sim-ℝ (right-zero-law-mul-ℝ two)) ∙
  eq-sim-ℝ (left-zero-law-mul-ℝ (qInv zero-ℝ))

encodedZeroIsEast : encodeReal zero-ℝ ＝ east
encodedZeroIsEast = denominatorZeroIsEast (encodeReal zero-ℝ) encodedZeroDenominator

encodedZeroNotWeak : ¬ (Weak (encodeReal zero-ℝ))
encodedZeroNotWeak w = w encodedZeroIsEast

encodedOneWeak : Weak (encodeReal one-ℝ)
encodedOneWeak = encodedWeak one-ℝ (λ h → neq-zero-one-ℝ (inv h))

RealApartnessStability : UU (lsuc lzero)
RealApartnessStability = (r : Real) → ¬ (¬ (apart-ℝ r zero-ℝ)) → apart-ℝ r zero-ℝ

realApartnessToStability : RealNonzeroApartness → RealApartnessStability
realApartnessToStability principle r nn = principle r
  (λ h → nn (λ a → nonequal-apart-ℝ r zero-ℝ a h))

realStabilityToApartness : RealApartnessStability → RealNonzeroApartness
realStabilityToApartness stable r nonzero = stable r
  (λ na → nonzero (eq-sim-ℝ (sim-nonapart-ℝ r zero-ℝ na)))

realApartnessIffStability : RealNonzeroApartness ↔ RealApartnessStability
realApartnessIffStability = realApartnessToStability , realStabilityToApartness

UniformRealInverse : UU (lsuc lzero)
UniformRealInverse = (r : Real) → r ≠ zero-ℝ → Σ Real (λ u → r *ℝ u ＝ one-ℝ)

realApartnessToInverse : RealNonzeroApartness → UniformRealInverse
realApartnessToInverse principle r nonzero =
  real-inv-nonzero-ℝ (r , principle r nonzero) ,
  eq-sim-ℝ (right-inverse-law-mul-nonzero-ℝ (r , principle r nonzero))

realInverseToApartness : UniformRealInverse → RealNonzeroApartness
realInverseToApartness invert r nonzero =
  is-nonzero-has-right-inverse-mul-ℝ r (pr1 (invert r nonzero))
    (sim-eq-ℝ (pr2 (invert r nonzero)))

realApartnessIffInverse : RealNonzeroApartness ↔ UniformRealInverse
realApartnessIffInverse = realApartnessToInverse , realInverseToApartness

liftIffRealInverse : Lift ↔ UniformRealInverse
liftIffRealInverse =
  (λ lift → realApartnessToInverse (liftToRealApartness lift)) ,
  (λ invert → realApartnessToLift (realInverseToApartness invert))

-- Sufficiency only: no unconditional instance or necessity of LEM is asserted.
excludedMiddleGivesRealApartness : ExcludedMiddle0 → RealNonzeroApartness
excludedMiddleGivesRealApartness em = liftToRealApartness
  (dneGivesLift (excludedMiddleToDNE em))
