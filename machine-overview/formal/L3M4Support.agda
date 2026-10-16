{-# OPTIONS --safe --cubical --guardedness #-}

-- Shared controls for the M4-lite L3 task set.  This module supplies the
-- independently checked objects used by the native renderers; it deliberately
-- does not contain any of the candidate proof terms searched by the symbolic
-- engine.

module L3M4Support where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)

data Stage : Type where
  start finish : Stage

phase : Stage → Bool
phase start = false
phase finish = true

phase-start : phase start ≡ false
phase-start = refl

phase-finish : phase finish ≡ true
phase-finish = refl

phase-apart : (phase start ≡ phase finish) → ⊥
phase-apart = false≢true

data Segment : Type where
  left right : Segment
  segment-path : left ≡ right

-- A finite observation carries a requested precision.  ExactArrival is empty
-- in this deliberately minimal boundary model: finite evidence alone does not
-- manufacture an exact arrival witness.
data FiniteApproximation : Type where
  approximate : ℕ → FiniteApproximation

data ExactArrival : Type where

exact-elim : ExactArrival → ⊥
exact-elim ()

finite-zero : FiniteApproximation
finite-zero = approximate zero
