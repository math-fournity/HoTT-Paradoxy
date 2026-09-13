module SemB04Positive where

open import category-theory.precategories
open import foundation.universe-levels
open import foundation-core.identity-types
open import reflection.precategory-solver

module _
  {l1 l2 : Level}
  {C : Precategory l1 l2}
  {a b c d : obj-Precategory C}
  {f : hom-Precategory C a b}
  {g : hom-Precategory C b c}
  {h : hom-Precategory C c d}
  where

  associativity-via-reflection :
    comp-hom-Precategory C h (comp-hom-Precategory C g f) ＝
    comp-hom-Precategory C (comp-hom-Precategory C h g) f
  associativity-via-reflection = solve-Precategory! C
