{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import SIPRepresentation as SIP

check-identification : SIP.s ≡ SIP.t
check-identification = SIP.C-124-identification

check-outside-observation : SIP.observable-s ≡ SIP.observable-t → ⊥
check-outside-observation = SIP.C-125-obs-differs

check-refined-separation : SIP.s' ≡ SIP.t' → ⊥
check-refined-separation = SIP.C-128-no-identification
