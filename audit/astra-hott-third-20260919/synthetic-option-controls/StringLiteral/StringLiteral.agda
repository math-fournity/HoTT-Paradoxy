{-# OPTIONS --cubical #-}
module StringLiteral where
open import Agda.Builtin.String using (String)
text : String
text = "{-# OPTIONS --safe --cubical #-}"
postulate witness : Set
