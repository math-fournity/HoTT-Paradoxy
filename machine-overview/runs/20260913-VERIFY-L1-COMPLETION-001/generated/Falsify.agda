{-# OPTIONS --safe --cubical --guardedness #-}

-- Negative control: this instance does NOT separate the pair, so the
-- kernel must reject the following claim (expected non-zero exit).

module Falsify where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import PartialityRaceTimeout
open import Target
open import MVSupport

bad : ¬ (Target.control-left ≡ Target.control-right)
bad e = MVSupport.some-neq-none true e
