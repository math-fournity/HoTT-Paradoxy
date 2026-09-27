{-# OPTIONS --safe --cubical --guardedness #-}
module ScanExplore3 where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import NoHitGroupoidUniverse
open import AscentStallAtSets
open import UIPEscape

c1 : Path (List Name) (hitsOf universeLoopSpaceAtSetIsSet) []
c1 = refl
c2 : Path (List Name) (hitsOf noLevel2AscentAtSets) []
c2 = refl
c3 : Path (List Name) (hitsOf typeIsNotASet) []
c3 = refl
c4 : Path (List Name) (primsOf ¬universeIsGroupoid) []
c4 = refl
