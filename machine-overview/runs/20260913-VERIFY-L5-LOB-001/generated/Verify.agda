{-# OPTIONS --safe #-}

module Verify where

open import Target
open import Proof

check : NoLobSelfCertification
check = proof
