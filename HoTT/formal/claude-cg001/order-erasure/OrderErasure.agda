{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The history index loses the order once patch laws are paths (Claude,
  session 91a6cdaa, 2026-09-25), in reply to Terra's audit 007 (section 4.2:
  "the count/log task can be handed to a trace/history layer").

  proof id : MP-CG001-ORDER-ERASURE-001
  claims   : CG001-C-48 (full statement in CLAIM.md)

  Source (paraphrased; locator in CLAIM.md): Angiuli, Morehouse, Licata,
  Harper, "Homotopical patch theory", J. Funct. Program. 26 (2016), sections
  7.1-7.2.  With patch contexts indexed by Boolean lists, the history records
  the exact order of the applied patches, so commuting patches cannot be
  equated; to state the commutation law as a path the authors quotient the
  lists by exchange of adjacent elements (multisets).  They remark that the
  elements still carry the order, while the paths identify logs that differ
  by a permutation.

  C-48 (a) on the exchange quotient MS of Boolean lists the number of entries
           is well defined and equals the list length;
       (b) the order is not: no function MS -> Maybe Bool agrees with "the
           first entry" on every list;
       (c) positive control: on lists (a log kept as data) the first entry is
           defined and separates true :: false :: [] from false :: true :: [].
           Negative control: defining the first entry directly on MS is
           rejected by the kernel.

  Bridge labels (history, log, patch, first) prove no fact about any
  version control system.
-}
module OrderErasure where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Bool using (Bool; true; false; true≢false)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Data.List using (List; []; _∷_; length)
open import Cubical.Relation.Nullary using (¬_)

-- the history index of section 7.1: Boolean lists up to exchange of neighbours
data MS : Type where
  []ms  : MS
  _∷ms_ : Bool → MS → MS
  ex    : (x y : Bool) (xs : MS) → x ∷ms (y ∷ms xs) ≡ y ∷ms (x ∷ms xs)

fromList : List Bool → MS
fromList []       = []ms
fromList (x ∷ xs) = x ∷ms fromList xs

------------------------------------------------------------------------
-- (a) the count survives the quotient

size : MS → ℕ
size []ms           = 0
size (x ∷ms xs)     = suc (size xs)
size (ex x y xs i)  = suc (suc (size xs))

sizeIsLength : (xs : List Bool) → size (fromList xs) ≡ length xs
sizeIsLength []       = refl
sizeIsLength (x ∷ xs) = cong suc (sizeIsLength xs)

------------------------------------------------------------------------
-- (b) the order does not

firstOf : List Bool → Maybe Bool
firstOf []      = nothing
firstOf (x ∷ _) = just x

fromJust : Bool → Maybe Bool → Bool
fromJust d nothing  = d
fromJust d (just x) = x

justInj : {x y : Bool} → just x ≡ just y → x ≡ y
justInj p = cong (fromJust true) p

orderErased : ¬ (Σ[ f ∈ (MS → Maybe Bool) ] ((xs : List Bool) → f (fromList xs) ≡ firstOf xs))
orderErased (f , agrees) =
  true≢false (justInj (sym (agrees (true ∷ false ∷ []))
                       ∙ cong f (ex true false []ms)
                       ∙ agrees (false ∷ true ∷ [])))

------------------------------------------------------------------------
-- (c) positive control: the log kept as data

dataLogKeepsOrder : ¬ (firstOf (true ∷ false ∷ []) ≡ firstOf (false ∷ true ∷ []))
dataLogKeepsOrder p = true≢false (justInj p)

logsIdentified : fromList (true ∷ false ∷ []) ≡ fromList (false ∷ true ∷ [])
logsIdentified = ex true false []ms
