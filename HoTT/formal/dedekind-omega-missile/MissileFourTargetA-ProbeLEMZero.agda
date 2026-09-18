{-# OPTIONS --cubical --guardedness #-}
-- 预期编译失败（exit 1）——失败即收据：LEM 格闭项 n-lem 不归约到 zero
-- （与 AC 格 / UA 格同法的 stuckness 演示；ChargeDemo 收费演示一的机械化补齐）。

module MissileFourTargetA-ProbeLEMZero where

open import MissileFourChargeDemo using (n-lem)
open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.Data.Nat.Base using (ℕ; zero)

test-probe-lem-zero : n-lem ≡ zero
test-probe-lem-zero = refl
