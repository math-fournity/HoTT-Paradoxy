module context-free-translate-impossible where

open import foundation.coproduct-types
open import foundation.dependent-pair-types
open import foundation.negation
open import foundation.unit-type
open import foundation.universe-levels

Surface : UU lzero
Surface = unit

Context : UU lzero
Context = unit + unit

Spec : UU lzero
Spec = unit + unit

meaning : Surface → Context → Spec
meaning _ (inl _) = inl star
meaning _ (inr _) = inr star

Perfect-Context-Free-Translate : UU lzero
Perfect-Context-Free-Translate =
  Σ (Surface → Spec) (λ T → (c : Context) → T star ＝ meaning star c)

no-context-free-perfect-translate :
  ¬ Perfect-Context-Free-Translate
no-context-free-perfect-translate (T , H) with T star
... | inl star = neq-inl-inr (H (inr star))
... | inr star = neq-inr-inl (H (inl star))
