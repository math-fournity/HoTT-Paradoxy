{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-54 (expected KERNEL_REJECTED).
  proof id : MP-CG001-HISTORY-COUNTS-NEG-001

  The two presentations true :: false :: [] and false :: true :: [] are equal
  elements of FMSet Bool only through the path constructor comm.  Claiming by
  refl that they are the same must be rejected: the kernel keeps the two
  presentations apart, which is where JFP's "explicit log" lives.
-}
module WrongPresentationsDefinitional where

open import Cubical.Foundations.Prelude
open import HistoryCounts using (trueFirst; falseFirst)

presentationsDefinitionallyEqual : trueFirst ≡ falseFirst
presentationsDefinitionallyEqual = refl
