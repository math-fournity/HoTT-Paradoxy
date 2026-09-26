{-# OPTIONS --cubical --guardedness #-}
module StringPragmaControl where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty
open import Agda.Builtin.String

fakeOptions : String
fakeOptions = "{-# OPTIONS --safe --cubical #-}"

postulate deliberatelyUnsafe : ⊥
