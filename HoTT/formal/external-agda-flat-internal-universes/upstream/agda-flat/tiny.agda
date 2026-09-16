{- Use with Andrea Vezzosi's agda-flat -}
{-# OPTIONS --no-pattern-matching --rewriting #-}

-- Some standard Agda definitions
open import agda.prelude
-- Some standard Agda-flat definitions
open import agda-flat.prelude
-- Definition 2.2
open import agda.fibration


module agda-flat.tiny
  -- the path functor is a parameter
  (℘ :{♭}
    {l : Level}
    (Γ : Set l)
    → ---------
    Set l)
  (℘` :{♭}
    {l m : Level}
    {Γ : Set l}
    {Δ : Set m}
    (γ : Δ → Γ)
    → -----------
    ℘ Δ → ℘ Γ)
  (℘`comp :{♭}
    {l m n : Level}
    {Γ : Set l}
    {Δ : Set m}
    {Θ : Set n}
    (γ : Δ → Γ)
    (σ : Θ → Δ)
    (p : ℘ Θ)
    → -----------
    ℘` γ (℘` σ p) ≡ ℘` (γ ∘ σ) p)
  where

----------------------------------------------------------------------
-- Instantiating this module with a path object functor, ℘, asserts
-- that ℘ has a right adjoint, √. For ℘ = 𝕀 → (_) this follows from
-- the fact that the interval is tiny.
----------------------------------------------------------------------
postulate
  -- the value of the right adjoint on objects
  √  :
    {l :{♭} Level}
    (A :{♭} Set l)
    → ------------
    Set l
  -- right transposition across the adjunction 
  R  :
    {l l' :{♭} Level}
    {A :{♭} Set l}
    {B :{♭} Set l'}
    (f :{♭} ℘ A → B)
    → ---------------
    A → √ B
  -- left transposition across the adjunction
  L  :
    {l l' :{♭} Level}
    {A :{♭} Set l}
    {B :{♭} Set l'}
    (g :{♭} A → √ B)
    → --------------
    ℘ A → B
  -- right and left transposition are mutually inverse
  LR :
    {l l' :{♭} Level}
    {A :{♭} Set l}
    {B :{♭} Set l'}
    {f :{♭} ℘ A → B}
    → ---------------
    L (R f) ≡ f
  RL :
    {l l' :{♭} Level}
    {A :{♭} Set l}
    {B :{♭} Set l'}
    {g :{♭} A → √ B}
    → ---------------
    R (L g) ≡ g
  -- one-sided naturality of right transposition
  R℘ :
    {l l' l'' :{♭} Level}
    {A :{♭} Set l}
    {B :{♭} Set l'}
    {C :{♭} Set l''}
    (g :{♭} A → B)
    (f :{♭} ℘ B → C)
    → --------------------
    R (f ∘ ℘` g) ≡ R f ∘ g

{-# REWRITE LR RL #-}
{- 
The use of these REWRITES is not necessary, but it does simplify
proofs of equality in the paper by making some of the steps
computational. The proof of L℘ below is an example.
-}

-- One-sided naturality of left transposition is derivable
L℘ :
  {l l' l'' :{♭} Level}
  {A :{♭} Set l}
  {B :{♭} Set l'}
  {C :{♭} Set l''}
  (f :{♭} B → √ C)
  (g :{♭} A → B)
  → --------------------
  L f ∘ ℘` g ≡ L (f ∘ g)
L℘ f g = cong♭ L (R℘ g (L f))
{- 
Here is the proof without declaring LR and RL to be REWRITES:
     proof
       (L f ∘ ℘` g)
     ≡[ symm LR  ]
       L (R (L f ∘ ℘` g))
     ≡[ cong♭ L (R℘ g (L f)) ]
       L (R (L f) ∘ g)
     ≡[ cong♭ (λ h → L (h ∘ g)) RL ]
       L (f ∘ g)
     qed
-}
  
-- Functoriality of √
√` :
  {l l' :{♭} Level}
  {A :{♭} Set l}
  {B :{♭} Set l'}
  (f :{♭} A → B)
  → ---------------
  √ A → √ B
√` f = R (f ∘ L id)

-- The other naturality property of right transposition
√R :
  {l l' l'' :{♭} Level}
  {A :{♭} Set l}
  {B :{♭} Set l'}
  {C :{♭} Set l''}
  (g :{♭} B → C)
  (f :{♭} ℘ A → B)
  → --------------------
  √` g ∘ R f ≡ R (g ∘ f)
√R g f =
  proof
    R (g ∘ L id) ∘ R f
  ≡[ symm (R℘ (R f) (g ∘ L id)) ]
    R (g ∘ L id ∘ ℘`(R f))
  ≡[ cong♭ (λ h → R (g ∘ h)) (L℘ id (R f)) ]
    R (g ∘ f)
  qed

-- The other naturality property of left transposition
L√ :
  {l l' l'' :{♭} Level}
  {A :{♭} Set l}
  {B :{♭} Set l'}
  {C :{♭} Set l''}
  (g :{♭} B → C)
  (f :{♭} A → √ B)
  → ---------------------
  g ∘ L f  ≡ L (√` g ∘ f)
L√ g f = cong♭ L (symm (√R g (L f)))
