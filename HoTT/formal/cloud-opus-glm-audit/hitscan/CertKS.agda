{-# OPTIONS --safe --cubical --guardedness #-}
{-
  HITScan certificates for the general-n Kraus–Sattler replay.
  claim COPUS-R1-C05: KS-Theorem-5-9, workOrderForm, KS-Theorem-5-10-U≤ and
                      KS-Theorem-5-10-Loop have HIT-free name-level closures
                      (363 / 364 / 363 / 364 names).
-}
module CertKS where

open import Cubical.Foundations.Prelude
open import Agda.Builtin.List
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.Unit
open import Agda.Builtin.Reflection using (Name)
open import HITScan
open import KSUniverseTower
  using (KS-Theorem-5-9 ; workOrderForm ; KS-Theorem-5-10-U≤ ; KS-Theorem-5-10-Loop)

ks59-noHIT : Path (List Name) (hitsOf KS-Theorem-5-9) []
ks59-noHIT = refl
ks59-size : Path Nat (sizeOf KS-Theorem-5-9) 363
ks59-size = refl

workOrder-noHIT : Path (List Name) (hitsOf workOrderForm) []
workOrder-noHIT = refl
workOrder-size : Path Nat (sizeOf workOrderForm) 364
workOrder-size = refl

ks510U-noHIT : Path (List Name) (hitsOf KS-Theorem-5-10-U≤) []
ks510U-noHIT = refl
ks510U-size : Path Nat (sizeOf KS-Theorem-5-10-U≤) 363
ks510U-size = refl

ks510Loop-noHIT : Path (List Name) (hitsOf KS-Theorem-5-10-Loop) []
ks510Loop-noHIT = refl
ks510Loop-size : Path Nat (sizeOf KS-Theorem-5-10-Loop) 364
ks510Loop-size = refl

report-workOrder : ⊤
report-workOrder = reportClosure workOrderForm
report-ks59 : ⊤
report-ks59 = reportClosure KS-Theorem-5-9
