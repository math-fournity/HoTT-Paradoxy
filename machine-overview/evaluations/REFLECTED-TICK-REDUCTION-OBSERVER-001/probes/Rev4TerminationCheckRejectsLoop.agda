{-# OPTIONS --cubical --guarded #-}
module Rev4TerminationCheckRejectsLoop where

open import Agda.Builtin.Nat

loop : Nat
loop = loop

