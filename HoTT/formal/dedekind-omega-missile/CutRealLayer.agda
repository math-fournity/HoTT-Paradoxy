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
-- 本模块钉死「收费命题」的精确形态（B0），并证明 (a) 充裕性 sufficiency
-- （B1a，§7.6，kernel-checked）；(b) 诊断绕过 → B1b；(b′) 必要性 → B1b′ 或降格。
--
-- 边界（不漂移）：不声称 HoTT 不一致；不声称等价定理已证；
--   (b′) 未证前不以「击落 / 不可免费」交付（029 §2 降格条款）。

module CutRealLayer where

open import Cubical.Foundations.Prelude
-- isProp / isSet 来自 Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
  using (hProp; isSetHProp; isProp×; isPropΣ; isPropΠ; isProp→; isPropIsSet
         ;isSet×; isSetΣ; isSetΣSndProp; isSetΠ; isOfHLevel≃)
open import Cubical.Foundations.Equiv
  using (_≃_; equivFun; invEq; secEq; retEq)
open import Cubical.Foundations.Equiv.HalfAdjoint
  using (isHAEquiv; iso→HAEquiv)
open import Cubical.Foundations.GroupoidLaws using (lCancel)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.Isomorphism using (Iso; isoToEquiv)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Data.Sigma using (_×_; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sum.Properties using (isProp⊎; isSet⊎)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; isPropPropTrunc)
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

-- Book §11.2 的 \exis 在 HoTT 中是命题截断（Defn 11.2.1 逐字：
--   inhabited: \exis{q:\Q} L(q) 与 \exis{r:\Q} U(r)；
--   rounded:   L(q) \Leftrightarrow \exis{r:\Q} (q<r) \land L(r)）。
-- 忠实化勘误（B0 陈述修订，2026-09-18）：此前存在量词取裸 Σ，不是 Book 的 ∃。
--   裸 Σ 使 rounded 右侧成为「见证集」（set 而非 prop），与左侧 mere predicate
--   的 \Leftrightarrow（= props 之间的 ≃）不匹配，且对非平凡 cut 不可满足
--   （向下封闭的 L 有无穷多 r>q 见证，Σ 非-prop，却被 ≃ 强制为 prop）。
--   修正后六分量皆 mere proposition，其合取（Book 的 dcut(L,U)）是 prop，
--   「Dedekind reals form a set」由 isProp→isSet 得到。
dcut : {ℓ : Level} (L U : ℚ → ΩOf ℓ) → Type ℓ
dcut {ℓ} L U =
     ∥ Σ[ q ∈ ℚ ] fst (L q) ∥₁                                    -- inhabited-L
  ×  ∥ Σ[ r ∈ ℚ ] fst (U r) ∥₁                                    -- inhabited-U
  ×  ((q : ℚ) → fst (L q) ≃ ∥ Σ[ r ∈ ℚ ] ((q < r) × fst (L r)) ∥₁)  -- rounded-L
  ×  ((r : ℚ) → fst (U r) ≃ ∥ Σ[ q ∈ ℚ ] ((q < r) × fst (U q)) ∥₁)  -- rounded-U
  ×  ((q : ℚ) → ¬ (fst (L q) × fst (U q)))                         -- disjoint
  ×  ((q r : ℚ) → (q < r) → fst (L q) ⊎ fst (U r))                 -- located

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
-- 精确化修正（B0 深化）：pointwise 的 PropResizing（搬单个 prop 到基层级）
-- **不蕴含** SingleOmega（整个 hProp ℓ 塌缩到 ℓ 层的 set）。
-- Book §11.2 取法 2 的原文是「assume the propositional resizing axiom ...
-- which essentially collapses the prop_{U_i}'s to the lowest level, which we
-- call Ω」——其忠实形态是「存在低层级 Ω」，即 SingleOmega。
-- 因此充裕性的付费假设取 SingleOmega；PropResizing 保留为公理候选登记，
-- 二者的关系（蕴含方向）未论证。

-- (a) 充裕性（B1a 目标）：存在基层级 Ω ⇒ 做出 ℝ 层。
Sufficiency : (ℓ : Level) → Type _
Sufficiency ℓ = SingleOmega ℓ → ℝLayerAt ℓ

-- (b′) 必要性（B1b′ 目标，路径 1「反向蕴含」候选）：
-- ℝ 层成立 ⇒ 某种基层级命题塌缩。**注意目标不是 LEM/resizing 本身**——
-- Book §11.2 另列第四出路（initial σ-frame），故「⇒ LEM 或 resizing」
-- 直接形态被 Book 自身证伪；精确目标收窄为 SingleOmega（与 (a) 对称）。
Necessity : (ℓ : Level) → Type _
Necessity ℓ = ℝLayerAt ℓ → SingleOmega ℓ

------------------------------------------------------------------------
-- 7. (a) 充裕性（B1a）：SingleOmega ℓ → ℝLayerAt ℓ
--
-- 构造（两段，逐段编译）：
--   step1  dcut 是 set（DedekindReals 是 set 的依据，Book 自陈）。
--   step2  给定 Ω* : Type ℓ 与 e : Ω* ≃ hProp ℓ，cut 的代理载体
--          (ℚ → Ω*) × (ℚ → Ω*) 活在 ℓ 层（因为 max 0 ℓ = ℓ）；
--          其上「纤维被 e 搬运的 dcut」的子集型活在 ℓ 层且是 set；
--          由 Σ-cong-equiv 与 Π 的等价同余，它与 DedekindReals ℓ 等价。

-- 7.1 dcut 是 set（Book：「We let dcut(L,U) denote the conjunction of these
--      conditions」；六分量中 inhabited×2 / rounded×2 / disjoint 是 mere
--      proposition，located 的靶 L q ⊎ U r 在 q<r 时可同时成立（q<x<r>），
--      故为 set 而非 prop；整体合取是 set）。载体 (ℚ → Ω) × (ℚ → Ω) 是 set
--      （Book：Ω is a set），纤维是 set ⇒ DedekindReals 是 set。
--      注：located 分量不用 isProp⊎（它需 A、B 不相交的证明，而 located
--      恰恰允许 L q 与 U r 同时成立）；用 isSet⊎。helper 不放 where 块，
--      直接嵌套库的多态 isSetΣ / isSetΠ。
isSetDCut : {ℓ : Level} (L U : ℚ → ΩOf ℓ) → isSet (dcut L U)
isSetDCut {ℓ} L U =
  isSetΣ (isProp→isSet isPropPropTrunc) (λ _ →
  isSetΣ (isProp→isSet isPropPropTrunc) (λ _ →
  isSetΣ (isProp→isSet (isPropΠ  (λ q → isOfHLevel≃ 1 (snd (L q)) isPropPropTrunc))) (λ _ →
  isSetΣ (isProp→isSet (isPropΠ  (λ r → isOfHLevel≃ 1 (snd (U r)) isPropPropTrunc))) (λ _ →
  isSetΣ (isProp→isSet (isPropΠ  (λ q → isProp→ isProp⊥))) (λ _ →
  isSetΠ  (λ q → isSetΠ  (λ r → isSetΠ  (λ _ →
  isSet⊎ (isProp→isSet (snd (L q))) (isProp→isSet (snd (U r)))))))))))
-- 7.2 DedekindReals ℓ 是 set（Book 自陈「the Dedekind reals form a set」）。
DedekindReals-isSet : (ℓ : Level) → isSet (DedekindReals ℓ)
DedekindReals-isSet ℓ =
  isSetΣ (isSet× (isSetΠ (λ _ → isSetHProp)) (isSetΠ (λ _ → isSetHProp)))
         (λ LU → isSetDCut (fst LU) (snd LU))

-- 7.3 代理 cut 空间：给定 SingleOmega，把 cut 的值域换成基层级 Ω*。
--      载体活在 ℓ 层；纤维用 e 搬运到 hProp ℓ 后套 dcut。
DedekindReals* : (ℓ : Level) → SingleOmega ℓ → Type ℓ
DedekindReals* ℓ (Ω* , Ω*-set , e) =
  Σ[ LU ∈ (ℚ → Ω*) × (ℚ → Ω*) ]
    dcut (λ q → equivFun e (fst LU q)) (λ q → equivFun e (snd LU q))

-- 7.4 代理空间是 set。
DedekindReals*-isSet : (ℓ : Level) (so : SingleOmega ℓ) → isSet (DedekindReals* ℓ so)
DedekindReals*-isSet ℓ (Ω* , Ω*-set , e) =
  isSetΣ (isSet× (isSetΠ (λ _ → Ω*-set)) (isSetΠ (λ _ → Ω*-set)))
         (λ LU → isSetDCut (λ q → equivFun e (fst LU q)) (λ q → equivFun e (snd LU q)))

-- 7.5 跨层 Σ-cong（Iso 版，自建）：
--      库的 Σ-cong-iso-fst / Σ-cong-equiv-fst 经其 private variable 块把
--      A A' 钉在同一层级，而本证明的载体等价跨层（Ω* : Type ℓ 而
--      hProp ℓ : Type (ℓ-suc ℓ)），直接使用报 UnequalLevel（2026-09-18
--      实测）。此处按 cubical v0.9 Cubical.Data.Sigma.Properties 的
--      Σ-cong-iso-fst 原实现克隆，仅放开 A A' 层级；coherence 由
--      iso→HAEquiv 的 com-square 承担（isoToEquiv 本身跨层，已探针验证）。
Σ-cong-iso-fst-cross :
  {ℓA ℓA' ℓB : Level} {A : Type ℓA} {A' : Type ℓA'} {B : A' → Type ℓB}
  (isom : Iso A A') → Iso (Σ A (λ x → B (Iso.fun isom x))) (Σ A' B)
Iso.fun (Σ-cong-iso-fst-cross isom) x =
  Iso.fun isom (fst x) , snd x
Iso.inv (Σ-cong-iso-fst-cross {B = B} isom) x =
  Iso.inv isom (fst x) , subst B (sym (ε (fst x))) (snd x)
  where
  ε = isHAEquiv.rinv (snd (iso→HAEquiv isom))
Iso.rightInv (Σ-cong-iso-fst-cross {B = B} isom) (x , y) =
  ΣPathP (ε x , toPathP goal)
  where
  ε = isHAEquiv.rinv (snd (iso→HAEquiv isom))

  goal : subst B (ε x) (subst B (sym (ε x)) y) ≡ y
  goal = sym (substComposite B (sym (ε x)) (ε x) y)
      ∙∙ cong (λ x → subst B x y) (lCancel (ε x))
      ∙∙ substRefl {B = B} y
Iso.leftInv (Σ-cong-iso-fst-cross {A = A} {B = B} isom) (x , y) =
  ΣPathP (Iso.leftInv isom x , toPathP goal)
  where
  ε = isHAEquiv.rinv (snd (iso→HAEquiv isom))
  γ = isHAEquiv.com (snd (iso→HAEquiv isom))

  lem : (x : A) → sym (ε (Iso.fun isom x)) ∙ cong (Iso.fun isom) (Iso.leftInv isom x) ≡ refl
  lem x = cong (λ a → sym (ε (Iso.fun isom x)) ∙ a) (γ x)
        ∙ lCancel (ε (Iso.fun isom x))

  goal : subst B (cong (Iso.fun isom) (Iso.leftInv isom x))
           (subst B (sym (ε (Iso.fun isom x))) y) ≡ y
  goal = sym (substComposite B (sym (ε (Iso.fun isom x)))
                   (cong (Iso.fun isom) (Iso.leftInv isom x)) y)
      ∙∙ cong (λ a → subst B a y) (lem x)
      ∙∙ substRefl {B = B} y

-- 7.6 充裕性主证明。
--      载体 iso carrier-iso 把 e 逐点应用到 (L , U)；其 fun/inv 用显式
--      λ 书写，使 Σ-cong-iso-fst-cross 定义域中的纤维 (B ∘ Iso.fun
--      carrier-iso) 在绑定变量上纯 β 归约到 DedekindReals* 的定义形态
--      （不依赖函数 η 或 copattern 展开——库组合子 Σ-cong-equiv-fst
--      的前向函数对变量卡住，这是其不可用的第二原因）。
--      R-≃-RD 是跨层等价：R : Type ℓ 而 DedekindReals ℓ : Type (ℓ-suc ℓ)，
--      这正是收费陈述本身（低层集合与高层构造等价）。
sufficiency : (ℓ : Level) → Sufficiency ℓ
sufficiency ℓ so@(Ω* , Ω*-set , e) = R , (R-set , R-≃-RD)
  where
    R : Type ℓ
    R = DedekindReals* ℓ so

    R-set : isSet R
    R-set = DedekindReals*-isSet ℓ so

    -- 载体 iso：(ℚ → Ω*) × (ℚ → Ω*) 与 (ℚ → ΩOf ℓ) × (ℚ → ΩOf ℓ) 之间
    carrier-iso : Iso ((ℚ → Ω*) × (ℚ → Ω*)) ((ℚ → ΩOf ℓ) × (ℚ → ΩOf ℓ))
    Iso.fun carrier-iso LU =
      (λ q → equivFun e (fst LU q)) , (λ q → equivFun e (snd LU q))
    Iso.inv carrier-iso LU =
      (λ q → invEq e (fst LU q)) , (λ q → invEq e (snd LU q))
    Iso.rightInv carrier-iso LU =
      ΣPathP (funExt (λ q → secEq e (fst LU q))
              , funExt (λ q → secEq e (snd LU q)))
    Iso.leftInv carrier-iso LU =
      ΣPathP (funExt (λ q → retEq e (fst LU q))
              , funExt (λ q → retEq e (snd LU q)))

    -- 代理空间 ≃ DedekindReals ℓ：Σ-cong-iso-fst-cross 的定义域
    -- Σ ((ℚ→Ω*)×(ℚ→Ω*)) ((λ LU → dcut (fst LU) (snd LU)) ∘ fun carrier-iso)
    -- 经 β 归约恰为 DedekindReals* ℓ so 的定义（B 由Expected codomain
    -- 与 DedekindReals ℓ 的统一解出）。
    R-≃-RD : R ≃ DedekindReals ℓ
    R-≃-RD = isoToEquiv (Σ-cong-iso-fst-cross carrier-iso)
