{-# OPTIONS --safe --cubical --guardedness #-}
{-
  CG-001 / seed I1 "each level agrees, yet no verdict of sameness": positive controls.

  proof id : MP-CG001-LEVEL-COMPARISON-001
  claim    : CG001-C-09 (full statement in CLAIM.md)

  (i)  Shapes with finitely many levels.  For types of h-level n, a map that
       is a bijection on connected components and on every homotopy group is
       an equivalence.  This is the library's WhiteheadsLemma (HoTT Book
       Theorem 8.8.3), restated under this package's name.
  (ii) The cell-filling step for shapes built from finitely many cells.  Over
       the sphere S (-1+ n) (the boundary of an n-cell; S (-1+ 0) is empty),
       any family whose fibres are n-connected in the cubical indexing
       (isConnected n, i.e. Book (n-2)-connected) merely has a section.  Only
       finitely many levels of connectivity are used.

  Not checked here: Whitehead's principle for arbitrary types (the Book
  reports it is not provable, homotopy L2353), and the full statement for
  finite CW complexes (an AI derivation recorded in the CG-001 workbench).
-}
module LevelComparison where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.NatMinusOne using (-1+_)
open import Cubical.HITs.Susp using (Susp; north; south; merid)
open import Cubical.HITs.Sn.Base using (S)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetTruncation using () renaming (map to setMap)
open import Cubical.HITs.Truncation using (propTruncTrunc1Iso)
open import Cubical.Homotopy.Connected using (isConnected; isConnectedPathP; isConnectedSubtr')
open import Cubical.Homotopy.Group.Base using (πHom)
open import Cubical.Homotopy.WhiteheadsLemma using (WhiteheadsLemma)

-- C-09 (i): level-by-level agreement decides sameness for finite-level shapes
finiteLevelComparison : ∀ {ℓ} {A B : Type ℓ} {n : ℕ}
  → isOfHLevel n A → isOfHLevel n B
  → (f : A → B)
  → isEquiv (setMap f)
  → ((a : A) (k : ℕ) → isEquiv (fst (πHom {A = (A , a)} {B = (B , f a)} k (f , refl))))
  → isEquiv f
finiteLevelComparison hA hB f h0 hk = WhiteheadsLemma hA hB f h0 hk

-- C-09 (ii): a family over the boundary sphere of an n-cell, n-connected in
-- the cubical indexing, merely has a section
sphereSection : ∀ {ℓ} (n : ℕ) (P : S (-1+ n) → Type ℓ)
  → ((x : S (-1+ n)) → isConnected n (P x))
  → ∥ ((x : S (-1+ n)) → P x) ∥₁
sphereSection zero P _ = ∣ (λ ()) ∣₁
sphereSection {ℓ} (suc n) P conn =
  PT.rec2 squash₁
    (λ pN pS → PT.map (assemble pN pS) (sphereSection n (Q pN pS) (connQ pN pS)))
    (inhabited north) (inhabited south)
  where
  inhabited : (y : Susp (S (-1+ n))) → ∥ P y ∥₁
  inhabited y = Iso.inv propTruncTrunc1Iso (isConnectedSubtr' n 1 (conn y) .fst)

  Q : P north → P south → S (-1+ n) → Type ℓ
  Q pN pS x = PathP (λ i → P (merid x i)) pN pS

  connQ : (pN : P north) (pS : P south) (x : S (-1+ n)) → isConnected n (Q pN pS x)
  connQ pN pS x = isConnectedPathP n (conn south) pN pS

  assemble : (pN : P north) (pS : P south) → ((x : S (-1+ n)) → Q pN pS x)
    → (y : Susp (S (-1+ n))) → P y
  assemble pN pS q north = pN
  assemble pN pS q south = pS
  assemble pN pS q (merid x i) = q x i
