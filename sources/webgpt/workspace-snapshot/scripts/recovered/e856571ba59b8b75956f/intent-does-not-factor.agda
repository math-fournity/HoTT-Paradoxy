module intent-does-not-factor where

open import foundation.cartesian-product-types
open import foundation.coproduct-types
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.negation
open import foundation.unit-type
open import foundation.universe-levels

Role : UU lzero
Role = unit + unit

Arithmetic Indexing : Role
Arithmetic = inl star
Indexing = inr star

Bare : UU lzero
Bare = unit

Enriched : UU lzero
Enriched = Bare × Role

forget-role : Enriched → Bare
forget-role (b , _) = b

role : Enriched → Role
role (_ , r) = r

arithmetic-value indexing-value : Enriched
arithmetic-value = star , Arithmetic
indexing-value = star , Indexing

Role-Recovery : UU lzero
Role-Recovery =
  Σ (Bare → Role) (λ R → (e : Enriched) → R (forget-role e) ＝ role e)

no-role-recovery : ¬ Role-Recovery
no-role-recovery (R , H) =
  neq-inl-inr ((inv (H arithmetic-value)) ∙ (H indexing-value))
