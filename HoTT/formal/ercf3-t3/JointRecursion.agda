module JointRecursion where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import CodeStoreFix
open import MutualInduction2
open import DecisionParam

-- T3 fourteenth pulse (bounded): discharge the obligation recorded in N34
-- (`TermIdentityFinal`): the remaining step is a *joint recursion over the
-- shared decision*, not a local transport.  Fix (b) from N33 made the
-- code-level substitution take the decision as an explicit argument
-- (`substFixTd`); this module does the same on the *syntax* side and then
-- proves the two sides agree for every shared decision value.

-- Syntax-level substitution with the decision as an explicit argument.
-- `d = true` means "this occurrence is the one being replaced".
substTd : Bool → Nat → Nat → Tm → Tm
substTd d k i (var m) with d
... | true  = num k
... | false = var m
substTd d k i (num m) = num m
substTd d k i (t +t u) = substTd d k i t +t substTd d k i u

-- Joint recursion: for every shared decision the code-level corrected
-- substitution computes exactly the code of the syntax-level result.
-- No `with`-abstraction transport is needed: both sides split on the *same*
-- explicit value `d`, so the three non-recursive cases are definitional.
substFixTd-agrees :
  (d : Bool) (k i : Nat) (t : Tm)
  → substFixTd d k i t ≡ codeT (substTd d k i t)
substFixTd-agrees true  k i (var m) = refl
substFixTd-agrees false k i (var m) = refl
substFixTd-agrees d     k i (num m) = refl
substFixTd-agrees d     k i (t +t u) =
  cong₂ (λ x y → 1 + (1 + (suc (suc (suc (x + y))))))
        (substFixTd-agrees d k i t)
        (substFixTd-agrees d k i u)

-- Corollary: the shared-decision syntax substitution agrees with the original
-- (implicit-decision) syntax substitution whenever the decision is the actual
-- comparison result.  This is what connects the joint recursion back to the
-- functions used by the diagonal construction.
substTd-true : (k i m : Nat) → i =n m ≡ true → substTd true k i (var m) ≡ num k
substTd-true k i m _ = refl

substTd-false : (k i m : Nat) → i =n m ≡ false → substTd false k i (var m) ≡ var m
substTd-false k i m _ = refl

-- Term-level identity for the *original* substitution, obtained by running the
-- joint recursion at the decision value the original function uses.
termIdentityAtDecision :
  (k i : Nat) (t : Tm)
  → substFixTd (i =n i) k i t ≡ codeT (substTd (i =n i) k i t)
termIdentityAtDecision k i t = substFixTd-agrees (i =n i) k i t

-- Matching occurrence, in the original shape used by the diagonal lemma.
termIdentity-self :
  (k i : Nat) (t : Tm)
  → i =n i ≡ true
  → substFixTd true k i t ≡ codeT (substTd true k i t)
termIdentity-self k i t _ = substFixTd-agrees true k i t

------------------------------------------------------------------------
-- Direct per-occurrence identity for the ORIGINAL functions.
--
-- The shared-decision result above is stronger than it looks: because only the
-- `var` clause of `substFixT` splits on the decision, the direct identity can
-- be proved by induction on the term with a single `with` in the variable
-- case, and the recursive case is a plain congruence.

fixT-agrees :
  (k i : Nat) (t : Tm)
  → substFixT k i t ≡ codeT (substT k i t)
fixT-agrees k i (var m) with i =n m
... | true  = refl
... | false = refl
fixT-agrees k i (num m) = refl
fixT-agrees k i (t +t u) =
  cong₂ (λ x y → 1 + (1 + (suc (suc (suc (x + y))))))
        (fixT-agrees k i t)
        (fixT-agrees k i u)

------------------------------------------------------------------------
-- Corrected formula-level code substitution.
--
-- `CodeStoreFixF.substFixF` has an off-by-one-level error in the *shadowed*
-- (`all`, matching variable) branch: it stores `codeF (all m φ)` -- the code of
-- the whole quantified formula -- where the code of the untouched formula
-- `all m φ`, namely `5 + m + codeF φ`, is required.  The corrected function
-- below fixes exactly that branch; the non-matching branch was already right.

substFixFc : Nat → Nat → Fml → Nat
substFixFc k i (t =f u) = 1 + (1 + (1 + (substFixT k i t + substFixT k i u)))
substFixFc k i bot = 4
substFixFc k i (φ =>f ψ) = 1 + (1 + (1 + (1 + (substFixFc k i φ + substFixFc k i ψ))))
substFixFc k i (all m φ) with i =n m
... | true  = 1 + (1 + (1 + (1 + (1 + (m + codeF φ)))))
... | false = 1 + (1 + (1 + (1 + (1 + (m + (substFixFc k i φ))))))

fixF-agrees :
  (k i : Nat) (φ : Fml)
  → substFixFc k i φ ≡ codeF (substF k i φ)
fixF-agrees k i (t =f u) =
  cong₂ (λ x y → 1 + (1 + (1 + (x + y)))) (fixT-agrees k i t) (fixT-agrees k i u)
fixF-agrees k i bot = refl
fixF-agrees k i (φ =>f ψ) =
  cong₂ (λ x y → 1 + (1 + (1 + (1 + (x + y)))))
        (fixF-agrees k i φ) (fixF-agrees k i ψ)
fixF-agrees k i (all m φ) with i =n m
... | true  = refl
... | false = cong-here (λ z → 1 + (1 + (1 + (1 + (1 + (m + z))))))
                        (fixF-agrees k i φ)
