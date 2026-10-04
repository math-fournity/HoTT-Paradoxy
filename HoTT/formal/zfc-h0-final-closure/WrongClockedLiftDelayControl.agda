{-# OPTIONS --cubical --guarded #-}
{- Expected-rejection control for the clocked Lift operational candidate. -}
module WrongClockedLiftDelayControl where

open import ClockedLiftDelayControl

wrong-never-answers : runFor (suc zero) never ≡ just zero
wrong-never-answers = refl
