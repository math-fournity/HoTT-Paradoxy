{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-56 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-SEMANTICS-NEG-002

  The symmetry reverse of the places type fixes both towns.  Claiming by refl
  that it also fixes the road go must be rejected: it sends go to sym back.
-}
module WrongReverseFixesGo where

open import Cubical.Foundations.Prelude
open import PedometerSemantics using (module Escape)
open Escape using (reverse; go)

reverseFixesGo : cong reverse go ≡ go
reverseFixesGo = refl
