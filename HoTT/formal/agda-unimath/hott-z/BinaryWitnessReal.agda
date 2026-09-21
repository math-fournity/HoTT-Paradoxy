{-# OPTIONS --without-K --exact-split #-}
module hott-z.BinaryWitnessReal where

-- A genuine small Dedekind real for an arbitrary Boolean sequence.
-- Its positive lower cut detects a mere true index; no Markov/LEM/choice input.
open import hott-z.BinaryWitnessWeights
open import hott-z.MarkovBookForms using (SomeTrue)
open import foundation.universe-levels
open import foundation.booleans
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.coproduct-types
open import foundation.decidable-types
open import foundation.conjunction
open import foundation.disjunction
open import foundation.existential-quantification
open import foundation.logical-equivalences
open import foundation.propositions
open import foundation.subtypes
open import foundation.negation
open import foundation.empty-types
open import foundation.identity-types
open import foundation.transport-along-identifications
open import elementary-number-theory.natural-numbers
open import elementary-number-theory.inequality-natural-numbers
open import elementary-number-theory.strict-inequality-natural-numbers
open import elementary-number-theory.rational-numbers
open import elementary-number-theory.positive-rational-numbers
open import elementary-number-theory.inequality-rational-numbers
open import elementary-number-theory.strict-inequality-rational-numbers
open import real-numbers.dedekind-real-numbers
open import real-numbers.lower-dedekind-real-numbers
open import real-numbers.real-numbers-from-lower-dedekind-real-numbers
open import real-numbers.rational-real-numbers
open import real-numbers.rational-lower-dedekind-real-numbers
open import real-numbers.inequality-lower-dedekind-real-numbers
open import real-numbers.inequality-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.apartness-real-numbers

module _ (f : ℕ → bool) where

  weightedWitness : ℚ → ℕ → Prop lzero
  weightedWitness q n = is-true-Prop (f n) ∧ le-ℚ-Prop q (weight n)

  lowerWitnessCut : subtype lzero ℚ
  lowerWitnessCut q = le-ℚ-Prop q zero-ℚ ∨ ∃ ℕ (weightedWitness q)

  weightedWitnessDecidable : (q : ℚ) (n : ℕ) →
    is-decidable (type-Prop (weightedWitness q n))
  weightedWitnessDecidable q n with f n
  ... | false = inr (λ { (() , h) })
  ... | true with is-decidable-le-ℚ q (weight n)
  ...   | inl h = inl (refl , h)
  ...   | inr nh = inr (λ p → nh (pr2 p))

  lowerWitnessInhabited : exists ℚ lowerWitnessCut
  lowerWitnessInhabited = elim-exists (∃ ℚ lowerWitnessCut)
    (λ q h → intro-exists q (inl-disjunction h)) (exists-lesser-ℚ zero-ℚ)

  lowerWitnessRounded : (q : ℚ) → type-Prop (lowerWitnessCut q) ↔
    exists ℚ (λ r → le-ℚ-Prop q r ∧ lowerWitnessCut r)
  pr1 (lowerWitnessRounded q) =
    elim-disjunction (∃ ℚ (λ r → le-ℚ-Prop q r ∧ lowerWitnessCut r))
      (λ h → intro-exists (mediant-ℚ q zero-ℚ)
        (le-left-mediant-ℚ h , inl-disjunction (le-right-mediant-ℚ h)))
      (elim-exists (∃ ℚ (λ r → le-ℚ-Prop q r ∧ lowerWitnessCut r))
        (λ n (fn , h) → intro-exists (mediant-ℚ q (weight n))
          (le-left-mediant-ℚ h , inr-disjunction
            (intro-exists n (fn , le-right-mediant-ℚ h)))))
  pr2 (lowerWitnessRounded q) = elim-exists (lowerWitnessCut q)
    (λ r (qr , h) → elim-disjunction (lowerWitnessCut q)
      (λ r0 → inl-disjunction (transitive-le-ℚ q r zero-ℚ r0 qr))
      (elim-exists (lowerWitnessCut q)
        (λ n (fn , rn) → inr-disjunction
          (intro-exists n (fn , transitive-le-ℚ q r (weight n) rn qr)))) h)

  binaryLowerReal : lower-ℝ lzero
  binaryLowerReal = lowerWitnessCut , lowerWitnessInhabited , lowerWitnessRounded

  oneNotLowerWitness : ¬ (type-Prop (lowerWitnessCut one-ℚ))
  oneNotLowerWitness = elim-disjunction empty-Prop
    (asymmetric-le-ℚ zero-ℚ one-ℚ le-zero-one-ℚ)
    (elim-exists empty-Prop
      (λ n p → not-leq-le-ℚ one-ℚ (weight n) (pr2 p) (weightAtMostOne n)))

  locatedWitnessNonnegative : (p q : ℚ) → leq-ℚ zero-ℚ p → le-ℚ p q →
    type-disjunction-Prop (lowerWitnessCut p) (¬' (lowerWitnessCut q))
  locatedWitnessNonnegative p q p0 pq with
    smallWeight (q , is-positive-le-zero-ℚ (concatenate-leq-le-ℚ zero-ℚ p q p0 pq))
  ... | N , wNq with finiteSearch (λ n → type-Prop (weightedWitness p n))
    (weightedWitnessDecidable p) N
  ...   | inl (n , nN , h) = inl-disjunction (inr-disjunction (intro-exists n h))
  ...   | inr noPrefix = inr-disjunction
    (elim-disjunction empty-Prop
      (asymmetric-le-ℚ zero-ℚ q (concatenate-leq-le-ℚ zero-ℚ p q p0 pq))
      (elim-exists empty-Prop impossibleWitness))
    where
    impossibleWitness : (n : ℕ) → type-Prop (weightedWitness q n) → empty
    impossibleWitness n (fn , qwn) with decide-le-leq-ℕ n N
    ... | inl nN = noPrefix (n , nN , fn , transitive-le-ℚ p q (weight n) qwn pq)
    ... | inr Nn = asymmetric-le-ℚ q (weight n) qwn
      (concatenate-leq-le-ℚ (weight n) (weight N) q (weightAntitone N n Nn) wNq)

  locatedWitnessCut : (p q : ℚ) → le-ℚ p q →
    type-disjunction-Prop (lowerWitnessCut p) (¬' (lowerWitnessCut q))
  locatedWitnessCut p q pq with decide-le-leq-ℚ p zero-ℚ
  ... | inl p0 = inl-disjunction (inl-disjunction p0)
  ... | inr p0 = locatedWitnessNonnegative p q p0 pq

  binaryWitnessReal : ℝ lzero
  binaryWitnessReal = real-lower-ℝ binaryLowerReal locatedWitnessCut
    (intro-exists one-ℚ oneNotLowerWitness)

  trueIndexGivesPositive : (n : ℕ) → is-true (f n) → le-ℝ zero-ℝ binaryWitnessReal
  trueIndexGivesPositive n fn = le-real-is-in-lower-cut-ℝ binaryWitnessReal
    (inr-disjunction (intro-exists n (fn , weightPositive n)))

  someTrueGivesPositive : SomeTrue f → le-ℝ zero-ℝ binaryWitnessReal
  someTrueGivesPositive = elim-exists (le-prop-ℝ zero-ℝ binaryWitnessReal)
    trueIndexGivesPositive

  positiveGivesSomeTrue : le-ℝ zero-ℝ binaryWitnessReal → SomeTrue f
  positiveGivesSomeTrue positive =
    elim-disjunction (exists-Prop ℕ (λ n → is-true-Prop (f n)))
      (λ h → ex-falso (irreflexive-le-ℚ zero-ℚ h))
      (elim-exists (exists-Prop ℕ (λ n → is-true-Prop (f n)))
        (λ n h → intro-exists n (pr1 h)))
      (is-in-lower-cut-le-real-ℚ binaryWitnessReal positive)

  witnessIffPositive : SomeTrue f ↔ le-ℝ zero-ℝ binaryWitnessReal
  witnessIffPositive = someTrueGivesPositive , positiveGivesSomeTrue

  abstract opaque
    unfolding leq-ℝ real-ℚ

    binaryWitnessNonnegative : leq-ℝ zero-ℝ binaryWitnessReal
    binaryWitnessNonnegative q h = inl-disjunction h

    noWitnessNonpositive : ¬ (SomeTrue f) → leq-ℝ binaryWitnessReal zero-ℝ
    noWitnessNonpositive absent q h = elim-disjunction (le-ℚ-Prop q zero-ℚ)
      (λ q0 → q0)
      (elim-exists (le-ℚ-Prop q zero-ℚ)
        (λ n p → ex-falso (absent (intro-exists n (pr1 p))))) h

  noWitnessGivesZero : ¬ (SomeTrue f) → binaryWitnessReal ＝ zero-ℝ
  noWitnessGivesZero absent = antisymmetric-leq-ℝ binaryWitnessReal zero-ℝ
    (noWitnessNonpositive absent) binaryWitnessNonnegative

  zeroGivesNoWitness : binaryWitnessReal ＝ zero-ℝ → ¬ (SomeTrue f)
  zeroGivesNoWitness equal some = nonequal-apart-ℝ binaryWitnessReal zero-ℝ
    (apart-le-ℝ' (someTrueGivesPositive some)) equal

  zeroIffNoWitness : (binaryWitnessReal ＝ zero-ℝ) ↔ ¬ (SomeTrue f)
  zeroIffNoWitness = zeroGivesNoWitness , noWitnessGivesZero

  doubleNegWitnessGivesNonzero : ¬ (¬ (SomeTrue f)) → ¬ (binaryWitnessReal ＝ zero-ℝ)
  doubleNegWitnessGivesNonzero nn equal = nn
    (λ some → nonequal-apart-ℝ binaryWitnessReal zero-ℝ
      (apart-le-ℝ' (someTrueGivesPositive some)) equal)

  apartWitnessGivesSomeTrue : apart-ℝ binaryWitnessReal zero-ℝ → SomeTrue f
  apartWitnessGivesSomeTrue =
    elim-disjunction (exists-Prop ℕ (λ n → is-true-Prop (f n)))
      (λ negative → ex-falso (not-le-leq-ℝ zero-ℝ binaryWitnessReal
        binaryWitnessNonnegative negative))
      positiveGivesSomeTrue
