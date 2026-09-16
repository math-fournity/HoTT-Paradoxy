{-# OPTIONS --without-K #-}

module agda.postulates where

open import agda.prelude

postulate
  -- Function extensionality
  funext :
    {l l' : Level}
    {A : Set l}
    {B : A → Set l'}
    {f g : (x : A) → B x}
    (_ : (x : A) → f x ≡ g x)
    → -----------------------
    f ≡ g

  -- Uniqueness of identity proofs
  uip :
    {l : Level}
    {A : Set l}
    {x y : A}
    {p q : x ≡ y}
    → -----------
    p ≡ q

  -- The interval
  𝕀   : Set
  O   : 𝕀
  I   : 𝕀
  O≠I : O ≡ I → ⊥

  -- Cofibrant types
  cof  : Set → Set
  cof⊥ : cof ⊥ -- (O ≡ I)
