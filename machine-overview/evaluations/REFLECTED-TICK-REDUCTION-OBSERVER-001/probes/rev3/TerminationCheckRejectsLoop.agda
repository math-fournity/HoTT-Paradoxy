{-# OPTIONS --cubical --guarded #-}
module TerminationCheckRejectsLoop where

open import Agda.Builtin.Nat

loop : Nat
loop = loop

