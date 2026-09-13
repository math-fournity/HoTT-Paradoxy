module RepairedSyntax where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import ObjectSyntax
open import DiagonalCore
open import CodingRepair
import StreamingParser as SP
import FormulaCoding as FC

-- T3 twenty-first pulse (bounded): substitution and quotation over the
-- *repaired* coding.
--
-- `StreamingParser` (C-176) and `FormulaCoding` (C-180) gave a decodable -- and
-- therefore injective -- Nat-valued coding of both `Tm` and `Fml`.  The old
-- coding needed a whole joint-recursion construction (`substFixT`/`substFixFd`,
-- C-157-C-159) to make code-level substitution agree with syntax-level
-- substitution.  With a decoder in hand the agreement becomes a corollary:
-- code-level substitution *is* decode, substitute, encode.
--
--   C-181  term layer: `(k n : Nat) (t : Tm) → substCodeT k n (codeT' t) ≡ codeT' (substT k n t)`;
--   C-182  formula layer: the same statement for `codeF'`/`substF`;
--   C-183  quotation and the diagonal instance: `⌜ φ ⌝' = num (codeF' φ)` is
--          injective, and `diagonalize' φ = substF (codeF' φ) 0 φ` is a
--          substitution instance of `φ` (the shape the diagonal lemma needs).
--
-- Honest boundary: `substCodeT`/`substCodeF` are defined *through the decoder*.
-- That makes the agreement exact, but it does **not** yet show that the object
-- theory can represent this substitution (that is the representability
-- obligation, which stays parked behind door B).  ERCF-3 remains `GATED`, no
-- earlier module is modified, and no historical pulse file is touched.

------------------------------------------------------------------------
-- C-181: code-level substitution of terms agrees with syntax-level
-- substitution on the image of the repaired coding.

substCodeT : Nat → Nat → Nat → Nat
substCodeT k n c = SP.codeT' (substT k n (SP.dec c))

substCodeT-agrees : (k n : Nat) (t : Tm) → substCodeT k n (SP.codeT' t) ≡ SP.codeT' (substT k n t)
substCodeT-agrees k n t rewrite SP.codeT'-roundtrip t = refl

------------------------------------------------------------------------
-- C-182: the same for formulas.

substCodeF : Nat → Nat → Nat → Nat
substCodeF k n c = FC.codeF' (substF k n (FC.decF c))

substCodeF-agrees : (k n : Nat) (φ : Fml) → substCodeF k n (FC.codeF' φ) ≡ FC.codeF' (substF k n φ)
substCodeF-agrees k n φ rewrite FC.codeF'-roundtrip φ = refl

------------------------------------------------------------------------
-- C-183: quotation and the diagonal instance over the repaired coding.

⌜_⌝' : Fml → Tm
⌜ φ ⌝' = num (FC.codeF' φ)

⌜-injective' : (φ ψ : Fml) → ⌜ φ ⌝' ≡ ⌜ ψ ⌝' → φ ≡ ψ
⌜-injective' φ ψ p = FC.codeF'-injective φ ψ (num-injective p)
  where
    num-injective : {m n : Nat} → num m ≡ num n → m ≡ n
    num-injective refl = refl

diagonalize' : Fml → Fml
diagonalize' φ = substF (FC.codeF' φ) 0 φ

diagonalize'-is-subst : (φ : Fml) → diagonalize' φ ≡ substF (FC.codeF' φ) 0 φ
diagonalize'-is-subst φ = refl

-- The diagonal instance is a substitution instance of the *same* formula, and
-- its code is therefore reachable by the code-level substitution of C-182:
diagonalize'-code : (φ : Fml) → FC.codeF' (diagonalize' φ) ≡ substCodeF (FC.codeF' φ) 0 (FC.codeF' φ)
diagonalize'-code φ = sym' (substCodeF-agrees (FC.codeF' φ) 0 φ)
