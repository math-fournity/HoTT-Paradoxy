{- 
Agda proof of Theorem 3.1 from Dan Licata, Ian Orton, Andrew M. Pitts
and Bas Spitters, "Internal Universes in Models of Homotopy Type Theory"
-}

{-# OPTIONS --no-pattern-matching #-}

module theorem-3-1 where

-- Some standard Agda definitions
open import agda.prelude
-- The axioms from Section 2
open import agda.postulates
-- Definition 2.2
open import agda.fibration
-- Theorem 3.1 concerns the path functor given by exponenting by 𝕀
open import agda.exp-path


{- 
We first show that if there is a universe that is weakly generic for
fibrations (for a given composition structure C), then families of
types that are fiberwise fibrant are fibrations.
-} 
record IntUniv (C : ℘ Set → Set₁) : Set₃
  where
  open Fib₀ ℘ ℘` ℘`comp C
  field
    U       : Set₂
    El      : Fib₀ U
    code    : {Γ : Set}(Φ : Fib₀ Γ) → Γ → U
    Elcode  : {Γ : Set}(Φ : Fib₀ Γ) → El [ code Φ ] ≡ Φ

  fiberwise-fibrant-is-fibrant :
    (P : ℘ Set)
    (π : (i : 𝕀) → isFib ⊤ (λ _ → P i))
    → ---------------------------------
    isFib 𝕀 P
  fiberwise-fibrant-is-fibrant P π = subst (isFib 𝕀) u (snd Φ)
    where
    Φ : Fib₀ 𝕀
    Φ = (El [ (λ i → code ((λ _ → P i) ,  π i) tt) ])

    u : fst Φ ≡ P
    u = funext (λ i → cong (λ x → fst x tt) (Elcode ((λ _ → P i) , π i)))

{-
 Next we show that if the composition structure has some reasonable
properties, there can be no such internal weakly generic universe.
-}
NoIntUniv :
  (C : ℘ Set → Set₁)
  -- if C has a transport function 
  (coe : (P : ℘ Set) → C P → P O → P I)
  -- and each constant path of types with value O ≡ i
  -- has a composition structure
  (O≡ : (i : 𝕀) → C (λ _ → O ≡ i))
  -- then there is no internal universe 
  → -----------------------------------
  IntUniv C → ⊥
NoIntUniv C coe O≡ iu = O≠I (coe P c refl)
  where
  P : ℘ Set
  P i = O ≡ i

  c : C P
  c = IntUniv.fiberwise-fibrant-is-fibrant iu P (λ i _ → O≡ i) id

{- 
CCHM composition has those properties, so there
is no weakly generic universe for CCHM fibrations.
-}
module NoIntCCHMUniv where
  open import agda.cchm

  coe :
    {l : Level}
    (P : ℘ (Set l))
    (c : CCHM P)
    → -------------
    P O → P I
  coe P c x =
    fst (c ⊥ cof⊥ (λ _ ()) (x , λ ())) 
    
  O≡ :
    (i : 𝕀)
    → -----------------
    CCHM (λ _ → O ≡ i)
  O≡ i _ _ _ a₀+ = (fst a₀+ , λ _ → uip) 
     
  NoIntCCHMUniv : IntUniv CCHM → ⊥
  NoIntCCHMUniv iu = NoIntUniv CCHM coe O≡ iu

{- 
Compostion from "Cartesian Cubical Type Theory" by Angiuli et al also
has those properties, so there is no weakly generic universe for this
kind of fibration either.
-}
module NoIntCCTTUniv where
  open import agda.cctt

  coe :
    {l : Level}
    (P : ℘ (Set l))
    (c : CCTT P)
    → -------------
    P O → P I
  coe P c x = fst (c ⊥ cof⊥ (λ _ ()) O x (λ ())) I
   
  O≡ :
    (i : 𝕀)
    → -----------------
    CCTT (λ _ → O ≡ i)
  O≡ r φ cofφ t r' b text =
    -- use J explicitly to avoid pattern-matching
    J (λ r₁ b₁ →  
        (t₁ : (i : 𝕀) → φ → O ≡ r₁) →
        Σ ((x : 𝕀) → O ≡ r₁)
        (λ f → Σ (f r' ≡ b₁) (λ _ → (j : 𝕀) (u : φ) → t₁ j u ≡ f j)))
      (λ t → ((λ _ → refl)) , refl , (λ _ _ → uip)) b t

  NoIntCCTTUniv : IntUniv CCTT → ⊥
  NoIntCCTTUniv iu = NoIntUniv CCTT coe O≡ iu
