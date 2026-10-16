{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-60 (expected KERNEL_REJECTED).
  proof id : MP-CG001-HPT-MULTISET-NEG-001

  Reading the first entry of a history by cases on the constructors of MS:
  the empty history has none, a history x :: xs starts with x.  The exchange
  constructor Ex x y xs then requires a path from just x to just y, for all
  x y.  Filling it with the constant just x fails at the right endpoint, and
  the definition below must be rejected.  (C-60 (d) shows that no function
  MS -> Maybe Bool, defined in any way, reads the first entry.)
-}
module WrongFirstEntryMS where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import HPTMultisetFidelity using (MS; []ms; _∷ms_; Ex)

firstEntry : MS → Maybe Bool
firstEntry []ms          = nothing
firstEntry (x ∷ms xs)    = just x
firstEntry (Ex x y xs i) = just x
