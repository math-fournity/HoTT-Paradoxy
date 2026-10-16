{-# OPTIONS --without-K #-}

module agda.fibration where

open import agda.prelude
open import agda.postulates

----------------------------------------------------------------------
-- The extension relation
----------------------------------------------------------------------
infix 4 _↗_
_↗_ :
  {l : Level}
  {φ : Set}
  {A : Set l}
  (t : φ → A)
  (x : A)
  → ---------
  Set l
t ↗ x = ∀ u → t u ≡ x

----------------------------------------------------------------------
-- Fibrations for a given composition structure
----------------------------------------------------------------------

-- A version where composition structure is polymorphic in levels
module
  Fib
    -- the path functor is a parameter
    (℘ :
       {l : Level}
       (Γ : Set l)
       → ---------
       Set l)
     (℘` :
       {l m : Level}
       {Γ : Set l}
       {Δ : Set m}
       (γ : Δ → Γ)
       → -----------
       ℘ Δ → ℘ Γ)
     (℘`comp :
       {l m n : Level}
       {Γ : Set l}
       {Δ : Set m}
       {Θ : Set n}
       (γ : Δ → Γ)
       (σ : Θ → Δ)
       (p : ℘ Θ)
       → -----------
       ℘` γ (℘` σ p) ≡ ℘` (γ ∘ σ) p)
    -- composition structure is a parameter
    (C : {l : Level} (P : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
    where
  
  -- Fibration structures
  isFib :
    {l l' : Level}
    (Γ : Set l')
    (A : Γ → Set l)
    → ---------------
    Set (ℓ₁ ⊔ l ⊔ l')
  isFib Γ A = (p : ℘ Γ) → C (℘` A p)
  
  -- Fibrations
  Fib :
    {l' : Level}
    (l : Level)
    (Γ : Set l')
    → ---------------
    Set (l' ⊔ lsuc l)
  Fib l Γ = Σ A ∶ (Γ → Set l), isFib Γ A

  -- Re-indexing
  infixl 5 _[_]
  _[_] :
    {l l' l'' : Level}
    {Γ : Set l'}
    {Γ' : Set l''}
    (Φ : Fib l Γ)
    (γ : Γ' → Γ)
    → --------------
    Fib l Γ'
  (A , α) [ γ ] = (A ∘ γ , α[γ]) where
    α[γ] : isFib _ (A ∘ γ)
    α[γ] p' = subst C (℘`comp A γ p') (α (℘` γ p'))


  Fib₀ :
    {l' : Level}
    (Γ : Set l')
    → -----------
    Set (ℓ₁ ⊔ l')
  Fib₀ = Fib ℓ₀

-- A version  where composition structure is just at level 0
module
  Fib₀
    -- the path functor is a parameter
    (℘ :
       {l : Level}
       (Γ : Set l)
       → ---------
       Set l)
     (℘` :
       {l m : Level}
       {Γ : Set l}
       {Δ : Set m}
       (γ : Δ → Γ)
       → -----------
       ℘ Δ → ℘ Γ)
     (℘`comp :
       {l m n : Level}
       {Γ : Set l}
       {Δ : Set m}
       {Θ : Set n}
       (γ : Δ → Γ)
       (σ : Θ → Δ)
       (p : ℘ Θ)
       → -----------
       ℘` γ (℘` σ p) ≡ ℘` (γ ∘ σ) p)
    -- composition structure is a parameter
    (C : ℘ Set → Set₁) where
  
  -- Fibration structures
  isFib :
    {l' : Level}
    (Γ : Set l')
    (A : Γ → Set)
    → -----------
    Set (ℓ₁ ⊔ l')
  isFib Γ A = (p : ℘ Γ) → C (℘` A p)

  -- Fibrations
  Fib₀ :
    {l' : Level}
    (Γ : Set l')
    → -----------
    Set (ℓ₁ ⊔ l')
  Fib₀ Γ = Σ A ∶ (Γ → Set), isFib Γ A
  
   -- Re-indexing operation
  infixl 5 _[_]
  _[_] :
    {l' l'' : Level}
    {Γ : Set l'}
    {Γ' : Set l''}
    (Φ : Fib₀ Γ)
    (γ : Γ' → Γ)
    → --------------
    Fib₀ Γ'
  (A , α) [ γ ] = (A ∘ γ , α[γ]) where
    α[γ] : isFib _ (A ∘ γ)
    α[γ] p' = subst C (℘`comp A γ p') (α (℘` γ p'))
  
