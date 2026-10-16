{-# OPTIONS --safe --cubical #-}
module BadTickPathRefl where

open import Cubical.Foundations.Prelude

data ExtTick : Type₀ where
  forcing ordinary : ExtTick
  tirr : forcing ≡ ordinary

bad-judgemental-collapse : forcing ≡ ordinary
bad-judgemental-collapse = refl
