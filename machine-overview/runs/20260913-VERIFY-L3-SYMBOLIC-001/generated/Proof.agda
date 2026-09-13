{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST e538925469002b158d745a35162bfd75827055fc4f3a5bb9991b25ddcb3813eb.

module Proof where

open import Cubical.Foundations.Prelude
import Target

proof : Target.NoSeparatedObservable
proof f apart = apart ((λ i → f i))
