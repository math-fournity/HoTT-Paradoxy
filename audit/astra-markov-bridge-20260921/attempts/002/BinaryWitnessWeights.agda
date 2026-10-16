{-# OPTIONS --without-K --exact-split #-}
module hott-z.BinaryWitnessWeights where

-- Positive rational weights and finite search for an actual binary-sequence cut.
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types
open import foundation.coproduct-types
open import foundation.decidable-types
open import foundation.negation
open import foundation.empty-types
open import foundation.unit-type
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.transport-along-identifications
open import elementary-number-theory.natural-numbers
open import elementary-number-theory.nonzero-natural-numbers
open import elementary-number-theory.inequality-natural-numbers
open import elementary-number-theory.strict-inequality-natural-numbers
open import elementary-number-theory.rational-numbers
open import elementary-number-theory.positive-rational-numbers
open import elementary-number-theory.unit-fractions-rational-numbers
open import elementary-number-theory.inequality-rational-numbers
open import elementary-number-theory.strict-inequality-rational-numbers
open import elementary-number-theory.multiplicative-group-of-positive-rational-numbers

weight : ℕ → ℚ
weight = reciprocal-rational-succ-ℕ

weightPositive : (n : ℕ) → le-ℚ zero-ℚ (weight n)
weightPositive n = le-zero-is-positive-ℚ
  (is-positive-rational-ℚ⁺ (positive-reciprocal-rational-succ-ℕ n))

weightAntitone : (m n : ℕ) → leq-ℕ m n → leq-ℚ (weight n) (weight m)
weightAntitone m n mn = leq-reciprocal-rational-ℕ⁺
  (succ-nonzero-ℕ' m) (succ-nonzero-ℕ' n) mn

weightZero : weight zero-ℕ ＝ one-ℚ
weightZero = ap rational-ℚ⁺ inv-one-ℚ⁺

weightAtMostOne : (n : ℕ) → leq-ℚ (weight n) one-ℚ
weightAtMostOne n = tr (leq-ℚ (weight n)) weightZero (weightAntitone zero-ℕ n star)

smallWeight : (q : ℚ⁺) → Σ ℕ (λ n → le-ℚ (weight n) (rational-ℚ⁺ q))
smallWeight q with smaller-reciprocal-ℚ⁺ q
... | n , h = pr1 n , concatenate-leq-le-ℚ _ _ _
  (leq-reciprocal-rational-ℕ⁺ n (succ-nonzero-ℕ' (pr1 n)) (succ-leq-ℕ (pr1 n))) h

BelowWitness : {l : Level} → (ℕ → UU l) → ℕ → UU l
BelowWitness P n = Σ ℕ (λ k → le-ℕ k n × P k)

finiteSearch : {l : Level} (P : ℕ → UU l) →
  ((k : ℕ) → is-decidable (P k)) → (n : ℕ) → is-decidable (BelowWitness P n)
finiteSearch P d zero-ℕ = inr (λ { (k , () , p) })
finiteSearch P d (succ-ℕ n) with d zero-ℕ
... | inl p = inl (zero-ℕ , star , p)
... | inr np with finiteSearch (λ k → P (succ-ℕ k)) (λ k → d (succ-ℕ k)) n
...   | inl (k , h , p) = inl (succ-ℕ k , h , p)
...   | inr noTail = inr (λ { (zero-ℕ , h , p) → np p
                            ; (succ-ℕ k , h , p) → noTail (k , h , p) })
