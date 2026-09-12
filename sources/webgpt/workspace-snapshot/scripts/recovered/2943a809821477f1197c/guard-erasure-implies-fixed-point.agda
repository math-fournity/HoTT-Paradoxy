module guard-erasure-implies-fixed-point where

open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.universe-levels

-- A time-indexed orbit can collapse to one state while preserving its update
-- law only by supplying a fixed point of F.
Guard-Erasure : {l : Level} (X : UU l) (F : X → X) → UU l
Guard-Erasure X F = Σ X (λ c → c ＝ F c)

fixed-point-guard-erasure :
  {l : Level} {X : UU l} {F : X → X} →
  Guard-Erasure X F → Σ X (λ c → c ＝ F c)
fixed-point-guard-erasure e = e
