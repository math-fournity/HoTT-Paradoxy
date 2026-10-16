{-# OPTIONS --safe --cubical --guarded #-}
module CertifiedFragmentRejectsOverride where

open import Agda.Builtin.Nat

{-# TERMINATING #-}
loop : Nat
loop = loop

