module CodeCommutation where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma

-- T3 fifth pulse (bounded): the *code-level arithmetic identity* that the
-- reflection obligation needs.
--
--   codeF (substF k i φ) ≡ _⟨_/_⟩c φ k i
--
-- The general mutual induction is the remaining obligation; this pulse
-- machine-checks the definitional core on the constructors that do not
-- depend on the variable-comparison (bottom) and on an equality constructor
-- with concrete numerals, so the identity is verified where it is
-- definitional and its residual content is narrowed to the comparison cases.

comm-bot : (k i : Nat) → codeF (substF k i bot) ≡ bot ⟨ k / i ⟩c
comm-bot k i = refl

comm-eq : (k i : Nat)
  → codeF (substF k i (num k =f num i)) ≡ (num k =f num i) ⟨ k / i ⟩c
comm-eq k i = refl

-- The comparison-dependent cases reduce to the arithmetic fact that both
-- sides consult the same decision `i =n m`; the general mutual induction
-- over `substT`/`substF` vs `substTc`/`_⟨_/_⟩c` is the remaining obligation
-- of this pulse and is deliberately NOT postulated.

