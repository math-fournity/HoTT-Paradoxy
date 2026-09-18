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

open import Cubical.Data.NatPlusOne.Base using (ℕ₊₁; ℕ₊₁→ℕ; 1+_)
open import Cubical.Data.NatPlusOne.Properties using (_·₊₁_)

open import Cubical.Data.Rationals.Base
  using (ℚ; [_]; [_/_]; eq/⁻¹; ℕ₊₁→ℤ)
open import Cubical.Data.Rationals.Properties
  using (·IdL)
  renaming (_·_ to _·ℚ_; ·Comm to ·ℚcomm)
open import Cubical.Data.Rationals.Order
  using (_≤_; _<_; isProp≤; isProp<; Trichotomy; lt; eq; gt; _≟_; isTrans<; isTrans≤; isAsym<; isIrrefl<; isAntisym≤)

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
