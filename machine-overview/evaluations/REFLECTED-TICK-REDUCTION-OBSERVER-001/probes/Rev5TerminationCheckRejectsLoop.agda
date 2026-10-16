{-# OPTIONS --cubical --guarded #-}
module Rev5TerminationCheckRejectsLoop where

open import Agda.Builtin.Nat

loop : Nat
loop = loop

