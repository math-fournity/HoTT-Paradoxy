{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-62 (expected KERNEL_REJECTED).
  proof id : MP-CG001-SST-FINITE-LEVELS-NEG-001

  The level-3 type of SSTLevels.agda, written by hand, with one face bounded
  by the wrong edge: the triangle x013 is given the edge x12 where its third
  edge must be x13.  The kernel must reject it (x2 against x3), which shows
  the face bookkeeping in the generated levels is checked, not merely parsed.
-}
module WrongFace where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Unit

WrongSST≤3 : Type₁
WrongSST≤3 =
  Σ[ A0 ∈ Type ]
  Σ[ A1 ∈ ((x0 : A0) (x1 : A0) → Type) ]
  Σ[ A2 ∈ ((x0 : A0) (x1 : A0) (x2 : A0)
           (x01 : A1 x0 x1) (x02 : A1 x0 x2) (x12 : A1 x1 x2) → Type) ]
  Σ[ A3 ∈ ((x0 : A0) (x1 : A0) (x2 : A0) (x3 : A0)
           (x01 : A1 x0 x1) (x02 : A1 x0 x2) (x03 : A1 x0 x3)
           (x12 : A1 x1 x2) (x13 : A1 x1 x3) (x23 : A1 x2 x3)
           (x012 : A2 x0 x1 x2 x01 x02 x12)
           (x013 : A2 x0 x1 x3 x01 x03 x12)
           (x023 : A2 x0 x2 x3 x02 x03 x23)
           (x123 : A2 x1 x2 x3 x12 x13 x23) → Type) ]
  Unit
