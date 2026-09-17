{-# OPTIONS --cubical --guardedness #-}

-- 第四弹 · 靶 A 路径 (i) 对照探针（预期 exit 0）：构造子与自身可互换——
-- 证明探针方法本身在「可转换」时正确放行（与 ProbeZero/ProbeSucZero 的失败对照）。

module MissileFourTargetA-ProbeControl where

open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.Data.Nat.Base using (ℕ; zero)

test-control : zero ≡ zero
test-control = refl
