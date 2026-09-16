{- Use with Andrea Vezzosi's agda-flat -}
{-# OPTIONS --without-K #-}

module agda-flat.prelude where

open import agda.prelude

----------------------------------------------------------------------
-- Congruence property for functions of a crisp variable
----------------------------------------------------------------------

cong♭ :
  {l :{♭} Level}
  {A :{♭} Set l}
  {l' : Level}
  {B : Set l'}
  (f : (x :{♭} A) → B){x y :{♭} A}
  → ------------------------------
  (_ :{♭} x ≡ y) → f x ≡ f y
cong♭ _ refl = refl

----------------------------------------------------------------------
-- Example that's in the paper
----------------------------------------------------------------------
private 
  right : (A :{♭} Set) (B : Set) (f : (_ :{♭} A) → B) (x :{♭} A) → B
  right A B f x = f x
