module SemB04FalseEqualityNegative where

open import category-theory.precategories
open import foundation.universe-levels
open import foundation-core.identity-types
open import reflection.precategory-solver

module _
  {l1 l2 : Level}
  {C : Precategory l1 l2}
  {x y : obj-Precategory C}
  {f g : hom-Precategory C x y}
  where

  -- Expected to be rejected: no precategory axiom identifies arbitrary f and g.
  arbitrary-morphisms-equal : f ＝ g
  arbitrary-morphisms-equal = solve-Precategory! C
