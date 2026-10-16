{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Negative control COPUS-KS-NEG-02 for KSUniverseTower (bookkeeping).
  Tries to obtain the one-level-stronger claim "U_n is not an (n+1)-type"
  from the same certificate tower n : NT (lvl n) n.  Expected: kernel
  rejection (the certificate is level-exact: n != suc n).  Together with
  KS-Theorem-5-10-U≤ (U_n^{<=n} IS an (n+1)-type) this shows the
  truncation bookkeeping is tight rather than accidentally generous.
-}
module KSNegOvershoot where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isOfHLevel)
open import Cubical.Data.Nat using (ℕ ; suc ; _+_)
open import Cubical.Relation.Nullary using (¬_)
open import KSUniverseTower using (lvl ; tower ; universeNotHLevel)

wrong : (n : ℕ) → ¬ isOfHLevel (3 + n) (Type (lvl n))
wrong n = universeNotHLevel (lvl n) (suc n) (tower n)
