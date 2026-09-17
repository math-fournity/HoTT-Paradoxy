{-# OPTIONS --safe --cubical --guardedness #-}

-- GENERATED MODULE.  Do not edit by hand; regenerate with
--   python3 machine-overview/machine_overview/v2_agreement.py
--
-- Stage-1 ground agreement for the V2 L2-cofibration fragment
-- (design source: Atria的方案/修订片/015 §5 stage 1).
--
-- Every entry of the declared denominator is checked DEFINITIONALLY:
--   groundAgreement : checkAll ≡ true     discharged by refl
-- can only pass when the native kernel's own evaluation of applyOps agrees
-- with the Python enumerator's expected observation on ALL 3179 of them.
-- A single disagreement is a type error (that error is the verification).
--
-- SCOPE: applyOps is exhaustive over 289 ground values x 11
-- declared op-lists.  separates is checked on the 11 DESIGNATED CONTROLS
-- only (see v2_agreement.scope_disclosure): the full pair matrix would need
-- ~918k SepResult literals, beyond a feasible module; the control set is
-- pinned independently by tests/test_v2_cofibration.py::SeparationTest.
--
-- FAITHFULNESS CAVEAT (revision 015 §3.4): the face lattice here is the
-- POINT-SET model, which is SOUND but NOT COMPLETE for the interval I (a De
-- Morgan algebra).  This module registers NO mathematical claim
-- (registers_new_claim: false); no result here is evidence about the real
-- interval I (F-011).

module V2GroundAgreement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; foldr; map)
open import V2Cofibration

record GroundCheck : Type where
  constructor gc
  field
    ops    : List Op
    inp    : V2
    expect : Obs

checkOne : GroundCheck → Bool
checkOne (gc ops inp exp) = obsEqB (proj₁ (applyOps ops inp noSupplied)) exp

record SepControl : Type where
  constructor sc
  field
    ops    : List Op
    left   : V2
    right  : V2
    expect : SepResult

checkSep : SepControl → Bool
checkSep (sc ops l r exp) = sepEqB (separates ops l r noSupplied) exp


allChecks : List GroundCheck
allChecks =
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vω) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vω) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vω) (obsDelay (vω)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vω) (obsDelay (vω)) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vω) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vω) (obsAvail absent) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vω) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vω) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vω) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vω) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vω) (obsTower false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits false true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits false true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (zero) (true) (faceFromBits true true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits false true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits false true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b0))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b2))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (zero) (false) (faceFromBits true true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (zero) (false) (faceFromBits true true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits false true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits false true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (true) (faceFromBits true true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsOptional (some true)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsOptional (some true)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (true) (faceFromBits true true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true false) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true false) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits false true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits false true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true true) (b0))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true true) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true true) (b2))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsOptional (some false)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (zero)) (false) (faceFromBits true true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits false true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (suc (zero)))) (true) (faceFromBits true true false false) (b0))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (true) (faceFromBits true true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsAvail available) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true false) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true false true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true false true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsDensity true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits false true true true) (b2)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b0)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b1)) (obsTower true) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opRaceR (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (suc (suc (zero))))) (false) (faceFromBits true false true false) (b1))) ∷
  gc (opSupply (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsDelay (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2))) ∷
  gc (opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsOptional (none)) ∷
  gc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opFillOf (faceFromBits true true false false) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsAvail pending) ∷
  gc (opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsTower false) ∷
  gc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsDensity false) ∷
  gc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opDeadline (suc (zero)) ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsOptional (some false)) ∷
  gc (opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ opTower b1 ∷ []) (vret (suc (suc (zero))) (false) (faceFromBits true true true true) (b2)) (obsTower true) ∷
  []

checkAll : Bool
checkAll = andL (map checkOne allChecks)

groundAgreement : checkAll ≡ true
groundAgreement = refl

allSepControls : List SepControl
allSepControls =
  -- positive-G-b-availability
  sc (opSupply (faceFromBits true true false false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (true) (faceFromBits true false true false) (b0)) ((true , obsAvail available , obsAvail pending , just kAvailabilityObservation)) ∷
  -- positive-G-c-level
  sc (opTower b0 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (true) (faceFromBits true true false false) (b1)) ((true , obsTower true , obsTower false , just kLevelObservation)) ∷
  -- positive-G-a-density
  sc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (true) (faceFromBits true true true true) (b0)) ((true , obsDensity true , obsDensity false , just kDensityObservation)) ∷
  -- negative-no-ops
  sc ([]) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (false) (faceFromBits true false true false) (b2)) ((false , obsDelay (vret (zero) (true) (faceFromBits true true false false) (b0)) , obsDelay (vret (zero) (false) (faceFromBits true false true false) (b2)) , nothing)) ∷
  -- negative-identical-inputs-delay-context
  sc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (suc (zero)) (false) (faceFromBits true false true false) (b1)}) ∷ []) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ((false , obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1)) , obsDelay (vret (suc (suc (suc (zero)))) (false) (faceFromBits true false true false) (b1)) , nothing)) ∷
  -- negative-G-b-both-faces-supplied
  sc (opSupply (faceFromBits true true false false) ∷ opSupply (faceFromBits true false true false) ∷ opFill fZERO ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (true) (faceFromBits true false true false) (b0)) ((false , obsAvail available , obsAvail available , nothing)) ∷
  -- negative-G-c-equal-levels
  sc (opTower b1 ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b1)) (vret (zero) (true) (faceFromBits true false true false) (b1)) ((false , obsTower true , obsTower true , nothing)) ∷
  -- negative-G-a-both-faces-at-bounds
  sc (opBetween (faceFromBits false false false false) (faceFromBits true true true true) ∷ []) (vret (zero) (true) (faceFromBits false false false false) (b0)) (vret (zero) (true) (faceFromBits true true true true) (b0)) ((false , obsDensity false , obsDensity false , nothing)) ∷
  -- l1-shared-value-mismatch
  sc (opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (false) (faceFromBits true true false false) (b0)) ((true , obsDelay (vret (zero) (true) (faceFromBits true true false false) (b0)) , obsDelay (vret (zero) (false) (faceFromBits true true false false) (b0)) , just kValueMismatch)) ∷
  -- l1-shared-completion-divergence
  sc (opBind (λ {true → vω; false → vret (zero) (false) (faceFromBits true false true false) (b0)}) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (zero) (false) (faceFromBits true true false false) (b0)) ((true , obsDelay (vω) , obsDelay (vret (suc (zero)) (false) (faceFromBits true false true false) (b0)) , just kCompletionDivergence)) ∷
  -- l1-shared-deadline-observation
  sc (opDeadline (zero) ∷ []) (vret (zero) (true) (faceFromBits true true false false) (b0)) (vret (suc (zero)) (true) (faceFromBits true true false false) (b0)) ((true , obsOptional (some true) , obsOptional (none) , just kDeadlineObservation)) ∷
  []

sepAll : Bool
sepAll = andL (map checkSep allSepControls)

sepAgreement : sepAll ≡ true
sepAgreement = refl
