{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Self-audit controls for A1 (Claude, session 6fd0312a, 2026-09-25), written in
  response to an external audit (GPT-5.6 Terra) of CG001-C-01..C-24.

  proof id : MP-CG001-FAMILY-CONTROL-001
  claims   : CG001-C-25 .. CG001-C-27 (full statements in CLAIM.md)

  C-25  the family route works for the finite reading task: on the realized
        four-place ring, a type family glued by +1,+1,-1,-1 carries a section
        whose raw values at the four named places are the heights 0,1,2,1;
        the raw readings at the first two places differ.  This concedes the
        auditor's point that C-19/C-20 concern non-dependent readings only.
  C-26  what survives the family route: in the total space of that family,
        the walker's state before the first step, (r0 , 0), and after it,
        (r1 , 1), are identified, so every observable of the total state takes
        equal values on them.
  C-27  time as data: a signal 0,1,0 on N exists; it does not respect the
        arrows of (N, <=).  This concedes that C-24's monotonicity was an
        assumption, not a consequence of direction.

  Bridge labels (ring, walker, height, signal) are interpretation.
-}
module FamilyControl where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc; znots; snotz; +-suc)
open import Cubical.Data.Nat.Order using (_≤_)
open import Cubical.Data.Int using (ℤ; pos; negsuc; sucℤ; predℤ; injPos; sucPathℤ; sucPred; predSuc)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- The realized four-place ring and a family glued by the height changes

data Ring : Type where
  r0 r1 r2 r3 : Ring
  e0 : r0 ≡ r1
  e1 : r1 ≡ r2
  e2 : r2 ≡ r3
  e3 : r3 ≡ r0

predPathℤ : ℤ ≡ ℤ
predPathℤ = ua (predℤ , isoToIsEquiv (iso predℤ sucℤ predSuc sucPred))

Gauge : Ring → Type
Gauge r0 = ℤ
Gauge r1 = ℤ
Gauge r2 = ℤ
Gauge r3 = ℤ
Gauge (e0 i) = sucPathℤ i
Gauge (e1 i) = sucPathℤ i
Gauge (e2 i) = predPathℤ i
Gauge (e3 i) = predPathℤ i

------------------------------------------------------------------------
-- CG001-C-25  The family route carries the height profile

heights : (x : Ring) → Gauge x
heights r0 = pos 0
heights r1 = pos 1
heights r2 = pos 2
heights r3 = pos 1
heights (e0 i) = toPathP {A = λ j → sucPathℤ j} {x = pos 0} {y = pos 1} refl i
heights (e1 i) = toPathP {A = λ j → sucPathℤ j} {x = pos 1} {y = pos 2} refl i
heights (e2 i) = toPathP {A = λ j → predPathℤ j} {x = pos 2} {y = pos 1} refl i
heights (e3 i) = toPathP {A = λ j → predPathℤ j} {x = pos 1} {y = pos 0} refl i

rawProfile : (heights r0 ≡ pos 0) × (heights r1 ≡ pos 1) × (heights r2 ≡ pos 2) × (heights r3 ≡ pos 1)
rawProfile = refl , refl , refl , refl

rawReadingsDiffer : ¬ (heights r0 ≡ heights r1)
rawReadingsDiffer p = znots (injPos p)

------------------------------------------------------------------------
-- CG001-C-26  What survives: the walker's state before and after a step is one state

stepIdentifiesStates : Path (Σ Ring Gauge) (r0 , pos 0) (r1 , pos 1)
stepIdentifiesStates = ΣPathP (e0 , toPathP {A = λ j → sucPathℤ j} {x = pos 0} {y = pos 1} refl)

stateObservablesFrozen : ∀ {ℓ} {P : Type ℓ} (g : Σ Ring Gauge → P)
  → g (r0 , pos 0) ≡ g (r1 , pos 1)
stateObservablesFrozen g = cong g stepIdentifiesStates

------------------------------------------------------------------------
-- CG001-C-27  Time as data carries an up-then-down signal, which respects no order

one≰zero : ¬ (1 ≤ 0)
one≰zero (k , p) = snotz (sym (+-suc k 0) ∙ p)

signal : ℕ → ℕ
signal zero = 0
signal (suc zero) = 1
signal (suc (suc n)) = 0

signalUpThenDown : (signal 0 ≡ 0) × (signal 1 ≡ 1) × (signal 2 ≡ 0)
signalUpThenDown = refl , refl , refl

signalRespectsNoOrder : ¬ ((m n : ℕ) → m ≤ n → signal m ≤ signal n)
signalRespectsNoOrder mono = one≰zero (mono 1 2 (1 , refl))
