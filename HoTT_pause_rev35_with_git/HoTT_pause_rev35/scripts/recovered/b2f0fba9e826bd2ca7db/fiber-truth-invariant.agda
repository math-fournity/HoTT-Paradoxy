module fiber-truth-invariant where

open import foundation.identity-types
open import foundation.universe-levels

-- Core Z lemma: every observable that factors through a representation is
-- constant on its identity fibres.
factorization-implies-fiber-constant :
  {l1 l2 l3 : Level}
  {W : UU l1} {M : UU l2} {Y : UU l3}
  (α : W → M) (J : W → Y) (Ĵ : M → Y) →
  ((w : W) → J w ＝ Ĵ (α w)) →
  {w₀ w₁ : W} → α w₀ ＝ α w₁ → J w₀ ＝ J w₁
factorization-implies-fiber-constant α J Ĵ H {w₀} {w₁} p =
  (H w₀) ∙ (ap Ĵ p) ∙ (inv (H w₁))
