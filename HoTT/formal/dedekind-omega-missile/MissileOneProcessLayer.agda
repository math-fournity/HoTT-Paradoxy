{-# OPTIONS --safe --cubical --guardedness #-}

-- 第一枚导弹（过程层）· Dedekind-Ω 簇 / √2 cut
-- claim id : CAND-F2-7-M1   (candidate, registers_new_claim semantics: 候选, 非已注册主张)
-- proof id : MP-DEDEKIND-OMEGA-M1
--
-- 弹种（023 片 §2）：过程层——P 在 ℚ 上不可完成。
-- 过程 P：对 √2 的 Dedekind cut，把两端（下集/上集）夹到相遇。
-- 机械证据：√2 的最优有理夹钳（Pell 连分数收敛子 p_n/q_n）满足
--           判别式 D n = p_n² - 2·q_n² ≡ ±1，对任意 n 都**不为 0**——
--           即夹钳缝隙在任何步数后都不闭合（可推广到任意有理夹钳序列的下界）。
--
-- 本模块的边界（不可漂移）：
--   * 这不是 HoTT 的内部矛盾，也不声称 HoTT 不一致（repo 纪律 + 008 片 §6）。
--   * 这是「过程层不可完成」的机械锚点；声明层（第二枚）见 CLAIM-PACKAGE.md。
--   * 未证明 ∀ q ∈ ℚ, q² ≠ 2（需另立下降引理）；本模块证明的是这条最优夹钳
--     序列的永不闭合，是 008 片 §2「构造一个具体 cut 及其有理逼近序列,
--     核验其不收敛」的精确化。

module MissileOneProcessLayer where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)

private
  ¬_ : Type₀ → Type₀
  ¬_ A = A → ⊥
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Int.Base as ℤ hiding (_+_ ; _·_ ; _-_ ; -_)
open import Cubical.Data.Int.Properties using (injPos; posNotnegsuc)
open import Cubical.Data.Nat.Properties using (znots)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)

open import Cubical.Algebra.CommRing
open import Cubical.Algebra.CommRing.Instances.Int
open import Cubical.Tactics.CommRingSolver
open CommRingStr (ℤCommRing .snd)

-- ℤ 在此结构下的运算即 ℤ 原生 _+ℤ_ / _·ℤ_ / -ℤ_；1r = pos 1, 0r = pos 0。
private
  variable
    p q : ℤ

------------------------------------------------------------------------
-- √2 的 Pell 夹钳序列（连分数收敛子：每个分母量级上的最优有理逼近）
------------------------------------------------------------------------

mutual
  pellP : ℕ → ℤ
  pellP zero      = 1r
  pellP (suc n)   = pellP n + ((1r + 1r) · pellQ n)

  pellQ : ℕ → ℤ
  pellQ zero      = 1r
  pellQ (suc n)   = pellP n + pellQ n

-- 判别式 D n = p_n² - 2·q_n²。写成「加负元」以避开环求解器对二元减号的展开限制。
D : ℕ → ℤ
D n = (pellP n · pellP n) + (- ((1r + 1r) · (pellQ n · pellQ n)))

-- 交替符号 ±1（判别式的「应是值」）
sign : ℕ → ℤ
sign zero     = - 1r
sign (suc n)  = - (sign n)

------------------------------------------------------------------------
-- 环恒等式：(p + 2q)² - 2·(p + q)² ≡ -(p² - 2q²)
-- 唯一的非平凡步骤；由 CommRingSolver 反射求解，避免手写环链。
------------------------------------------------------------------------

D-step-identity : (p q : ℤ) →
  (  (p + ((1r + 1r) · q)) · (p + ((1r + 1r) · q))
   + (- ((1r + 1r) · ((p + q) · (p + q))) ) )
  ≡
  ( - ( (p · p) + (- ((1r + 1r) · (q · q))) ) )
D-step-identity p q = solve! ℤCommRing

-- 提升到序列：D (suc n) ≡ - (D n)（定义性归约 pellP/pellQ 的递推后逐字成立）
D-step : (n : ℕ) → D (suc n) ≡ - (D n)
D-step n = D-step-identity (pellP n) (pellQ n)

------------------------------------------------------------------------
-- 主不变量：D n ≡ sign n（即判别式恒为交替的 ±1）
------------------------------------------------------------------------

D-invariant : (n : ℕ) → D n ≡ sign n
D-invariant zero    = solve! ℤCommRing
D-invariant (suc n) = D-step n ∙ cong -_ (D-invariant n)

-- 符号的形状：sign n 恰为 +1 或 -1
sign-shape : (n : ℕ) → (sign n ≡ 1r) ⊎ (sign n ≡ - 1r)
sign-shape zero    = inr refl
sign-shape (suc n) with sign-shape n
... | inl h = inr (cong -_ h)
... | inr h = inl (cong -_ h)

------------------------------------------------------------------------
-- 主定理：最优有理夹钳的缝隙永不闭合
------------------------------------------------------------------------

pell-gap-never-closes : (n : ℕ) → (D n ≡ 1r) ⊎ (D n ≡ - 1r)
pell-gap-never-closes n with D-invariant n
... | h with sign-shape n
...   | inl s = inl (h ∙ s)
...   | inr s = inr (h ∙ s)

-- 推论：判别式永不为 0，即夹钳两端永不相遇（过程 P 在 ℚ 上不可完成）

pos0≢pos1 : ¬ (pos 0 ≡ pos 1)
pos0≢pos1 h = znots (injPos h)

pos0≢negsuc0 : ¬ (pos 0 ≡ negsuc 0)
pos0≢negsuc0 = posNotnegsuc 0 0

gap-never-zero : (n : ℕ) → ¬ (D n ≡ pos 0)
gap-never-zero n hyp with pell-gap-never-closes n
... | inl h = pos0≢pos1 (sym hyp ∙ h)
... | inr h = pos0≢negsuc0 (sym hyp ∙ h)
