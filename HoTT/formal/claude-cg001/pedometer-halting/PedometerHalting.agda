{-# OPTIONS --safe --cubical --guardedness #-}
{-
  A walk that never stops (Claude, session 91a6cdaa, 2026-09-25), in reply to
  Terra's audit 007 (section 4.4: "a function that does not exist is not
  non-halting").

  proof id : MP-CG001-PEDOMETER-HALTING-001
  claims   : CG001-C-47 (full statement in CLAIM.md)

  The process.  A walker goes back and forth along a road between two towns,
  carrying a pedometer, and stops as soon as the pedometer has advanced by
  two.  With a real pedometer the walker stops after one round trip.

  C-47 (a) Think in HoTT: the road is a path p : a = b, a round trip is
           p . sym p, and whatever the walker carries is moved along the walk
           by transport in some family B.  For every family B, every readout
           read : B a -> N and every start value, after any number n of round
           trips the carried value is the start value again; so there is no n
           at which the reading has advanced by two, and the fuel-bounded
           search for the stopping time returns nothing for every fuel: the
           process does not halt.
       (b) the same holds for the one family that does count forward steps:
           the helix over the circle adds one on every forward loop
           (subst helix loop (pos 0) = pos 1), yet a counter read off it never
           reaches two over there-and-back walks.
       (c) positive control: the walk recorded as data (a list of steps), with
           the pedometer reading its length, advances by two after one round
           trip, and the same search halts at fuel 1 with answer 1.

  Bridge labels (walker, road, pedometer, stop) prove no physical fact.
-}
module PedometerHalting where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (rCancel; rUnit)
open import Cubical.Data.Sigma
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_; snotz)
open import Cubical.Data.Nat.Properties using (m+n≡n→m≡0; discreteℕ)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.List using (List; []; _∷_; _++_; length)
open import Cubical.Data.Int using (ℤ; pos; negsuc; abs)
open import Cubical.HITs.S1 using (S¹; base; loop; helix)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)

private
  variable
    ℓ ℓ' : Level

------------------------------------------------------------------------
-- a stopping-time search with fuel: the first k <= fuel satisfying P

module Search {ℓ} (P : ℕ → Type ℓ) (dec : (k : ℕ) → Dec (P k)) where

  pick : (k : ℕ) → Dec (P k) → Maybe ℕ → Maybe ℕ
  pick k (yes _) _    = just k
  pick k (no _)  rest = rest

  scan : ℕ → ℕ → Maybe ℕ
  scan k zero       = pick k (dec k) nothing
  scan k (suc fuel) = pick k (dec k) (scan (suc k) fuel)

  run : ℕ → Maybe ℕ
  run fuel = scan 0 fuel

  scanNever : ((k : ℕ) → ¬ P k) → (k fuel : ℕ) → scan k fuel ≡ nothing
  scanNever np k zero = stop (dec k)
    where
    stop : (d : Dec (P k)) → pick k d nothing ≡ nothing
    stop (yes pk) = ⊥.rec (np k pk)
    stop (no _)   = refl
  scanNever np k (suc fuel) = step (dec k)
    where
    step : (d : Dec (P k)) → pick k d (scan (suc k) fuel) ≡ nothing
    step (yes pk) = ⊥.rec (np k pk)
    step (no _)   = scanNever np (suc k) fuel

  neverHalts : ((k : ℕ) → ¬ P k) → (fuel : ℕ) → run fuel ≡ nothing
  neverHalts np fuel = scanNever np 0 fuel

------------------------------------------------------------------------
-- (a) the walk as a path, the pedometer carried by transport

roundTrips : {A : Type ℓ} {a b : A} → a ≡ b → ℕ → a ≡ a
roundTrips p zero    = refl
roundTrips p (suc n) = roundTrips p n ∙ (p ∙ sym p)

roundTripsAreStaying : {A : Type ℓ} {a b : A} (p : a ≡ b) (n : ℕ) → roundTrips p n ≡ refl
roundTripsAreStaying p zero    = refl
roundTripsAreStaying p (suc n) =
  cong₂ _∙_ (roundTripsAreStaying p n) (rCancel p) ∙ sym (rUnit refl)

module Carried {A : Type ℓ} {a b : A} (p : a ≡ b)
               (B : A → Type ℓ') (read : B a → ℕ) (start : B a) where

  after : ℕ → B a
  after n = subst B (roundTrips p n) start

  neverMoves : (n : ℕ) → after n ≡ start
  neverMoves n = cong (λ q → subst B q start) (roundTripsAreStaying p n) ∙ substRefl {B = B} start

  -- the stop rule: the pedometer has advanced by two
  Advanced : ℕ → Type
  Advanced n = read (after n) ≡ 2 + read start

  neverAdvanced : (n : ℕ) → ¬ Advanced n
  neverAdvanced n adv = snotz (m+n≡n→m≡0 {m = 2} (sym adv ∙ cong read (neverMoves n)))

  noHaltingTime : ¬ (Σ[ n ∈ ℕ ] Advanced n)
  noHaltingTime (n , adv) = neverAdvanced n adv

  decAdvanced : (n : ℕ) → Dec (Advanced n)
  decAdvanced n = discreteℕ (read (after n)) (2 + read start)

  run : ℕ → Maybe ℕ
  run = Search.run Advanced decAdvanced

  neverHalts : (fuel : ℕ) → run fuel ≡ nothing
  neverHalts = Search.neverHalts Advanced decAdvanced neverAdvanced

------------------------------------------------------------------------
-- (b) the family that does count forward steps

helixCountsForward : subst helix loop (pos 0) ≡ pos 1
helixCountsForward = refl

module HelixWalk = Carried loop helix abs (pos 0)

helixWalkNeverHalts : (fuel : ℕ) → HelixWalk.run fuel ≡ nothing
helixWalkNeverHalts = HelixWalk.neverHalts

------------------------------------------------------------------------
-- (c) positive control: the walk as data

data Step : Type where
  fwd back : Step

oscillation : ℕ → List Step
oscillation zero    = []
oscillation (suc n) = oscillation n ++ (fwd ∷ back ∷ [])

stepsAfter : ℕ → ℕ
stepsAfter n = length (oscillation n)

DataAdvanced : ℕ → Type
DataAdvanced n = stepsAfter n ≡ 2

dataHaltingTime : Σ[ n ∈ ℕ ] DataAdvanced n
dataHaltingTime = 1 , refl

dataRun : ℕ → Maybe ℕ
dataRun = Search.run DataAdvanced (λ n → discreteℕ (stepsAfter n) 2)

dataHalts : dataRun 1 ≡ just 1
dataHalts = refl
