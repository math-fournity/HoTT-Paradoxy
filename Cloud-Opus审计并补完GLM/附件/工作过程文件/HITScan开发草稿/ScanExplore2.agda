{-# OPTIONS --safe --cubical --guardedness #-}
module ScanExplore2 where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import NoHitGroupoidUniverse
open import AscentStallAtSets
open import UIPEscape

b1 : Path Nat (sizeOf ¬universeIsGroupoid) 0
b1 = refl
