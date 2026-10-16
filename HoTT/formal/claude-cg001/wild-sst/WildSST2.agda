{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The second rung (Claude, session 7f138325, 2026-09-26; goal CG-002, gate G3).

  proof id : MP-CG001-WILD-SST2-001
  claim    : CG001-C-66 (full statement in CLAIM-C66.md)

  WildSST (CG001-C-64) lacks the hexagon.  Add it as data: WildSST₂ is a
  WildSST together with a filler for every hexagon.  This file shows that the
  fillers are genuinely new data, and that the next condition up is not
  automatic either.

  flat is the degenerate WildSST whose simplices of dimension 0 are points of
  the 2-sphere and whose higher simplices are points of Unit, with every face
  identity refl.  Each level-0 hexagon then has the same composite path r on
  both sides, so a filler is any element of r ≡ r.

  (a) The Hopf family over S² (the same Glue definition as S¹Hopf.HopfS² in
      the cubical library) detects surf: carrying base along it gives a loop
      of winding number -1, computed by refl.  So surf is not refl, and the
      conjugate σr of surf is a filler of r ≡ r different from refl.
  (b) Two WildSST₂ structures on flat: all fillers refl, or the level-0
      filler at (0,0,0) equal to σr.  They are different (twoFillings); with
      uniqueness of identity proofs they could not be.
  (c) Deg₃ is the condition that the four level-0 fillers around every
      quadruple i ≤ j ≤ k ≤ l in Fin 2 compose to the same element in two
      ways, h(jkl) ∙ h(ijl) ≡ h(ikl) ∙ h(ijk).  CLAIM-C66.md derives, by hand
      and with a script over the permutohedron P₄, that this is what the
      second coherence (P₄) of the face identities reduces to on flat; that
      derivation is not machine-checked.  Here: the all-refl structure
      satisfies Deg₃, the σr structure violates it at (0,0,0,1).
-}
module WildSST2 where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Foundations.GroupoidLaws using (lUnit ; rUnit ; lCancel ; assoc)
open import Cubical.Core.Glue using (Glue)
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Unit using (Unit ; tt)
open import Cubical.Data.Sum using (inl ; inr)
open import Cubical.Data.Int using (pos ; negsuc)
open import Cubical.Data.Int.Properties using (negsucNotpos)
open import Cubical.HITs.S1.Base using (S¹ ; base ; loop ; winding ; rotIsEquiv)
open import Cubical.HITs.S2.Base using (S² ; surf) renaming (base to north)
open import Cubical.Relation.Nullary using (¬_)

open import WildSST

------------------------------------------------------------------------
-- (a) The Hopf family detects surf.

Hopf : S² → Type
Hopf north = S¹
Hopf (surf i j) = Glue S¹ (λ { (i = i0) → _ , idEquiv S¹
                             ; (i = i1) → _ , idEquiv S¹
                             ; (j = i0) → _ , idEquiv S¹
                             ; (j = i1) → _ , _ , rotIsEquiv (loop i) } )

carry : {p q : north ≡ north} → p ≡ q → subst Hopf p base ≡ subst Hopf q base
carry β = cong (λ r → subst Hopf r base) β

surfWinds : winding (carry surf) ≡ negsuc 0
surfWinds = refl

surf≢refl : ¬ (surf ≡ refl)
surf≢refl e = negsucNotpos 0 0 (sym surfWinds ∙ cong (λ β → winding (carry β)) e)

------------------------------------------------------------------------
-- The degenerate WildSST.

flat : WildSST
WildSST.X flat zero = S²
WildSST.X flat (suc n) = Unit
WildSST.d flat zero _ _ = north
WildSST.d flat (suc n) _ _ = tt
WildSST.sid flat zero _ _ _ _ = refl
WildSST.sid flat (suc n) _ _ _ _ = refl

r : north ≡ north
r = refl ∙ refl ∙ refl

ρ : r ≡ refl
ρ = sym (lUnit (refl ∙ refl)) ∙ sym (lUnit refl)

σr : r ≡ r
σr = ρ ∙ surf ∙ sym ρ

σr≢refl : ¬ (σr ≡ refl)
σr≢refl e = surf≢refl (surf≡ρσρ ∙ cong (λ β → sym ρ ∙ β ∙ ρ) e ∙ cancel)
  where
  surf≡ρσρ : surf ≡ sym ρ ∙ σr ∙ ρ
  surf≡ρσρ =
    surf                              ≡⟨ lUnit surf ⟩
    refl ∙ surf                       ≡⟨ cong (_∙ surf) (sym (lCancel ρ)) ⟩
    (sym ρ ∙ ρ) ∙ surf                ≡⟨ sym (assoc (sym ρ) ρ surf) ⟩
    sym ρ ∙ ρ ∙ surf                  ≡⟨ cong (λ β → sym ρ ∙ ρ ∙ β) (rUnit surf) ⟩
    sym ρ ∙ ρ ∙ surf ∙ refl           ≡⟨ cong (λ β → sym ρ ∙ ρ ∙ surf ∙ β) (sym (lCancel ρ)) ⟩
    sym ρ ∙ ρ ∙ surf ∙ sym ρ ∙ ρ      ≡⟨ cong (λ β → sym ρ ∙ ρ ∙ β) (assoc surf (sym ρ) ρ) ⟩
    sym ρ ∙ ρ ∙ (surf ∙ sym ρ) ∙ ρ    ≡⟨ cong (sym ρ ∙_) (assoc ρ (surf ∙ sym ρ) ρ) ⟩
    sym ρ ∙ (ρ ∙ surf ∙ sym ρ) ∙ ρ    ∎
  cancel : sym ρ ∙ refl ∙ ρ ≡ refl
  cancel = cong (sym ρ ∙_) (sym (lUnit ρ)) ∙ lCancel ρ

------------------------------------------------------------------------
-- (b) Adding the hexagon as data: the data is not unique.

record WildSST₂ : Type₁ where
  field
    underlying : WildSST
    hexagon    : Coh₂ underlying

cohTrivial : Coh₂ flat
cohTrivial zero i j k p q x = refl
cohTrivial (suc m) i j k p q x = refl

cohSurf : Coh₂ flat
cohSurf zero (inl _) (inl _) (inl _) p q x = σr
cohSurf zero i j k p q x = refl
cohSurf (suc m) i j k p q x = refl

flatTrivial flatSurf : WildSST₂
flatTrivial = record { underlying = flat ; hexagon = cohTrivial }
flatSurf    = record { underlying = flat ; hexagon = cohSurf }

twoFillings : ¬ (cohTrivial ≡ cohSurf)
twoFillings e = σr≢refl (sym (cong (λ C → C zero fzero fzero fzero tt tt tt) e))

------------------------------------------------------------------------
-- (c) The next condition up, in the form it takes on flat (CLAIM-C66.md).

Deg₃ : Coh₂ flat → Type
Deg₃ C = (i j k l : Fin 2) (pij : i ≤F j) (pjk : j ≤F k) (pkl : k ≤F l)
  → C zero j k l pjk pkl tt ∙ C zero i j l pij (≤F-trans j k l pjk pkl) tt
    ≡ C zero i k l (≤F-trans i j k pij pjk) pkl tt ∙ C zero i j k pij pjk tt

trivialSatisfies : Deg₃ cohTrivial
trivialSatisfies i j k l pij pjk pkl = refl

surfViolates : ¬ Deg₃ cohSurf
surfViolates h = σr≢refl (lUnit σr ∙ sym at0001 ∙ sym (lUnit refl))
  where
  at0001 : refl ∙ refl ≡ refl ∙ σr
  at0001 = h fzero fzero fzero (fsuc fzero) tt tt tt
