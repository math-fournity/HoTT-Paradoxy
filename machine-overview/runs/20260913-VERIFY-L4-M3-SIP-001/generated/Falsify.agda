{-# OPTIONS --safe --cubical --guardedness #-}

module Falsify where

open import Cubical.Foundations.Prelude
import SIPRepresentation as SIP

-- Negative control: the coarse identification cannot identify the refined structures.
bad-refined-identification : SIP.s' ≡ SIP.t'
bad-refined-identification = SIP.C-124-identification
