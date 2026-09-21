{-# OPTIONS --without-K --exact-split #-}
module hott-z.WeakCoverageMarkov where

-- The Book's forward direction is derived using an actual binary-sequence cut,
-- then connected to the original fixed final curve. No converse/independence claim.
open import hott-z.BinaryWitnessReal
open import hott-z.MarkovBookForms
open import hott-z.RealPrincipleBookScope
open import hott-z.WeakLiftPrinciple
open import hott-z.PunctureApartness
open import hott-z.NativeMotionComplete
open import foundation.universe-levels
open import foundation.booleans
open import foundation.identity-types
open import foundation.negation
open import foundation.empty-types
open import foundation.existential-quantification
open import elementary-number-theory.natural-numbers
open import real-numbers.rational-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import logic.markovs-principle

realApartnessImpliesBookMarkov : RealNonzeroApartness → BookMarkov
realApartnessImpliesBookMarkov principle f nn = apartWitnessGivesSomeTrue f
  (principle (binaryWitnessReal f) (doubleNegWitnessGivesNonzero f nn))

pairApartnessImpliesBookMarkov : RealPairApartness → BookMarkov
pairApartnessImpliesBookMarkov principle =
  realApartnessImpliesBookMarkov (pairToZeroApartness principle)

circleLiftImpliesBookMarkov : Lift → BookMarkov
circleLiftImpliesBookMarkov lift = realApartnessImpliesBookMarkov (liftToRealApartness lift)

fixedWeakCoverageImpliesBookMarkov : WeakFinalCoverage → BookMarkov
fixedWeakCoverageImpliesBookMarkov coverage =
  circleLiftImpliesBookMarkov (weakFinalCoverageGivesLift coverage)

realInverseImpliesBookMarkov : UniformRealInverse → BookMarkov
realInverseImpliesBookMarkov invert =
  realApartnessImpliesBookMarkov (realInverseToApartness invert)

fixedWeakCoverageImpliesLibraryMarkov : WeakFinalCoverage → Markov's-Principle
fixedWeakCoverageImpliesLibraryMarkov coverage =
  bookToLibrary (fixedWeakCoverageImpliesBookMarkov coverage)

-- Explicit conditional only; the premise is not supplied by this module.
noFixedWeakCoverageIfNotMarkov : ¬ BookMarkov → ¬ WeakFinalCoverage
noFixedWeakCoverageIfNotMarkov notMarkov coverage =
  notMarkov (fixedWeakCoverageImpliesBookMarkov coverage)

falseSequenceRealIsZero : binaryWitnessReal (λ _ → false) ＝ zero-ℝ
falseSequenceRealIsZero = noWitnessGivesZero (λ _ → false)
  (elim-exists empty-Prop (λ n ()))

trueSequenceRealIsPositive : le-ℝ zero-ℝ (binaryWitnessReal (λ _ → true))
trueSequenceRealIsPositive = trueIndexGivesPositive (λ _ → true) zero-ℕ refl

falseSequenceHasNoTrue : ¬ (SomeTrue (λ _ → false))
falseSequenceHasNoTrue = zeroGivesNoWitness (λ _ → false) falseSequenceRealIsZero
