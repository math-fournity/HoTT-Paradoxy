{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST b2776ba84685650a08e7184b4bce5f8f2573f89691216d1583eb3163338b0ae3.

module Proof where

open import Cubical.Foundations.Prelude
import Target

proof : Target.NoJointPathAndApart
proof path apart = apart (path)
