{-# OPTIONS --safe --cubical --guarded #-}
module Rev4CertifiedFragmentRejectsOverride where

open import Agda.Builtin.Nat

{-# TERMINATING #-}
loop : Nat
loop = loop

