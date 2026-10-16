module snapshot-provenance-counterexample where

open import foundation.cartesian-product-types
open import foundation.coproduct-types
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.negation
open import foundation.unit-type
open import foundation.universe-levels

Provenance : UU lzero
Provenance = unit + unit

original replica : Provenance
original = inl star
replica = inr star

Snapshot : UU lzero
Snapshot = unit

History : UU lzero
History = Snapshot × Provenance

snapshot : History → Snapshot
snapshot (s , _) = s

provenance : History → Provenance
provenance (_ , p) = p

original-history replica-history : History
original-history = star , original
replica-history = star , replica

Provenance-Recovery : UU lzero
Provenance-Recovery =
  Σ (Snapshot → Provenance)
    (λ R → (h : History) → R (snapshot h) ＝ provenance h)

no-provenance-recovery : ¬ Provenance-Recovery
no-provenance-recovery (R , H) =
  neq-inl-inr ((inv (H original-history)) ∙ (H replica-history))
