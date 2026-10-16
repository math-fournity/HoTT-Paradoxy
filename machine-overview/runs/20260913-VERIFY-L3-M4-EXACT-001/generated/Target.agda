{-# OPTIONS --safe --cubical --guardedness #-}

-- M4-lite finite-to-exact candidate target for MS-TASK-L3-FINITE-TO-EXACT-001 / WV-0001.
-- The task asks whether finite approximation evidence alone supplies exact arrival.

module Target where

open import Cubical.Foundations.Prelude
open import L3M4Support

FiniteToExact : Type
FiniteToExact = FiniteApproximation → ExactArrival
