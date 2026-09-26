{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control for CG001-C-37 (expected KERNEL_REJECTED).
  proof id : MP-CG001-DIRECTED-READING-NEG-001

  In the walking retraction, f then g is the idempotent e, not the identity
  of A, so the up-then-down cycle f, g is not a mutually inverse pair.
  Claiming that f then g is id_A by refl must be rejected by the kernel.
  The target is restated here so that this file is self-contained.
-}
module WrongInversePair where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; true; false)
open import Cubical.Data.Unit using (Unit; tt)

data EndA : Type where
  idAA idem : EndA

WHom : Bool → Bool → Type
WHom true true = EndA
WHom true false = Unit
WHom false true = Unit
WHom false false = Unit

wcomp : {a b c : Bool} → WHom a b → WHom b c → WHom a c
wcomp {true} {true} {true} idAA y = y
wcomp {true} {true} {true} idem idAA = idem
wcomp {true} {true} {true} idem idem = idem
wcomp {true} {true} {false} x y = tt
wcomp {true} {false} {true} x y = idem
wcomp {true} {false} {false} x y = tt
wcomp {false} {true} {true} x y = tt
wcomp {false} {true} {false} x y = tt
wcomp {false} {false} {true} x y = tt
wcomp {false} {false} {false} x y = tt

wrongInverse : wcomp {true} {false} {true} tt tt ≡ idAA
wrongInverse = refl
