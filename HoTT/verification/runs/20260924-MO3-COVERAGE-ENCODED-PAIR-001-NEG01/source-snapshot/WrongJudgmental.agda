{-# OPTIONS --safe --without-K --exact-split #-}
module WrongJudgmental where
open import EncodedPair
open import Agda.Builtin.Bool using (Bool)
open import Agda.Builtin.Nat using (Nat; zero; suc)
open import Agda.Builtin.Equality using (_≡_; refl)

-- Expected type-check rejection: replace the supplied propositional beta
-- evidence with refl for exactly the same expression and hypotheses.
module Attempt
  (ext : {B : Bool → Set} {f g : (x : Bool) → B x}
       → ((x : Bool) → f x ≡ g x) → f ≡ g)
  (ext-id : {B : Bool → Set} (f : (x : Bool) → B x)
          → ext (λ x → refl {x = f x}) ≡ refl {x = f}) where
  open WithExt ext ext-id
  wrong : encoded-elim (λ _ → Nat) (λ a b → a) (pair zero (suc zero)) ≡ zero
  wrong = refl
