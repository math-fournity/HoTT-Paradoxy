{- 
Agda-flat proof of Theorem 5.2 from Dan Licata, Ian Orton, Andrew M. Pitts
and Bas Spitters, "Internal Universes in Models of Homotopy Type Theory"
-}

{-# OPTIONS --rewriting --no-pattern-matching #-}

-- Some standard Agda definitions
open import agda.prelude 
-- Some standard Agda-flat definitions
open import agda-flat.prelude
-- The axioms from Section 2
open import agda.postulates
-- Definition 2.2
open import agda.fibration

module theorem-5-2
  -- the proof is parametric in both the path functor
  -- and the composition structure
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
  (C :{♭} {l : Level} (P : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
  where

open Fib ℘ ℘` ℘`comp C

-- The axioms from Section 5
open import agda-flat.tiny ℘ ℘` ℘`comp

{- 
We wish to construct a term of following data type.  (Agda-flat's
current limitations with respect to record types forces us to use a
single-constructor data type here, rather than a record type.)
-}
data Univ (l :{♭} Level) : Set (ℓ₃ ⊔ lsuc (lsuc l)) where
  univ :
    (U  :{♭} Set (ℓ₂ ⊔ lsuc l))
    (El :{♭} Fib l U)
    (code : {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}(Φ :{♭} Fib l Γ) → Γ → U)
    (Elcode : {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}(Φ :{♭} Fib l Γ) → El [ code Φ ] ≡ Φ)
    (codeEl : {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}(γ :{♭} Γ → U) → code (El [ γ ]) ≡ γ)
    → -----------------------------------------------------------------------
    Univ l

-- The display function associated with Set l
Elt : (l :{♭} Level) → Set (lsuc l)
Elt l = Σ A ∶ (Set l) , A

pr₁ : {l :{♭} Level} → Elt l → Set l
pr₁ = fst

-- We form the pullback of R C : Set l → √(Set(ℓ₁ ⊔ l)) and
-- √` pr₁ : √(Elt (ℓ₁ ⊔ l)) → √(Set(ℓ₁ ⊔ l))
U : (l :{♭} Level) → Set (ℓ₂ ⊔ lsuc l)
U l = Σ X ∶ (Set l × √(Elt (ℓ₁ ⊔ l))) , √` pr₁ (snd X) ≡ R C (fst X)

π₁ : {l :{♭} Level} → U l → Set l
π₁ x = fst (fst x)

π₂ : {l :{♭} Level} → U l → √(Elt (ℓ₁ ⊔ l))
π₂ x = snd (fst x)

-- Transposing the pullback square across the adjunction ℘ ⊣ √
-- gives a commutative square
pr₁Lπ₂ :
  {l :{♭} Level}
  → --------------------------
  pr₁ ∘ L (π₂ {l}) ≡ C ∘ ℘` π₁ 
pr₁Lπ₂ = 
  proof
    pr₁ ∘ L π₂
  ≡[ L√ pr₁ π₂ ]
    L (√` pr₁ ∘ π₂)
  ≡[ cong♭ L (funext snd) ]
    L (R C ∘ π₁)
  ≡[ cong♭ L (symm (R℘ π₁ C)) ]
    C ∘ ℘` π₁
  qed

-- L π₂ is of the form ⟨ C ∘ ℘` π₁ , υ ⟩, where υ is:
υ : {l :{♭} Level} → isFib (U l) π₁
υ p = subst id (cong (apply p) pr₁Lπ₂) (snd (L π₂ p))

Lπ₂ :
  {l :{♭} Level}(p : ℘(U l))
  → --------------------------
  L π₂ p ≡ (C (℘` π₁ p) , υ p)
Lπ₂ p = Σext (cong (apply p) pr₁Lπ₂) refl

-- Hence we get a fibration in Fib l (U l):
El : {l :{♭} Level} → Fib l (U l)
El = (π₁ , υ)

-- Now we can construct the code function:
code :
  {l1 l :{♭} Level}
  {Γ :{♭} Set l1}
  (Φ :{♭} Fib l Γ)
  → ------------------------
  Γ → U l
code {l1}{l} {Γ} Aα x = ((A x , f x) , cong (apply x) u)
  where
  A = fst Aα
  α = snd Aα

  f : Γ → √(Elt (ℓ₁ ⊔ l))
  f = R ⟨ C ∘ ℘` A , α ⟩

  u : √` pr₁ ∘ f ≡ R C ∘ A
  u =
    proof
      √` pr₁ ∘ f
    ≡[ cong♭ R (symm (L√ pr₁ f)) ]
      R (pr₁ ∘ ⟨ C ∘ ℘` A , α ⟩)
    ≡[ R℘ A C ]
      R C ∘ A
    qed
    
-- Next we construct Elcode
module _
  {l1 :{♭} Level}
  {l :{♭} Level}
  {Γ :{♭} Set l1}
  (Φ :{♭} Fib l Γ)
  where
  υ∘℘`codeΦ : isFib Γ (fst Φ)
  υ∘℘`codeΦ p = subst C (℘`comp π₁ (code Φ) p) (υ (℘` (code Φ) p))
  υ∘℘code : υ∘℘`codeΦ ≡ snd Φ
  υ∘℘code = funext (λ p → congsnd (v p) refl)
    where
    congsnd :
      {l l' : Level}
      {A : Set l}
      {B : A → Set l'}
      {z z' : Σ A B}
      (p : z ≡ z')
      (q : fst z ≡ fst z')
      → ------------------------
      subst B q (snd z) ≡ snd z'
    congsnd {B = B} {z} {z'} p q =
      proof 
        subst B q (snd z)
      ≡[ cong (λ h → subst B h (snd z)) (uip {p = q} {cong fst p}) ]
        subst B (cong fst p) (snd z)
      ≡[ symm (cong (λ h → h (snd z)) (subst-cong-assoc B fst p)) ]
        subst (λ z₁ → B (fst z₁)) p (snd z)
      ≡[ congd snd p ]
        snd z'
      qed
    
    A : Γ → Set l
    A = fst Φ

    α : isFib Γ A
    α = snd Φ

    v :
      (p : ℘ Γ)
      → --------------------------------------------------
      (C (℘` A p) , υ∘℘`codeΦ p) ≡ (C (℘` A p) , α p)
    v p =
      proof
        (C (℘` A p) , υ∘℘`codeΦ p)
      ≡[ symm (Σext (cong C (℘`comp π₁ (code Φ) p))
          (symm (cong (λ f → f (υ (℘` (code Φ) p))) (subst-cong-assoc (λ A → A) C (℘`comp π₁ (code Φ) p))))) ]
        (C (℘` π₁ (℘` (code Φ) p)) , υ (℘` (code Φ) p))
      ≡[ symm (Lπ₂ (℘`(code Φ) p)) ]
        L π₂ (℘`(code Φ) p)
      ≡[ cong (apply p) (L℘ π₂ (code Φ)) ]
        (C (℘` A p) , α p)
      qed

  Elcode : El [ code Φ ] ≡ Φ
  Elcode = Σext refl υ∘℘code

-- The code function is natural
code[] :
  {l1 l2 l :{♭} Level}
  {Γ :{♭} Set l1}
  {Δ :{♭} Set l2}
  (Φ :{♭} Fib l Γ)
  (γ :{♭} Δ → Γ)
  (x : Δ)
  → -----------------------------
  code (Φ [ γ ]) x ≡ code Φ (γ x)
code[] {l = l} {Γ} Aα γ x = Σext (×ext refl (e x)) uip
  where
  A = fst Aα
  α = snd Aα
  RC℘` : {l' :{♭} Level}{Γ :{♭} Set l'}(_ :{♭} Fib l Γ) → Γ → √ (Elt (lsuc lzero ⊔ l))
  RC℘` Bβ = R ⟨ C ∘ ℘`(fst Bβ) , snd Bβ ⟩
  e :
    (x : _ )
    → ---------------------------------------------------------
    RC℘` (Aα [ γ ]) x ≡ RC℘` Aα (γ x)
  e x = step₁ · step₂ where
    step₁ : RC℘` (Aα [ γ ]) x ≡ R ⟨ C ∘ (℘` A) ∘ (℘` γ) , α ∘ ℘` γ ⟩ x
    step₁ = cong♭ (λ X → R X x) (funext (λ p → symm (helper p))) where
      helper : (p : ℘ _) → (C (℘` A (℘` γ p)) , α (℘` γ p)) ≡ (C (℘` (A ∘ γ) p) , snd (Aα [ γ ]) p)
      helper p = cong (λ x → (C (fst x) , snd x)) (Σext (℘`comp A γ p) refl)
    step₂ : R ⟨ C ∘ (℘` A) ∘ (℘` γ) , α ∘ ℘` γ ⟩ x ≡ RC℘` Aα (γ x)
    step₂ = cong♭ (apply x) (R℘ γ ⟨ C ∘ ℘` A , α ⟩)

-- Next we construct codeEl
codeEl≡id : {l :{♭} Level}(X : U l) → code El X ≡ X
codeEl≡id {l} X = Σext (cong (λ f → (π₁ X , f X)) u) uip
  where
  u : R ⟨ C ∘ ℘` π₁ , υ ⟩ ≡ π₂ {l}
  u = cong♭ R (symm (funext Lπ₂))
 
codeEl :
  {l1 l :{♭} Level}
  {Γ :{♭} Set l1}
  (γ :{♭} Γ → U l)
  → ------------------------
  code (El [ γ ]) ≡ γ
codeEl γ = funext (λ x →
  proof
    code (El [ γ ]) x
  ≡[ code[] El γ x  ]
    code El (γ x)
  ≡[ codeEl≡id (γ x) ]
    γ x
  qed)

-- So altogether we have a term of type Univ l, completeing the proof:
prf : {l :{♭} Level} → Univ l
prf {l} = univ (U l) El code Elcode codeEl

-- We also have the following, which doesn't fix the universe levels of Γ

module UnivOverall (l :{♭} Level) where
  U'  :{♭} Set (ℓ₂ ⊔ lsuc l)
  U' = U l

  El' :{♭} Fib l U'
  El' = El

  code' : {l1 :{♭} Level} {Γ :{♭} Set l1} (Φ :{♭} Fib l Γ) → Γ → U'
  code' = code

  Elcode' : {l1 :{♭} Level} {Γ :{♭} Set l1} (Φ :{♭} Fib l Γ) → El' [ code' Φ ] ≡ Φ
  Elcode' = Elcode

  codeEl' : {l1 :{♭} Level} {Γ :{♭} Set l1} (γ :{♭} Γ → U') → code' (El' [ γ ]) ≡ γ
  codeEl' = codeEl


