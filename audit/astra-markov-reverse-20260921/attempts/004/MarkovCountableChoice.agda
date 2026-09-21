{-# OPTIONS --without-K --exact-split #-}
module hott-z.MarkovCountableChoice where

-- The all-Dedekind converse has an explicit data-supply/choice hypothesis.
-- The binary-encoded family converse below needs no countable-choice input.
open import hott-z.MarkovRationalBounds
open import hott-z.BinaryWitnessReal
open import hott-z.MarkovBookForms
open import hott-z.WeakCoverageMarkov
open import hott-z.WeakLiftPrinciple
open import hott-z.PunctureApartness
open import hott-z.NativeMotionComplete
open import hott-z.NativeRealCircleQualification using (Real)
open import foundation.universe-levels
open import foundation.booleans
open import foundation.dependent-pair-types
open import foundation.logical-equivalences
open import foundation.propositions
open import foundation.propositional-truncations
open import foundation.identity-types
open import foundation.negation
open import foundation.negated-equality
open import foundation.sets
open import foundation.axiom-of-countable-choice
open import elementary-number-theory.natural-numbers
open import elementary-number-theory.rational-numbers
open import elementary-number-theory.unit-fractions-rational-numbers
open import real-numbers.arithmetically-located-dedekind-cuts
open import real-numbers.rational-real-numbers
open import real-numbers.apartness-real-numbers

MereBoundSequence : Real → UU lzero
MereBoundSequence x = type-trunc-Prop (RationalBoundSequence x)

AllMereBoundSequences : UU (lsuc lzero)
AllMereBoundSequences = (x : Real) → MereBoundSequence x

boundAtSet : (x : Real) → ℕ → foundation.sets.Set lzero
boundAtSet x n = Σ-Set (product-Set ℚ-Set ℚ-Set)
  (λ pair → set-Prop (close-bounds-ℝ x (positive-reciprocal-rational-succ-ℕ n) pair))

pointwiseMereBounds : (x : Real) (n : ℕ) → type-trunc-Prop (BoundAt x n)
pointwiseMereBounds x n =
  is-arithmetically-located-ℝ x (positive-reciprocal-rational-succ-ℕ n)

countableChoiceGivesMereBounds : level-ACℕ lzero → AllMereBoundSequences
countableChoiceGivesMereBounds ac x = ac (boundAtSet x) (pointwiseMereBounds x)

markovWithMereBoundsGivesApartness :
  BookMarkov → (x : Real) → MereBoundSequence x → x ≠ zero-ℝ → apart-ℝ x zero-ℝ
markovWithMereBoundsGivesApartness markov x supplied nonzero =
  rec-trunc-Prop (apart-prop-ℝ x zero-ℝ)
    (λ bounds → markovWithBoundsGivesApartness x bounds markov nonzero) supplied

suppliedBoundsMarkovGivesRNZA : AllMereBoundSequences → BookMarkov → RealNonzeroApartness
suppliedBoundsMarkovGivesRNZA supplied markov x =
  markovWithMereBoundsGivesApartness markov x (supplied x)

choiceMarkovGivesRNZA : level-ACℕ lzero → BookMarkov → RealNonzeroApartness
choiceMarkovGivesRNZA ac = suppliedBoundsMarkovGivesRNZA (countableChoiceGivesMereBounds ac)

rnzaIffMarkovWithChoice : level-ACℕ lzero → (RealNonzeroApartness ↔ BookMarkov)
rnzaIffMarkovWithChoice ac = realApartnessImpliesBookMarkov , choiceMarkovGivesRNZA ac

choiceMarkovGivesCircleLift : level-ACℕ lzero → BookMarkov → Lift
choiceMarkovGivesCircleLift ac markov = realApartnessToLift (choiceMarkovGivesRNZA ac markov)

choiceMarkovGivesWeakCoverage : level-ACℕ lzero → BookMarkov → WeakFinalCoverage
choiceMarkovGivesWeakCoverage ac markov =
  liftGivesWeakFinalCoverage (choiceMarkovGivesCircleLift ac markov)

choiceMarkovGivesChosenWeakOutput : level-ACℕ lzero → BookMarkov → ChosenWeakFinalOutput
choiceMarkovGivesChosenWeakOutput ac markov =
  liftGivesChosenWeakFinalOutput (choiceMarkovGivesCircleLift ac markov)

weakCoverageIffMarkovWithChoice : level-ACℕ lzero → (WeakFinalCoverage ↔ BookMarkov)
weakCoverageIffMarkovWithChoice ac =
  fixedWeakCoverageImpliesBookMarkov , choiceMarkovGivesWeakCoverage ac

inverseIffMarkovWithChoice : level-ACℕ lzero → (UniformRealInverse ↔ BookMarkov)
inverseIffMarkovWithChoice ac = realInverseImpliesBookMarkov ,
  (λ markov → realApartnessToInverse (choiceMarkovGivesRNZA ac markov))

-- A genuine specified subfamily: every Boolean sequence has the actual C321 real.
BinaryRealApartness : UU (lsuc lzero)
BinaryRealApartness = (f : ℕ → bool) →
  binaryWitnessReal f ≠ zero-ℝ → apart-ℝ (binaryWitnessReal f) zero-ℝ

markovGivesBinaryApartness : BookMarkov → BinaryRealApartness
markovGivesBinaryApartness markov f nonzero = apart-le-ℝ'
  (someTrueGivesPositive f (markov f (λ absent → nonzero (noWitnessGivesZero f absent))))

binaryApartnessGivesMarkov : BinaryRealApartness → BookMarkov
binaryApartnessGivesMarkov principle f nn = apartWitnessGivesSomeTrue f
  (principle f (doubleNegWitnessGivesNonzero f nn))

binaryApartnessIffMarkov : BinaryRealApartness ↔ BookMarkov
binaryApartnessIffMarkov = binaryApartnessGivesMarkov , markovGivesBinaryApartness

-- No inhabitant of level-ACℕ, BookMarkov, RNZA or arbitrary Weak coverage is supplied.
-- No necessity/independence of choice and no unconditional all-Dedekind converse.
