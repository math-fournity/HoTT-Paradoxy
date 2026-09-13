{-# OPTIONS --safe --cubical --guardedness #-}

-- Negative-control fixture: a candidate that tries to buy the target statement
-- with a postulate.  The coordinator must reject it by hygiene scan before any
-- run directory is created.

module Proof where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import PartialityRaceTimeout
open import Target

postulate
  cheat : Target.p ≈ Target.q

equiv : Target.p ≈ Target.q
equiv = cheat
