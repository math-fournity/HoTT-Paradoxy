{-# OPTIONS --safe --cubical --guardedness --two-level #-}

module flash-first-hunt.BreakpointBridge where

open import Cubical.Foundations.Prelude
  using (Level; Type; _≡_; sym; Σ-syntax)
open import Cubical.Data.Sigma using (_,_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Int.Base using (ℤ; pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Nat.Base using (ℕ; suc; zero)
open import Cubical.Data.Nat.Properties using (znots)

private
  ¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
  ¬ A = A → ⊥

------------------------------------------------------------------------
-- 1. 排除载体（ℝ 层线形态；与 RingOrigin.SourceCarrier 同型）
------------------------------------------------------------------------

ExcludedCarrier : {ℓ : Level} (C : Type ℓ) (r : C) → Type ℓ
ExcludedCarrier C r = Σ[ q ∈ C ] (¬ (q ≡ r))

------------------------------------------------------------------------
-- 2. 桥命题（同一 Σ 类型的两线重述；t → t 的恒等即桥）
------------------------------------------------------------------------

bridge : {ℓ : Level} {C : Type ℓ} {r : C}
  → ExcludedCarrier C r → ExcludedCarrier C r
bridge x = x

------------------------------------------------------------------------
-- 3. 实例正控：ℤ∖{0} 非空，排除证据构造性
--    （pos 1 ≡ pos 0 ⟹ 1 ≡ 0 (ℕ) 经 injPos；与 znots 矛盾）
------------------------------------------------------------------------

0z : ℤ
0z = pos 0

pos1≢pos0 : ¬ (pos 1 ≡ pos 0)
pos1≢pos0 h = znots (sym (injPos h))

ℤ-excluded : ExcludedCarrier ℤ 0z
ℤ-excluded = pos 1 , pos1≢pos0
