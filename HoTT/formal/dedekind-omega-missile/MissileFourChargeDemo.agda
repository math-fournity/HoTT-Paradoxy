{-# OPTIONS --cubical --guardedness #-}
-- 注意：本文件刻意不带 --safe。postulate 是公理的注入点——去掉 --safe 不是疏忽，
-- 而是本演示的全部内容：经典理想元素以公理身份注入引擎后，闭项可以卡在公理上。

-- 第四弹 · 靶 B 支撑演示：公理/公设注入的最小实例（Astra 一审 A04 采纳后的
-- 精确命名：**不受限排中公设（LEM∞ 型）格 / 现成选择函数公设格**）。
-- 精确身份：本文件的 LEM : (A : Set) → A ⊎ (A → ⊥) 是对**所有类型**的排中
-- （Book §3.4 称 LEM∞），**不是**限于 mere propositions 的 LEM₋₁；
-- Book thm:not-lem（logic.tex:234，SOURCE_REPORTED）：LEM∞ 与 univalence
-- 不相容——本模块运行于 --cubical（原生 UA）下，按 Book 该组合不一致
-- （不一致性未在本 repo 形式化重跑；stuckness 演示不依赖该不一致性）。
-- AC 格实为**现成选择函数** postulate（非"截断存在→整体选择"的 AC 原则）。
-- 修订片 027 §2.2 定义三 + 对齐矩阵 F2 v1 的机械化演示件（演示身份，非
-- Book 标准公理的忠实实例；标准 LEM₋₁ 样例为义务 R2，未完成）。
--
-- 它证明什么：postulate 注入后，内核照样接受**闭的** ℕ 项 n-lem / n-ac——
-- 但这两个项的头部符号是公理应用（中性项），不是 zero/suc 构造子：
-- canonicity（完成义务）被收费。这就是「显式假设」格的机械形态。
-- 它不证明什么：本文件不给出「不可归约」的内部证明（那是元层性质——
-- 靶 A 的设计问题，见 CanonicityCounterexample-DESIGN.md）；也不声称 HoTT 不一致
-- （公理注入导致的非规范是已知元定理现象，非矛盾）。

module MissileFourChargeDemo where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)

------------------------------------------------------------------------
-- 收费演示一（LEM 格）：公理化排中律注入后，闭项 n-lem 卡在公理应用上
------------------------------------------------------------------------

postulate
  LEM : (A : Set) → A ⊎ (A → ⊥)

n-lem : ℕ
n-lem with LEM ℕ
... | inl x = x
... | inr _ = zero

------------------------------------------------------------------------
-- 收费演示二（AC 格）：对公理化命题族的选择函数，闭项 n-ac 同样卡在公理上
------------------------------------------------------------------------

postulate
  P  : ℕ → ℕ → Set
  ch : (n : ℕ) → Σ[ k ∈ ℕ ] P n k

n-ac : ℕ
n-ac = ch 0 .fst

------------------------------------------------------------------------
-- 对照组（完成义务的免费侧，027 §5 债务定位）：ℚ 层判定不收费——
-- 见 MissileThreeUnconditional.agda（判定表无 LEM 无条件构造）。
-- 本演示与该收据合读：收费是选择性的——经典理想元素收费，构造性原则免费；
-- 且收费点在「公理注入/承载层升格」处，不在数据本身。
------------------------------------------------------------------------
