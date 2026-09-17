{-# OPTIONS --safe --cubical --guardedness #-}

-- GENERATED MODULE for the V2 first-family kernel verification
-- witness WV-23233; regenerate with
--   python3 -m machine_overview.v2_verify
-- DENOMINATOR_SINGLE_SOURCE: every expected literal below is
-- computed by machine_overview/v2_cofibration.py, the same
-- canonical semantics that produced the SEARCH run.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import V2Cofibration

p : V2
p = vret (zero) (true) (faceFromBits false false false false) (b0)

q : V2
q = vret (suc (zero)) (true) (faceFromBits true true false false) (b0)

opsList : OpList
opsList = opBind (λ {true → vret (zero) (true) (faceFromBits true true false false) (b0); false → vret (zero) (true) (faceFromBits true false true false) (b1)}) ∷ opRaceL (vret (suc (zero)) (false) (faceFromBits true false true false) (b1)) ∷ opTower b0 ∷ []

