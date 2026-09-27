{-# OPTIONS --safe --cubical --guardedness #-}
module ScanExplore where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import NoHitGroupoidUniverse
open import AscentStallAtSets
open import UIPEscape

a1 : Path (List Name) (hitsOf ¬universeIsGroupoid) []
a1 = refl
a2 : Path (List Name) (axiomsOf ¬universeIsGroupoid) []
a2 = refl
