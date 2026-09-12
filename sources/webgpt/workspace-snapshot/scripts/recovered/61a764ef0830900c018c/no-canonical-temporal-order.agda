module no-canonical-temporal-order where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

-- Any temporal structure from which an earliest event can be extracted would
-- induce the forbidden global section. This covers strict total orders on a
-- two-element carrier once their unique minimum operation is supplied.
module _
  {l1 l2 : Level}
  (Temporal-Structure : UU l1 → UU l2)
  (earliest : (A : UU l1) → Temporal-Structure A → A)
  where

  Canonical-Temporal-Structure : UU (lsuc l1 ⊔ l2)
  Canonical-Temporal-Structure =
    (X : 2-Element-Type l1) →
    Temporal-Structure (type-2-Element-Type X)

  no-canonical-temporal-structure :
    ¬ Canonical-Temporal-Structure
  no-canonical-temporal-structure F =
    no-section-type-2-Element-Type
      (λ X → earliest (type-2-Element-Type X) (F X))
