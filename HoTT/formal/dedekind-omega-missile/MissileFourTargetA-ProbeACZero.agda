{-# OPTIONS --cubical --guardedness #-}
-- 预期编译失败（exit 1）——失败即收据：AC 格闭项 n-ac = ch 0 .fst 不归约到 zero
-- （与 LEM/UA 格同法的 stuckness 演示；对齐矩阵 F2 v2 的 AC 格机械化部分）。

module MissileFourTargetA-ProbeACZero where

open import MissileFourChargeDemo using (n-ac)
open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.Data.Nat.Base using (ℕ; zero)

test-probe-ac-zero : n-ac ≡ zero
test-probe-ac-zero = refl
