{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-32 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PATCH-CONTRACTIBLE-NEG-001

  The contexts before and after an edit are equal as paths (C-31: the context
  type is contractible), but they are not equal by definition: their normal
  forms hdoc [] and hdoc (true :: []) differ.  Claiming the path by refl must
  be rejected by the kernel.  The context HIT is restated here so that this
  file is self-contained.
-}
module WrongStateRefl where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; true)
open import Cubical.Data.List using (List; []; _∷_)

data HistCtx : Type where
  hdoc : List Bool → HistCtx
  hadd : (b : Bool) (h : List Bool) → hdoc h ≡ hdoc (b ∷ h)

wrongStateRefl : Path HistCtx (hdoc []) (hdoc (true ∷ []))
wrongStateRefl = refl
