{-# OPTIONS --safe --cubical --guardedness #-}
module ScanExplore4 where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import RealisticIotaSyntaxSet

d1 : Path (List Name) (hitsOf realisticIotaSyntaxIsASet) []
d1 = refl
