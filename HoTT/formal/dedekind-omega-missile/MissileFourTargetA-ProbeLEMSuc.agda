{-# OPTIONS --cubical --guardedness #-}
-- 预期编译失败（exit 1）——失败即收据：n-lem 也不归约到 suc zero。

module MissileFourTargetA-ProbeLEMSuc where

open import MissileFourChargeDemo using (n-lem)
open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)

test-probe-lem-suc : n-lem ≡ suc zero
test-probe-lem-suc = refl
