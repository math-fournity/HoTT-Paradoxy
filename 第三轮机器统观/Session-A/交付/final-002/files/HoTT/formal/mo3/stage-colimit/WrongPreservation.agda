{-# OPTIONS --safe --cubical --guardedness #-}
module WrongPreservation where

-- Expected type rejection: a finite-stage accessibility term cannot be
-- silently reused as accessibility for the aggregate relation.
open import Cubical.Induction.WellFounded
open import Cubical.Data.Nat
open import Cubical.Data.Fin.Inductive.Base
open import StageColimit

bad : Acc TotalStep (terminal zero)
bad = stageWellFounded zero fzero
