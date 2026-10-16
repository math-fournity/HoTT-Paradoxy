{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module WrongWholeCover where

open import Cubical.Data.Sigma
open import IntervalCover
open import RationalCuts
open import OpenCoverMargins

-- Deliberately omit the positive inner margin; an OpenUnit lower bound
-- is not a lower bound at the stricter midpoint.
badLower : (x : R) → OpenUnit x → Lower x (mid q0 quarter)
badLower x bounds = fst bounds
