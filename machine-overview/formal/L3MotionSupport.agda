{-# OPTIONS --safe --cubical --guardedness #-}

-- Trusted controls for the L3 interval/time-structure experiment.
-- This module deliberately contains no proof of the searched obstruction.

module L3MotionSupport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)

data Stage : Type where
  start finish : Stage

-- Operational control: a two-stage activity can change its discrete
-- completion observation exactly at the stage boundary.
phase : Stage → Bool
phase start = false
phase finish = true

phase-changes : (phase start ≡ phase finish) → ⊥
phase-changes = false≢true

-- Geometric control: a genuine Type with a declared endpoint Path supports
-- path-valued motion.  The primitive dimension I itself has sort IUniv, so it
-- is deliberately not misrepresented here as an ordinary Type.
data Segment : Type where
  left right : Segment
  segment-motion : left ≡ right
