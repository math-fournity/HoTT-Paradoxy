{-# OPTIONS --safe --cubical --guardedness #-}

-- 第三枚导弹（识别层）· Dedekind-Ω 簇 / 「读出」与「算出」的判定对撞
-- claim id : CAND-F2-7-M3   (candidate, registers_new_claim semantics: 候选, 非已注册主张)
-- proof id : MP-DEDEKIND-OMEGA-M3
--
-- 弹种（025 片 §3/§5）：识别层——核证明「读出任务」与「算出任务」的规格类型不等价。
--   Spec_A（读出）：√2 的判定表作为给定数据；答案存在输入里，读出是一步操作。
--   Spec_B（算出）：交付类型 Σ (q : ℚ), q·q ≡ 2r（第二枚已证居住性为空）。
--   M3-L1 : LEMᵒ → ¬ (Spec_A ≃ Spec_B)——若二者等价，等价映射传输居住性，
--           Spec_A 居住 ⟹ Spec_B 居住，与第二枚矛盾。
--
-- LEM 的地位（025 片 §1.2/§2，逐字标注不藏在「显然」里）：Spec_A 的居住性
-- 依赖 LEM。这正是 Book §11.2 Ω 依赖链的具体体现：实数取值命题要塌缩到
-- 单一 Ω，必须假设 resizing 或 LEM——「实数已完成」的身份逻辑上依赖
-- 「命题判定已完成」。本包把该依赖作为显式假设。
--
-- 边界（不可漂移，025 片 §6）：
--   * 本引理不是 HoTT 内部矛盾。它证明的是「A=B 不可得」：对最自然的判据 J
--     （规格类型等价），用户第③件事被核否定。理论把 A、B 当同一任务使用的
--     位置在前提层，由逼选结构（025 片 §3.2）定位：要么放弃「实数位置已确定」
--     的工作方式，要么在核可证的 Spec_A ≄ Spec_B 之上仍以同一性使用二者——
--     两支都命中，无处逃逸。
--   * 不声称爆炸原理被点燃；不声称 HoTT 不一致；不声称 HoTT 崩塌。

module MissileThreeVerdictCollision where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; equivFun)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)

private
  ¬_ : Type₀ → Type₀
  ¬_ A = A → ⊥

  absurd : ∀ {ℓ} {A : Type ℓ} → ⊥ → A
  absurd ()

open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)

open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.Data.Rationals.Order using (_<_; isProp<)
open import MissileTwoUniversalIrrationality using (2r; spec-B-empty)

------------------------------------------------------------------------
-- LEM（显式假设；Ω 依赖链的具体体现，见文件头）
------------------------------------------------------------------------

LEMᵒ : Type₁
LEMᵒ = (A : Type₀) → isProp A → A ⊎ (A → ⊥)

------------------------------------------------------------------------
-- 两个规格：同一任务（确定 √2 的有理位置）的两种读法（025 片 §2）
------------------------------------------------------------------------

-- Spec_B（算出）：只准用 ℚ 与其算术，不给 cut；停机条件 = 输出那个有理位置。
-- （第二枚已机械证明其居住性为空：不是「还没停」，是「不可能停」。）
Spec_B : Type₀
Spec_B = Σ[ q ∈ ℚ ] q ·ℚ q ≡ 2r

-- Spec_A（读出）：√2 的判定表作为给定数据。A 的合法性完全来自
-- 「把理想元素当作已到手的输入」——即 023 片要求预先生成、025 片升格为
-- A 的定义的那个反弹：「实数就是 cut，直接读」。
-- 布尔表对应 Book §11.2 的 Ω ≡ Bool 塌缩读法（LEM 之下）。
Spec_A : Type₀
Spec_A = Σ[ f ∈ (ℚ → Bool) ]
           (∀ q → Σ[ fwd ∈ (f q ≡ true → q ·ℚ q < 2r) ] (q ·ℚ q < 2r → f q ≡ true))

------------------------------------------------------------------------
-- ① A 合法（数据层）：LEM 假设下判定表居住——显式假设构造
------------------------------------------------------------------------

specA-inhabited : LEMᵒ → Spec_A
specA-inhabited lem = f , table
  where
  P : ℚ → Type₀
  P q = q ·ℚ q < 2r
  isP : ∀ q → isProp (P q)
  isP q = isProp< (q ·ℚ q) 2r
  f : ℚ → Bool
  f q with lem (P q) (isP q)
  ... | inl _ = true
  ... | inr _ = false
  table : ∀ q → Σ[ fwd ∈ (f q ≡ true → P q) ] (P q → f q ≡ true)
  table q with lem (P q) (isP q)
  ... | inl p  = (λ _ → p) , (λ _ → refl)
  ... | inr np = (λ prf → absurd (true≢false (sym prf))) , (λ h → absurd (np h))

------------------------------------------------------------------------
-- ③ M3-L1：核拒绝「读出 = 算出」这一任务同一性
------------------------------------------------------------------------

M3-L1 : LEMᵒ → ¬ (Spec_A ≃ Spec_B)
M3-L1 lem eq = spec-B-empty (equivFun eq (specA-inhabited lem))

------------------------------------------------------------------------
-- 逼选结构的机械两侧（025 片 §3.2；本包固定其核侧事实）
--
--   要么理论放弃「实数位置已确定」的工作方式（A 不再冒充 B 的完成）——
--     §11.2 实数层失去「已完成」身份；
--   要么理论保留该工作方式——那么它在 M3-L1（LEMᵒ 假设下）明知的
--     Spec_A ≄ Spec_B 之上仍以同一性使用二者：非现实性在被使用的位置上
--     被机械暴露。
--
-- 三枚的层关系：第一枚 = 过程层（M1，缝隙永不闭合）；
--               第二枚 = 声明层（M2，Spec_B 为空）；
--               第三枚 = 识别层（本包，Spec_A ≄ Spec_B）。链式：M3 消费 M2。
------------------------------------------------------------------------
