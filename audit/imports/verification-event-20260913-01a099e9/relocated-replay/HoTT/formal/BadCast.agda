{-# OPTIONS --safe --cubical #-}

module BadCast where

open import VerificationEvent

-- Intentionally invalid calibration: freeze the source at the initial
-- stage, then silently reinterpret it at afterP. The kernel must reject.
bad : Historical → Current afterP
bad q = q
