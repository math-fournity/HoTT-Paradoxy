{-# OPTIONS --safe --cubical --guardedness #-}

-- A class-relative completeness certificate for one bounded completion-search
-- language.  Raw programs use an explicit later syntax; normalization maps
-- them into the canonical Delay representation from PartialityRaceTimeout.
-- The proofs cover every Raw n term for a fixed TaskSpec, preserve finite
-- deadline observations and convergence, and show that every reduced
-- candidate occurs in the generated canonical space.

module CandidateCoverage where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Nat.Base using (ℕ ; zero ; suc)
open import Cubical.Data.List.Base using (List ; [] ; _∷_ ; map)
open import Cubical.Data.Empty.Base using (⊥*)
open import PartialityRaceTimeout

------------------------------------------------------------------------
-- 1. A finite-by-bound raw syntax and its complete enumerator
------------------------------------------------------------------------

data Raw : ℕ → Type where
  never : {n : ℕ} → Raw n
  now : {n : ℕ} → Bool → Raw n
  laterR : {n : ℕ} → Raw n → Raw (suc n)

data _∈_ {ℓ : Level} {A : Type ℓ} (x : A) : List A → Type ℓ where
  here : {xs : List A} → x ∈ (x ∷ xs)
  there : {y : A} {xs : List A} → x ∈ xs → x ∈ (y ∷ xs)

map-member : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (f : A → B) {x : A} {xs : List A} → x ∈ xs → f x ∈ map f xs
map-member f here = here
map-member f (there p) = there (map-member f p)

allRaw : (n : ℕ) → List (Raw n)
allRaw zero = never ∷ now false ∷ now true ∷ []
allRaw (suc n) =
  never ∷ now false ∷ now true ∷ map (λ r → laterR r) (allRaw n)

allRaw-complete : {n : ℕ} (r : Raw n) → r ∈ allRaw n
allRaw-complete {zero} never = here
allRaw-complete {zero} (now false) = there here
allRaw-complete {zero} (now true) = there (there here)
allRaw-complete {suc n} never = here
allRaw-complete {suc n} (now false) = there here
allRaw-complete {suc n} (now true) = there (there here)
allRaw-complete {suc n} (laterR r) =
  there (there (there (map-member (λ x → laterR x) (allRaw-complete r))))

------------------------------------------------------------------------
-- 2. Normalization and two independently stated observable semantics
------------------------------------------------------------------------

normalize : {n : ℕ} → Raw n → Delay Bool
normalize never = ω
normalize (now b) = ret zero b
normalize (laterR r) = later (normalize r)

RawConv : {n : ℕ} → Raw n → Bool → Type
RawConv never b = ⊥*
RawConv (now a) b = a ≡ b
RawConv (laterR r) b = RawConv r b

normalization-preserves-convergence : {n : ℕ} (r : Raw n) (b : Bool)
  → RawConv r b ⇔ Conv (normalize r) b
normalization-preserves-convergence never b = ⇔-refl (⊥*)
normalization-preserves-convergence (now a) b = ⇔-refl (a ≡ b)
normalization-preserves-convergence (laterR r) b =
  ⇔-comp (normalization-preserves-convergence r b)
    (⇔-sym (later-conv (normalize r) b))

rawDeadline : {n : ℕ} → ℕ → Raw n → Optional Bool
rawDeadline k never = none
rawDeadline k (now b) = some b
rawDeadline zero (laterR r) = none
rawDeadline (suc k) (laterR r) = rawDeadline k r

deadline-zero-later : (d : Delay Bool) → deadline zero (later d) ≡ none
deadline-zero-later ω = refl
deadline-zero-later (ret n b) = refl

deadline-suc-later : (k : ℕ) (d : Delay Bool)
  → deadline (suc k) (later d) ≡ deadline k d
deadline-suc-later k ω = refl
deadline-suc-later k (ret n b) = refl

normalization-preserves-deadline : {n : ℕ} (k : ℕ) (r : Raw n)
  → rawDeadline k r ≡ deadline k (normalize r)
normalization-preserves-deadline k never = refl
normalization-preserves-deadline k (now b) = refl
normalization-preserves-deadline zero (laterR r) =
  sym (deadline-zero-later (normalize r))
normalization-preserves-deadline (suc k) (laterR r) =
  normalization-preserves-deadline k r
  ∙ sym (deadline-suc-later k (normalize r))

------------------------------------------------------------------------
-- 3. A fixed-task candidate envelope and task-preserving reduction
------------------------------------------------------------------------

record Candidate (n : ℕ) : Type where
  constructor candidate
  field
    rawHorizon : ℕ
    rawExpected : Optional Bool
    rawProgram : Raw n

record CanonicalCandidate : Type where
  constructor canonical
  field
    canonicalHorizon : ℕ
    canonicalExpected : Optional Bool
    canonicalProgram : Delay Bool

open Candidate public
open CanonicalCandidate public

reduceCandidate : {n : ℕ} → Candidate n → CanonicalCandidate
reduceCandidate (candidate k expected r) =
  canonical k expected (normalize r)

rawObservation : {n : ℕ} → Candidate n → Optional Bool
rawObservation (candidate k expected r) = rawDeadline k r

canonicalObservation : CanonicalCandidate → Optional Bool
canonicalObservation (canonical k expected d) = deadline k d

horizon-preserved : {n : ℕ} (c : Candidate n)
  → canonicalHorizon (reduceCandidate c) ≡ rawHorizon c
horizon-preserved (candidate k expected r) = refl

expected-preserved : {n : ℕ} (c : Candidate n)
  → canonicalExpected (reduceCandidate c) ≡ rawExpected c
expected-preserved (candidate k expected r) = refl

observation-preserved : {n : ℕ} (c : Candidate n)
  → rawObservation c ≡ canonicalObservation (reduceCandidate c)
observation-preserved (candidate k expected r) =
  normalization-preserves-deadline k r

------------------------------------------------------------------------
-- 4. Coverage of both the raw and reduced spaces for a fixed TaskSpec
------------------------------------------------------------------------

candidateSpace : (n k : ℕ) → Optional Bool → List (Candidate n)
candidateSpace n k expected =
  map (λ r → candidate k expected r) (allRaw n)

candidate-space-complete : {n : ℕ} (k : ℕ) (expected : Optional Bool)
  (r : Raw n) → candidate k expected r ∈ candidateSpace n k expected
candidate-space-complete k expected r =
  map-member (λ x → candidate k expected x) (allRaw-complete r)

canonicalSpace : (n k : ℕ) → Optional Bool → List CanonicalCandidate
canonicalSpace n k expected = map reduceCandidate (candidateSpace n k expected)

reduced-space-complete : {n : ℕ} (k : ℕ) (expected : Optional Bool)
  (r : Raw n)
  → reduceCandidate (candidate k expected r) ∈ canonicalSpace n k expected
reduced-space-complete k expected r =
  map-member reduceCandidate (candidate-space-complete k expected r)

------------------------------------------------------------------------
-- 5. Fixed controls
------------------------------------------------------------------------

rawNever0 : Raw zero
rawNever0 = never

rawLaterNever1 : Raw (suc zero)
rawLaterNever1 = laterR rawNever0

rawNowTrue0 : Raw zero
rawNowTrue0 = now true

rawLaterTrue1 : Raw (suc zero)
rawLaterTrue1 = laterR rawNowTrue0

later-never-normalizes :
  normalize rawLaterNever1 ≡ normalize (never {n = suc zero})
later-never-normalizes = refl

control-now-member :
  candidate zero (some true) (now true)
    ∈ candidateSpace zero zero (some true)
control-now-member = candidate-space-complete zero (some true) (now true)

control-later-member :
  candidate (suc zero) (some true) rawLaterTrue1
    ∈ candidateSpace (suc zero) (suc zero) (some true)
control-later-member =
  candidate-space-complete (suc zero) (some true) rawLaterTrue1

control-too-early :
  rawObservation (candidate zero none rawLaterTrue1) ≡ none
control-too-early = refl

control-on-time :
  rawObservation (candidate (suc zero) (some true) rawLaterTrue1)
    ≡ some true
control-on-time = refl

control-never :
  canonicalObservation (reduceCandidate (candidate (suc zero) none rawLaterNever1))
    ≡ none
control-never = refl
