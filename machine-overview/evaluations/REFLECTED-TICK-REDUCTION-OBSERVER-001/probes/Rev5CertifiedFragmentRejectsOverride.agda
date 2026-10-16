{-# OPTIONS --safe --cubical --guarded #-}
module Rev5CertifiedFragmentRejectsOverride where

open import Agda.Builtin.Nat

{-# TERMINATING #-}
loop : Nat
loop = loop

