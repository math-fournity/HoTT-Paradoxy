{-# OPTIONS --safe --cubical #-}

-- GZ-010: distinguish formula syntax from the meta-level certificate checker.

module CCTTminiFormula where

open import Agda.Builtin.Nat using (Nat; zero)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Bool using (Bool; true)
open import Agda.Builtin.List using ([])
open import CCTTmini
open import CCTTminiNat

infixr 4 _⇒F_

data Formula : Set where
  provF  : Nat → Formula
  atomF  : Nat → Formula
  botF   : Formula
  _⇒F_   : Formula → Formula → Formula

-- This is deliberately a meta-level predicate.  It runs the certified
-- fragment's total decoder/checker; it is not an object-arithmetic formula.
validCode : Nat → Bool
validCode n = accepts [] (decode n)

data ProvWitness : Nat → Set where
  certWitness : {n : Nat} (c : RawCert)
    → code c ≡ n
    → Checked [] c
    → ProvWitness n

quoteCert : RawCert → Formula
quoteCert c = provF (code c)

-- A partial satisfaction relation for the one formula constructor whose
-- intended meta-level meaning is fixed in this unit.  No semantics is claimed
-- for atomF, botF or implication yet.
data ProvHolds : Formula → Set where
  holdsProv : {n : Nat} → ProvWitness n → ProvHolds (provF n)

closedC : RawCert
closedC = reflC zeroC

closedChecked : Checked [] closedC
closedChecked = checked (pathTy natTy zeroT zeroT) (drefl dzero)

closedAccepted : validCode (code closedC) ≡ true
closedAccepted = refl

closedProvWitness : ProvWitness (code closedC)
closedProvWitness = certWitness closedC refl closedChecked

quoteClosed : quoteCert closedC ≡ provF (code closedC)
quoteClosed = refl

quoteClosedHolds : ProvHolds (quoteCert closedC)
quoteClosedHolds = holdsProv closedProvWitness
