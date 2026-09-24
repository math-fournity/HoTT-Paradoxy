{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module WrongTouching where

open import Cubical.Data.Unit
open import IntervalCover

-- An incorrect input/control: touching open intervals do not carry the
-- strict overlap required by the certificate.
badCertificate : Cert touching pairIndices
badCertificate = decWitness (checkCert touching pairIndices) tt
