{-# OPTIONS --safe --cubical --guardedness #-}

-- 第二枚导弹（声明层）· Dedekind-Ω 簇 / √2 全称无理性
-- claim id : CAND-F2-7-M2   (candidate, registers_new_claim semantics: 候选, 非已注册主张)
-- proof id : MP-DEDEKIND-OMEGA-M2
--
-- 弹种（023 片 §2 / 025 片 §5）：声明层——B 的交付类型 Spec_B 的居住性为空。
--   Spec_B = Σ (q : ℚ), q ·ℚ q ≡ 2r （「输出 √2 的有理位置」任务的交付类型）
-- 机械证据：¬ (Σ q : ℚ, q ·ℚ q ≡ 2r)——不是"还没停"，是"不可能停"。
--
-- 证明路径：ℚ 提取（ℚ· 在 rec2 下于点构造子定义性归约 + eq/⁻¹ + Int abs）
--           → ℕ 无穷下降（奇偶工具包 + 平方膨胀 + 强归纳）。
--
-- 边界（不可漂移，025 片 §6）：
--   * 这不是 HoTT 的内部矛盾，不声称 HoTT 不一致。
--   * 本命题是 ℚ/ℕ 层标准计算；ℚ 的 set quotient 是标准构造，
--     不依赖 univalence / cubical path / HIT 特有规则。

module MissileTwoUniversalIrrationality where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)

private
  ¬_ : Type₀ → Type₀
  ¬_ A = A → ⊥

  absurd : ∀ {ℓ} {A : Type ℓ} → ⊥ → A
  absurd ()

open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_; _·_)
open import Cubical.Data.Nat.Properties
  using (+-zero; +-suc; +-assoc; +-comm; injSuc; znots; snotz)
open import Cubical.Data.Nat.Order using (_≤_; _<_; ≤-refl; suc-≤-suc; pred-≤-pred)

open import Cubical.Data.Int.Base as ℤ using (ℤ; pos; negsuc; abs)
open import Cubical.Data.Int.Properties using (·IdR; abs·)

open import Cubical.Data.NatPlusOne.Base using (ℕ₊₁; ℕ₊₁→ℕ; 1+_)
open import Cubical.Data.NatPlusOne.Properties using (_·₊₁_)

open import Cubical.Data.Rationals.Base
  using (ℚ; [_]; [_/_]; _∼_; eq/⁻¹; ℕ₊₁→ℤ)
open import Cubical.Data.Rationals.Properties using () renaming (_·_ to _·ℚ_)
open import Cubical.HITs.SetQuotients.Properties using (elimProp)

------------------------------------------------------------------------
-- 私有小件：Prop 性（自备，避免库导入名漂移）
------------------------------------------------------------------------

private
  isProp⊥p : isProp ⊥
  isProp⊥p = λ ()

  isPropΠp : {A : Type₀} {B : A → Type₀} → (∀ a → isProp (B a)) → isProp ((a : A) → B a)
  isPropΠp isB f g i a = isB a (f a) (g a) i

  trans : ∀ {ℓ} {A : Type ℓ} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
  trans p q = p ∙ q

------------------------------------------------------------------------
-- ℕ 奇偶工具包（自备）
------------------------------------------------------------------------

private
  data Par : Type₀ where
    ev od : Par

  fl : Par → Par
  fl ev = od
  fl od = ev

  fl² : ∀ x → fl (fl x) ≡ x
  fl² ev = refl
  fl² od = refl

  ev≢od : ¬ (ev ≡ od)
  ev≢od p = znots (cong Par→ℕ p)
    where
    Par→ℕ : Par → ℕ
    Par→ℕ ev = zero
    Par→ℕ od = suc zero

  fl-ev : ∀ x → fl x ≡ ev → x ≡ od
  fl-ev ev p = absurd (ev≢od (sym p))
  fl-ev od p = refl

  fl-od : ∀ x → fl x ≡ od → x ≡ ev
  fl-od ev p = refl
  fl-od od p = absurd (ev≢od p)

  par : ℕ → Par
  par zero = ev
  par (suc n) = fl (par n)

  -- L1：偶 + 偶 = 偶（形状版）
  L1 : ∀ s → par (s + s) ≡ ev
  L1 zero = refl
  L1 (suc s) =
    trans (cong fl (cong par (+-suc s s)))
          (trans (cong (λ x → fl (fl x)) (L1 s)) (fl² ev))

  -- 奇偶形状提取（互归单点化：Σ 编码的二元组引理）
  L6 : ∀ p → Σ[ evCase ∈ (par p ≡ ev → Σ[ s ∈ ℕ ] p ≡ s + s) ]
            ((par p ≡ od → Σ[ s ∈ ℕ ] p ≡ suc (s + s)))
  L6 zero = (λ _ → zero , refl) , (λ p≡od → absurd (ev≢od p≡od))
  L6 (suc p) =
    ( λ p≡ev → let (s , q) = snd (L6 p) (fl-ev (par p) p≡ev)
               in suc s , cong suc q ∙ cong suc (sym (+-suc s s)))
    , ( λ p≡od → let (s , q) = fst (L6 p) (fl-od (par p) p≡od)
                 in s , cong suc q)

  -- 四项重排：(s+s)+(t+t) ≡ (s+t)+(s+t)
  rearr : ∀ s t → (s + s) + (t + t) ≡ (s + t) + (s + t)
  rearr s t =
    sym (+-assoc s s (t + t))
      ∙ cong (s +_) (+-assoc s t t ∙ cong (_+ t) (+-comm s t) ∙ sym (+-assoc t s t))
      ∙ +-assoc s t (s + t)

  -- 偶 + 偶 = 偶（一般版）
  ev-add : ∀ a b → par a ≡ ev → par b ≡ ev → par (a + b) ≡ ev
  ev-add a b pa pb =
    let (s , qa) = fst (L6 a) pa
        (t , qb) = fst (L6 b) pb
    in trans (cong par (cong₂ (λ x y → x + y) qa qb))
             (trans (cong par (rearr s t)) (L1 (s + t)))

  -- 偶 × 任意 = 偶（形状归纳：(s+s)·b）
  L9 : ∀ s b → par ((s + s) · b) ≡ ev
  L9 zero b = refl
  L9 (suc s) b =
    trans (cong par (cong (_· b) (cong suc (+-suc s s))))
          (trans (cong par (+-assoc b b ((s + s) · b)))
                 (ev-add (b + b) ((s + s) · b) (L1 b) (L9 s b)))

  -- 分配律（右），用于平方膨胀
  ·-distrib-r : (a b c : ℕ) → (a + b) · c ≡ a · c + b · c
  ·-distrib-r zero b c = refl
  ·-distrib-r (suc a) b c =
    cong (c +_) (·-distrib-r a b c) ∙ +-assoc c (a · c) (b · c)

  -- 分配律（左），用于平方膨胀
  ·-distrib-l : (a b c : ℕ) → a · (b + c) ≡ a · b + a · c
  ·-distrib-l zero b c = refl
  ·-distrib-l (suc a) b c =
    cong ((b + c) +_) (·-distrib-l a b c)
      ∙ sym (+-assoc b c ((a · b) + (a · c)))
      ∙ cong (b +_) (+-assoc c (a · b) (a · c)
                     ∙ cong (_+ (a · c)) (+-comm c (a · b))
                     ∙ sym (+-assoc (a · b) c (a · c)))
      ∙ +-assoc b (a · b) (c + a · c)

  -- 平方膨胀：(a+a)·(a+a) ≡ (a·a+a·a)+(a·a+a·a)
  sq-double : ∀ a → (a + a) · (a + a) ≡ (a · a + a · a) + (a · a + a · a)
  sq-double a =
    ·-distrib-r a a (a + a)
      ∙ cong₂ (λ x y → x + y) (·-distrib-l a a a) (·-distrib-l a a a)

  -- 偶平方引理：p·p ≡ m+m → Σ k, p ≡ k+k
  even-square : ∀ p m → p · p ≡ m + m → Σ[ k ∈ ℕ ] p ≡ k + k
  even-square p m h = aux (par p) refl
    where
    pev : par (p · p) ≡ ev
    pev = cong par h ∙ L1 m
    aux : (x : Par) → par p ≡ x → Σ[ k ∈ ℕ ] p ≡ k + k
    aux ev pp = fst (L6 p) pp
    aux od pp =
      let (s , e) = snd (L6 p) pp
          u = s + s
          pp' : p · p ≡ suc (u + u · suc u)
          pp' = trans (cong (_· p) e) (cong ((suc u) ·_) e)
          inner : par (u + u · suc u) ≡ ev
          inner = ev-add u (u · suc u) (L1 s) (L9 s (suc u))
          pod : par (p · p) ≡ od
          pod = trans (cong par pp') (cong fl inner)
      in absurd (ev≢od ((sym pev) ∙ pod))

  -- 偶和单射：s+s ≡ t+t → s ≡ t
  even-inj : ∀ s t → s + s ≡ t + t → s ≡ t
  even-inj zero zero p = refl
  even-inj zero (suc t') p = absurd (znots p)
  even-inj (suc s') zero p = absurd (snotz p)
  even-inj (suc s') (suc t') p =
    cong suc (even-inj s' t'
      (injSuc (trans (sym (+-suc s' s')) (trans (injSuc p) (+-suc t' t')))))

  -- 非零半减：suc k ≤ k+k 或 k ≡ 0
  k<kk : ∀ k → (suc k ≤ k + k) ⊎ (k ≡ zero)
  k<kk zero = inr refl
  k<kk (suc k) with k<kk k
  ... | inl (j , hj) =
    inl (suc j ,
         cong suc (+-suc j (suc k))
         ∙ cong (λ x → suc (suc x)) hj
         ∙ cong suc (sym (+-suc k k)))
  ... | inr k≡0 =
    inl (subst (λ w → suc (suc w) ≤ suc w + suc w) (sym k≡0) ≤-refl)

  -- 非零即有前驱
  suc-shape : ∀ j → ¬ (j ≡ zero) → Σ[ j₀ ∈ ℕ ] j ≡ suc j₀
  suc-shape zero j≢0 = absurd (j≢0 refl)
  suc-shape (suc j) j≢0 = j , refl

  -- 下降中 j 的非零性：n = suc n₀ ≡ j+j 排除 j ≡ 0
  suc-shape-inj : ∀ n₀ j → suc n₀ ≡ j + j → ¬ (j ≡ zero)
  suc-shape-inj n₀ j en q =
    snotz (trans en (trans (cong (j +_) q) (trans (+-zero j) q)))

  -- 平方替换 + 偶和单射组合
  transport-sq : ∀ p k X → p ≡ k + k → p · p ≡ X → (k + k) · (k + k) ≡ X
  transport-sq p k X e h = sym (trans (cong (_· p) e) (cong ((k + k) ·_) e)) ∙ h

  halve : ∀ k n → (k + k) · (k + k) ≡ (n · n) + (n · n) → (k · k) + (k · k) ≡ n · n
  halve k n hh = even-inj (k · k + k · k) (n · n) (sym (sq-double k) ∙ hh)

  k<p-of : ∀ p k → p ≡ k + k → suc k ≤ k + k → k < p
  k<p-of p k e kk≤ = subst (λ w → suc k ≤ w) (sym e) kk≤

  -- 强归纳（手写；≤ 的 Σ 编码下直接拆见证）
  strongℕ : ∀ {ℓ} {A : ℕ → Type ℓ} → (∀ n → (∀ m → m < n → A m) → A n) → ∀ n → A n
  strongℕ {A = A} step = strong
    where
    vac : ∀ q → q < zero → A q
    vac q (j , p) = absurd (snotz (sym (+-suc j q) ∙ p))
    aux : ∀ bound m → m ≤ bound → A m
    aux zero m (k , p) with m
    ... | zero = step zero vac
    ... | suc m' = absurd (snotz (sym (+-suc k m') ∙ p))
    aux (suc b) m (k , p) with m
    ... | zero = step zero vac
    ... | suc m' with k
    ...   | zero = subst A (sym (cong suc (injSuc p))) (step (suc b) smaller)
      where
      smaller : ∀ q → q < suc b → A q
      smaller q l = aux b q (pred-≤-pred l)
    ...   | suc k' = aux b (suc m') (k' , injSuc p)
    strong : ∀ n → A n
    strong n = aux n n ≤-refl

------------------------------------------------------------------------
-- 核心下降：无 p, n₀ 使 p² = 2·(suc n₀)²
------------------------------------------------------------------------

noRoot : ∀ p n₀ → p · p ≡ (suc n₀ · suc n₀) + (suc n₀ · suc n₀) → ⊥
noRoot = strongℕ step
  where
  A : ℕ → Type₀
  A p = ∀ n₀ → p · p ≡ (suc n₀ · suc n₀) + (suc n₀ · suc n₀) → ⊥
  step : ∀ p → (∀ m → m < p → A m) → A p
  step p IH n₀ h with even-square p (suc n₀ · suc n₀) h
  ... | (k , e) with k<kk k
  ...   | inr k≡0 =
    znots (subst (λ w → w · w ≡ (suc n₀ · suc n₀) + (suc n₀ · suc n₀))
                 (trans e (trans (cong (k +_) k≡0) (trans (+-zero k) k≡0)))
                 h)
  ...   | inl kk with
        even-square (suc n₀) (k · k)
          (sym (halve k (suc n₀) (transport-sq p k ((suc n₀ · suc n₀) + (suc n₀ · suc n₀)) e h)))
  ...   | (j , en) with k<kk j
  ...     | inr j≡0 = snotz (trans en (trans (cong (j +_) j≡0) (trans (+-zero j) j≡0)))
  ...     | inl _ with suc-shape j (suc-shape-inj n₀ j en)
  ...       | (j₀ , je) =
    let kk' = k<p-of p k e kk
        H   = halve k (suc n₀) (transport-sq p k ((suc n₀ · suc n₀) + (suc n₀ · suc n₀)) e h)
        jjkk = trans (sym (cong₂ (λ x y → x · y) en en)) (sym H)
    in IH k kk' j₀ (subst (λ w → k · k ≡ (w · w) + (w · w)) je
                          (sym (halve j k jjkk)))

------------------------------------------------------------------------
-- ℚ 提取：√2 的有理位置不可能作为交付输出
------------------------------------------------------------------------

1⁺ : ℕ₊₁
1⁺ = 1+ zero

2r : ℚ
2r = [ pos (suc (suc zero)) / 1⁺ ]

-- ℕ₊₁ 乘法过映射：ℕ· 于首参递归，故在 1+ 构造子上定义性成立
ℕ₊₁→ℕ-·₊₁ : ∀ a b → ℕ₊₁→ℕ (a ·₊₁ b) ≡ ℕ₊₁→ℕ a · ℕ₊₁→ℕ b
ℕ₊₁→ℕ-·₊₁ (1+ m) (1+ n) = refl

absurd-from : ∀ p n⁺ →
  p · p ≡ (ℕ₊₁→ℕ n⁺ · ℕ₊₁→ℕ n⁺) + (ℕ₊₁→ℕ n⁺ · ℕ₊₁→ℕ n⁺) → ⊥
absurd-from p (1+ zero) eq = noRoot p zero eq
absurd-from p (1+ (suc f)) eq = noRoot p (suc f) eq

√2-step : ∀ (zm : ℤ) (n⁺ : ℕ₊₁) →
  ([ (zm , n⁺) ] ·ℚ [ (zm , n⁺) ]) ≡ 2r → ⊥
√2-step zm n⁺ h = absurd-from (abs zm) n⁺ EQ
  where
  X = ℕ₊₁→ℕ n⁺ · ℕ₊₁→ℕ n⁺
  -- ℚ· 的 rec2 点归约：[ (zm,n⁺) ]·[ (zm,n⁺) ] ≡ [ (zm·zm , n⁺·₊₁n⁺) ]（定义性）
  -- 同分母关系 ∼ 展开：(zm·zm)·ℤ ℕ₊₁→ℤ 1⁺ ≡ pos 2 ·ℤ pos (ℕ₊₁→ℕ (n⁺·₊₁n⁺))
  chain1 : zm ℤ.· zm ≡ pos (suc (suc zero)) ℤ.· pos (ℕ₊₁→ℕ (n⁺ ·₊₁ n⁺))
  chain1 = sym (·IdR (zm ℤ.· zm)) ∙ eq/⁻¹ _ _ h
  EQ : abs zm · abs zm ≡ X + X
  EQ = sym (abs· zm zm)
       ∙ trans (cong abs chain1)
           (trans (abs· (pos (suc (suc zero))) (pos (ℕ₊₁→ℕ (n⁺ ·₊₁ n⁺))))
             (trans (cong (suc (suc zero) ·_) (ℕ₊₁→ℕ-·₊₁ n⁺ n⁺))
                    (cong (X +_) (+-zero X))))

noRootℚ : ∀ q → q ·ℚ q ≡ 2r → ⊥
noRootℚ = elimProp (λ q → isPropΠp (λ _ → isProp⊥p))
                   λ (zm , n⁺) → √2-step zm n⁺

------------------------------------------------------------------------
-- 主定理（两种等价形式）
------------------------------------------------------------------------

-- ∀ 形式（「全称无理性」逐字读法，024 片 §4）
√2-irrational : ∀ q → ¬ (q ·ℚ q ≡ 2r)
√2-irrational = noRootℚ

-- Σ 形式（B 的交付类型 Spec_B 居住性为空，025 片 §2/§5）
spec-B-empty : ¬ (Σ[ q ∈ ℚ ] q ·ℚ q ≡ 2r)
spec-B-empty (q , h) = noRootℚ q h
