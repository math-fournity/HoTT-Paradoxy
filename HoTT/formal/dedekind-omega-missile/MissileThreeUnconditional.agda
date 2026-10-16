{-# OPTIONS --safe --cubical --guardedness #-}

-- 第四弹 · 修订片 027 §5 待核发现的核实 + M3 去条件化（更强收据）
-- claim id : CAND-F2-7-M3-UNC   (candidate, registers_new_claim semantics: 候选, 非已注册主张)
-- proof id : MP-DEDEKIND-OMEGA-M3-UNC
--
-- 027 §5 待核发现（判定表或可去 LEM）的核实结果：**属实**。
-- ℚ 的序可构造判定（`_≟_ : (m n : ℚ) → Trichotomy m n`，Cubical.Data.Rationals.Order），
-- 判定表 f : ℚ → Bool 直接由序三分定义——不需要 LEM。
-- 由此取得两条更强收据（相对 `MP-DEDEKIND-OMEGA-M3` 的条件版）：
--   1. specA-inhabited-unc : Spec_A      —— 无条件居住（无 LEM、无任何追加假设）
--   2. M3-L1-unc : ¬ (Spec_A ≃ Spec_B)   —— 识别拒绝去条件化
--
-- 债务定位同步修正（027 §5）：ℚ 层判定可计算（不收费）；理想元素本体——把判定表
-- 升格为实数层对象、完整 cut——才收费。完成义务在承载层跨界处收费。
--
-- 边界（不可漂移，027 §6/§8）：不声称 HoTT 不一致；不推翻 M3 条件版收据
-- （条件版仍真，本版更强）；「判定表合法性依赖 LEM」的旧叙事以本包为准修正。

module MissileThreeUnconditional where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; equivFun)
open import Cubical.Data.Empty.Base using (⊥)

private
  ¬_ : Type₀ → Type₀
  ¬_ A = A → ⊥

  absurd : ∀ {ℓ} {A : Type ℓ} → ⊥ → A
  absurd ()

open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)

open import Cubical.Data.Rationals.Base using (ℚ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.Data.Rationals.Order
  using (_<_; Trichotomy; _≟_; lt; eq; gt; isIrrefl<; isAsym<)
open import MissileTwoUniversalIrrationality using (2r; spec-B-empty)
open import MissileThreeVerdictCollision using (Spec_A; Spec_B)

------------------------------------------------------------------------
-- 待核发现核实：判定表无需 LEM——ℚ 序可构造判定
------------------------------------------------------------------------

specA-inhabited-unc : Spec_A
specA-inhabited-unc = f , table
  where
  f : ℚ → Bool
  f q with (q ·ℚ q) ≟ 2r
  ... | lt p = true
  ... | eq e = false
  ... | gt g = false

  table : ∀ q → Σ[ fwd ∈ (f q ≡ true → q ·ℚ q < 2r) ] (q ·ℚ q < 2r → f q ≡ true)
  table q with (q ·ℚ q) ≟ 2r
  ... | lt p  = (λ _ → p) , (λ _ → refl)
  ... | eq e  = (λ prf → absurd (true≢false (sym prf))) ,
                (λ h → absurd (isIrrefl< 2r (subst (λ w → w < 2r) e h)))
  ... | gt g  = (λ prf → absurd (true≢false (sym prf))) ,
                (λ h → absurd (isAsym< (q ·ℚ q) 2r h g))

------------------------------------------------------------------------
-- M3-L1 去条件化：核拒绝任务同一性（无 LEM、无任何追加假设）
------------------------------------------------------------------------

M3-L1-unc : ¬ (Spec_A ≃ Spec_B)
M3-L1-unc eqv = spec-B-empty (equivFun eqv specA-inhabited-unc)

------------------------------------------------------------------------
-- 债务定位（修订片 027 §5，本包为核实收据）：判定表在 ℚ 层免费（本包无条件
-- 居住即证）；理想元素本体——判定表升格为实数层对象、完整 cut——才收费。
-- 完成义务在承载层跨界处收费：债务不在数据，在升格。
------------------------------------------------------------------------
