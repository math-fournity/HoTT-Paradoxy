{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Data.Empty.Base using (⊥)
import TransitionLift as TL

check-local-limit : TL.LimTruncA
check-local-limit = TL.C-115-limTrunc

check-exact-empty : TL.LimA → ⊥
check-exact-empty = TL.C-114-LimA-empty
