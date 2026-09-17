{-# OPTIONS --safe --cubical --guardedness #-}

-- GENERATED MODULE for the gap-A DM3 kernel verification
-- witness BOOL_LAW_INDEPENDENCE; regenerate with
--   python3 -m machine_overview.v2_dm3_verify
-- DENOMINATOR_SINGLE_SOURCE: every expected literal below is
-- computed by machine_overview/v2_dm3.py, the same canonical
-- semantics that produced the SEARCH run.

module BLIFalsify where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import Cubical.Relation.Nullary.Base using (¬_)
-- the DM3/B3 constructors and the meet/neg operations are imported into
-- V2DM3 from V2Cofibration; Agda does not re-export open-imported names
-- to importers, so the generated modules import them directly.
open import V2Cofibration using (DM3; d0; da; d1; dm3Meet; dm3Neg;
                                          B3; b0; b1; b2;
                                          Avail; absent; pending; available)
open import V2DM3

-- NEGATIVE CONTROL.  This module deliberately CLAIMS that the boolean
-- law HOLDS in DM3, i.e. that a && ~a = 0.  It must be REJECTED by the
-- kernel: dm3Meet da (dm3Neg da) reduces to da, so the goal is
-- da ≡ d0, which refl cannot prove.  A kernel ACCEPT here would mean
-- DM3 is boolean and the gap-A upgrade is void.
wrongClaim : dm3Meet da (dm3Neg da) ≡ d0
wrongClaim = refl

