module DecodingFence where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma

-- Local negative (builtins only; no stdlib `¬`).
data Empty : Set where

Not : Set → Set
Not A = A → Empty

-- T3 fifteenth pulse (bounded): the *decodability/injectivity fence*.
--
-- `ObjectSyntax.agda` states that "Goedel coding with decodability/injectivity"
-- is a T3 obligation deliberately not formalised there, and `DiagonalCore`'s
-- `⌜-injective` is a congruence lemma (it transports a substitution along a
-- code equality) rather than an injectivity statement.  This module checks the
-- fence: the concrete `codeT`/`codeF` of `DiagonalCore` are **not** injective,
-- so this coding cannot be decoded, and the decodability obligation therefore
-- requires a repaired coding (tag-disjoint or list/pair based) before any
-- proof-predicate representability can be stated over it.

-- C-160: the collision.  `var 2` and `num 0` share one code.
var2-num0-collide : codeT (var 2) ≡ codeT (num 0)
var2-num0-collide = refl

-- `var` and `num` are different constructors, so the two colliding terms are
-- distinct.
var≢num : (n m : Nat) → Not (var n ≡ num m)
var≢num n m ()

-- C-160 (statement): no function can be an injective decoder of `codeT`.
no-injective-codeT :
  Not ((t u : Tm) → codeT t ≡ codeT u → t ≡ u)
no-injective-codeT decode = var≢num 2 0 (decode (var 2) (num 0) refl)

-- C-161: the collision lifts to the formula level, so `codeF` is not
-- injective either.
varEq≢numEq : (n m : Nat) → Not ((var n =f var n) ≡ (num m =f num m))
varEq≢numEq n m ()

eqVar2-collides-eqNum0 :
  codeF (var 2 =f var 2) ≡ codeF (num 0 =f num 0)
eqVar2-collides-eqNum0 = refl

no-injective-codeF :
  Not ((φ ψ : Fml) → codeF φ ≡ codeF ψ → φ ≡ ψ)
no-injective-codeF decode =
  varEq≢numEq 2 0 (decode (var 2 =f var 2) (num 0 =f num 0) refl)

-- Positive control: the collision is not vacuous — on the numeral fragment the
-- coding *is* injective (the numeral case of `codeT` is `suc ∘ suc ∘ suc`).
num-code-injective : (n m : Nat) → codeT (num n) ≡ codeT (num m) → n ≡ m
num-code-injective n m refl = refl

-- Repair requirement (recorded, not proved here): an injective/decodable
-- coding needs tag-disjoint value ranges (e.g. `var n ↦ 3 * n`,
-- `num n ↦ 3 * n + 1`, `_+t_ ↦ 3 * ⟨pair⟩ + 2` for a pairing function
-- `⟨_,_⟩`, or a list-based encoding).  Any such repair changes the concrete
-- codes and therefore the diagonal instance; it is the next bounded pulse.
repairRequirement : Set
repairRequirement = Nat
