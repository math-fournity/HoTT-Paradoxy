{-# OPTIONS --safe --cubical --guardedness #-}

-- 廉价副产品（修订片 025 §5 保留项；非第三枚，不得冒充识别层）
-- claim id : CAND-F2-7-BP   (candidate, registers_new_claim semantics: 候选, 非已注册主张)
-- proof id : MP-DEDEKIND-OMEGA-BP
--
-- 目的：机械确认「序列层存在命题可判定、搜索过程不可停机」这一对必须
-- 分开登记的事实（025 片 §5 发射顺序更正的根据）：
--   * decGapAt：序列层存在命题的逐点判定是一个**已完成对象**（已判定为
--     「否」）——这正是第一枚战果（gap-never-zero）不能直接当作第三枚 B 侧
--     锚点的原因：判定本身已完成，非终止只住在搜索算法里；
--   * noGapWitness：Σ 形式的居住性否定——与第二枚 spec-B-empty 同形，
--     是本簇内「交付类型居住性为空」的第二个独立实例（基于 D n ≡ ±1 的
--     Pell 不变量，与全称无理性的下降法证据路径独立）。

module MissileByproductGapDecidable where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Sum.Base using (_⊎_; inr)
open import Cubical.Data.Int.Base as ℤ using (pos)

private
  ¬_ : Type₀ → Type₀
  ¬_ A = A → ⊥

open import MissileOneProcessLayer using (D; gap-never-zero)

zeroℤ : ℤ.ℤ
zeroℤ = pos 0

decGapAt : (n : ℕ) → (D n ≡ zeroℤ) ⊎ (¬ (D n ≡ zeroℤ))
decGapAt n = inr (gap-never-zero n)

noGapWitness : ¬ (Σ[ n ∈ ℕ ] D n ≡ zeroℤ)
noGapWitness (n , h) = gap-never-zero n h
