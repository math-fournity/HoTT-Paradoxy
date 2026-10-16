{-# OPTIONS --safe --cubical #-}

-- GZ-011: a separate, minimal formula language whose codes and numeral
-- substitution are explicit.  It is intentionally smaller than a full
-- first-order language: no binders, axioms, or representation theorem occur.

module CCTTminiFormulaCode where

open import Agda.Builtin.Nat using (Nat; zero; suc)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Bool using (Bool; true; false)
open import CCTTminiNat using (parity; half; twice; parity-twice; parity-suc-twice; half-twice; half-suc-twice)

data Expr₁ : Set where
  lit  : Nat → Expr₁
  fvar : Nat → Expr₁

data Formula₁ : Set where
  prov₁ : Expr₁ → Formula₁
  bot₁  : Formula₁

codeExpr : Expr₁ → Nat
codeExpr (lit n) = twice n
codeExpr (fvar n) = suc (twice n)

decodeExpr : Nat → Expr₁
decodeExpr n with parity n
... | false = lit (half n)
... | true = fvar (half n)

decodeExprCode : (e : Expr₁) → decodeExpr (codeExpr e) ≡ e
decodeExprCode (lit n) rewrite parity-twice n | half-twice n = refl
decodeExprCode (fvar n) rewrite parity-suc-twice n | half-suc-twice n = refl

codeFormula : Formula₁ → Nat
codeFormula bot₁ = zero
codeFormula (prov₁ e) = suc (codeExpr e)

decodeFormula : Nat → Formula₁
decodeFormula zero = bot₁
decodeFormula (suc n) = prov₁ (decodeExpr n)

decodeFormulaCode : (φ : Formula₁) → decodeFormula (codeFormula φ) ≡ φ
decodeFormulaCode bot₁ = refl
decodeFormulaCode (prov₁ e) rewrite decodeExprCode e = refl

sym' : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym' refl = refl

trans' : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans' refl q = q

cong' : {A B : Set} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
cong' f refl = refl

formulaCodeInjective : (φ ψ : Formula₁) → codeFormula φ ≡ codeFormula ψ → φ ≡ ψ
formulaCodeInjective φ ψ p =
  trans' (sym' (decodeFormulaCode φ))
    (trans' (cong' decodeFormula p) (decodeFormulaCode ψ))

_==_ : Nat → Nat → Bool
zero == zero = true
zero == suc n = false
suc n == zero = false
suc n == suc m = n == m

==-refl : (n : Nat) → n == n ≡ true
==-refl zero = refl
==-refl (suc n) = ==-refl n

substExpr : Nat → Nat → Expr₁ → Expr₁
substExpr k x (lit n) = lit n
substExpr k x (fvar n) with x == n
... | true = lit k
... | false = fvar n

substFormula : Nat → Nat → Formula₁ → Formula₁
substFormula k x (prov₁ e) = prov₁ (substExpr k x e)
substFormula k x bot₁ = bot₁

quoteFormula : Formula₁ → Expr₁
quoteFormula φ = lit (codeFormula φ)

selfInstance : Formula₁ → Formula₁
selfInstance φ = substFormula (codeFormula φ) zero φ

template : Formula₁
template = prov₁ (fvar zero)

selfInstanceShape : selfInstance template ≡ prov₁ (lit (codeFormula template))
selfInstanceShape = refl

selfInstanceQuotesFormula : selfInstance template ≡ prov₁ (quoteFormula template)
selfInstanceQuotesFormula = selfInstanceShape
