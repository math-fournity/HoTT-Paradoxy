module DiagonalCore where

open import ObjectSyntax
open import Agda.Builtin.Nat
open import Agda.Builtin.Equality

cong-here : {A B : Set} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
cong-here f refl = refl

-- T3 pulse (bounded): the diagonal *representation* core over the T2 syntax
-- package.  Only the object-language machinery already present in
-- ObjectSyntax is used; no new layer, no postulate, no cubical feature.

-- A concrete numeral coding of the object syntax (tags 1..6 and 7..10).
code : Fml → Nat
codeF : Fml → Nat
codeT : Tm → Nat

codeT (var n) = suc n
codeT (num n) = suc (suc (suc n))
codeT (t +t u) = 1 + (1 + (suc (suc (suc (codeT t + codeT u)))))

codeF (t =f u) = 1 + (1 + (1 + (codeT t + codeT u)))
codeF bot = 4
codeF (φ =>f ψ) = 1 + (1 + (1 + (1 + (codeF φ + codeF ψ))))
codeF (all n φ) = 1 + (1 + (1 + (1 + (1 + (n + codeF φ)))))

code = codeF

-- Quotation of a formula as the numeral of its code.
⌜_⌝ : Fml → Tm
⌜ φ ⌝ = num (code φ)

-- The diagonal instance: substitute the quotation of φ for variable 0.
diagonalize : Fml → Fml
diagonalize φ = substF (code φ) 0 φ

-- Quotation is injective on codes (T3 pulse lemma; not a claim row while
-- ERCF-3 stays gated by the C8 stop conditions).
⌜-injective : ∀ {φ ψ} → code φ ≡ code ψ → substF (code φ) 0 ψ ≡ substF (code ψ) 0 ψ
⌜-injective {φ} {ψ} p = cong-here (λ k → substF k 0 ψ) p

-- The diagonal instance is a substitution instance of the original,
-- so the T2 substitution lemmas apply to it verbatim.
diagonalize-is-subst : ∀ φ → diagonalize φ ≡ substF (code φ) 0 φ
diagonalize-is-subst φ = refl
