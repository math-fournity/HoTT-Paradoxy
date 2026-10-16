{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-33 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PATCH-CONTRACTIBLE-NEG-002

  The detour "add one, then undo it", loop followed by sym loop, is equal to
  the no-op patch refl as a path (rCancel), and the optimizer that keeps its
  input is equal inside the theory to the one that normalizes it (C-33).  But
  the kept detour is not the no-op patch by computation: claiming the path by
  refl must be rejected by the kernel.
-}
module WrongDetourRefl where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.S1 using (S¹; base; loop)

wrongDetourRefl : Path (base ≡ base) (loop ∙ sym loop) refl
wrongDetourRefl = refl
