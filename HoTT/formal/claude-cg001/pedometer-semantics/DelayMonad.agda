{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The monad structure of the Delay type used by C-55, and what "≡ never"
  means observationally (Claude, session 91a6cdaa, 2026-09-25), in reply to
  Terra's audit 013 (section 2.1, scope items 1 and 2).

  proof id : MP-CG001-DELAY-MONAD-001
  claim    : CG001-C-59 (full statement in CLAIM-C59.md)

  Terra 013: PedometerSemantics.agda defines a Capretta-style coinductive
  Delay object but no bind and no monad laws, so "Delay monad" is only a
  source shorthand there; and "≡ never" is Cubical path equality, which that
  file reads as bisimilarity.  This file imports that very type (it does not
  restate it) and adds:

  C-59 (a) return and bind (sequencing: run the first program, then feed its
           value to the continuation), with the three monad laws as paths:
           left identity, right identity, associativity;
       (b) never is a left zero of bind: a program that first waits for a
           diverging program diverges, whatever the continuation; and never
           is not a returning program;
       (c) divergence is observational: d ≡ never if and only if
           runFor n d ≡ nothing for every fuel n.  So "≡ never" says exactly
           that no finite amount of running ever yields a result; reading the
           path as bisimilarity is not needed;
       (d) sequencing with a pure continuation maps the fuel-bounded result:
           runFor n (bind d (return ∘ f)) ≡ map-Maybe f (runFor n d);
       (e) for the P-rev specification of C-55 (b): every fuel-bounded run of
           the stop program returns nothing (the content of C-47 (c), now
           derived from the program), and the stop program followed by any
           continuation (for instance "report the count") is never;
           positive controls: under the escape, directed and data
           specifications of C-55 (c), "stop, then report the count plus one"
           reports 2 at fuel 1.
-}
module DelayMonad where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Maybe using (Maybe; nothing; just; map-Maybe)
open import Cubical.Data.Maybe.Properties using (¬just≡nothing)
open import Cubical.Relation.Nullary using (¬_)

open import PedometerSemantics
  using (Delay; Delay'; now; later; never; evalFor; runFor;
         module PRevProgram; module Escape; module Directed; module AsData)

open Delay

private
  variable
    ℓ ℓ' : Level
    A B C : Type

------------------------------------------------------------------------
-- (a) return, bind and the monad laws

return : A → Delay A
return a .force = now a

mutual
  bind : Delay A → (A → Delay B) → Delay B
  bind d f .force = bind' (d .force) f

  bind' : Delay' A → (A → Delay B) → Delay' B
  bind' (now a)   f = f a .force
  bind' (later d) f = later (bind d f)

leftIdentity : (a : A) (f : A → Delay B) → bind (return a) f ≡ f a
leftIdentity a f i .force = f a .force

mutual
  rightIdentity : (d : Delay A) → bind d return ≡ d
  rightIdentity d i .force = rightIdentity' (d .force) i

  rightIdentity' : (d : Delay' A) → bind' d return ≡ d
  rightIdentity' (now a)     = refl
  rightIdentity' (later d) i = later (rightIdentity d i)

mutual
  associativity : (d : Delay A) (f : A → Delay B) (g : B → Delay C)
                → bind (bind d f) g ≡ bind d (λ a → bind (f a) g)
  associativity d f g i .force = associativity' (d .force) f g i

  associativity' : (d : Delay' A) (f : A → Delay B) (g : B → Delay C)
                 → bind' (bind' d f) g ≡ bind' d (λ a → bind (f a) g)
  associativity' (now a)   f g   = refl
  associativity' (later d) f g i = later (associativity d f g i)

------------------------------------------------------------------------
-- (b) never is a left zero of bind, and never returns nothing

neverBind : (f : A → Delay B) → bind never f ≡ never
neverBind f i .force = later (neverBind f i)

runForNever : (n : ℕ) → runFor n (never {A}) ≡ nothing
runForNever zero    = refl
runForNever (suc n) = runForNever n

neverIsNotReturn : (a : A) → ¬ (never ≡ return a)
neverIsNotReturn a p = ¬just≡nothing (sym (cong (runFor 0) p))

------------------------------------------------------------------------
-- (c) divergence is observational

divergesRunsNothing : (d : Delay A) → d ≡ never → (n : ℕ) → runFor n d ≡ nothing
divergesRunsNothing d p n = cong (runFor n) p ∙ runForNever n

mutual
  runsNothingDiverges : (d : Delay A) → ((n : ℕ) → runFor n d ≡ nothing) → d ≡ never
  runsNothingDiverges d h i .force = runsNothingDiverges' (d .force) h i

  runsNothingDiverges' : (d : Delay' A) → ((n : ℕ) → evalFor n d ≡ nothing)
                       → d ≡ later never
  runsNothingDiverges' (now a)   h   = ⊥.rec (¬just≡nothing (h 0))
  runsNothingDiverges' (later d) h i = later (runsNothingDiverges d (λ n → h (suc n)) i)

------------------------------------------------------------------------
-- (d) a pure continuation maps the fuel-bounded result

evalForBindReturn : (n : ℕ) (d : Delay' A) (f : A → B)
                  → evalFor n (bind' d (λ a → return (f a))) ≡ map-Maybe f (evalFor n d)
evalForBindReturn n       (now a)   f = refl
evalForBindReturn zero    (later d) f = refl
evalForBindReturn (suc n) (later d) f = evalForBindReturn n (d .force) f

runForBindReturn : (n : ℕ) (d : Delay A) (f : A → B)
                 → runFor n (bind d (λ a → return (f a))) ≡ map-Maybe f (runFor n d)
runForBindReturn n d f = evalForBindReturn n (d .force) f

------------------------------------------------------------------------
-- (e) the stop program of C-55 as a component

module PRevConsequences {X : Type ℓ} {a b : X} (p : a ≡ b)
                        (F : X → Type ℓ') (read : F a → ℕ) (start : F a) where

  open PRevProgram p F read start

  stopProgramRunsNothing : (n : ℕ) → runFor n stopProgram ≡ nothing
  stopProgramRunsNothing = divergesRunsNothing stopProgram stopProgramIsNever

  stopThenAnythingIsNever : (k : ℕ → Delay C) → bind stopProgram k ≡ never
  stopThenAnythingIsNever k = cong (λ d → bind d k) stopProgramIsNever ∙ neverBind k

  stopThenReportIsNever : bind stopProgram (λ n → return (suc n)) ≡ never
  stopThenReportIsNever = stopThenAnythingIsNever (λ n → return (suc n))

escapeStopThenReport : runFor 1 (bind Escape.stopProgram (λ n → return (suc n))) ≡ just 2
escapeStopThenReport =
  runForBindReturn 1 Escape.stopProgram suc ∙ cong (map-Maybe suc) Escape.stopProgramConverges

directedStopThenReport : runFor 1 (bind Directed.stopProgram (λ n → return (suc n))) ≡ just 2
directedStopThenReport = refl

dataStopThenReport : runFor 1 (bind AsData.stopProgram (λ n → return (suc n))) ≡ just 2
dataStopThenReport = refl
