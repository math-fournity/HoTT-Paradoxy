{-# OPTIONS --safe --cubical --guardedness #-}
module EndpointMaps where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool
open import Cubical.Data.Empty
open import Cubical.Data.Sigma

-- Distinct boundary marks cannot acquire equal images under an injective map.
injectivePreservesDistinct : {ℓ ℓ' : Level} {E : Type ℓ} {F : Type ℓ'}
  (f : E → F) → ((x y : E) → f x ≡ f y → x ≡ y)
  → (a b : E) → ((a ≡ b) → ⊥) → (f a ≡ f b) → ⊥
injectivePreservesDistinct f inj a b separate imagePath = separate (inj a b imagePath)

-- A general ambient equivalence is an eligible injective change of coordinates.
equivalencePreservesDistinct : {ℓ ℓ' : Level} {E : Type ℓ} {F : Type ℓ'}
  (e : E ≃ F) (a b : E) → ((a ≡ b) → ⊥) → (equivFun e a ≡ equivFun e b) → ⊥
equivalencePreservesDistinct e a b separate p = separate
  (sym (retEq e a) ∙ cong (invEq e) p ∙ retEq e b)

-- Explicit restricted deformation language: only the interior Boolean varies.
Shape : Type
Shape = Bool × (Bool × Bool)

data Reach : Shape → Shape → Type where
  stay : {x : Shape} → Reach x x
  deform : (l r u v : Bool) → Reach (l , r , u) (l , r , v)
  chain : {x y z : Shape} → Reach x y → Reach y z → Reach x z

leftInvariant : {x y : Shape} → Reach x y → fst x ≡ fst y
leftInvariant stay = refl
leftInvariant (deform l r u v) = refl
leftInvariant (chain p q) = leftInvariant p ∙ leftInvariant q

N M : Shape
N = false , true , false
M = true , true , false

relativeNonreach : Reach N M → ⊥
relativeNonreach p = false≢true (leftInvariant p)

nontrivialInteriorChange : Reach M (true , true , true)
nontrivialInteriorChange = deform true true false true

-- Adding a permitted construction changes the question; it is not forbidden by HoTT.
data ExtendedReach : Shape → Shape → Type where
  old : {x y : Shape} → Reach x y → ExtendedReach x y
  construct : (x : Shape) → ExtendedReach x M

extendedReachable : ExtendedReach N M
extendedReachable = construct N
