{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-19/C-20 (MP-CG001-GRAPH-REALIZATION-NEG-001).
  Expected result: KERNEL_REJECTED.

  Claim tested: the height profile of the four-place ring cannot be carried
  across the realization.  Sending each step to "the height at its start"
  leaves the end of the step reading the wrong height, and the kernel must
  refuse the definition.
-}
module WrongRealizedHeight where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)

data Place : Type where
  p0 p1 p2 p3 : Place

next : Place → Place
next p0 = p1
next p1 = p2
next p2 = p3
next p3 = p0

height : Place → ℕ
height p0 = 0
height p1 = 1
height p2 = 2
height p3 = 1

data Ring : Type where
  vtx  : Place → Ring
  edge : (x y : Place) → next x ≡ y → vtx x ≡ vtx y

realizedHeight : Ring → ℕ
realizedHeight (vtx v) = height v
realizedHeight (edge x y e i) = height x
