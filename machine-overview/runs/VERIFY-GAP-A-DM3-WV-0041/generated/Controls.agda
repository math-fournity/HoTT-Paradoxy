{-# OPTIONS --safe --cubical --guardedness #-}

-- GENERATED MODULE for the gap-A DM3 kernel verification
-- witness WV-0041; regenerate with
--   python3 -m machine_overview.v2_dm3_verify
-- DENOMINATOR_SINGLE_SOURCE: every expected literal below is
-- computed by machine_overview/v2_dm3.py, the same canonical
-- semantics that produced the SEARCH run.

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
-- the DM3/B3 constructors and the meet/neg operations are imported into
-- V2DM3 from V2Cofibration; Agda does not re-export open-imported names
-- to importers, so the generated modules import them directly.
open import V2Cofibration using (DM3; d0; da; d1; dm3Meet; dm3Neg;
                                          B3; b0; b1; b2;
                                          Avail; absent; pending; available)
open import V2DM3

open import Target

-- Positive control 1: identical inputs never separate under the same
-- context (the context is deterministic in the supplied set).
sameValueControl : sepEqD (separatesD Target.opsList Target.p Target.p noSuppliedD)
  (false , obsTowerD false , obsTowerD false , nothing) ≡ true
sameValueControl = refl

-- Positive control 2: the delay axis (L1 visibility).  The expected
-- value is the canonical semantics' own verdict, whatever it is; the
-- kernel confirms the enumerator and the mirror agree on the axis
-- that the L1 fragment can see.
delayAxisControl : delayEquivD Target.p Target.q ≡ true
delayAxisControl = refl

