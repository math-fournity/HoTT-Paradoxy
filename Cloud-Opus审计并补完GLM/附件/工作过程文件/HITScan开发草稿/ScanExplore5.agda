{-# OPTIONS --safe --cubical --guardedness #-}
module ScanExplore5 where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import UniverseHasNoLevel

e1 : Path (List Name) (hitsOf localGlobal) []
e1 = refl
-- e2 : Path (List Name) (hitsOf gatheringNeverSettled) []
-- e2 = refl
