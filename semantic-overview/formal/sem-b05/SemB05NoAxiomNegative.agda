module SemB05NoAxiomNegative where

open import Agda.Builtin.Bool
open import Agda.Builtin.Equality

-- Negative control: without the explicit reflection postulate, reflexivity
-- cannot inhabit this false equality.
false-equality-without-axiom : true ≡ false
false-equality-without-axiom = refl
