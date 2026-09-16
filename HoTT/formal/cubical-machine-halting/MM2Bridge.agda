{-# OPTIONS --cubical --safe --guardedness #-}

module MM2Bridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc ; _+_)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Maybe using (Maybe ; nothing ; just)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.HITs.PropositionalTruncation as PT
open import Agda.Builtin.List using (List ; [] ; _∷_)

open import MachineHalting using
  ( Instr ; inc0 ; inc1 ; dec0 ; dec1 ; halt
  ; Config ; cfg ; pc ; r0 ; r1 ; stepInstr ; isFinal
  )
open import ProgramCode using
  ( ProgramCode ; pcNil ; pcCons ; lookupInstr ; decode
  ; universalStep ; runFor ; finalAt ; CodeHalts
  )
import NatProgramCode as NPC

------------------------------------------------------------------------
-- Functional presentation of the upstream MM2 instruction semantics.
--
-- Program labels start at 1.  Increment falls through to label i+1.
-- Decrement jumps to j on a positive counter and falls through on zero.
-- Label 0 and labels beyond the finite list are stopped configurations.

data MM2Instr : Type where
  incA : MM2Instr
  incB : MM2Instr
  decA : ℕ → MM2Instr
  decB : ℕ → MM2Instr

MM2Program : Type
MM2Program = List MM2Instr

lookup0 : MM2Program → ℕ → Maybe MM2Instr
lookup0 [] offset = nothing
lookup0 (instruction ∷ rest) zero = just instruction
lookup0 (instruction ∷ rest) (suc offset) = lookup0 rest offset

lookupMM2 : MM2Program → ℕ → Maybe MM2Instr
lookupMM2 program zero = nothing
lookupMM2 program (suc offset) = lookup0 program offset

sourceFinalFrom : Maybe MM2Instr → Bool
sourceFinalFrom nothing = true
sourceFinalFrom (just instruction) = false

mm2IsFinal : MM2Program → Config → Bool
mm2IsFinal program state = sourceFinalFrom (lookupMM2 program (pc state))

sourceStepFrom : Maybe MM2Instr → Config → Config
sourceStepFrom nothing state = state
sourceStepFrom (just incA) (cfg label left right) =
  cfg (suc label) (suc left) right
sourceStepFrom (just incB) (cfg label left right) =
  cfg (suc label) left (suc right)
sourceStepFrom (just (decA jump)) (cfg label zero right) =
  cfg (suc label) zero right
sourceStepFrom (just (decA jump)) (cfg label (suc left) right) =
  cfg jump left right
sourceStepFrom (just (decB jump)) (cfg label left zero) =
  cfg (suc label) left zero
sourceStepFrom (just (decB jump)) (cfg label left (suc right)) =
  cfg jump left right

mm2Step : MM2Program → Config → Config
mm2Step program state = sourceStepFrom (lookupMM2 program (pc state)) state

mm2Run : ℕ → MM2Program → Config → Config
mm2Run zero program state = state
mm2Run (suc steps) program state =
  mm2Run steps program (mm2Step program state)

mm2FinalAt : ℕ → MM2Program → Config → Bool
mm2FinalAt steps program state =
  mm2IsFinal program (mm2Run steps program state)

MM2Halts : MM2Program → Config → Type
MM2Halts program state =
  ∥ Σ[ steps ∈ ℕ ] mm2FinalAt steps program state ≡ true ∥₁

------------------------------------------------------------------------
-- Compiler into the project's finite ProgramCode language.

compileInstr : ℕ → MM2Instr → Instr
compileInstr label incA = inc0 (suc label)
compileInstr label incB = inc1 (suc label)
compileInstr label (decA jump) = dec0 (suc label) jump
compileInstr label (decB jump) = dec1 (suc label) jump

compileObserved : ℕ → Maybe MM2Instr → Instr
compileObserved label nothing = halt
compileObserved label (just instruction) = compileInstr label instruction

compileTail : ℕ → MM2Program → ProgramCode
compileTail label [] = pcNil
compileTail label (instruction ∷ rest) =
  pcCons (compileInstr label instruction) (compileTail (suc label) rest)

-- Label 0 is a halt sentinel.  Source label 1 is therefore target table
-- index 1, and a source jump to 0 reaches the same stopped state.
compileMM2 : MM2Program → ProgramCode
compileMM2 program = pcCons halt (compileTail (suc zero) program)

lookup-compileTail :
  (program : MM2Program) (base offset : ℕ) →
  lookupInstr (compileTail base program) offset ≡
  compileObserved (base + offset) (lookup0 program offset)
lookup-compileTail [] base offset = refl
lookup-compileTail (instruction ∷ rest) base zero =
  cong (λ label → compileInstr label instruction)
    (sym (NPC.+-zero base))
lookup-compileTail (instruction ∷ rest) base (suc offset) =
  lookup-compileTail rest (suc base) offset
  ∙ cong
      (λ label → compileObserved label (lookup0 rest offset))
      (sym (NPC.+-suc base offset))

lookup-compileMM2 :
  (program : MM2Program) (label : ℕ) →
  lookupInstr (compileMM2 program) label ≡
  compileObserved label (lookupMM2 program label)
lookup-compileMM2 program zero = refl
lookup-compileMM2 program (suc offset) =
  lookup-compileTail program (suc zero) offset

------------------------------------------------------------------------
-- Pointwise observation and step preservation.

finalInstr : Instr → Bool
finalInstr (inc0 next) = false
finalInstr (inc1 next) = false
finalInstr (dec0 onZero onSuc) = false
finalInstr (dec1 onZero onSuc) = false
finalInstr halt = true

isFinal-as-instruction :
  (program : ℕ → Instr) (state : Config) →
  isFinal program state ≡ finalInstr (program (pc state))
isFinal-as-instruction program state with program (pc state)
... | inc0 next = refl
... | inc1 next = refl
... | dec0 onZero onSuc = refl
... | dec1 onZero onSuc = refl
... | halt = refl

sourceFinal-compileObserved :
  (label : ℕ) (observed : Maybe MM2Instr) →
  sourceFinalFrom observed ≡ finalInstr (compileObserved label observed)
sourceFinal-compileObserved label nothing = refl
sourceFinal-compileObserved label (just incA) = refl
sourceFinal-compileObserved label (just incB) = refl
sourceFinal-compileObserved label (just (decA jump)) = refl
sourceFinal-compileObserved label (just (decB jump)) = refl

compileFinal-agrees :
  (program : MM2Program) (state : Config) →
  mm2IsFinal program state ≡ isFinal (decode (compileMM2 program)) state
compileFinal-agrees program state =
  sourceFinal-compileObserved (pc state) (lookupMM2 program (pc state))
  ∙ cong finalInstr (sym (lookup-compileMM2 program (pc state)))
  ∙ sym (isFinal-as-instruction (decode (compileMM2 program)) state)

sourceStep-compileObserved :
  (observed : Maybe MM2Instr) (state : Config) →
  sourceStepFrom observed state ≡
  stepInstr (compileObserved (pc state) observed) state
sourceStep-compileObserved nothing (cfg label left right) = refl
sourceStep-compileObserved (just incA) (cfg label left right) = refl
sourceStep-compileObserved (just incB) (cfg label left right) = refl
sourceStep-compileObserved (just (decA jump)) (cfg label zero right) = refl
sourceStep-compileObserved (just (decA jump)) (cfg label (suc left) right) = refl
sourceStep-compileObserved (just (decB jump)) (cfg label left zero) = refl
sourceStep-compileObserved (just (decB jump)) (cfg label left (suc right)) = refl

compileStep-agrees :
  (program : MM2Program) (state : Config) →
  mm2Step program state ≡ universalStep (compileMM2 program) state
compileStep-agrees program state =
  sourceStep-compileObserved (lookupMM2 program (pc state)) state
  ∙ cong (λ instruction → stepInstr instruction state)
      (sym (lookup-compileMM2 program (pc state)))

------------------------------------------------------------------------
-- Finite-run and halting preservation.

compileRun-agrees :
  (steps : ℕ) (program : MM2Program) (state : Config) →
  mm2Run steps program state ≡ runFor steps (compileMM2 program) state
compileRun-agrees zero program state = refl
compileRun-agrees (suc steps) program state =
  compileRun-agrees steps program (mm2Step program state)
  ∙ cong (runFor steps (compileMM2 program))
      (compileStep-agrees program state)

compileFinalAt-agrees :
  (steps : ℕ) (program : MM2Program) (state : Config) →
  mm2FinalAt steps program state ≡
  finalAt steps (compileMM2 program) state
compileFinalAt-agrees steps program state =
  cong (mm2IsFinal program) (compileRun-agrees steps program state)
  ∙ compileFinal-agrees program (runFor steps (compileMM2 program) state)

MM2Halts-to-CodeHalts :
  (program : MM2Program) (state : Config) →
  MM2Halts program state → CodeHalts (compileMM2 program) state
MM2Halts-to-CodeHalts program state =
  PT.map λ where
    (steps , sourceHalts) →
      steps , sym (compileFinalAt-agrees steps program state) ∙ sourceHalts

CodeHalts-to-MM2Halts :
  (program : MM2Program) (state : Config) →
  CodeHalts (compileMM2 program) state → MM2Halts program state
CodeHalts-to-MM2Halts program state =
  PT.map λ where
    (steps , targetHalts) →
      steps , compileFinalAt-agrees steps program state ∙ targetHalts

MM2Halts↔CodeHalts :
  (program : MM2Program) (state : Config) →
  (MM2Halts program state → CodeHalts (compileMM2 program) state) ×
  (CodeHalts (compileMM2 program) state → MM2Halts program state)
MM2Halts↔CodeHalts program state =
  MM2Halts-to-CodeHalts program state ,
  CodeHalts-to-MM2Halts program state

------------------------------------------------------------------------
-- Translation controls: fall-through, out-of-range stop and jump-to-zero.

empty-program-final : (left right : ℕ) →
  mm2FinalAt zero [] (cfg (suc zero) left right) ≡ true
empty-program-final left right = refl

single-incA-step : (left right : ℕ) →
  mm2Step (incA ∷ []) (cfg (suc zero) left right) ≡
  cfg (suc (suc zero)) (suc left) right
single-incA-step left right = refl

single-incA-final-after-one : (left right : ℕ) →
  mm2FinalAt (suc zero) (incA ∷ [])
    (cfg (suc zero) left right) ≡ true
single-incA-final-after-one left right = refl

single-decA-zero-fallthrough : (right jump : ℕ) →
  mm2Step (decA jump ∷ []) (cfg (suc zero) zero right) ≡
  cfg (suc (suc zero)) zero right
single-decA-zero-fallthrough right jump = refl

single-decA-positive-jump-zero : (left right : ℕ) →
  mm2Step (decA zero ∷ []) (cfg (suc zero) (suc left) right) ≡
  cfg zero left right
single-decA-positive-jump-zero left right = refl

single-incA-CodeHalts : (left right : ℕ) →
  CodeHalts (compileMM2 (incA ∷ [])) (cfg (suc zero) left right)
single-incA-CodeHalts left right =
  MM2Halts-to-CodeHalts (incA ∷ []) (cfg (suc zero) left right)
    ∣ suc zero , single-incA-final-after-one left right ∣₁
