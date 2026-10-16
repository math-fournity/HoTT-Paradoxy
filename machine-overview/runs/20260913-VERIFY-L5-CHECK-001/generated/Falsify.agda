{-# OPTIONS --safe #-}

module Falsify where

import ObjectSyntax as OS
import L5ConsumerSupport as L5

-- Negative control: a K derivation is not a derivation of bottom.
bad : OS.⊢ OS.bot
bad = L5.givenK
