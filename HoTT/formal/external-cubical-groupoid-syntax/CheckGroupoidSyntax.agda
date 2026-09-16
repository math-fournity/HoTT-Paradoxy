{-# OPTIONS --safe --cubical --guardedness #-}

module CheckGroupoidSyntax where

open import Cubical.Foundations.Prelude hiding (Sub)
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Isomorphism

module _ (X : hSet ℓ-zero) (Y : X .fst → hSet ℓ-zero) where
  import TT.Groupoid.Syntax X Y as G
  import TT.Groupoid.NTy X Y as N
  import TT.Groupoid.IsoSet X Y as I
  import TT.Groupoid.ToSet X Y as GS

  module S where
    open import TT.Set.Syntax X Y public
    open import TT.Set.ConPath X Y public

  groupoid-types-are-sets : (Γ : G.Con) → isSet (G.Ty Γ)
  groupoid-types-are-sets = N.isSetTy

  groupoid-contexts-match-set-syntax : Iso G.Con S.Con
  groupoid-contexts-match-set-syntax = I.isoCon

  groupoid-substitutions-match-set-syntax :
    {Δ Γ : G.Con} → Iso (G.Sub Δ Γ) (S.Sub GS.⟦ Δ ⟧ GS.⟦ Γ ⟧)
  groupoid-substitutions-match-set-syntax = I.isoSub

  groupoid-types-match-set-syntax :
    {Γ : G.Con} → Iso (G.Ty Γ) (S.Ty GS.⟦ Γ ⟧)
  groupoid-types-match-set-syntax = I.isoTy

  groupoid-terms-match-set-syntax :
    {Γ : G.Con} {A : G.Ty Γ} → Iso (G.Tm Γ A) (S.Tm GS.⟦ Γ ⟧ GS.⟦ A ⟧)
  groupoid-terms-match-set-syntax = I.isoTm
