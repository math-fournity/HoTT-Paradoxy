{-# OPTIONS --safe --cubical --guardedness --two-level #-}

-- 一次性探针（不提交）：验证库 isoToEquiv 是否接受跨层 Iso。
module ProbeCrossIso where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (hProp)
open import Cubical.Foundations.Isomorphism using (Iso; isoToEquiv)
open import Cubical.Foundations.Equiv using (_≃_)

probe : {ℓ : Level} {X : Type ℓ} → Iso X (hProp ℓ) → (X ≃ hProp ℓ)
probe i = isoToEquiv i
