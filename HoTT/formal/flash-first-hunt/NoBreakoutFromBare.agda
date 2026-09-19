{-# OPTIONS --safe --cubical --guardedness --two-level #-}

module flash-first-hunt.NoBreakoutFromBare where

open import Cubical.Foundations.Prelude
  using (Level; Type; _≡_; refl)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma using (Σ; fst; snd)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (znots)
open import Cubical.Data.Unit.Base using (Unit; tt)

private
  ¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
  ¬ A = A → ⊥

------------------------------------------------------------------------
-- 参数多态定理（① 不可定义性的严格化）：
--
--   ∀ (C : Type ℓ) (p : C) → ¬ ((x : C) → ¬ (x ≡ p))
--
-- 含义：**裸载体 C 上**，断点取出函数（"对每个 x 给出 x ≢ p"）**不可构造**
-- （在参数模型 / free-theorem 意义下）：取 C := Unit、p := tt，则该函数
-- 的存在立即给出 tt ≢ tt，与 refl 矛盾。这是对**所有** C、p 一致的构造
-- 的不可行性——即「不知道 p 就无法排除 p」的参数化严格化。
--
-- 范围限定（诚实）：这是 closed-argument 不可行（Agda 的参数多态 +
-- 一个具体反例实例），不是任意实现/任意演算的不可定义性元定理。
------------------------------------------------------------------------

no-breakout-from-bare : {ℓ : Level} (C : Type ℓ) (p : C)
  → ¬ ((x : C) → ¬ (x ≡ p))
no-breakout-from-bare C p f = f p refl

-- 单位型实例化（参数化论证的具体化步骤）：
module _ where
  C₁ : Type
  C₁ = Unit
  p₁ : C₁
  p₁ = tt

  instance-absurd : ¬ ((x : C₁) → ¬ (x ≡ p₁))
  instance-absurd = no-breakout-from-bare C₁ p₁
