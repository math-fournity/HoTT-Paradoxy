{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-63 (expected KERNEL_REJECTED).
  proof id : MP-CG001-UIP-ESCAPE-NEG-001

  Carrying true along the identification ua notEquiv computes to false.
  Claiming by refl that it stays true must be rejected: the kernel computes
  the transport, so the two identifications of Bool are told apart by
  computation, not only by a proof.
-}
module WrongTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool

stillTrue : transport (ua notEquiv) true ≡ true
stillTrue = refl
