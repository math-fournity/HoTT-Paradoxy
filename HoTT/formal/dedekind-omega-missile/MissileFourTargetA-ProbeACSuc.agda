{-# OPTIONS --cubical --guardedness #-}
-- 预期编译失败（exit 1）——失败即收据：n-ac 不归约到 suc zero。

module MissileFourTargetA-ProbeACSuc where

open import MissileFourChargeDemo using (n-ac)
open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)

test-probe-ac-suc : n-ac ≡ suc zero
test-probe-ac-suc = refl
