{-# OPTIONS --without-K --exact-split #-}
module hott-z.MarkovBookForms where

open import foundation.universe-levels
open import foundation.identity-types
open import foundation.action-on-identifications-functions
open import foundation.dependent-pair-types
open import foundation.logical-equivalences
open import foundation.negation
open import foundation.empty-types
open import foundation.propositions
open import foundation.booleans
open import foundation.existential-quantification
open import elementary-number-theory.natural-numbers
open import logic.markovs-principle

SomeTrue SomeFalse : (ℕ → bool) → UU lzero
SomeTrue f = exists ℕ (λ n → is-true-Prop (f n))
SomeFalse f = exists ℕ (λ n → is-false-Prop (f n))

-- HoTT Book ex:reals-apart-neq-MP, with its mere existential unchanged.
BookMarkov : UU lzero
BookMarkov = (f : ℕ → bool) → ¬ (¬ (SomeTrue f)) → SomeTrue f

flip : bool → bool
flip true = false
flip false = true

flipTrueToFalse : (b : bool) → is-true (flip b) → is-false b
flipTrueToFalse true ()
flipTrueToFalse false h = refl

flipFalseToTrue : (b : bool) → is-false (flip b) → is-true b
flipFalseToTrue true h = refl
flipFalseToTrue false ()

trueToFlipFalse : (b : bool) → is-true b → is-false (flip b)
trueToFlipFalse b h = ap flip h

falseToFlipTrue : (b : bool) → is-false b → is-true (flip b)
falseToFlipTrue b h = ap flip h

bookToLibrary : BookMarkov → Markov's-Principle
bookToLibrary book f notAllTrue =
  elim-exists (exists-Prop ℕ (λ n → is-false-Prop (f n)))
    (λ n h → intro-exists n (flipTrueToFalse (f n) h))
    (book (λ n → flip (f n))
      (λ noFlipTrue → notAllTrue (λ n → is-true-is-not-false (f n)
        (λ fnFalse → noFlipTrue (intro-exists n (falseToFlipTrue (f n) fnFalse))))))

libraryToBook : Markov's-Principle → BookMarkov
libraryToBook library f nnSomeTrue =
  elim-exists (exists-Prop ℕ (λ n → is-true-Prop (f n)))
    (λ n h → intro-exists n (flipFalseToTrue (f n) h))
    (library (λ n → flip (f n))
      (λ allFlipTrue → nnSomeTrue
        (elim-exists empty-Prop (λ n fnTrue →
          is-not-true-is-false (f n) (flipTrueToFalse (f n) (allFlipTrue n)) fnTrue))))

bookIffLibraryMarkov : BookMarkov ↔ Markov's-Principle
bookIffLibraryMarkov = bookToLibrary , libraryToBook

-- This proves a translation of principles, not an inhabitant of either principle.
