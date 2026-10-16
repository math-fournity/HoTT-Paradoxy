{-# OPTIONS --safe --cubical --guardedness #-}
-- Negative control for C-363: a generic completion-gap bridge must fail at the
-- same concrete `nothing != just 1` boundary as C-360.
module WrongHoTTCompletionBridge where

open import Cubical.Foundations.Prelude

open import HoTTCompletionContract using (CompletionGap; hottCompletionGap)

wrongBridge : CompletionGap.RevisedDone hottCompletionGap → CompletionGap.OriginalDone hottCompletionGap
wrongBridge _ = 0 , 1 , refl
