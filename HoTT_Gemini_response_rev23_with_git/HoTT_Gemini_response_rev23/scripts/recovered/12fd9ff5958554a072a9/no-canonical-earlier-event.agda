module no-canonical-earlier-event where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

-- A canonical "earlier event" on an unlabeled two-event history is exactly a
-- global section of the canonical family over the type of 2-element types.
Canonical-Earlier-Event : (l : Level) → UU (lsuc l)
Canonical-Earlier-Event l =
  (X : 2-Element-Type l) → type-2-Element-Type X

no-canonical-earlier-event :
  {l : Level} → ¬ (Canonical-Earlier-Event l)
no-canonical-earlier-event = no-section-type-2-Element-Type
