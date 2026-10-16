{-# OPTIONS --without-K --exact-split #-}
module hott-z.RealPrincipleBookScope where

open import hott-z.NativeRealCircleQualification
open import hott-z.PunctureApartness
open import hott-z.WeakLiftPrinciple
open import hott-z.MarkovBookForms public
open import foundation.universe-levels
open import foundation.identity-types
open import foundation.negated-equality
open import foundation.dependent-pair-types
open import foundation.logical-equivalences
open import real-numbers.rational-real-numbers
open import real-numbers.difference-real-numbers
open import real-numbers.apartness-real-numbers

RealPairApartness : UU (lsuc lzero)
RealPairApartness = (x y : Real) → x ≠ y → apart-ℝ x y

differenceZeroImpliesEqual : (x y : Real) → x -ℝ y ＝ zero-ℝ → x ＝ y
differenceZeroImpliesEqual x y h =
  inv (right-unit-law-diff-ℝ x) ∙ transpose-eq-right-diff-ℝ x y zero-ℝ h

zeroToPairApartness : RealNonzeroApartness → RealPairApartness
zeroToPairApartness principle x y different =
  apart-is-nonzero-diff-ℝ x y
    (principle (x -ℝ y) (λ h → different (differenceZeroImpliesEqual x y h)))

pairToZeroApartness : RealPairApartness → RealNonzeroApartness
pairToZeroApartness principle r = principle r zero-ℝ

zeroIffPairApartness : RealNonzeroApartness ↔ RealPairApartness
zeroIffPairApartness = zeroToPairApartness , pairToZeroApartness

pairPrincipleIffCircleLift : RealPairApartness ↔ Lift
pairPrincipleIffCircleLift =
  (λ principle → realApartnessToLift (pairToZeroApartness principle)) ,
  (λ lift → zeroToPairApartness (liftToRealApartness lift))

pairPrincipleIffRealInverse : RealPairApartness ↔ UniformRealInverse
pairPrincipleIffRealInverse =
  (λ principle → realApartnessToInverse (pairToZeroApartness principle)) ,
  (λ invert → zeroToPairApartness (realInverseToApartness invert))

-- No real-principle-to-Markov or Markov-to-real-principle bridge is asserted here.
