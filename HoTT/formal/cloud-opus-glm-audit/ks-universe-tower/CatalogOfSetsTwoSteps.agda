{-# OPTIONS --safe --cubical --guardedness #-}
{-
  COPUS-KS-C06 (Cloud-Opus, 2026-09-27; final-verdict round).

  The adjacent control of the Russell-face final verdict
  (Cloud-Opus审计并补完GLM/14-罗素面终局判词.md, §3.2, §4, §5 row S3+S4):
  "the catalog of all sets stops at step two" -- asking of hSet ℓ-zero
  "are any two entries the same in at most one way?" gives NO (it is not a
  set), and asking "are any two ways of being the same themselves the same
  in at most one way?" gives YES (it is a groupoid).

  This is Kraus–Sattler Theorem 5.10 at n = 0 (KS-Theorem-5-10-U≤ 0 from
  KSUniverseTower), restated with the library names:
    T (lvl 0) 0 = TypeOfHLevel ℓ-zero (2 + 0)   and   hSet ℓ = TypeOfHLevel ℓ 2,
  so the two sides agree definitionally.

  History: this exact one-liner was first type-checked in the session
  scratchpad (not a receipt); on the user's instruction that every piece of
  code of this work must live in the repository, it is kept here and
  captured as an F-011 run.
-}
module CatalogOfSetsTwoSteps where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Relation.Nullary using (¬_)
open import KSUniverseTower using (KS-Theorem-5-10-U≤)

catalogOfSetsTwoSteps : isOfHLevel 3 (hSet ℓ-zero) × (¬ isSet (hSet ℓ-zero))
catalogOfSetsTwoSteps = KS-Theorem-5-10-U≤ 0
