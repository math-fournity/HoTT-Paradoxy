{-# OPTIONS --safe --cubical --guardedness #-}

-- CutInfra：金形态 cut 的 ℚ 序算术基础设施（CutGoldForm-DESIGN §5 步骤 2）
-- claim id : CAND-F2-7-GOLD-INFRA（candidate，构造基础设施，非已注册主张）
-- proof id : MP-DEDEKIND-OMEGA-GOLD（与 CutGoldForm 共用发射单元）
--
-- 内容：
--   * <-≤          ：ℚ 严格序弱化为非严格序
--   * ·-mono-≤-nn  ：非负乘子保持 ≤（crux；DESIGN §3 定案的 ℤ.≤-·o 商表示路线）
--   * ·-mono-<-nn  ：正乘子保持 <（strict 版；located/rounded 需要）
--
-- 路线（交接文档 0022 §二.1 / DESIGN §3）：ℚ 无乘法单调性引理（solver 路线已
-- 否决：ℚCommRing 挂 QuoQ 异型 ℚ）；经 elimProp3 降到代表元 (ℤ × ℕ₊₁)，
-- 0 ≤ k 提取分子非负见证 j，全部交乘归约为 ℤ 层 ≤-·o + pos·pos 重排。
--
-- 边界：本模块是 ℚ 层标准序算术，不依赖 univalence / cubical path / HIT
-- 特有规则（set quotient 为标准构造）；不声称 HoTT 内部矛盾。

module CutInfra where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)

open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_; _·_)
open import Cubical.Data.Nat.Properties using (·-comm)

open import Cubical.Data.Int.Base
  using (ℤ; pos; negsuc; sucℤ; _+pos_)
  renaming (_·_ to _·z_)
open import Cubical.Data.Int.Properties
  using (·Comm; ·Assoc; ·IdR; pos·pos)

open import Cubical.Data.Int.Order
  using (≤-·o; 0≤o→≤-·o; <-·o; 0<o→<-·o; <-weaken; isTrans≤; isTrans<; isAsym<; isIrrefl<)
  renaming (_≤_ to _≤z_; _<_ to _<z_)

open import Cubical.Data.NatPlusOne.Base using (ℕ₊₁; ℕ₊₁→ℕ; 1+_)
open import Cubical.Data.NatPlusOne.Properties using (_·₊₁_)

open import Cubical.Data.Rationals.Base
  using (ℚ; [_]; [_/_]; eq/⁻¹; ℕ₊₁→ℤ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.Data.Rationals.Order
  using (_≤_; _<_; isProp≤; isProp<; Trichotomy; _≟_; isTrans<; isAsym<; isIrrefl<)

open import Cubical.HITs.SetQuotients.Properties using (elimProp; elimProp2; elimProp3)

------------------------------------------------------------------------
-- 私有小件
------------------------------------------------------------------------

private
  1⁺ : ℕ₊₁
  1⁺ = 1+ zero

  0r : ℚ
  0r = [ pos 0 / 1⁺ ]

  2r : ℚ
  2r = [ pos (suc (suc zero)) / 1⁺ ]

  isPropΠp : {A : Type₀} {B : A → Type₀} → (∀ a → isProp (B a)) → isProp ((a : A) → B a)
  isPropΠp isB f g i a = isB a (f a) (g a) i

  isPropΠ2p : {A B : Type₀} {C : A → B → Type₀}
             → (∀ a b → isProp (C a b)) → isProp (∀ a b → C a b)
  isPropΠ2p isC f g i a b = isC a b (f a b) (g a b) i

  -- ℕ₊₁ 乘法过映射：与 M2 同款（构造子上定义性）
  ℕ₊₁→ℕ-·₊₁ : ∀ a b → ℕ₊₁→ℕ (a ·₊₁ b) ≡ ℕ₊₁→ℕ a ℕ.· ℕ₊₁→ℕ b
  ℕ₊₁→ℕ-·₊₁ (1+ m) (1+ n) = refl

  +pos-pos0 : ∀ (n : ℕ) → pos 0 +pos n ≡ pos n
  +pos-pos0 zero = refl
  +pos-pos0 (suc n) = cong sucℤ (+pos-pos0 n)

------------------------------------------------------------------------
-- 严格序弱化
------------------------------------------------------------------------

<-≤ : ∀ m n → m < n → m ≤ n
<-≤ = elimProp2 {P = λ x y → x < y → x ≤ y}
       (λ x y → isPropΠp (λ _ → isProp≤ x y))
       λ { (a , b) (c , d) h → <-weaken h }

------------------------------------------------------------------------
-- crux：非负乘子保持 ≤（DESIGN §3 定案的 ≤-·o 商表示路线）
------------------------------------------------------------------------

private
  -- ℤ 重排一：(x·z pos y)·z pos r ≡ x·z pos(r·y)
  stepA : ∀ (x : ℤ) (y r : ℕ) → (x ·z pos y) ·z pos r ≡ x ·z pos (r ℕ.· y)
  stepA x y r =
    sym (·Assoc x (pos y) (pos r))
      ∙ cong (x ·z_) (sym (pos·pos y r) ∙ cong pos (·-comm y r))

  -- ℤ 重排二：x·z pos((j·y)·r) ≡ (pos j·z x)·z pos(y·r)
  stepB : ∀ (x : ℤ) (j y r : ℕ)
        → x ·z pos ((j ℕ.· y) ℕ.· r) ≡ (pos j ·z x) ·z pos (y ℕ.· r)
  stepB x j y r =
    cong (x ·z_) (pos·pos (j ℕ.· y) r)
      ∙ cong (λ X → x ·z (X ·z pos r)) (pos·pos j y)
      ∙ ·Assoc x (pos j ·z pos y) (pos r)
      ∙ cong (λ U → U ·z pos r) (·Assoc x (pos j) (pos y))
      ∙ cong (λ X → (X ·z pos y) ·z pos r) (·Comm x (pos j))
      ∙ sym (·Assoc (pos j ·z x) (pos y) (pos r))
      ∙ cong (λ W → (pos j ·z x) ·z W) (sym (pos·pos y r))

·-mono-≤-nn : ∀ k a b → 0r ≤ k → a ≤ b → k ·ℚ a ≤ k ·ℚ b
·-mono-≤-nn =
  elimProp3 {P = λ k a b → 0r ≤ k → a ≤ b → k ·ℚ a ≤ k ·ℚ b}
    (λ k a b → isPropΠ2p (λ _ _ → isProp≤ (k ·ℚ a) (k ·ℚ b)))
    λ { (p , m) (a , b) (c , d) h0 hab →
      let j  = fst h0
          pp : pos j ≡ p
          pp = sym (+pos-pos0 j) ∙ snd h0 ∙ ·IdR p
          dm = ℕ₊₁→ℕ m
          db = ℕ₊₁→ℕ b
          dd = ℕ₊₁→ℕ d
          w  = j ℕ.· dm
          -- 交乘归约：hab 两侧乘 pos w（w 由 0≤k 的分子见证 j 与 k 的正分母合成，恒非负）
          mono : (a ·z pos dd) ·z pos w ≤z (c ·z pos db) ·z pos w
          mono = ≤-·o {k = w} hab
          mono' : a ·z pos (w ℕ.· dd) ≤z c ·z pos (w ℕ.· db)
          mono' = subst2 _≤z_ (stepA a dd w) (stepA c db w) mono
          -- 抬回 k 的分子：pos j 经 pp 传输为 p
          final : (pos j ·z a) ·z pos (dm ℕ.· dd) ≤z
                  (pos j ·z c) ·z pos (dm ℕ.· db)
          final = subst2 _≤z_ (stepB a j dm dd) (stepB c j dm db) mono'
          P : ℤ → Type₀
          P q = (q ·z a) ·z pos (dm ℕ.· dd) ≤z (q ·z c) ·z pos (dm ℕ.· db)
          atp : P p
          atp = subst P pp final
      in  subst2 (λ X Y → (p ·z a) ·z X ≤z (p ·z c) ·z Y)
                 (sym (cong pos (ℕ₊₁→ℕ-·₊₁ m d))) (sym (cong pos (ℕ₊₁→ℕ-·₊₁ m b))) atp }

------------------------------------------------------------------------
-- crux（strict）：正乘子保持 <
------------------------------------------------------------------------

private
  +pos-pos1 : ∀ (n : ℕ) → pos 1 +pos n ≡ pos (suc n)
  +pos-pos1 zero = refl
  +pos-pos1 (suc n) = cong sucℤ (+pos-pos1 n)

  zero<pos : ∀ (n : ℕ) → pos 0 <z pos (suc n)
  zero<pos n = n , +pos-pos1 n

·-mono-<-nn : ∀ k a b → 0r < k → a < b → k ·ℚ a < k ·ℚ b
·-mono-<-nn =
  elimProp3 {P = λ k a b → 0r < k → a < b → k ·ℚ a < k ·ℚ b}
    (λ k a b → isPropΠ2p (λ _ _ → isProp< (k ·ℚ a) (k ·ℚ b)))
    λ { (p , 1+ dm₀) (a , b) (c , d) h0 hab →
      let dm = ℕ₊₁→ℕ (1+ dm₀)
          db = ℕ₊₁→ℕ b
          dd = ℕ₊₁→ℕ d
          j  = fst h0
          pp : pos (suc j) ≡ p
          pp = sym (+pos-pos1 j) ∙ snd h0 ∙ ·IdR p
          w  = (suc j) ℕ.· dm
          -- 0 < pos w：w = suc j · dm 定义性归约为 suc (dm₀ + j·suc dm₀)，pos 恒正（显式见证）
          mono : (a ·z pos dd) ·z pos w <z (c ·z pos db) ·z pos w
          mono = 0<o→<-·o {o = pos w} (zero<pos (dm₀ ℕ.+ j ℕ.· suc dm₀)) hab
          mono' : a ·z pos (w ℕ.· dd) <z c ·z pos (w ℕ.· db)
          mono' = subst2 _<z_ (stepA a dd w) (stepA c db w) mono
          final : (pos (suc j) ·z a) ·z pos (dm ℕ.· dd) <z
                  (pos (suc j) ·z c) ·z pos (dm ℕ.· db)
          final = subst2 _<z_ (stepB a (suc j) dm dd) (stepB c (suc j) dm db) mono'
          P : ℤ → Type₀
          P q = (q ·z a) ·z pos (dm ℕ.· dd) <z (q ·z c) ·z pos (dm ℕ.· db)
          atp : P p
          atp = subst P pp final
      in  subst2 (λ X Y → (p ·z a) ·z X <z (p ·z c) ·z Y)
                 (sym (cong pos (ℕ₊₁→ℕ-·₊₁ (1+ dm₀) d)))
                 (sym (cong pos (ℕ₊₁→ℕ-·₊₁ (1+ dm₀) b))) atp }
