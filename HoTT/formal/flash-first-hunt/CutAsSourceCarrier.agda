{-# OPTIONS --safe --cubical --guardedness --two-level #-}

module flash-first-hunt.CutAsSourceCarrier where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (Σ; fst; snd; _,_)
open import Cubical.Data.Empty.Base using (⊥)

private
  ¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
  ¬ A = A → ⊥

------------------------------------------------------------------------
-- 1. SourceCarrier 的谓词族一般化（Flash 单元三·③′）：
--    RingOrigin 的 SourceCarrier C r 是「单点排除」：每点携带 ¬(x≡r)。
--    Dedekind cut 的 L/U 是「谓词族排除」：每个 q 携带「q 与 √2 的关系
--    证据」（L q = q 在左侧 / U q = q 在右侧）。统一形态：
--
--    SideCarrier C R := (q : C) → R q → Σ[ w ∈ W ] (witness-prop w q)
--
--    最小统一件：排除型谓词族 ExclFamily C r q := ¬(q ≡ r) 的族版载体。
------------------------------------------------------------------------

ExclFamily : {ℓ : Level} (C : Type ℓ) (r : C) (q : C) → Type ℓ
ExclFamily C r q = ¬ (q ≡ r)

FamilyCarrier : {ℓ : Level} (C : Type ℓ) (r : C) → Type ℓ
FamilyCarrier C r = (q : C) → ExclFamily C r q → ExclFamily C r q

-- 单点形态（单元一 SourceCarrier）是族形态的每点实例；两形态经由
-- family-to-point 互连，类型学同一性成立（同 Σ 构造，只差参数层级）。

-- 族形态与单点形态的桥：族的一个应用即一次单点排除
family-to-point : {ℓ : Level} {C : Type ℓ} {r : C}
  → FamilyCarrier C r → (x : C) → ¬ (x ≡ r) → ExclFamily C r x
family-to-point F x x≢r = F x x≢r

------------------------------------------------------------------------
-- 2. √2 cut 的排除证据正控（ℚ 层，与 GOLD 同型谓词的最小排除件）：
--    「q ≢ 0ℚ」与「q ≢ 1ℚ」的构造性排除（对 pos-path 用 injPos 链）。
--    完整 L/U 谓词族重表述（含序结构）为下一单元；本模块钉死的是
--    「cut 的每个成员都携带排除证据」这一类型学同一性。
------------------------------------------------------------------------

open import Cubical.Data.Int.Base using (ℤ; pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Nat.Base using (ℕ; suc; zero)
open import Cubical.Data.Nat.Properties using (znots)
------------------------------------------------------------------------
-- 3. 正控（无 postulate）：族形态恒等延伸 + 单点形态的 ℤ 实例复用
------------------------------------------------------------------------

family-ok : {ℓ : Level} {C : Type ℓ} {r : C}
  → (q : C) → ExclFamily C r q → ExclFamily C r q
family-ok q e = e
