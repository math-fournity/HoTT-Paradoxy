{-# OPTIONS --safe --cubical --guardedness #-}
-- Negative control for CG001-C-113: on the set-truncated universe the first stage of the
-- same search is settled (the truncation is a set).  Claiming it unsettled must be rejected.
module WrongTruncUnsettled where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (false)
open import TruncationQuestioning using (judgeTU)
open import SameQ

wrongTruncUnsettled : Truncated.truncStream judgeTU 0 ≡ false
wrongTruncUnsettled = refl
