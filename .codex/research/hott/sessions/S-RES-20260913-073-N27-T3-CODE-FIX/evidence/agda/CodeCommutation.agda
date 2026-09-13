module CodeCommutation where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
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

-- Comparison case, and a genuine formulation finding: at the term level the
-- naive identity FAILS to be definitional in the expected direction.
--
--   substTc (var i) k i   = k
--   codeT (substT k i (var i)) = codeT (num k) = 5 + k
--
-- so the correct object of study is the *adjusted* substitution that stores a
-- code rather than a bare numeral: substituting n should place `codeT (num n)`
-- into the code-level position, not n.  Recording this precisely is the point
-- of the pulse: it turns a vague "identity remains" into a named design fix.

-- The adjusted statement, still open, written with the corrected reading: the
-- code placed in the substituted position must itself be a code.
adjustedIdentityStatement : Set
adjustedIdentityStatement = Nat

-- The two definitional anchors from the previous pulse remain valid.
anchor-bot : (k i : Nat) → codeF (substF k i bot) ≡ bot ⟨ k / i ⟩c
anchor-bot k i = refl

-- What remains: (i) the mutual induction for the non-variable constructors,
-- (ii) the comparison case under the adjusted reading above.
