{-# OPTIONS --cubical --safe --guardedness #-}

module ProgramCode where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (isProp⊥)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.HITs.PropositionalTruncation as PT

open import MachineHalting
  using
    ( Instr ; inc0 ; inc1 ; dec0 ; dec1 ; halt
    ; Program ; Config ; cfg ; step ; iterate ; isFinal ; initial
    )

-- A finite instruction table.  A label outside the table decodes to halt,
-- so decoding is a total map into MachineHalting.Program.

data ProgramCode : Type where
  pcNil  : ProgramCode
  pcCons : Instr → ProgramCode → ProgramCode

lookupInstr : ProgramCode → ℕ → Instr
lookupInstr pcNil label = halt
lookupInstr (pcCons instruction rest) zero = instruction
lookupInstr (pcCons instruction rest) (suc label) = lookupInstr rest label

decode : ProgramCode → Program
decode code label = lookupInstr code label

decode-head : (instruction : Instr) (rest : ProgramCode) →
  decode (pcCons instruction rest) zero ≡ instruction
decode-head instruction rest = refl

decode-tail : (instruction : Instr) (rest : ProgramCode) (label : ℕ) →
  decode (pcCons instruction rest) (suc label) ≡ decode rest label
decode-tail instruction rest label = refl

decode-outside-empty : (label : ℕ) → decode pcNil label ≡ halt
decode-outside-empty label = refl

-- The universal evaluator is total because fuel is structurally decreasing.
-- It interprets any finite ProgramCode for exactly the requested number of
-- transitions.

universalStep : ProgramCode → Config → Config
universalStep code state = step (decode code) state

runFor : ℕ → ProgramCode → Config → Config
runFor zero code state = state
runFor (suc fuel) code state = runFor fuel code (universalStep code state)

runFor-agrees : (fuel : ℕ) (code : ProgramCode) (state : Config) →
  runFor fuel code state ≡ iterate fuel (step (decode code)) state
runFor-agrees zero code state = refl
runFor-agrees (suc fuel) code state =
  runFor-agrees fuel code (universalStep code state)

finalAt : ℕ → ProgramCode → Config → Bool
finalAt fuel code state = isFinal (decode code) (runFor fuel code state)

finalAt-agrees : (fuel : ℕ) (code : ProgramCode) (state : Config) →
  finalAt fuel code state ≡
  isFinal (decode code) (iterate fuel (step (decode code)) state)
finalAt-agrees fuel code state =
  cong (isFinal (decode code)) (runFor-agrees fuel code state)

-- `haltsWithin fuel` checks the initial observation and at most `fuel`
-- transitions.  It is a total bounded observation, not a total halting
-- decider for unbounded executions.

or : Bool → Bool → Bool
or false right = right
or true right = true

haltsWithin : ℕ → ProgramCode → Config → Bool
haltsWithin zero code state = isFinal (decode code) state
haltsWithin (suc fuel) code state =
  or (isFinal (decode code) state)
     (haltsWithin fuel code (universalStep code state))

haltCode : ProgramCode
haltCode = pcCons halt pcNil

loopCode : ProgramCode
loopCode = pcCons (inc0 zero) pcNil

haltCode-within : (fuel : ℕ) → haltsWithin fuel haltCode initial ≡ true
haltCode-within zero = refl
haltCode-within (suc fuel) = refl

loopCode-not-final-from : (fuel x y : ℕ) →
  finalAt fuel loopCode (cfg zero x y) ≡ false
loopCode-not-final-from zero x y = refl
loopCode-not-final-from (suc fuel) x y =
  loopCode-not-final-from fuel (suc x) y

loopCode-not-final : (fuel : ℕ) → finalAt fuel loopCode initial ≡ false
loopCode-not-final fuel = loopCode-not-final-from fuel zero zero

loopCode-never-within-from : (fuel x y : ℕ) →
  haltsWithin fuel loopCode (cfg zero x y) ≡ false
loopCode-never-within-from zero x y = refl
loopCode-never-within-from (suc fuel) x y =
  loopCode-never-within-from fuel (suc x) y

loopCode-never-within : (fuel : ℕ) →
  haltsWithin fuel loopCode initial ≡ false
loopCode-never-within fuel = loopCode-never-within-from fuel zero zero

CodeHalts : ProgramCode → Config → Type
CodeHalts code state =
  ∥ Σ[ fuel ∈ ℕ ] finalAt fuel code state ≡ true ∥₁

loopCode-not-halts : ¬ CodeHalts loopCode initial
loopCode-not-halts = PT.rec isProp⊥ λ where
  (fuel , reaches-final) →
    false≢true (sym (loopCode-not-final fuel) ∙ reaches-final)
