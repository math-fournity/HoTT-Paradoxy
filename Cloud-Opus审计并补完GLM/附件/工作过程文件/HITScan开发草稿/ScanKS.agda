{-# OPTIONS --safe --cubical --guardedness #-}
module ScanKS where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import KSUniverseTower

k1 : Path (List Name) (hitsOf KS-Theorem-5-9) []
k1 = refl
k2 : Path (List Name) (hitsOf workOrderForm) []
k2 = refl
k3 : Path (List Name) (hitsOf KS-Theorem-5-10-Loop) []
k3 = refl
k4 : Path Nat (sizeOf workOrderForm) 0
k4 = refl
