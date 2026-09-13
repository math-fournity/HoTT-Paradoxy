{-# OPTIONS --safe --without-K #-}
module Countercheck where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import ArithmeticTags using (Atom; avar; anum; codeAtom)
open import CodingRepair using (Σ'; _,_)

-- AUD-C168-ONE-20260913: a preimage of 1 under the exact C-167 coder.
-- This concerns codeAtom, not the separate double function in C-168's type.
one-has-codeAtom-preimage : codeAtom (anum zero) ≡ suc zero
one-has-codeAtom-preimage = refl

cong-suc2 : {m n : Nat} → m ≡ n → suc (suc m) ≡ suc (suc n)
cong-suc2 refl = refl

-- AUD-C168-SURJ-20260913: the exact atom coder is in fact surjective.
-- No claim about the later tree or formula coders is made.
codeAtom-surjective : (n : Nat) → Σ' Atom (λ a → codeAtom a ≡ n)
codeAtom-surjective zero = avar zero , refl
codeAtom-surjective (suc zero) = anum zero , refl
codeAtom-surjective (suc (suc n)) with codeAtom-surjective n
... | avar m , p = avar (suc m) , cong-suc2 p
... | anum m , p = anum (suc m) , cong-suc2 p
