{-# OPTIONS --cubical --guardedness #-}
-- 预期编译失败（exit 1）——失败即收据：n 与 suc zero 不可互换，即 n 的范式不是
-- suc zero（修订片 027 §3.1 靶 A / 路径 (i) 外部归约检查）。

module MissileFourTargetA-ProbeSucZero where

open import MissileFourTargetA-UACounterexample using (n)
open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)

test-probe-suc-zero : n ≡ suc zero
test-probe-suc-zero = refl
