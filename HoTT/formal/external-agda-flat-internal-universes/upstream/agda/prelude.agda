{-# OPTIONS --without-K --rewriting #-}

module agda.prelude where

----------------------------------------------------------------------
-- Universe levels
----------------------------------------------------------------------
open import Agda.Primitive public

ℓ₀ = lzero
ℓ₁ = lsuc ℓ₀
ℓ₂ = lsuc ℓ₁
ℓ₃ = lsuc ℓ₂

----------------------------------------------------------------------
-- Equality
----------------------------------------------------------------------
open import Agda.Builtin.Equality public

J :
  {l l' : Level}
  {A : Set l}
  {a : A}
  (C : (x : A) → a ≡ x → Set l')
  (c : C a refl)
  {b : A}
  (p : a ≡ b)
  → ----------------------------
  C b p
J _ c refl = c

symm :
  {l : Level}
  {A : Set l}
  {x y : A}
  (p : x ≡ y)
  → ---------
  y ≡ x
symm refl = refl

infixr 10 _·_
_·_ :
  {l : Level}
  {A : Set l}
  {x y z : A}
  (p : x ≡ y)
  (q : y ≡ z)
  → ---------
  x ≡ z
refl · q = q

cong :
  {l l' : Level}
  {A : Set l}
  {B : Set l'}
  (f : A → B)
  {x y : A}
  (p : x ≡ y)
  → -----------
  f x ≡ f y
cong _ refl = refl

subst :
  {l l' : Level}
  {A  : Set l}
  (B : A → Set l')
  {x y : A}
  (p : x ≡ y)
  → --------------
  B x → B y
subst B refl b = b

subst-cong-assoc :
  {l l' l'' : Level}
  {A : Set l}
  {B : Set l'}
  (C : B → Set l'')
  (f : A → B)
  {x y : A}
  (p : x ≡ y) 
  → ------------------------------------------
  subst (λ x → C (f x)) p ≡ subst C (cong f p)
subst-cong-assoc _ _ refl = refl

congd :
  {l l' : Level}
  {A : Set l}
  {B : A → Set l'}
  (f : (x : A) → B x)
  {x y : A}
  (p : x ≡ y)
  → -----------
  subst B p (f x) ≡ f y
congd _ refl = refl

infix 1 proof_ 
proof_ :
  {l : Level}
  {A : Set l}
  {x y : A}
  → -------------
  x ≡ y → x ≡ y
proof refl = refl

infixr 2 _≡[_]_
_≡[_]_ :
  {l : Level}
  {A : Set l}
  (x : A)
  {y z : A}
  → -------------------
  x ≡ y → y ≡ z → x ≡ z
x ≡[ refl ] p = p

infix  3 _qed 
_qed :
  {l : Level}
  {A : Set l}
  (x : A)
  → ---------
  x ≡ x
_ qed = refl

----------------------------------------------------------------------
-- Rewriting
----------------------------------------------------------------------
{-# BUILTIN REWRITE _≡_ #-}

----------------------------------------------------------------------
-- Unit type
----------------------------------------------------------------------
open import Agda.Builtin.Unit public
    
----------------------------------------------------------------------
-- Functions
----------------------------------------------------------------------
Π :
  {l l' : Level}
  (A : Set l)
  (B : A → Set l')
  → --------------
  Set (l ⊔ l')
Π A B = (x : A) → B x

apply :
  {l l' : Level}
  {A : Set l}
  {B : A → Set l'}
  (x : A)
  → -------------
  Π A B → B x
apply x f  = f x 

infixr 5 _∘_
_∘_ :
  {l m n : Level}
  {A : Set l}
  {B : A → Set m}
  {C : (x : A) → B x → Set n}
  (g : {x : A}(y : B x) → C x y)
  (f : (x : A) → B x)
  (x : A)
  → ----------------------------
  C x (f x)
(g ∘ f) x = g (f x)

id :
 {l : Level}
 {A : Set l}
 → ---------
 A → A
id x = x

congid :
  {l : Level}
  {A : Set l}
  {x y : A}
  (p : x ≡ y)
  → ---------------
  cong id p ≡ p
congid refl = refl

K :
  {l m : Level}
  {A : Set l}
  {B : Set m}
  → -----------
  B → (A → B)
K y _ = y

----------------------------------------------------------------------
-- Empty type
----------------------------------------------------------------------
data ⊥ : Set where

⊥elim : {l : Level}{A : Set l} → ⊥ → A
⊥elim ()

----------------------------------------------------------------------
-- Product type
----------------------------------------------------------------------
infix  1 Σ
infixr 3 _,_
record
  Σ
    {ℓ m : Level}
    (A : Set ℓ)
    (B : A → Set m)
    : -------------
    Set(ℓ ⊔ m)
  where
  constructor _,_
  field
    fst : A
    snd : B fst

open Σ public

syntax Σ A (λ x → B) = Σ x ∶ A , B

Σext :
  {l l' : Level}
  {A : Set l}
  {B : A → Set l'}
  {x x' : A}
  {y : B x}
  {y' : B x'}
  (p : x ≡ x')
  (q : subst B p y ≡ y')
  → --------------------
  (x , y) ≡ (x' , y')
Σext refl refl = refl

infix 6 ⟨_,_⟩
⟨_,_⟩ :
   {l l' l'' : Level}
   {A : Set l}
   {B : Set l'}
   {C : B → Set l''}
   (f : A → B)
   (g : (x : A) → C (f x))
   → ---------------------
   A → Σ B C
⟨ f , g ⟩ x = (f x , g x)

----------------------------------------------------------------------
-- Cartesian product
----------------------------------------------------------------------
infixr 3 _×_
_×_ : {ℓ m : Level} → Set ℓ → Set m → Set (ℓ ⊔ m)
A × B = Σ A (λ _ → B)

×ext :
  {ℓ m : Level}
  {A : Set ℓ}
  {B : Set m}
  {x x' : A}
  {y y' : B}
  (p : x ≡ x')
  (q : y ≡ y')
  → -----------------
  (x , y) ≡ (x' , y')
×ext refl refl = refl

