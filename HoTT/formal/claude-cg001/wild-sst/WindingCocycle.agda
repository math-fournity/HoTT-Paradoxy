{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Is the hexagon Coh₂ of CG001-C-64 the right condition?  A positive control
  (Claude, session 7f138325, 2026-09-26; goal CG-003, gate G2).

  proof id : MP-CG001-WINDING-COCYCLE-001
  claim    : CG001-C-69 (full statement in CLAIM-C69.md)

  Terra's question T-039 asks whether the two routes of Coh₂ really describe
  the hexagon of the semi-simplicial identities.  One way a wrong formula
  would show itself: it would reject structures that are coherent, or accept
  ones that are not.  Here the definition of CG001-C-64 is used unchanged.

  windingSST w has X n = S¹, every face map the identity, and the identity
  sid n i j at a point x the loop at x of winding number w n i j (the
  library's basechange2 x (intLoop z); at base it is intLoop z).

  (a) Coh₂ (windingSST w) holds exactly when w satisfies the equation
        w(m+1, j+1, k+1) + (w(m, i, k) + w(m+1, i, j))
          = w(m, i, j) + (w(m+1, i, k+1) + w(m, j, k))
      for all i ≤ j ≤ k, i.e. when the winding numbers met along the two
      routes add up to the same total (cocycle).  Both directions are proved.
  (b) spinW (winding 1 at level 0, indices 0 0, and 0 elsewhere, the winding
      pattern of spin in CG001-C-64) violates the equation, so Coh₂ fails;
      uniformW (winding 1 everywhere) satisfies it, so Coh₂ holds although
      every identity is a non-trivial loop; levelW (winding n at level n)
      violates it.

  So the formula accepts non-trivial coherent data and rejects exactly the
  data whose routes wind differently.
-}
module WindingCocycle where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc)
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Nat.Properties using (znots ; snotz ; injSuc)
open import Cubical.Data.Int using (ℤ ; pos ; negsuc ; _+_)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Sum using (inl ; inr)
open import Cubical.Data.Unit using (tt)
open import Cubical.HITs.S1.Base
  using (S¹ ; base ; winding ; intLoop ; windingℤLoop ; winding-hom ; intLoop-hom
       ; basechange2 ; isSetΩx ; toPropElim)
open import Cubical.Relation.Nullary using (¬_)

open import WildSST

------------------------------------------------------------------------
-- The loop of winding number z at every point of the circle.

rot : ℤ → (x : S¹) → x ≡ x
rot z x = basechange2 x (intLoop z)

Windings : Type
Windings = (n : ℕ) → Fin (suc (suc n)) → Fin (suc (suc n)) → ℤ

windingSST : Windings → WildSST
WildSST.X (windingSST w) _ = S¹
WildSST.d (windingSST w) _ _ x = x
WildSST.sid (windingSST w) n i j _ x = rot (w n i j) x

cocycle : Windings → Type
cocycle w = (m : ℕ) (i j k : Fin (suc (suc m))) (p : i ≤F j) (q : j ≤F k)
  → w (suc m) (fsuc j) (fsuc k) + (w m i k + w (suc m) (weaken i) (weaken j))
    ≡ w m i j + (w (suc m) (weaken i) (fsuc k) + w m j k)

open Routes

------------------------------------------------------------------------
-- (a) Coh₂ is exactly the cocycle equation.

winding₃ : (a b c : ℤ) → winding (intLoop a ∙ intLoop b ∙ intLoop c) ≡ a + (b + c)
winding₃ a b c =
    winding-hom (intLoop a) (intLoop b ∙ intLoop c)
  ∙ cong₂ _+_ (windingℤLoop a) (winding-hom (intLoop b) (intLoop c)
                                ∙ cong₂ _+_ (windingℤLoop b) (windingℤLoop c))

intLoop₃ : (a b c : ℤ) → intLoop a ∙ intLoop b ∙ intLoop c ≡ intLoop (a + (b + c))
intLoop₃ a b c = cong (intLoop a ∙_) (intLoop-hom b c) ∙ intLoop-hom a (b + c)

-- the winding numbers met along routeA and routeB
module _ (w : Windings) (m : ℕ) (i j k : Fin (suc (suc m))) where
  a₁ b₁ c₁ a₂ b₂ c₂ : ℤ
  a₁ = w (suc m) (fsuc j) (fsuc k)
  b₁ = w m i k
  c₁ = w (suc m) (weaken i) (weaken j)
  a₂ = w m i j
  b₂ = w (suc m) (weaken i) (fsuc k)
  c₂ = w m j k

coh₂→cocycle : (w : Windings) → Coh₂ (windingSST w) → cocycle w
coh₂→cocycle w h m i j k p q =
    sym (winding₃ (a₁ w m i j k) (b₁ w m i j k) (c₁ w m i j k))
  ∙ cong winding (h m i j k p q base)
  ∙ winding₃ (a₂ w m i j k) (b₂ w m i j k) (c₂ w m i j k)

cocycle→coh₂ : (w : Windings) → cocycle w → Coh₂ (windingSST w)
cocycle→coh₂ w c m i j k p q =
  toPropElim (λ x → isSetΩx x _ _)
    ( intLoop₃ (a₁ w m i j k) (b₁ w m i j k) (c₁ w m i j k)
    ∙ cong intLoop (c m i j k p q)
    ∙ sym (intLoop₃ (a₂ w m i j k) (b₂ w m i j k) (c₂ w m i j k)))

------------------------------------------------------------------------
-- (b) Three winding patterns.

spinW : Windings
spinW zero (inl _) (inl _) = pos 1
spinW _ _ _ = pos 0

uniformW : Windings
uniformW _ _ _ = pos 1

levelW : Windings
levelW n _ _ = pos n

spinW-not-cocycle : ¬ cocycle spinW
spinW-not-cocycle c = znots (injSuc (injPos (c zero fzero fzero fzero tt tt)))

spinWIncoherent : ¬ Coh₂ (windingSST spinW)
spinWIncoherent h = spinW-not-cocycle (coh₂→cocycle spinW h)

uniformWCoherent : Coh₂ (windingSST uniformW)
uniformWCoherent = cocycle→coh₂ uniformW (λ _ _ _ _ _ _ → refl)

levelW-not-cocycle : ¬ cocycle levelW
levelW-not-cocycle c = snotz (injSuc (injPos (c zero fzero fzero fzero tt tt)))

levelWIncoherent : ¬ Coh₂ (windingSST levelW)
levelWIncoherent h = levelW-not-cocycle (coh₂→cocycle levelW h)
