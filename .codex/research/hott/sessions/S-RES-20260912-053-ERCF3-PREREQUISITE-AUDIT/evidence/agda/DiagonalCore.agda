{-# OPTIONS --safe --cubical --guardedness #-}

-- ERCF-3 prerequisite probe (T1): the abstract diagonal core.
--
-- 1. Lawvere's fixed-point theorem: an exact encoding e : A -> (A -> B) (with a
--    section) forces every g : B -> B to have a fixed point.
-- 2. Bool has a fixed-point-free endomorphism (not), so no exact encoding
--    A -> (A -> Bool) exists.  This is the abstract form of "a code space
--    cannot exactly enumerate and observe all Bool-valued predicates on itself".
-- 3. Positive control: the fragment of constant predicates IS exactly
--    representable, so the impossibility is precisely about exactness of the
--    full self-encoding, not about encodings as such.
module DiagonalCore where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.Data.Sigma
open import Cubical.Data.Empty

¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
¬ A = A → ⊥

private
  variable
    ℓ ℓ' : Level

-- T1a: Lawvere fixed point.
lawvere-fixed-point :
  {A : Type ℓ} {B : Type ℓ'}
  (e : A → (A → B))
  (s : (f : A → B) → Σ[ a ∈ A ] e a ≡ f)
  (g : B → B)
  → Σ[ b ∈ B ] g b ≡ b
lawvere-fixed-point {A = A} {B = B} e s g = e a a , sym (cong (λ h → h a) p)
  where
  f : A → B
  f x = g (e x x)

  r : Σ[ a ∈ A ] e a ≡ f
  r = s f

  a : A
  a = fst r

  p : e a ≡ f
  p = snd r

-- T1b: Bool has a fixed-point-free endomorphism.
not-fixed-point-free : ∀ b → ¬ (not b ≡ b)
not-fixed-point-free true = false≢true
not-fixed-point-free false = true≢false

-- T1c: no exact self-encoding of all Bool-valued predicates on a code space.
no-exact-self-encoding :
  {A : Type ℓ}
  (e : A → (A → Bool))
  (s : (f : A → Bool) → Σ[ a ∈ A ] e a ≡ f)
  → ⊥
no-exact-self-encoding e s =
  not-fixed-point-free
    (fst (lawvere-fixed-point e s not))
    (snd (lawvere-fixed-point e s not))

-- T1d (positive control): the constant-predicate fragment is exactly
-- representable: every constant predicate has a code, and the encoding is
-- injective, so exactness on a restricted family is not blocked.
const-code : Bool → (Bool → Bool)
const-code b _ = b

const-code-injective : ∀ b c → const-code b ≡ const-code c → b ≡ c
const-code-injective b c p = cong (λ h → h true) p

const-code-hits : (b : Bool) → Σ[ c ∈ Bool ] const-code c ≡ const-code b
const-code-hits b = b , refl
