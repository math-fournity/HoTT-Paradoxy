module SemB04NonEqualityNegative where

open import category-theory.precategories
open import foundation.unit-type
open import foundation.universe-levels
open import reflection.precategory-solver

module _
  {l1 l2 : Level}
  {C : Precategory l1 l2}
  where

  -- Expected to be rejected by boundary-Type-Checker before proof generation.
  not-an-equality : unit
  not-an-equality = solve-Precategory! C
