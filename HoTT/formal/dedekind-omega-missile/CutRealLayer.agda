{-# OPTIONS --safe --cubical --guardedness --two-level #-}

-- CutRealLayer：Book §11.2「ℝ 层」精确陈述（B0 · 陈述精确化，修订片 029 §4.1）
-- claim id : CAND-F2-7-REAL-LAYER   (candidate；registers_new_claim:false)
-- proof id : MP-DEDEKIND-OMEGA-REAL-LAYER（statement 阶段，尚无证明收据）
--
-- 任务：钉死「收费命题」的精确形态（含量词、假设、宇宙层级）。
--   逐字原文：HoTT/theory-schema/upstream/book-578b85cc/reals.tex §11.2
--   （「单一命题类型 Ω」的四种取法 + Defn 11.2.1 四条件），
--   全文转写与逐字核对登记于 CLAIM-PACKAGE-REAL-LAYER.md §1。
--
-- 本模块只声明命题形态（类型），不证明 Sufficiency / Necessity：
--   (a)  充裕性 → B1a；   (b) 诊断绕过 → B1b；   (b′) 必要性 → B1b′ 或降格。
--
-- 边界（不漂移）：不声称 HoTT 不一致；不声称等价定理已证；
--   (b′) 未证前不以「击落 / 不可免费」交付（029 §2 降格条款）。

module CutRealLayer where

open import Cubical.Foundations.Prelude
-- isProp / isSet 来自 Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (hProp; isSetHProp)
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Rationals.Base using (ℚ; isSetℚ)
open import Cubical.Data.Rationals.Order using (_<_; isProp<)

private
  ¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
  ¬_ A = A → ⊥

private variable
  ℓ : Level

------------------------------------------------------------------------
-- 1. Book §11.2 的「Ω-值谓词」精确化
--
-- Book：「a cut is a pair of maps L, U : ℚ → Ω」，其中 Ω 是「a single type of
-- propositions」且「In all of the above cases Ω is a set」。
-- 精确化：Ω = 某层级 ℓ 的 hProp（每个 inhabitant 是 mere proposition，
-- 且 hProp ℓ 本身是 set —— 即 Book 所需的「Ω is a set」）。

ΩOf : (ℓ : Level) → Type (ℓ-suc ℓ)
ΩOf ℓ = hProp ℓ

------------------------------------------------------------------------
-- 2. 两种「付费方式」的精确公理形态（Book §11.2 取法 2 / 取法 3）

-- propositional resizing at level ℓ：
-- 任意 ℓ-suc ℓ 层的 mere proposition 都等价于一个 ℓ 层的 mere proposition。
PropResizing : (ℓ : Level) → Type (ℓ-suc (ℓ-suc ℓ))
PropResizing ℓ =
  (A : Type (ℓ-suc ℓ)) → (isProp A) → Σ[ B ∈ Type ℓ ] (isProp B × (A ≃ B))

-- excluded middle for mere propositions at level ℓ（使 Ω ≃ Bool 的取法）：
LEMProp : (ℓ : Level) → Type (ℓ-suc (ℓ-suc ℓ))
LEMProp ℓ =
  (A : Type (ℓ-suc ℓ)) → (isProp A) → A ⊎ (¬ A)

------------------------------------------------------------------------
-- 3. 「单一命题类型 Ω」= 收费位置的精确化
--
-- Book 的简化假设「a single type of propositions Ω is sufficient」精确化为：
-- 基层级 ℓ 上存在一个 set Ω，与 hProp ℓ 等价。
-- 关键事实（本陈述的核心）：hProp ℓ 本身活在 ℓ-suc ℓ，故
--   「在 ℓ-suc ℓ 取 Ω = hProp ℓ」= Book 取法 1（层级追踪），免费但层级上升；
--   「在 ℓ 取 Ω」= 本结构，等价于 propositional resizing 的收费。
SingleOmega : (ℓ : Level) → Type (ℓ-suc ℓ)
SingleOmega ℓ =
  Σ[ Ω ∈ Type ℓ ] (isSet Ω × (Ω ≃ hProp ℓ))

------------------------------------------------------------------------
-- 4. Book §11.2 Defn 11.2.1 四条件（逐字对应，量词显式）
--
--   inhabited : ∃ q, L(q) 且 ∃ r, U(r)
--   rounded   : L(q) ⇔ ∃ r, (q<r) ∧ L(r)；U(r) ⇔ ∃ q, (q<r) ∧ U(q)
--   disjoint  : ¬ (L(q) ∧ U(q))
--   located   : (q<r) ⇒ L(q) ∨ U(r)

dcut : {ℓ : Level} (L U : ℚ → ΩOf ℓ) → Type ℓ
dcut {ℓ} L U =
     (Σ[ q ∈ ℚ ] fst (L q))                                   -- inhabited-L
  ×  (Σ[ r ∈ ℚ ] fst (U r))                                   -- inhabited-U
  ×  ((q : ℚ) → fst (L q) ≃ (Σ[ r ∈ ℚ ] ((q < r) × fst (L r))))  -- rounded-L
  ×  ((r : ℚ) → fst (U r) ≃ (Σ[ q ∈ ℚ ] ((q < r) × fst (U q))))  -- rounded-U
  ×  ((q : ℚ) → ¬ (fst (L q) × fst (U q)))                       -- disjoint
  ×  ((q r : ℚ) → (q < r) → (fst (L q)) ⊎ (fst (U r)))           -- located

------------------------------------------------------------------------
-- 5. Dedekind reals（Book §11.2 的 RD）与「ℝ 层」收费陈述

-- RD at level ℓ：cut 对的子集型。Book：「since ℚ → Ω is a set the Dedekind
-- reals form a set too」——这一层（ℚ 层）免费，但对象活在 ℓ-suc ℓ。
DedekindReals : (ℓ : Level) → Type (ℓ-suc ℓ)
DedekindReals ℓ =
  Σ[ LU ∈ (ℚ → ΩOf ℓ) × (ℚ → ΩOf ℓ) ] dcut (fst LU) (snd LU)

-- ℝ 层陈述（收费命题）：实数作为「基层级 ℓ 上已完成的集合对象」，
-- 即 DedekindReals ℓ 等价于一个 ℓ 层的集合。
-- 这正是「把 cut 取等价类、把 ℝ 取值命题塌缩到单一 Ω」的下一升格。
ℝLayerAt : (ℓ : Level) → Type (ℓ-suc ℓ)
ℝLayerAt ℓ =
  Σ[ R ∈ Type ℓ ] (isSet R × (R ≃ DedekindReals ℓ))

------------------------------------------------------------------------
-- 6. 两个方向的命题形态（只声明，不证）
--
-- (a) 充裕性（B1a 目标）：付 resizing 即可做出 ℝ 层。
Sufficiency : (ℓ : Level) → Type _
Sufficiency ℓ = PropResizing ℓ → ℝLayerAt ℓ

-- (b′) 必要性（B1b′ 目标，路径 1「反向蕴含」候选）：
-- ℝ 层成立 ⇒ 某种基层级命题塌缩。**注意目标不是 LEM/resizing 本身**——
-- Book §11.2 另列第四出路（initial σ-frame），故「⇒ LEM 或 resizing」
-- 直接形态被 Book 自身证伪；精确目标须收窄为 SingleOmega 一类的
-- 「基层级命题塌缩」结构（见 CLAIM-PACKAGE-REAL-LAYER.md §3）。
Necessity : (ℓ : Level) → Type _
Necessity ℓ = ℝLayerAt ℓ → SingleOmega ℓ
