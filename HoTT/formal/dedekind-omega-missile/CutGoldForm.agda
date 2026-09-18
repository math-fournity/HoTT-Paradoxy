{-# OPTIONS --safe --cubical --guardedness #-}

-- CutGoldForm：√2 的金形态 Dedekind cut（Ω/hProp 值 L/U + 四条件，Book §11.2）
-- claim id : CAND-F2-7-GOLD     (candidate，构造，非已注册主张)
-- proof id : MP-DEDEKIND-OMEGA-GOLD
--
-- 设计依据：CutGoldForm-DESIGN.md（§2 勘误版：U 带正性合取）。
--   L q := (q < 0r) ⊎ ((0r ≤ q) × (q·ℚq < 2r))   两支不相容，hProp 可证
--   U q := (0r < q) × (2r < q·ℚq)                正性合取显式在场
-- 四条件（全部 ℚ 层构造，无 LEM/resizing 假设）：
--   inhabited L / inhabited U / disjoint (L q → U r → q < r) /
--   rounded (L↔ / U↔ 双向) / located (q < r → L q ⊎ U r)
-- crux 消费：CutInfra.·-mono-≤-nn / ·-mono-<-nn（非负/正乘子保序）。
-- LEM 收费位置（仅登记，不机械化）：Book §11.2 把 cut 取等价类、把「ℝ 取值
-- 命题」塌缩到单一 Ω 的下一步需要 LEM 或 propositional resizing；本模块的
-- ℚ 层四条件全部可构造（与 M3-UNC 的「ℚ 层免费」一致）。
--
-- 边界：本模块不声称 HoTT 内部矛盾；「击毁」= 非现实锚定，非不一致。

module CutGoldForm where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (hProp)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sum.Properties using (isProp⊎)
open import Cubical.Data.Sigma using (_×_)

open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_; _·_)
open import Cubical.Data.Nat.Properties using (+-zero; +-suc; +-comm; ·-comm)
open import Cubical.Data.Nat.Order using (suc-≤-suc)
  renaming (_≤_ to _≤ℕ_; _<_ to _<ℕ_)

open import Cubical.Data.Int.Base
  using (ℤ; pos; negsuc; sucℤ; _+pos_)
  renaming (_·_ to _·z_)
open import Cubical.Data.Int.Properties
  using (·Comm; ·Assoc; ·IdR; pos·pos; posNotnegsuc; injPos)
open import Cubical.Data.Int.Order
  using ()
  renaming (_≤_ to _≤z_; _<_ to _<z_)

open import Cubical.Data.NatPlusOne.Base
open import Cubical.Data.NatPlusOne.Properties using (_·₊₁_)

open import Cubical.Data.Rationals.Base
  using (ℚ; [_]; [_/_]; eq/; eq/⁻¹; ℕ₊₁→ℤ)
open import Cubical.Data.Rationals.Properties
  using (-Invol)
  renaming (_·_ to _·ℚ_; ·Comm to ·ℚcomm; _+_ to _+ℚ_; -_ to -ℚ_; _-_ to _-ℚ_
            ;·Assoc to ·ℚassoc; ·IdR to ·ℚidR; ·IdL to ·ℚidL
            ;·AnnihilL to ·ℚannihilL; ·AnnihilR to ·ℚannihilR
            ;·DistL+ to ·ℚdistL+; ·DistR+ to ·ℚdistR+
            ;+Comm to +ℚcomm; +IdL to +ℚidL; +IdR to +ℚidR
            ;+Assoc to +ℚassoc; +InvL to +ℚinvL; +InvR to +ℚinvR
            ;+CancelL to +ℚcancelL)
open import Cubical.Data.Rationals.Order
  using (_≤_; _<_; isProp≤; isProp<; Trichotomy; lt; eq; gt; _≟_
         ;isTrans<; isTrans≤; isTrans<≤; isTrans≤<; isAsym<; isIrrefl<; isAntisym≤
         ;isRefl≤; <Weaken≤
         ;≤-+o; ≤-o+; ≤-+o-cancel; <-+o; <-o+; <-+o-cancel
         ;≤Monotone+; ≤-·o; <-·o; ≤-·o-cancel; <-·o-cancel)

open import Cubical.HITs.SetQuotients.Properties using (elimProp; elimProp2; elimProp3)

open import CutInfra using (<-≤; ·-mono-≤-nn; ·-mono-<-nn)
open import MissileTwoUniversalIrrationality using (√2-irrational)
open import MissileTwoUniversalIrrationality using (√2-irrational)

------------------------------------------------------------------------
-- 私有小件：字面量与提升
------------------------------------------------------------------------

private
  1⁺ : ℕ₊₁
  1⁺ = 1+ zero

  0r 1r 2r : ℚ
  0r = [ pos 0 / 1⁺ ]
  1r = [ pos 1 / 1⁺ ]
  2r = [ pos (suc (suc zero)) / 1⁺ ]

  isPropΠp : {A : Type₀} {B : A → Type₀} → (∀ a → isProp (B a)) → isProp ((a : A) → B a)
  isPropΠp isB f g i a = isB a (f a) (g a) i

  isPropΠ2p : {A B : Type₀} {C : A → B → Type₀}
             → (∀ a b → isProp (C a b)) → isProp (∀ a b → C a b)
  isPropΠ2p isC f g i a b = isC a b (f a b) (g a b) i

  isProp×p : {A B : Type₀} → isProp A → isProp B → isProp (A × B)
  isProp×p iA iB (a₁ , b₁) (a₂ , b₂) i = (iA a₁ a₂ i , iB b₁ b₂ i)

  -- +pos 的 pos 形闭式（对任意 ℕ 见证）
  +pos-pos : ∀ (m k : ℕ) → pos m +pos k ≡ pos (m ℕ.+ k)
  +pos-pos m zero = cong pos (sym (+-zero m))
  +pos-pos m (suc k) = cong sucℤ (+pos-pos m k) ∙ cong pos (sym (+-suc m k))

  -- pos 0 <z pos (suc n)
  zero<pos : ∀ (n : ℕ) → pos 0 <z pos (suc n)
  zero<pos n = n , +pos-pos 1 n

  -- ℤ pos< 与 ℕ< 的双向提升
  pos<pos→ℕ< : ∀ (m n : ℕ) → pos m <z pos n → m <ℕ n
  pos<pos→ℕ< m n (k , prf) =
    k , (+-comm k (suc m) ∙ injPos (sym (+pos-pos (suc m) k) ∙ prf))

  ℕ<→pos< : ∀ (m n : ℕ) → m <ℕ n → pos m <z pos n
  ℕ<→pos< m n (k , prf) =
    k , (+pos-pos (suc m) k ∙ cong pos (+-comm (suc m) k ∙ prf))

------------------------------------------------------------------------
-- 金形态谓词与 hProp 包装（勘误版：U 带正性合取）
------------------------------------------------------------------------

L : ℚ → Type₀
L q = (q < 0r) ⊎ ((0r ≤ q) × (q ·ℚ q < 2r))

U : ℚ → Type₀
U q = (0r < q) × (2r < q ·ℚ q)

private
  L-disj : ∀ q → q < 0r → (0r ≤ q) × (q ·ℚ q < 2r) → ⊥
  L-disj q q<0 (q≥0 , _) =
    isIrrefl< q (subst (λ w → q < w) (sym (isAntisym≤ q 0r (<-≤ q 0r q<0) q≥0)) q<0)

  isPropL : ∀ q → isProp (L q)
  isPropL q = isProp⊎ (isProp< q 0r)
                      (isProp×p (isProp≤ 0r q) (isProp< (q ·ℚ q) 2r))
                      (L-disj q)

  isPropU : ∀ q → isProp (U q)
  isPropU q = isProp×p (isProp< 0r q) (isProp< 2r (q ·ℚ q))

-- Ω/hProp 值形态：Lₚ/Uₚ 即 Book §11.2 意义下 cut 的取值（无 resizing 时
-- Ω := hProp ℓ-zero）。LEM/resizing 的收费点在把 cut 取等价类、把「ℝ 取值
-- 命题」塌缩到单一 Ω 的下一升格（DESIGN §4；此处仅登记，不机械化）。
Lₚ Uₚ : ℚ → hProp ℓ-zero
Lₚ q = L q , isPropL q
Uₚ q = U q , isPropU q

------------------------------------------------------------------------
-- 条件一/二：inhabited
------------------------------------------------------------------------

inhabL : L 1r
inhabL = inr ((1 , refl) , (0 , refl))

inhabU : U 2r
inhabU = ((1 , refl) , (1 , refl))

------------------------------------------------------------------------
-- 条件三：不交性（Book §11.2 (iii)：L q ∧ U r → q < r）
------------------------------------------------------------------------

private
  absurd : ∀ {ℓ} {A : Type ℓ} → ⊥ → A
  absurd ()

disjoint : ∀ q r → L q → U r → q < r
disjoint q r Lq Ur with q ≟ r
... | lt hqr = hqr
... | eq q≡r = absurd (aux q≡r Lq Ur)
  where
  aux : q ≡ r → L q → U r → ⊥
  aux q≡r (inl q<0) (0r<r , 2r<rsq) =
    isAsym< r 0r (subst (λ w → w < 0r) q≡r q<0) 0r<r
  aux q≡r (inr (_ , qsq<2r)) (_ , 2r<rsq) =
    isAsym< (q ·ℚ q) 2r qsq<2r (subst (λ w → 2r < w ·ℚ w) (sym q≡r) 2r<rsq)
... | gt h = absurd (aux h Lq Ur)
  where
  aux : r < q → L q → U r → ⊥
  aux r<q (inl q<0) (0r<r , _) =
    isAsym< q 0r q<0 (isTrans< 0r r q 0r<r r<q)
  aux r<q (inr (0r≤q , qsq<2r)) (0r<r , 2r<rsq) =
    let 0r<q : 0r < q
        0r<q = isTrans< 0r r q 0r<r r<q
        link1 : r ·ℚ r < r ·ℚ q
        link1 = ·-mono-<-nn r r q 0r<r r<q
        link2 : r ·ℚ q < q ·ℚ q
        link2 = subst (λ x → x < q ·ℚ q) (sym (·ℚcomm r q))
                      (·-mono-<-nn q r q 0r<q r<q)
        sq-chain : r ·ℚ r < q ·ℚ q
        sq-chain = isTrans< (r ·ℚ r) (r ·ℚ q) (q ·ℚ q) link1 link2
    in  isIrrefl< 2r (isTrans< 2r (r ·ℚ r) 2r 2r<rsq
                        (isTrans< (r ·ℚ r) (q ·ℚ q) 2r sq-chain qsq<2r))


------------------------------------------------------------------------
-- 点事实、rounded → 方向与 located
------------------------------------------------------------------------

private
  0sq<2r : 0r ·ℚ 0r < 2r
  0sq<2r = 1 , refl

  0r≤0r : 0r ≤ 0r
  0r≤0r = 0 , refl

roundedL→ : ∀ q p → q < p → L p → L q
roundedL→ q p q<p (inl p<0) = inl (isTrans< q p 0r q<p p<0)
roundedL→ q p q<p (inr (0r≤p , psq<2r)) with q ≟ 0r
... | lt q<0 = inl q<0
... | eq q≡0 =
  inr ( subst (λ w → 0r ≤ w) (sym q≡0) 0r≤0r
      , subst (λ w → w ·ℚ w < 2r) (sym q≡0) 0sq<2r )
... | gt 0r<q =
  inr ( <-≤ 0r q 0r<q
      , isTrans< (q ·ℚ q) (p ·ℚ p) 2r
          (isTrans< (q ·ℚ q) (p ·ℚ q) (p ·ℚ p)
            (subst (λ x → q ·ℚ q < x) (·ℚcomm q p)
              (·-mono-<-nn q q p 0r<q q<p))
            (·-mono-<-nn p q p (isTrans< 0r q p 0r<q q<p) q<p))
          psq<2r )

roundedU→ : ∀ q r → q < r → U q → U r
roundedU→ q r q<r (0r<q , qsq>2r) =
  let 0r<r = isTrans< 0r q r 0r<q q<r
      qsq<rsq = isTrans< (q ·ℚ q) (r ·ℚ q) (r ·ℚ r)
                  (subst (λ x → q ·ℚ q < x) (·ℚcomm q r)
                    (·-mono-<-nn q q r 0r<q q<r))
                  (·-mono-<-nn r q r 0r<r q<r)
  in  (0r<r , isTrans< 2r (q ·ℚ q) (r ·ℚ r) qsq>2r qsq<rsq)

located : ∀ q r → q < r → L q ⊎ U r
located q r q<r with q ≟ 0r
... | lt q<0 = inl (inl q<0)
... | eq q≡0 =
  inl (inr ( subst (λ w → 0r ≤ w) (sym q≡0) 0r≤0r
           , subst (λ w → w ·ℚ w < 2r) (sym q≡0) 0sq<2r ))
... | gt 0r<q with (q ·ℚ q) ≟ 2r
...   | lt qsq<2r = inl (inr (<-≤ 0r q 0r<q , qsq<2r))
...   | eq qsq≡2r = absurd (√2-irrational q qsq≡2r)
...   | gt 2r<qsq =
    inr ( isTrans< 0r q r 0r<q q<r
        , isTrans< 2r (q ·ℚ q) (r ·ℚ r) 2r<qsq qsq<rsq )
  where
  qsq<rsq : q ·ℚ q < r ·ℚ r
  qsq<rsq =
    let 0r<r = isTrans< 0r q r 0r<q q<r in
    isTrans< (q ·ℚ q) (r ·ℚ q) (r ·ℚ r)
      (subst (λ x → q ·ℚ q < x) (·ℚcomm q r) (·-mono-<-nn q q r 0r<q q<r))
      (·-mono-<-nn r q r 0r<r q<r)

------------------------------------------------------------------------
-- δ-路线基础设施（roundedL← / roundedU← 的内在 ℚ 见证）
-- 代表元依赖见证在商上不良定义；改用 q 自身的 δ := (2 - q·q)·¼r 路线。
------------------------------------------------------------------------

private
  ¼r ½r r3/2 r9/4 m1r : ℚ
  ¼r   = [ pos 1 / 4 ]
  ½r   = [ pos 1 / 2 ]
  r3/2 = [ pos 3 / 2 ]
  r9/4 = [ pos 9 / 4 ]
  m1r  = [ negsuc zero / 1⁺ ]

  -- 封闭序事实（显式 ℕ 见证，全部点归约可核）
  0r<¼r   : 0r < ¼r
  0r<¼r   = (0 , refl)
  0r≤¼r   : 0r ≤ ¼r
  0r≤¼r   = (1 , refl)
  0r<½r   : 0r < ½r
  0r<½r   = (0 , refl)
  ½r<1r   : ½r < 1r
  ½r<1r   = (0 , refl)
  ¼r<1r   : ¼r < 1r
  ¼r<1r   = (2 , refl)
  0r<2r   : 0r < 2r
  0r<2r   = (1 , refl)
  0r≤2r   : 0r ≤ 2r
  0r≤2r   = (2 , refl)
  0r≤r3/2 : 0r ≤ r3/2
  0r≤r3/2 = (3 , refl)
  2r<r9/4 : 2r < r9/4
  2r<r9/4 = (0 , refl)

  1r+1r≡2r : 1r +ℚ 1r ≡ 2r
  1r+1r≡2r = refl

  2r+2r≡2r·2r : 2r +ℚ 2r ≡ 2r ·ℚ 2r
  2r+2r≡2r·2r = refl

  2r<2r·2r : 2r < 2r ·ℚ 2r
  2r<2r·2r = (1 , refl)

  -- [pos 2/4] ≢ [pos 1/2]：封闭恒等式不总是 refl，须走 eq/
  2r·¼r≡½r : 2r ·ℚ ¼r ≡ ½r
  2r·¼r≡½r = eq/ (pos 2 , 4) (pos 1 , 2) refl

  -- L 侧唯一需要的合成常数界：((3/2 + 3/2) + 1/2) · (1/4) < 1
  boundL : ((r3/2 +ℚ r3/2) +ℚ ½r) ·ℚ ¼r < 1r
  boundL = (3 , refl)

  -- U 侧唯一需要的合成常数界：2 · (2 · (1/4)) ≤ 1
  boundU : 2r ·ℚ (2r ·ℚ ¼r) ≤ 1r
  boundU = (0 , refl)

  -- 环重排：x·(y·z) ≡ y·(x·z)
  ·-reshuffle : ∀ x y z → x ·ℚ (y ·ℚ z) ≡ y ·ℚ (x ·ℚ z)
  ·-reshuffle x y z =
      ·ℚassoc x y z
    ∙ cong (λ W → W ·ℚ z) (·ℚcomm x y)
    ∙ sym (·ℚassoc y x z)

  negDistrib : ∀ x y → (-ℚ x) ·ℚ y ≡ -ℚ (x ·ℚ y)
  negDistrib x y = sym (·ℚassoc m1r x y)

  negDistribL : ∀ x y → x ·ℚ (-ℚ y) ≡ -ℚ (x ·ℚ y)
  negDistribL x y =
      ·ℚcomm x (-ℚ y)
    ∙ negDistrib y x
    ∙ cong (λ w → -ℚ w) (·ℚcomm y x)

  neg-neg : ∀ x y → (-ℚ x) ·ℚ (-ℚ y) ≡ x ·ℚ y
  neg-neg x y =
      negDistrib x (-ℚ y)
    ∙ cong (λ w → -ℚ w) (negDistribL x y)
    ∙ -Invol (x ·ℚ y)

  neg-add : ∀ x y → (-ℚ x) +ℚ (-ℚ y) ≡ -ℚ (x +ℚ y)
  neg-add x y = sym (·ℚdistL+ m1r x y)

  -- 平方展开（链的自然形状）：(x+y)·(x+y) ≡ (x·x + x·y) + (y·x + y·y)
  sq² : ∀ x y → (x +ℚ y) ·ℚ (x +ℚ y)
              ≡ (x ·ℚ x +ℚ x ·ℚ y) +ℚ (y ·ℚ x +ℚ y ·ℚ y)
  sq² x y =
      ·ℚdistR+ x y (x +ℚ y)
    ∙ cong₂ (λ A B → A +ℚ B) (·ℚdistL+ x x y) (·ℚdistL+ y x y)

  -- 序助手
  pos-add< : ∀ a b → 0r < b → a < a +ℚ b
  pos-add< a b 0r<b =
    subst (λ X → X < a +ℚ b) (+ℚidR a) (<-o+ 0r b a 0r<b)

  diff-pos : ∀ a b → a < b → 0r < b -ℚ a
  diff-pos a b a<b =
    subst (λ X → X < b -ℚ a) (+ℚinvR a) (<-+o a b (-ℚ a) a<b)

  b-a+a : ∀ a b → (b -ℚ a) +ℚ a ≡ b
  b-a+a a b =
      sym (+ℚassoc b (-ℚ a) a)
    ∙ cong (λ W → b +ℚ W) (+ℚinvL a)
    ∙ +ℚidR b

  ·-idR-≤ : ∀ x → x ·ℚ 1r ≤ x
  ·-idR-≤ x = subst (λ X → X ≤ x) (sym (·ℚidR x)) (isRefl≤ x)

------------------------------------------------------------------------
-- 条件四的一半：rounded ← 方向（L 侧）
-- L q → ∃ p, (q < p) × (L p)：q<0 取 p=0r；否则 δ := (2r - q·q)·¼r, p := q+δ
------------------------------------------------------------------------

roundedL← : ∀ q → L q → Σ[ p ∈ ℚ ] ((q < p) × (L p))
roundedL← q (inl q<0) = 0r , (q<0 , inr (0r≤0r , 0sq<2r))
roundedL← q (inr (0r≤q , qsq<2r)) = p , (q<p , inr (0r≤p , pp<2r))
  where
    s : ℚ
    s = 2r -ℚ (q ·ℚ q)
    δ : ℚ
    δ = s ·ℚ ¼r
    p : ℚ
    p = q +ℚ δ
    B : ℚ
    B = ((r3/2 +ℚ r3/2) +ℚ ½r) ·ℚ ¼r

    0r<s : 0r < s
    0r<s = diff-pos (q ·ℚ q) 2r qsq<2r
    0r<δ : 0r < δ
    0r<δ = subst (λ X → X < δ) (·ℚannihilL ¼r) (<-·o 0r s ¼r 0r<¼r 0r<s)
    0r≤δ : 0r ≤ δ
    0r≤δ = <Weaken≤ 0r δ 0r<δ
    q<p : q < p
    q<p = subst (λ X → X < p) (+ℚidR q) (<-o+ 0r δ q 0r<δ)
    0r≤p : 0r ≤ p
    0r≤p = subst (λ X → X ≤ p) (+ℚidL 0r) (≤Monotone+ 0r q 0r δ 0r≤q 0r≤δ)

    0r≤qsq : 0r ≤ q ·ℚ q
    0r≤qsq = subst (λ X → X ≤ q ·ℚ q) (·ℚannihilR q)
               (·-mono-≤-nn q 0r q 0r≤q 0r≤q)

    s+qsq : s +ℚ (q ·ℚ q) ≡ 2r
    s+qsq = sym (+ℚassoc 2r (-ℚ (q ·ℚ q)) (q ·ℚ q))
          ∙ cong (λ W → 2r +ℚ W) (+ℚinvL (q ·ℚ q))
          ∙ +ℚidR 2r
    qsq+s : (q ·ℚ q) +ℚ s ≡ 2r
    qsq+s = +ℚcomm (q ·ℚ q) s ∙ s+qsq
    s≤2r : s ≤ 2r
    s≤2r = isTrans≤ s (s +ℚ (q ·ℚ q)) 2r
             (subst (λ X → X ≤ (s +ℚ (q ·ℚ q))) (+ℚidR s) (≤-o+ 0r (q ·ℚ q) s 0r≤qsq))
             (subst (λ X → X ≤ 2r) (sym s+qsq) (isRefl≤ 2r))

    q≤r3/2 : q ≤ r3/2
    q≤r3/2 with q ≟ r3/2
    ... | lt q<3/2 = <-≤ q r3/2 q<3/2
    ... | eq h     = subst (λ X → X ≤ r3/2) (sym h) (isRefl≤ r3/2)
    ... | gt 3/2<q = absurd (isAsym< (q ·ℚ q) 2r qsq<2r
                          (isTrans<≤ 2r (r3/2 ·ℚ r3/2) (q ·ℚ q) 2r<r9/4
                            (isTrans≤ (r3/2 ·ℚ r3/2) (q ·ℚ r3/2) (q ·ℚ q)
                              (subst (λ X → (r3/2 ·ℚ r3/2) ≤ X) (·ℚcomm r3/2 q)
                                 (·-mono-≤-nn r3/2 r3/2 q 0r≤r3/2 (<-≤ r3/2 q 3/2<q)))
                              (·-mono-≤-nn q r3/2 q 0r≤q (<-≤ r3/2 q 3/2<q)))))

    δ≤½r : δ ≤ ½r
    δ≤½r = isTrans≤ δ (2r ·ℚ ¼r) ½r
             (≤-·o s 2r ¼r 0r≤¼r s≤2r)
             (subst (λ X → (2r ·ℚ ¼r) ≤ X) 2r·¼r≡½r (isRefl≤ (2r ·ℚ ¼r)))

    -- (q+δ)² ≡ q² + ((q·δ + q·δ) + δ·δ)
    pp : p ·ℚ p ≡ (q ·ℚ q) +ℚ ((q ·ℚ δ +ℚ q ·ℚ δ) +ℚ (δ ·ℚ δ))
    pp = sq² q δ
       ∙ cong (λ W → (q ·ℚ q +ℚ q ·ℚ δ) +ℚ (W +ℚ δ ·ℚ δ)) (·ℚcomm δ q)
       ∙ sym (+ℚassoc (q ·ℚ q) (q ·ℚ δ) ((q ·ℚ δ) +ℚ (δ ·ℚ δ)))
       ∙ cong (λ W → (q ·ℚ q) +ℚ W) (+ℚassoc (q ·ℚ δ) (q ·ℚ δ) (δ ·ℚ δ))

    -- 单调收集：(q·δ + q·δ) + δ·δ ≤ ((3/2+3/2)+1/2)·δ
    Cd : (q ·ℚ δ +ℚ q ·ℚ δ) +ℚ (δ ·ℚ δ)
         ≤ (r3/2 ·ℚ δ +ℚ r3/2 ·ℚ δ) +ℚ (½r ·ℚ δ)
    Cd = ≤Monotone+ (q ·ℚ δ +ℚ q ·ℚ δ) (r3/2 ·ℚ δ +ℚ r3/2 ·ℚ δ)
                       (δ ·ℚ δ) (½r ·ℚ δ)
           (≤Monotone+ (q ·ℚ δ) (r3/2 ·ℚ δ) (q ·ℚ δ) (r3/2 ·ℚ δ)
              (≤-·o q r3/2 δ 0r≤δ q≤r3/2) (≤-·o q r3/2 δ 0r≤δ q≤r3/2))
           (≤-·o δ ½r δ 0r≤δ δ≤½r)

    collectL : (r3/2 ·ℚ δ +ℚ r3/2 ·ℚ δ) +ℚ (½r ·ℚ δ)
               ≡ ((r3/2 +ℚ r3/2) +ℚ ½r) ·ℚ δ
    collectL = sym (+ℚassoc (r3/2 ·ℚ δ) (r3/2 ·ℚ δ) (½r ·ℚ δ))
             ∙ sym (cong (λ W → r3/2 ·ℚ δ +ℚ W) (·ℚdistR+ r3/2 ½r δ))
             ∙ sym (·ℚdistR+ r3/2 (r3/2 +ℚ ½r) δ)
             ∙ cong (λ W → W ·ℚ δ) (+ℚassoc r3/2 r3/2 ½r)

    Y≡Z : (r3/2 ·ℚ δ +ℚ r3/2 ·ℚ δ) +ℚ (½r ·ℚ δ) ≡ s ·ℚ B
    Y≡Z = collectL ∙ ·-reshuffle ((r3/2 +ℚ r3/2) +ℚ ½r) s ¼r

    fin : s ·ℚ B < s
    fin = subst (λ X → s ·ℚ B < X) (·ℚidR s) (·-mono-<-nn s B 1r 0r<s boundL)

    rest : (q ·ℚ δ +ℚ q ·ℚ δ) +ℚ (δ ·ℚ δ) < s
    rest = isTrans≤< ((q ·ℚ δ +ℚ q ·ℚ δ) +ℚ (δ ·ℚ δ))
                     ((r3/2 ·ℚ δ +ℚ r3/2 ·ℚ δ) +ℚ (½r ·ℚ δ)) s Cd
             (subst (λ W → W < s) (sym Y≡Z) fin)

    pp<2r : p ·ℚ p < 2r
    pp<2r = subst (λ Z → Z < 2r) (sym pp)
              (subst (λ Y → (q ·ℚ q) +ℚ ((q ·ℚ δ +ℚ q ·ℚ δ) +ℚ (δ ·ℚ δ)) < Y)
                 qsq+s
                 (<-o+ ((q ·ℚ δ +ℚ q ·ℚ δ) +ℚ (δ ·ℚ δ)) s (q ·ℚ q) rest))
