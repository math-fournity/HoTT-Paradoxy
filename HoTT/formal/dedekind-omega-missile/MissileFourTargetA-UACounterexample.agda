{-# OPTIONS --cubical --guardedness #-}
-- 注意：本文件刻意不带 --safe。ua 是公理注入点——注入本身即演示内容。

-- 第四弹 · 靶 A 路径 (i) 主模块：UA-作公理 → canonicity 破坏的最小反例
-- （修订片 027 §3.1 靶 A / CanonicityCounterexample-DESIGN.md 构造草图三步）
--
-- e : Bool ≡ Bool 由 ua 公理给出（无计算规则），transport 沿 e 不再可约简，
-- 闭 ℕ 项 n = if transport e true then 0 else 1 卡在公理上——既非 zero 也非
-- suc _ 的范式。卡住的机械化证据 = 两个预期失败探针（ProbeZero/ProbeSucZero）
-- 与一个对照探针（ProbeControl），见各自文件头与 runs/TA-01..04。

module MissileFourTargetA-UACounterexample where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; if_then_else_)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)

postulate
  ua : ∀ {A B : Set} → (f : A → B) → (g : B → A) → (∀ b → f (g b) ≡ b) → (∀ a → g (f a) ≡ a) → A ≡ B

not-not : ∀ b → not (not b) ≡ b
not-not true  = refl
not-not false = refl

e : Bool ≡ Bool
e = ua not not not-not not-not

b' : Bool
b' = subst (λ X → X) e true

n : ℕ
n = if b' then zero else suc zero
