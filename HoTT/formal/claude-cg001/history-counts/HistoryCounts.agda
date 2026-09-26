{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The history index is its counts (Claude, session 91a6cdaa, 2026-09-25),
  in reply to Terra's audit 009, O-026.

  proof id : MP-CG001-HISTORY-COUNTS-001
  claims   : CG001-C-54 (full statement in CLAIM.md)

  JFP 2016, section 7.2 (p. 30), says two things in one paragraph about the
  multiset index MS of patch contexts: the replay representation Nat x Nat
  "is in fact isomorphic to MS"; and yet "the elements of MS maintain an
  explicit log of the order in which patches were applied, even though the
  paths in MS identify those logs which differ only by permutation".  This
  file checks both halves on the cubical library's finite multisets, a
  set-truncated quotient higher inductive type with the exchange law comm.

  C-54 (a) FMSet Bool is equivalent to N x N (the counts of true and of
           false), so by univalence FMSet Bool = N x N;
       (b) every function out of FMSet Bool factors through the counts:
           g xs = g (build (counts xs));
       (c) no function FMSet Bool -> Maybe Bool returns the first entry of
           every list (the set-truncated form of C-48 (b));
       (d) the presentations true :: false :: [] and false :: true :: []
           are equal elements (comm) with equal counts (refl); the kernel
           keeps the two presentations apart definitionally (negative
           control), which is where the "explicit log" of JFP lives, and by
           (b) no function can read it.

  Bridge labels (history, log, order) prove no fact about any version
  control system.
-}
module HistoryCounts where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties using (+-zero)
open import Cubical.Data.Bool using (Bool; true; false; _≟_; true≢false; false≢true)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.HITs.FiniteMultiset
  using (FMSet; comm; FMScount; FMScount-≡-lemma-refl; FMScount-≢-lemma)
  renaming ([] to []ₘ; _∷_ to _∷ₘ_)
open import Cubical.HITs.FiniteMultiset.CountExtensionality using (module FMScountExt)
open import Cubical.Relation.Nullary using (¬_)

private
  variable
    ℓ : Level

------------------------------------------------------------------------
-- counts and the canonical presentation

count : Bool → FMSet Bool → ℕ
count = FMScount _≟_

counts : FMSet Bool → ℕ × ℕ
counts xs = count true xs , count false xs

falses : ℕ → FMSet Bool
falses zero    = []ₘ
falses (suc n) = false ∷ₘ falses n

trues : ℕ → FMSet Bool → FMSet Bool
trues zero    ys = ys
trues (suc n) ys = true ∷ₘ trues n ys

-- all trues first, then all falses
build : ℕ × ℕ → FMSet Bool
build (t , f) = trues t (falses f)

countTrueFalses : (f : ℕ) → count true (falses f) ≡ 0
countTrueFalses zero    = refl
countTrueFalses (suc f) = FMScount-≢-lemma _≟_ (falses f) true≢false ∙ countTrueFalses f

countFalseFalses : (f : ℕ) → count false (falses f) ≡ f
countFalseFalses zero    = refl
countFalseFalses (suc f) = FMScount-≡-lemma-refl _≟_ (falses f) ∙ cong suc (countFalseFalses f)

countTrueTrues : (t : ℕ) (ys : FMSet Bool) → count true (trues t ys) ≡ t + count true ys
countTrueTrues zero    ys = refl
countTrueTrues (suc t) ys = FMScount-≡-lemma-refl _≟_ (trues t ys) ∙ cong suc (countTrueTrues t ys)

countFalseTrues : (t : ℕ) (ys : FMSet Bool) → count false (trues t ys) ≡ count false ys
countFalseTrues zero    ys = refl
countFalseTrues (suc t) ys = FMScount-≢-lemma _≟_ (trues t ys) false≢true ∙ countFalseTrues t ys

countsBuild : (tf : ℕ × ℕ) → counts (build tf) ≡ tf
countsBuild (t , f) = ΣPathP
  ( countTrueTrues t (falses f) ∙ cong (t +_) (countTrueFalses f) ∙ +-zero t
  , countFalseTrues t (falses f) ∙ countFalseFalses f )

-- (a) the history index is its counts

buildCounts : (xs : FMSet Bool) → build (counts xs) ≡ xs
buildCounts xs = FMScountExt.Thm _≟_ (build (counts xs)) xs same
  where
  same : (a : Bool) → count a (build (counts xs)) ≡ count a xs
  same true  = cong fst (countsBuild (counts xs))
  same false = cong snd (countsBuild (counts xs))

countsIso : Iso (FMSet Bool) (ℕ × ℕ)
countsIso = iso counts build countsBuild buildCounts

historyIsCounts : FMSet Bool ≃ ℕ × ℕ
historyIsCounts = isoToEquiv countsIso

historyIsCountsPath : FMSet Bool ≡ ℕ × ℕ
historyIsCountsPath = ua historyIsCounts

-- (b) every observation factors through the counts

factorsThroughCounts : {X : Type ℓ} (g : FMSet Bool → X) (xs : FMSet Bool)
  → g xs ≡ g (build (counts xs))
factorsThroughCounts g xs = cong g (sym (buildCounts xs))

------------------------------------------------------------------------
-- (c) no first entry

fromList : List Bool → FMSet Bool
fromList []       = []ₘ
fromList (x ∷ xs) = x ∷ₘ fromList xs

firstOf : List Bool → Maybe Bool
firstOf []      = nothing
firstOf (x ∷ _) = just x

fromJust : Bool → Maybe Bool → Bool
fromJust d nothing  = d
fromJust _ (just x) = x

justInj : {x y : Bool} → just x ≡ just y → x ≡ y
justInj p = cong (fromJust true) p

noFirstEntry : ¬ (Σ[ f ∈ (FMSet Bool → Maybe Bool) ] ((xs : List Bool) → f (fromList xs) ≡ firstOf xs))
noFirstEntry (f , agrees) =
  true≢false (justInj (sym (agrees (true ∷ false ∷ []))
                       ∙ cong f (comm true false []ₘ)
                       ∙ agrees (false ∷ true ∷ [])))

------------------------------------------------------------------------
-- (d) two presentations, one element

trueFirst falseFirst : FMSet Bool
trueFirst  = true ∷ₘ (false ∷ₘ []ₘ)
falseFirst = false ∷ₘ (true ∷ₘ []ₘ)

presentationsAreOneElement : trueFirst ≡ falseFirst
presentationsAreOneElement = comm true false []ₘ

presentationsHaveTheSameCounts : counts trueFirst ≡ counts falseFirst
presentationsHaveTheSameCounts = refl

canonicalPresentation : build (counts falseFirst) ≡ trueFirst
canonicalPresentation = refl
