{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST 2ae6a0d6679ca7071c580d6690536b693fca05f05ffa1199be1118a71e3d6243.

module Proof where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; not)
open import M3BreadthSupport
import Target

proof : Target.NoExactSelfCoding
proof {A = A} encode decode section = notNoFixed (encode self self) (cong (λ h → h self) (section liar))
  where
  liar : A → Bool
  liar x = not (encode x x)
  self : A
  self = decode liar
