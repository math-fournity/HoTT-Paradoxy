{-# OPTIONS --safe --cubical --guardedness #-}

-- GENERATED MODULE for the V2 first-family kernel verification
-- witness WV-23233; regenerate with
--   python3 -m machine_overview.v2_verify
-- DENOMINATOR_SINGLE_SOURCE: every expected literal below is
-- computed by machine_overview/v2_cofibration.py, the same
-- canonical semantics that produced the SEARCH run.

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import V2Cofibration

open import Target

-- Positive control 1: identical inputs never separate under the same
-- context (the context is deterministic in the supplied set).
sameValueControl : sepEqB (separates Target.opsList Target.p Target.p noSupplied)
  (false , obsTower true , obsTower true , nothing) ≡ true
sameValueControl = refl

-- Positive control 2: the delay axis (L1 visibility).  The expected
-- value is the canonical semantics' own verdict, whatever it is; the
-- kernel confirms the enumerator and the mirror agree on the axis
-- that the L1 fragment can see.
delayAxisControl : delayEquiv Target.p Target.q ≡ true
delayAxisControl = refl

