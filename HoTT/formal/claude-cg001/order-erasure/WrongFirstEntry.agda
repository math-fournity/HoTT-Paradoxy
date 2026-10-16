{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-48 (expected KERNEL_REJECTED).
  proof id : MP-CG001-ORDER-ERASURE-NEG-001

  On the exchange quotient of Boolean lists, "the first entry" must send
  x :: y :: xs and y :: x :: xs to the same value, which fails when x and y
  differ.  Defining it by its obvious clauses must be rejected.
-}
module WrongFirstEntry where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; true; false)
open import Cubical.Data.Maybe using (Maybe; nothing; just)

data MS : Type where
  []ms  : MS
  _∷ms_ : Bool → MS → MS
  ex    : (x y : Bool) (xs : MS) → x ∷ms (y ∷ms xs) ≡ y ∷ms (x ∷ms xs)

firstEntry : MS → Maybe Bool
firstEntry []ms              = nothing
firstEntry (x ∷ms xs)        = just x
firstEntry (ex true  true  xs i) = just true
firstEntry (ex true  false xs i) = just true
firstEntry (ex false true  xs i) = just false
firstEntry (ex false false xs i) = just false
