{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The one-line definition of semi-simplicial structure, in Cubical Agda
  (Claude, session 7f138325, 2026-09-26; goal CG-002, gate G2).

  proof id : MP-CG001-WILD-SST-001
  claim    : CG001-C-64 (full statement in CLAIM.md)

  WildSST is the presheaf-style definition used when sameness is a mere fact:
  a type X n of n-simplices, face maps d n i : X (n+1) -> X n, and the
  semi-simplicial identities d_i d_{j+1} = d_j d_i (i <= j), each given as
  an equation.  The same definition is written in Lean 4 in the companion
  package wild-sst-lean (CG001-C-65), with the same Fin, weaken and order.

  Coh2 is the next condition up (the hexagon): rewriting d_i d_{j+1} d_{k+2}
  into d_k d_j d_i can be done along two routes, and the two resulting proofs
  should agree.

  (a) If every X n is a set, Coh2 holds for every instance (setsCohere).
  (b) The instance spin (X n = S1, every face map the identity, every
      identity refl except sid 0 zero zero = rotLoop) satisfies all the face
      identities of the definition, yet at m = 0, i = j = k = 0 the two routes
      wind once and twice around the circle at base, so Coh2 fails
      (spinIncoherent).

  So the same text that defines semi-simplicial sets correctly defines, in
  homotopy type theory, a structure that admits incoherent data.
-}
module WildSST where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Nat.Properties using (znots ; injSuc)
open import Cubical.Data.Sum using (_⊎_ ; inl ; inr)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Int using (ℤ ; pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.HITs.S1.Base using (S¹ ; base ; loop ; rotLoop ; winding)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- Fin n, weaken and the order, by recursion on n (the same definitions as
-- in the Lean package; recursion avoids indexed pattern matching).

Fin : ℕ → Type
Fin zero = ⊥
Fin (suc n) = Unit ⊎ Fin n

fzero : {n : ℕ} → Fin (suc n)
fzero = inl tt

fsuc : {n : ℕ} → Fin n → Fin (suc n)
fsuc = inr

weaken : {n : ℕ} → Fin n → Fin (suc n)
weaken {suc n} (inl _) = inl tt
weaken {suc n} (inr i) = inr (weaken i)

_≤F_ : {n : ℕ} → Fin n → Fin n → Type
_≤F_ {suc n} (inl _) _ = Unit
_≤F_ {suc n} (inr _) (inl _) = ⊥
_≤F_ {suc n} (inr a) (inr b) = a ≤F b

≤F-trans : {n : ℕ} (a b c : Fin n) → a ≤F b → b ≤F c → a ≤F c
≤F-trans {suc n} (inl _) b c _ _ = tt
≤F-trans {suc n} (inr a) (inl _) c () q
≤F-trans {suc n} (inr a) (inr b) (inl _) p ()
≤F-trans {suc n} (inr a) (inr b) (inr c) p q = ≤F-trans a b c p q

weaken≤ : {n : ℕ} (a b : Fin n) → a ≤F b → weaken a ≤F weaken b
weaken≤ {suc n} (inl _) b _ = tt
weaken≤ {suc n} (inr a) (inl _) ()
weaken≤ {suc n} (inr a) (inr b) p = weaken≤ a b p

weaken≤suc : {n : ℕ} (a b : Fin n) → a ≤F b → weaken a ≤F fsuc b
weaken≤suc {suc n} (inl _) b _ = tt
weaken≤suc {suc n} (inr a) (inl _) ()
weaken≤suc {suc n} (inr a) (inr b) p = weaken≤suc a b p

------------------------------------------------------------------------
-- The definition.

record WildSST : Type₁ where
  field
    X   : ℕ → Type
    d   : (n : ℕ) → Fin (suc (suc n)) → X (suc n) → X n
    sid : (n : ℕ) (i j : Fin (suc (suc n))) → i ≤F j → (x : X (suc (suc n)))
        → d n i (d (suc n) (fsuc j) x) ≡ d n j (d (suc n) (weaken i) x)

------------------------------------------------------------------------
-- The two routes from d_i d_{j+1} d_{k+2} to d_k d_j d_i, and the hexagon.

module Routes (S : WildSST) where
  open WildSST S

  routeA : (m : ℕ) (i j k : Fin (suc (suc m))) (p : i ≤F j) (q : j ≤F k)
    (x : X (suc (suc (suc m))))
    → d m i (d (suc m) (fsuc j) (d (suc (suc m)) (fsuc (fsuc k)) x))
      ≡ d m k (d (suc m) (weaken j) (d (suc (suc m)) (weaken (weaken i)) x))
  routeA m i j k p q x =
      cong (d m i) (sid (suc m) (fsuc j) (fsuc k) q x)
    ∙ sid m i k (≤F-trans i j k p q) (d (suc (suc m)) (weaken (fsuc j)) x)
    ∙ cong (d m k) (sid (suc m) (weaken i) (weaken j) (weaken≤ i j p) x)

  routeB : (m : ℕ) (i j k : Fin (suc (suc m))) (p : i ≤F j) (q : j ≤F k)
    (x : X (suc (suc (suc m))))
    → d m i (d (suc m) (fsuc j) (d (suc (suc m)) (fsuc (fsuc k)) x))
      ≡ d m k (d (suc m) (weaken j) (d (suc (suc m)) (weaken (weaken i)) x))
  routeB m i j k p q x =
      sid m i j p (d (suc (suc m)) (fsuc (fsuc k)) x)
    ∙ cong (d m j) (sid (suc m) (weaken i) (fsuc k)
                      (weaken≤suc i k (≤F-trans i j k p q)) x)
    ∙ sid m j k q (d (suc (suc m)) (weaken (weaken i)) x)

open Routes

Coh₂ : WildSST → Type
Coh₂ S = (m : ℕ) (i j k : Fin (suc (suc m))) (p : i ≤F j) (q : j ≤F k)
  (x : WildSST.X S (suc (suc (suc m))))
  → routeA S m i j k p q x ≡ routeB S m i j k p q x

------------------------------------------------------------------------
-- (a) When sameness is a fact at every level, the hexagon is automatic.

setsCohere : (S : WildSST) → ((n : ℕ) → isSet (WildSST.X S n)) → Coh₂ S
setsCohere S setX m i j k p q x =
  setX m _ _ (routeA S m i j k p q x) (routeB S m i j k p q x)

------------------------------------------------------------------------
-- (b) An instance on the circle that satisfies every face identity of the
-- definition but not the hexagon.

spin : WildSST
WildSST.X spin _ = S¹
WildSST.d spin _ _ x = x
WildSST.sid spin zero (inl _) (inl _) _ x = rotLoop x
WildSST.sid spin _ _ _ _ x = refl

routeA-spin : base ≡ base
routeA-spin = routeA spin zero fzero fzero fzero tt tt base

routeB-spin : base ≡ base
routeB-spin = routeB spin zero fzero fzero fzero tt tt base

windsOnce : winding routeA-spin ≡ pos 1
windsOnce = refl

windsTwice : winding routeB-spin ≡ pos 2
windsTwice = refl

spinIncoherent : ¬ Coh₂ spin
spinIncoherent h =
  znots (injSuc (injPos (sym windsOnce ∙ cong winding (h zero fzero fzero fzero tt tt base)
                         ∙ windsTwice)))
