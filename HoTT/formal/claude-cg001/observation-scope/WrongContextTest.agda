{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-44 (d) (expected KERNEL_REJECTED).
  proof id : MP-CG001-OBSERVATION-SCOPE-NEG-001

  The index-level test "is the history empty" answers true at [] and false
  at true :: [].  Defining the same test directly on the history-indexed
  context HIT must fail: the path constructor hadd b [] joins a context
  where the test says true to one where it says false, and no Bool path
  connects true to false.
-}
module WrongContextTest where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool ; true ; false)
open import Cubical.Data.List using (List ; [] ; _∷_)

data HistCtx : Type where
  hdoc : List Bool → HistCtx
  hadd : (b : Bool) (h : List Bool) → hdoc h ≡ hdoc (b ∷ h)

isEmptyCtx : HistCtx → Bool
isEmptyCtx (hdoc [])          = true
isEmptyCtx (hdoc (_ ∷ _))     = false
isEmptyCtx (hadd b [] i)      = false
isEmptyCtx (hadd b (_ ∷ _) i) = false
