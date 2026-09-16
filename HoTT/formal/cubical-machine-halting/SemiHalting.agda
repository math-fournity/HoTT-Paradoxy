{-# OPTIONS --cubical --safe --guardedness #-}

module SemiHalting where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty renaming (rec to ⊥rec)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Maybe using (Maybe ; nothing ; just)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sum.Base using (_⊎_ ; inl ; inr)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.HITs.PropositionalTruncation as PT

open import MachineHalting using (Config ; isFinal ; initial)
open import ProgramCode using
  ( ProgramCode ; decode ; universalStep
  ; finalAt ; haltsWithin ; or ; CodeHalts
  ; haltCode ; loopCode ; haltCode-within ; loopCode-never-within
  ; loopCode-not-halts
  )
open import FairEnumeration using
  ( SearchCase ; caseAt ; caseIndex ; searchCase
  ; observeCase ; observeAt ; observeAt-caseIndex
  ; haltCase-visited-true ; loopCase-visited-false
  )

------------------------------------------------------------------------
-- A stage-indexed partial answer.
--
-- Every call at a finite stage is total.  `just tt` is a positive finite
-- halting witness; `nothing` means only that the current finite budget has
-- not yet found one.  It is deliberately not a negative answer about the
-- unbounded execution.

isSome : {A : Type} → Maybe A → Bool
isSome nothing = false
isSome (just value) = true

semiHaltAt : ℕ → ProgramCode → Config → Maybe Unit
semiHaltAt stage program input with haltsWithin stage program input
... | false = nothing
... | true = just tt

isSome-semiHaltAt :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  isSome (semiHaltAt stage program input) ≡
  haltsWithin stage program input
isSome-semiHaltAt stage program input
  with haltsWithin stage program input
... | false = refl
... | true = refl

SemiReturns : ProgramCode → Config → Type
SemiReturns program input =
  ∥ Σ[ stage ∈ ℕ ]
      isSome (semiHaltAt stage program input) ≡ true ∥₁

------------------------------------------------------------------------
-- Relating exact-step witnesses, bounded search and the partial procedure.

or-right-true : (left : Bool) → or left true ≡ true
or-right-true false = refl
or-right-true true = refl

or-left-true : (right : Bool) → or true right ≡ true
or-left-true right = refl

or-true-split : (left right : Bool) →
  or left right ≡ true → (left ≡ true) ⊎ (right ≡ true)
or-true-split false false equality = ⊥rec (false≢true equality)
or-true-split false true equality = inr refl
or-true-split true false equality = inl refl
or-true-split true true equality = inl refl

finalAt-implies-haltsWithin :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  finalAt stage program input ≡ true →
  haltsWithin stage program input ≡ true
finalAt-implies-haltsWithin zero program input exact = exact
finalAt-implies-haltsWithin (suc stage) program input exact =
  cong (or (isFinal (decode program) input))
    (finalAt-implies-haltsWithin
      stage program (universalStep program input) exact)
  ∙ or-right-true (isFinal (decode program) input)

haltsWithin-next-stage :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  haltsWithin stage program input ≡ true →
  haltsWithin (suc stage) program input ≡ true
haltsWithin-next-stage zero program input bounded =
  cong
    (λ current →
      or current
        (haltsWithin zero program (universalStep program input)))
    bounded
  ∙ or-left-true
      (haltsWithin zero program (universalStep program input))
haltsWithin-next-stage (suc stage) program input bounded
  with or-true-split
    (isFinal (decode program) input)
    (haltsWithin stage program (universalStep program input))
    bounded
... | inl current =
  cong
    (λ observed →
      or observed
        (haltsWithin (suc stage) program (universalStep program input)))
    current
  ∙ or-left-true
      (haltsWithin (suc stage) program (universalStep program input))
... | inr later =
  cong (or (isFinal (decode program) input))
    (haltsWithin-next-stage
      stage program (universalStep program input) later)
  ∙ or-right-true (isFinal (decode program) input)

semiHaltAt-persistent :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  isSome (semiHaltAt stage program input) ≡ true →
  isSome (semiHaltAt (suc stage) program input) ≡ true
semiHaltAt-persistent stage program input returned =
  isSome-semiHaltAt (suc stage) program input
  ∙ haltsWithin-next-stage stage program input
      (sym (isSome-semiHaltAt stage program input) ∙ returned)

haltsWithin-implies-CodeHalts :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  haltsWithin stage program input ≡ true →
  CodeHalts program input
haltsWithin-implies-CodeHalts zero program input bounded =
  ∣ zero , bounded ∣₁
haltsWithin-implies-CodeHalts (suc stage) program input bounded
  with or-true-split
    (isFinal (decode program) input)
    (haltsWithin stage program (universalStep program input))
    bounded
... | inl current = ∣ zero , current ∣₁
... | inr later =
  PT.map
    (λ { (witness , exact) → suc witness , exact })
    (haltsWithin-implies-CodeHalts
      stage program (universalStep program input) later)

CodeHalts-to-SemiReturns :
  (program : ProgramCode) (input : Config) →
  CodeHalts program input → SemiReturns program input
CodeHalts-to-SemiReturns program input =
  PT.rec PT.isPropPropTrunc λ where
    (stage , exact) →
      ∣ stage ,
        isSome-semiHaltAt stage program input
        ∙ finalAt-implies-haltsWithin stage program input exact
      ∣₁

SemiReturns-to-CodeHalts :
  (program : ProgramCode) (input : Config) →
  SemiReturns program input → CodeHalts program input
SemiReturns-to-CodeHalts program input =
  PT.rec PT.isPropPropTrunc λ where
    (stage , returned) →
      haltsWithin-implies-CodeHalts stage program input
        (sym (isSome-semiHaltAt stage program input) ∙ returned)

CodeHalts↔SemiReturns :
  (program : ProgramCode) (input : Config) →
  (CodeHalts program input → SemiReturns program input) ×
  (SemiReturns program input → CodeHalts program input)
CodeHalts↔SemiReturns program input =
  CodeHalts-to-SemiReturns program input ,
  SemiReturns-to-CodeHalts program input

------------------------------------------------------------------------
-- A single fair stream of all positive program/input/fuel cases.

enumerateHalting : ℕ → Maybe SearchCase
enumerateHalting index with observeAt index
... | false = nothing
... | true = just (caseAt index)

isSome-enumerateHalting : (index : ℕ) →
  isSome (enumerateHalting index) ≡ observeAt index
isSome-enumerateHalting index with observeAt index
... | false = refl
... | true = refl

enumerated-positive-sound : (index : ℕ) →
  isSome (enumerateHalting index) ≡ true →
  observeCase (caseAt index) ≡ true
enumerated-positive-sound index emitted =
  sym (isSome-enumerateHalting index) ∙ emitted

bounded-case-eventually-emitted :
  (program : ProgramCode) (input : Config) (stage : ℕ) →
  haltsWithin stage program input ≡ true →
  isSome (enumerateHalting (caseIndex program input stage)) ≡ true
bounded-case-eventually-emitted program input stage bounded =
  isSome-enumerateHalting (caseIndex program input stage)
  ∙ observeAt-caseIndex program input stage
  ∙ bounded

canonical-emission-sound :
  (program : ProgramCode) (input : Config) (stage : ℕ) →
  isSome (enumerateHalting (caseIndex program input stage)) ≡ true →
  haltsWithin stage program input ≡ true
canonical-emission-sound program input stage emitted =
  sym (observeAt-caseIndex program input stage)
  ∙ sym (isSome-enumerateHalting (caseIndex program input stage))
  ∙ emitted

------------------------------------------------------------------------
-- Positive and persistent-running controls.

haltCode-returns-at-zero :
  isSome (semiHaltAt zero haltCode initial) ≡ true
haltCode-returns-at-zero = refl

loopCode-never-returns : (stage : ℕ) →
  isSome (semiHaltAt stage loopCode initial) ≡ false
loopCode-never-returns stage =
  isSome-semiHaltAt stage loopCode initial
  ∙ loopCode-never-within stage

loopCode-not-SemiReturns : ¬ SemiReturns loopCode initial
loopCode-not-SemiReturns returns =
  loopCode-not-halts (SemiReturns-to-CodeHalts loopCode initial returns)

haltCode-scheduled-positive : (stage : ℕ) →
  isSome (enumerateHalting (caseIndex haltCode initial stage)) ≡ true
haltCode-scheduled-positive stage =
  isSome-enumerateHalting (caseIndex haltCode initial stage)
  ∙ haltCase-visited-true stage

loopCode-scheduled-negative : (stage : ℕ) →
  isSome (enumerateHalting (caseIndex loopCode initial stage)) ≡ false
loopCode-scheduled-negative stage =
  isSome-enumerateHalting (caseIndex loopCode initial stage)
  ∙ loopCase-visited-false stage
