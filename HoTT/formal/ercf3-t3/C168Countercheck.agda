module C168Countercheck where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import ArithmeticTags using (Atom; avar; anum; codeAtom)
open import CodingRepair using (Σ'; _,_)

-- T3 audit pulse (bounded): the countercheck for the C-168 *narrative* error.
--
-- An independent audit (2026-09-13) found that the C-168 row in
-- `HoTT/CLAIM_EVIDENCE_MATRIX.md` and the package narrative stated
-- "the coder is not surjective (`1` has no preimage), so any total decoder
-- needs a default branch" about `codeAtom`.  The machine-checked lemma
-- `ArithmeticTags.one-has-no-preimage`, however, is about the *function*
-- `double` (`¬ Σ m, double m ≡ 1`), not about `codeAtom`; and the fragment
-- coder `codeAtom` is in fact **surjective**.
--
-- This module re-proves the two audit propositions inside this repo, with the
-- complete transitive import closure pinned in the run's source manifest:
--
--   C-184  `codeAtom (anum zero) ≡ suc zero`   -- 1 has an explicit preimage;
--   C-185  `(n : Nat) → Σ' Atom (λ a → codeAtom a ≡ n)` -- the atom coder is
--          surjective.
--
-- Scope: these two propositions are about `ArithmeticTags.codeAtom` only.
-- They do **not** touch `double`'s no-preimage lemma, the later tree/formula
-- coders `codeT'`/`codeF'` (whose image really does miss `1`, because their bit
-- lists are non-empty), or any HoTT-specific statement.

-- C-184: the exact atom coder has a preimage of 1.
one-has-codeAtom-preimage : codeAtom (anum zero) ≡ suc zero
one-has-codeAtom-preimage = refl

cong-suc2 : {m n : Nat} → m ≡ n → suc (suc m) ≡ suc (suc n)
cong-suc2 refl = refl

-- C-185: the atom coder is surjective (by parity classes: the induction step
-- adds two, which preserves the class, so the two base cases cover both).
codeAtom-surjective : (n : Nat) → Σ' Atom (λ a → codeAtom a ≡ n)
codeAtom-surjective zero = avar zero , refl
codeAtom-surjective (suc zero) = anum zero , refl
codeAtom-surjective (suc (suc n)) with codeAtom-surjective n
... | avar m , p = avar (suc m) , cong-suc2 p
... | anum m , p = anum (suc m) , cong-suc2 p
