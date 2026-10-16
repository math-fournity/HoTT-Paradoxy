{-# OPTIONS --safe --without-K #-}
module RestrictedReflection where

-- Shared intensional type-theory fragment. Not compiled in this session.
-- This is a dependent interpreter and proof transformer for an explicit small
-- object theory, NOT an interpreter for the whole Agda/HoTT ambient language.
open import Agda.Primitive using (Level; lzero; lsuc; _⊔_)
open import Agda.Builtin.Nat using (Nat)
open import Agda.Builtin.List using (List; []; _∷_)

data Empty : Set where

elimEmpty : ∀ {ℓ} {X : Set ℓ} → Empty → X
elimEmpty ()

data Form : Set where
  atom : Nat → Form
  bot : Form
  _⇒_ : Form → Form → Form
infixr 5 _⇒_

infix 4 _∈_
data _∈_ {X : Set} (a : X) : List X → Set where
  here : ∀ {xs} → a ∈ (a ∷ xs)
  there : ∀ {b xs} → a ∈ xs → a ∈ (b ∷ xs)

data Der (Σ : List Form) : List Form → Form → Set where
  hyp : ∀ {Γ A} → A ∈ Γ → Der Σ Γ A
  ax : ∀ {Γ A} → A ∈ Σ → Der Σ Γ A
  lam : ∀ {Γ A B} → Der Σ (A ∷ Γ) B → Der Σ Γ (A ⇒ B)
  app : ∀ {Γ A B} → Der Σ Γ (A ⇒ B) → Der Σ Γ A → Der Σ Γ B
  absurd : ∀ {Γ A} → Der Σ Γ bot → Der Σ Γ A

-- At the fixed semantic universe ℓ, atoms can denote arbitrary types.
-- A lifted empty type keeps this file independent of a standard library.
data EmptyAt {ℓ : Level} : Set ℓ where

emptyAtElim : ∀ {ℓ ℓ′} {X : Set ℓ′} → EmptyAt {ℓ} → X
emptyAtElim ()

El : ∀ {ℓ} → (Nat → Set ℓ) → Form → Set ℓ
El ρ (atom n) = ρ n
El ρ bot = EmptyAt
El ρ (A ⇒ B) = El ρ A → El ρ B

Val : ∀ {ℓ} → (Nat → Set ℓ) → List Form → Set ℓ
Val ρ Γ = ∀ {A} → A ∈ Γ → El ρ A

extend : ∀ {ℓ} {ρ : Nat → Set ℓ} {Γ A} → Val ρ Γ → El ρ A → Val ρ (A ∷ Γ)
extend γ a here = a
extend γ a (there i) = γ i

interpret : ∀ {ℓ} {ρ : Nat → Set ℓ} {Σ Γ A} →
            Der Σ Γ A → Val ρ Σ → Val ρ Γ → El ρ A
interpret (hyp i) α γ = γ i
interpret (ax i) α γ = α i
interpret (lam d) α γ = λ a → interpret d α (extend γ a)
interpret (app d e) α γ = interpret d α γ (interpret e α γ)
interpret (absurd d) α γ = emptyAtElim (interpret d α γ)

Ren : List Form → List Form → Set
Ren Γ Δ = ∀ {A} → A ∈ Γ → A ∈ Δ

lift : ∀ {Γ Δ A} → Ren Γ Δ → Ren (A ∷ Γ) (A ∷ Δ)
lift r here = here
lift r (there i) = there (r i)

rename : ∀ {Σ Γ Δ A} → Ren Γ Δ → Der Σ Γ A → Der Σ Δ A
rename r (hyp i) = hyp (r i)
rename r (ax i) = ax i
rename r (lam d) = lam (rename (lift r) d)
rename r (app d e) = app (rename r d) (rename r e)
rename r (absurd d) = absurd (rename r d)

closedWeakening : ∀ {Σ Γ A} → Der Σ [] A → Der Σ Γ A
closedWeakening d = rename (λ ()) d

Bridges : List Form → List Form → Set
Bridges Σ Δ = ∀ {A} → A ∈ Σ → Der Δ [] A

migrate : ∀ {Σ Δ Γ A} → Bridges Σ Δ → Der Σ Γ A → Der Δ Γ A
migrate b (hyp i) = hyp i
migrate b (ax i) = closedWeakening (b i)
migrate b (lam d) = lam (migrate b d)
migrate b (app d e) = app (migrate b d) (migrate b e)
migrate b (absurd d) = absurd (migrate b d)

WholeTransfer : List Form → List Form → Set
WholeTransfer Σ Δ = ∀ {A} → Der Σ [] A → Der Δ [] A

bridges-to-transfer : ∀ {Σ Δ} → Bridges Σ Δ → WholeTransfer Σ Δ
bridges-to-transfer b = migrate b

transfer-to-bridges : ∀ {Σ Δ} → WholeTransfer Σ Δ → Bridges Σ Δ
transfer-to-bridges f i = f (ax i)

-- Mutual implications, NOT a proof that these transformations are inverse on
-- proof-relevant function spaces.

data Extended (Σ : List Form) : List Form → Form → Set where
  base : ∀ {Γ A} → Der Σ Γ A → Extended Σ Γ A
  imported : ∀ {Θ Γ A} → Bridges Θ Σ → Der Θ [] A → Extended Σ Γ A
  lamE : ∀ {Γ A B} → Extended Σ (A ∷ Γ) B → Extended Σ Γ (A ⇒ B)
  appE : ∀ {Γ A B} → Extended Σ Γ (A ⇒ B) → Extended Σ Γ A → Extended Σ Γ B
  absurdE : ∀ {Γ A} → Extended Σ Γ bot → Extended Σ Γ A

expand : ∀ {Σ Γ A} → Extended Σ Γ A → Der Σ Γ A
expand (base d) = d
expand (imported b d) = closedWeakening (migrate b d)
expand (lamE d) = lam (expand d)
expand (appE d e) = app (expand d) (expand e)
expand (absurdE d) = absurd (expand d)

identity : ∀ {Σ A} → Der Σ [] (A ⇒ A)
identity = lam (hyp here)

-- A constructive separating model: the target assumes Q (possibly twice),
-- but cannot derive P. No classical truth-table completeness is needed.
open import Agda.Builtin.Unit using (⊤; tt)
open import Agda.Builtin.Nat using (zero; suc)

P : Form
P = atom zero
Q : Form
Q = atom (suc zero)

separating : Nat → Set
separating zero = EmptyAt
separating (suc n) = ⊤

targetModel : Val separating (Q ∷ Q ∷ [])
targetModel here = tt
targetModel (there here) = tt
targetModel (there (there ()))

noTargetP : Der (Q ∷ Q ∷ []) [] P → EmptyAt {lzero}
noTargetP d = interpret d targetModel (λ ())
