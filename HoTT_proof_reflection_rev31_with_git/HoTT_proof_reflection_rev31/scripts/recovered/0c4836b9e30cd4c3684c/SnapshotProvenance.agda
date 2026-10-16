module SnapshotProvenance where

open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where
¬_ : Set → Set
¬ A = A → ⊥
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬ (x ≡ y)

data Bit : Set where b0 b1 : Bit
neq01 : b0 ≢ b1
neq01 ()

data Unit : Set where unit : Unit

sym : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q


snapshot : Bit → Unit
snapshot _ = unit
provenance : Bit → Bit
provenance h = h

snapshotCannotRecoverProvenance :
  (r : Unit → Bit) → ¬ ((h : Bit) → r (snapshot h) ≡ provenance h)
snapshotCannotRecoverProvenance r exact =
  neq01 (trans (sym (exact b0)) (exact b1))
