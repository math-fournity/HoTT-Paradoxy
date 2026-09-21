{-# OPTIONS --without-K --exact-split #-}
module hott-z.MarkovRationalBounds where

-- Markov is applied to a concrete Boolean test on supplied rational bounds.
-- Existence of an entire bounds sequence is kept separate from pointwise location.
open import hott-z.BinaryWitnessWeights
open import hott-z.MarkovBookForms
open import hott-z.NativeRealCircleQualification using (Real)
open import foundation.universe-levels
open import foundation.booleans
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.coproduct-types
open import foundation.decidable-types
open import foundation.disjunction
open import foundation.existential-quantification
open import foundation.logical-equivalences
open import foundation.propositions
open import foundation.propositional-truncations
open import foundation.subtypes
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import foundation.negation
open import foundation.negated-equality
open import foundation.empty-types
open import elementary-number-theory.natural-numbers
open import elementary-number-theory.rational-numbers
open import elementary-number-theory.positive-rational-numbers
open import elementary-number-theory.unit-fractions-rational-numbers
open import elementary-number-theory.addition-positive-rational-numbers
open import elementary-number-theory.addition-rational-numbers
open import elementary-number-theory.difference-rational-numbers
open import elementary-number-theory.strict-inequality-rational-numbers
open import real-numbers.dedekind-real-numbers
open import real-numbers.arithmetically-located-dedekind-cuts
open import real-numbers.rational-real-numbers
open import real-numbers.rational-lower-dedekind-real-numbers
open import real-numbers.rational-upper-dedekind-real-numbers
open import real-numbers.strict-inequality-real-numbers
open import real-numbers.apartness-real-numbers
open import real-numbers.similarity-real-numbers

BoundAt : Real → ℕ → UU lzero
BoundAt x n = type-subtype (close-bounds-ℝ x (positive-reciprocal-rational-succ-ℕ n))

RationalBoundSequence : Real → UU lzero
RationalBoundSequence x = (n : ℕ) → BoundAt x n

decisionBool : {A : UU lzero} → is-decidable A → bool
decisionBool (inl _) = true
decisionBool (inr _) = false

decisionTrue : {A : UU lzero} (d : is-decidable A) → is-true (decisionBool d) → A
decisionTrue (inl a) h = a
decisionTrue (inr na) ()

trueDecision : {A : UU lzero} (d : is-decidable A) → A → is-true (decisionBool d)
trueDecision (inl a) h = refl
trueDecision (inr na) h = ex-falso (na h)

module _ (x : Real) (bounds : RationalBoundSequence x) where

  lowerAt upperAt : ℕ → ℚ
  lowerAt n = pr1 (pr1 (bounds n))
  upperAt n = pr2 (pr1 (bounds n))

  narrowAt : (n : ℕ) → le-ℚ (upperAt n) (lowerAt n +ℚ weight n)
  narrowAt n = pr1 (pr2 (bounds n))

  lowerIn : (n : ℕ) → is-in-lower-cut-ℝ x (lowerAt n)
  lowerIn n = pr1 (pr2 (pr2 (bounds n)))

  upperIn : (n : ℕ) → is-in-upper-cut-ℝ x (upperAt n)
  upperIn n = pr2 (pr2 (pr2 (bounds n)))

  hitProp : ℕ → Prop lzero
  hitProp n = le-ℚ-Prop zero-ℚ (lowerAt n) ∨ le-ℚ-Prop (upperAt n) zero-ℚ

  hitDecision : (n : ℕ) → is-decidable (type-Prop (hitProp n))
  hitDecision n with is-decidable-le-ℚ zero-ℚ (lowerAt n)
  ... | inl p = inl (inl-disjunction p)
  ... | inr np with is-decidable-le-ℚ (upperAt n) zero-ℚ
  ...   | inl p = inl (inr-disjunction p)
  ...   | inr nq = inr (elim-disjunction empty-Prop np nq)

  hitBool : ℕ → bool
  hitBool n = decisionBool (hitDecision n)

  Detection : UU lzero
  Detection = SomeTrue hitBool

  detectionProp : Prop lzero
  detectionProp = exists-Prop ℕ (λ n → is-true-Prop (hitBool n))

  introduceHit : (n : ℕ) → type-Prop (hitProp n) → Detection
  introduceHit n h = intro-exists n (trueDecision (hitDecision n) h)

  hitGivesApartness : (n : ℕ) → type-Prop (hitProp n) → apart-ℝ x zero-ℝ
  hitGivesApartness n = elim-disjunction (apart-prop-ℝ x zero-ℝ)
    (λ pos → apart-le-ℝ' (le-real-is-in-lower-cut-ℝ x
      (le-lower-cut-ℝ x pos (lowerIn n))))
    (λ neg → apart-le-ℝ (le-real-is-in-upper-cut-ℝ x
      (le-upper-cut-ℝ x neg (upperIn n))))

  detectionGivesApartness : Detection → apart-ℝ x zero-ℝ
  detectionGivesApartness = elim-exists (apart-prop-ℝ x zero-ℝ)
    (λ n h → hitGivesApartness n (decisionTrue (hitDecision n) h))

  positiveRationalDetects : (r : ℚ) → le-ℚ zero-ℚ r → is-in-lower-cut-ℝ x r → Detection
  positiveRationalDetects r positive rx with smallWeight (r , is-positive-le-zero-ℚ positive)
  ... | n , wn = introduceHit n (inl-disjunction lowerPositive)
    where
    rBelowSum : le-ℚ r (lowerAt n +ℚ weight n)
    rBelowSum = transitive-le-ℚ r (upperAt n) (lowerAt n +ℚ weight n)
      (narrowAt n) (le-lower-upper-cut-ℝ x rx (upperIn n))

    lowerPositive : le-ℚ zero-ℚ (lowerAt n)
    lowerPositive = transitive-le-ℚ zero-ℚ (r -ℚ weight n) (lowerAt n)
      (le-transpose-right-add-ℚ r (lowerAt n) (weight n) rBelowSum)
      (le-zero-is-positive-ℚ (is-positive-diff-le-ℚ wn))

  negativeRationalDetects : (r : ℚ) → le-ℚ r zero-ℚ → is-in-upper-cut-ℝ x r → Detection
  negativeRationalDetects r negative xr with smallWeight (positive-diff-le-ℚ negative)
  ... | n , wn = introduceHit n (inr-disjunction upperNegative)
    where
    shiftedNegative : le-ℚ (r +ℚ weight n) zero-ℚ
    shiftedNegative = tr (λ q → le-ℚ q zero-ℚ) (commutative-add-ℚ (weight n) r)
      (le-transpose-right-diff-ℚ (weight n) zero-ℚ r wn)

    upperNegative : le-ℚ (upperAt n) zero-ℚ
    upperNegative = transitive-le-ℚ (upperAt n) (lowerAt n +ℚ weight n) zero-ℚ
      (transitive-le-ℚ (lowerAt n +ℚ weight n) (r +ℚ weight n) zero-ℚ
        shiftedNegative (preserves-le-left-add-ℚ (weight n) (lowerAt n) r
          (le-lower-upper-cut-ℝ x (lowerIn n) xr))) (narrowAt n)

  abstract opaque
    unfolding le-ℝ real-ℚ

    positiveDetects : le-ℝ zero-ℝ x → Detection
    positiveDetects = elim-exists detectionProp (λ r (positive , rx) →
      positiveRationalDetects r positive rx)

    negativeDetects : le-ℝ x zero-ℝ → Detection
    negativeDetects = elim-exists detectionProp (λ r (xr , negative) →
      negativeRationalDetects r negative xr)

  apartnessGivesDetection : apart-ℝ x zero-ℝ → Detection
  apartnessGivesDetection = elim-disjunction detectionProp negativeDetects positiveDetects

  apartnessIffDetection : apart-ℝ x zero-ℝ ↔ Detection
  apartnessIffDetection = apartnessGivesDetection , detectionGivesApartness

  nonzeroGivesDoubleNegDetection : x ≠ zero-ℝ → ¬ (¬ Detection)
  nonzeroGivesDoubleNegDetection nonzero absent = nonzero
    (eq-sim-ℝ (sim-nonapart-ℝ x zero-ℝ (λ apart → absent (apartnessGivesDetection apart))))

  markovWithBoundsGivesApartness : BookMarkov → x ≠ zero-ℝ → apart-ℝ x zero-ℝ
  markovWithBoundsGivesApartness markov nonzero = detectionGivesApartness
    (markov hitBool (nonzeroGivesDoubleNegDetection nonzero))

-- Actual nonempty supplied-data controls on rational reals.
opaque
  unfolding real-ℚ

  rationalCloseBounds : (q : ℚ) (ε : ℚ⁺) → type-subtype (close-bounds-ℝ (real-ℚ q) ε)
  rationalCloseBounds q ε with bound-double-le-ℚ⁺ ε
  ... | d⁺@(d , _) , ddε = (q -ℚ d , q +ℚ d) , width ,
    le-diff-rational-ℚ⁺ q d⁺ , le-right-add-rational-ℚ⁺ q d⁺
    where
    width : le-ℚ (q +ℚ d) ((q -ℚ d) +ℚ rational-ℚ⁺ ε)
    width = tr (λ v → le-ℚ v ((q -ℚ d) +ℚ rational-ℚ⁺ ε))
      (inv (associative-add-ℚ (q -ℚ d) d d) ∙ ap (_+ℚ d) (is-section-diff-ℚ d q))
      (preserves-le-right-add-ℚ (q -ℚ d) (d +ℚ d) (rational-ℚ⁺ ε) ddε)

rationalBoundSequence : (q : ℚ) → RationalBoundSequence (real-ℚ q)
rationalBoundSequence q n = rationalCloseBounds q (positive-reciprocal-rational-succ-ℕ n)

zeroNoDetection : ¬ (Detection zero-ℝ (rationalBoundSequence zero-ℚ))
zeroNoDetection h = antireflexive-apart-ℝ zero-ℝ
  (detectionGivesApartness zero-ℝ (rationalBoundSequence zero-ℚ) h)

oneDetection : Detection one-ℝ (rationalBoundSequence one-ℚ)
oneDetection = apartnessGivesDetection one-ℝ (rationalBoundSequence one-ℚ)
  (apart-le-ℝ' le-zero-one-ℝ)
