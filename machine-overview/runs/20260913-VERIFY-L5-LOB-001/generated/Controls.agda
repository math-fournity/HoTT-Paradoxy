{-# OPTIONS --safe #-}

module Controls where

open import Agda.Builtin.Bool using (false; true)
open import Agda.Builtin.Equality using (_≡_)
open import Agda.Builtin.Nat using (zero; suc)
import ObjectSyntax as OS
import L5ConsumerSupport as L5

check-given : OS.⊢ L5.kFormula
check-given = L5.checkGivenProof L5.givenK

check-zero-fuel : L5.searchK zero ≡ false
check-zero-fuel = L5.searchAtZero

check-one-fuel : L5.searchK (suc zero) ≡ true
check-one-fuel = L5.searchAtOne

check-finite-true : L5.evalB L5.truthFormula ≡ true
check-finite-true = L5.truthDecision

check-finite-false : L5.evalB L5.falseFormula ≡ false
check-finite-false = L5.falseDecision
