{-# OPTIONS --safe --cubical --guardedness #-}

-- M4-lite explicit-event target for MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001 / WV-0001.
-- The event carrier is distinct from cubical dimension and keeps exact endpoint observations.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Prod.Base using (_×_)
open import L3M4Support

ExactEventBoundary : Type
ExactEventBoundary =
  (phase start ≡ false) × ((phase finish ≡ true) × ((phase start ≡ phase finish) → ⊥))
