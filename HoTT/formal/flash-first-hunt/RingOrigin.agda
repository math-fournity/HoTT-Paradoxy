{-# OPTIONS --safe --cubical --guardedness --two-level #-}

-- RingOrigin：圆环主线单元一（Flash 第一次寻找尝试，2026-09-19）
-- claim id : CAND-G4-RING-ORIGIN (candidate；registers_new_claim:false)
-- 任务合同：001 片。R 判据形式化第一步——「来源携带胚型」的最小类型化。
--
-- 数学内容（用户 2026-09-19 开火令的形式化）：
--   用户判定：M（圆去点）不是线段，而是「圆上拿掉一点」的来源胚型；
--   其断点信息（两个端点 + 被拿掉的点）是 M 的固有部分，N=(0,1) 不携带。
--   本模块给出该直觉的**最小 HoTT 形态**：
--     SourceCarrier C p := Σ[ x ∈ C ] (x ≡ p → ⊥) ——「去点载体」：
--       一个点 x 加上「x 不是被拿走的点」的证据（来源信息的核心）。
--   正控制：携带来源的合法构造（给定 C、p 与 x≢p，元素可构造）——
--       --safe 零公理过核即证「来源携带不是 postulate」。
--   靶形：取出「断点排除证据」需要 p 在场。裸载体 C（没有来源记录）上
--       该取出的参数化类型缺席——以参数化类型差异陈述；不可定义性的
--       完整证明留下一单元（需函发性/元层论证，本模块不做 ∀ 主张）。
--
-- 边界：本模块不声称 S¹(HIT) 与点集圆的同一；不声称找到 HoTT 共同体的
-- 实际植入现场；不声称圆环悖论完整形式化。无全称新主张。

module RingOrigin where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma using (Σ; fst; snd)

private
  ¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
  ¬ A = A → ⊥

------------------------------------------------------------------------
-- 1. 去点载体（来源携带的最小形态）
------------------------------------------------------------------------

SourceCarrier : {ℓ : Level} (C : Type ℓ) (p : C) → Type ℓ
SourceCarrier C p = Σ[ x ∈ C ] (¬ (x ≡ p))

------------------------------------------------------------------------
-- 2. 正控制：来源携带是合法构造（零 postulate）
------------------------------------------------------------------------

module _ {ℓ : Level} {C : Type ℓ} (p : C) where

  postulate-free-build : (x : C) → ¬ (x ≡ p) → SourceCarrier C p
  postulate-free-build x x≢p = x , x≢p

------------------------------------------------------------------------
-- 3. 靶形：断点三件套在 M 侧可取出（p 作为来源记录在类型中）
------------------------------------------------------------------------

BreakoutFromM : {ℓ : Level} (C : Type ℓ) (p : C) → Type ℓ
BreakoutFromM C p = (x : SourceCarrier C p) → Σ[ y ∈ C ] (¬ (y ≡ p))

breakout-witness : {ℓ : Level} (C : Type ℓ) (p : C)
  → BreakoutFromM C p
breakout-witness C p x = x .fst , x .snd

------------------------------------------------------------------------
-- 4. 具体实例正控（ℤ，p := pos 0）
------------------------------------------------------------------------

open import Cubical.Data.Int.Base using (ℤ; pos)
open import Cubical.Data.Int.Properties using (discreteℤ; injPos)

0z : ℤ
0z = pos 0

pos1≢pos0 : ¬ (pos 1 ≡ pos 0)
pos1≢pos0 h = ℕ0≢ℕ1 (sym (injPos h))
  where
  open import Cubical.Data.Nat.Base using (ℕ; suc; zero)
  open import Cubical.Data.Nat.Properties using (znots)
  ℕ0≢ℕ1 : ¬ (zero ≡ suc zero)
  ℕ0≢ℕ1 = znots

instance-witness : SourceCarrier ℤ 0z
instance-witness = pos 1 , pos1≢pos0
