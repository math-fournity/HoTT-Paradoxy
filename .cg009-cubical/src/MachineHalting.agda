{-# OPTIONS --cubical --safe --guardedness #-}

module MachineHalting where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (isProp⊥)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.HITs.PropositionalTruncation as PT

-- A deterministic two-counter instruction language.  Programs are total
-- functions from labels to instructions, so one transition is computable.

data Instr : Type where
  inc0 : ℕ → Instr
  inc1 : ℕ → Instr
  dec0 : ℕ → ℕ → Instr
  dec1 : ℕ → ℕ → Instr
  halt : Instr

Program : Type
Program = ℕ → Instr

record Config : Type where
  constructor cfg
  field
    pc : ℕ
    r0 : ℕ
    r1 : ℕ

open Config public

stepInstr : Instr → Config → Config
stepInstr (inc0 next) (cfg label x y) = cfg next (suc x) y
stepInstr (inc1 next) (cfg label x y) = cfg next x (suc y)
stepInstr (dec0 onZero onSuc) (cfg label zero y) = cfg onZero zero y
stepInstr (dec0 onZero onSuc) (cfg label (suc x) y) = cfg onSuc x y
stepInstr (dec1 onZero onSuc) (cfg label x zero) = cfg onZero x zero
stepInstr (dec1 onZero onSuc) (cfg label x (suc y)) = cfg onSuc x y
stepInstr halt (cfg label x y) = cfg label x y

step : Program → Config → Config
step P c = stepInstr (P (pc c)) c

iterate : ℕ → (Config → Config) → Config → Config
iterate zero f c = c
iterate (suc n) f c = iterate n f (f c)

isFinal : Program → Config → Bool
isFinal P c with P (pc c)
... | halt = true
... | inc0 _ = false
... | inc1 _ = false
... | dec0 _ _ = false
... | dec1 _ _ = false

-- Halting is mere existence of a finite step index.  Propositional
-- truncation removes any significance from choosing one witness over another.

Halts : Program → Config → Type
Halts P initial = ∥ Σ[ n ∈ ℕ ] isFinal P (iterate n (step P) initial) ≡ true ∥₁

DoesNotHaltWithin : ℕ → Program → Config → Type
DoesNotHaltWithin n P initial =
  isFinal P (iterate n (step P) initial) ≡ false

Diverges : Program → Config → Type
Diverges P initial = (n : ℕ) → DoesNotHaltWithin n P initial

initial : Config
initial = cfg zero zero zero

-- Positive control: this program is already at a halting instruction.

haltProgram : Program
haltProgram _ = halt

halt-now : Halts haltProgram initial
halt-now = ∣ zero , refl ∣₁

-- Concrete divergence witness: every label increments counter zero and
-- returns to label zero.  Hence the finality test is false at every finite
-- observation index.

loopProgram : Program
loopProgram _ = inc0 zero

loop-diverges : Diverges loopProgram initial
loop-diverges n = refl

-- The step-indexed invariant eliminates any purported truncated finite
-- halting witness for the concrete loop program.

loop-not-halts : ¬ Halts loopProgram initial
loop-not-halts = PT.rec isProp⊥ λ where
  (n , reaches-final) →
    false≢true (sym (loop-diverges n) ∙ reaches-final)
