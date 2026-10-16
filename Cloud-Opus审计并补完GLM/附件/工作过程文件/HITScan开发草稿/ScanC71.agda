{-# OPTIONS --safe --cubical --guardedness #-}
module ScanC71 where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import HSetNotSet
a : Path Nat (sizeOf hSetNotSet) 0
a = refl
