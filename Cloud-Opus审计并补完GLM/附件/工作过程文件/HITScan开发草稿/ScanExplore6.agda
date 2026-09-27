{-# OPTIONS --safe --cubical --guardedness #-}
module ScanExplore6 where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import UniverseHasNoLevel

f1 : Path (List Name) (hitsOf universeHasNoLevel) []
f1 = refl
