{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control MP-CG001-TWO-CHOICES-CUBICAL-NEG-003 (CG-010 R4).

  Rejected claim: without monotonicity a switch sequence still settles; here
  the alternating question is claimed settled at stage 0 (checked at the next
  stage).  Expected: the kernel computes false != true.
  Positive counterpart: noSettlingWithoutMonotone.
-}
module WrongAltSettles where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (_+_)
open import SameQ using (alt)

altSettlesAtOne : alt (1 + 0) ≡ alt 0
altSettlesAtOne = refl
