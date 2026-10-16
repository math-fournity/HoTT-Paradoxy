{-# OPTIONS --without-K --exact-split #-}
module hott-z.FiniteTrace where

-- Finite witnessed transitions; no assertion that arbitrary functions are steps.
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation.cartesian-product-types

data Trace {lS lE : Level} {S : UU lS} (Step : S → S → UU lE) :
  S → S → UU (lS ⊔ lE) where
  stop : {s : S} → Trace Step s s
  step : {s t u : S} → Step s t → Trace Step t u → Trace Step s u

appendTrace : {lS lE : Level} {S : UU lS} {Step : S → S → UU lE} {s t u : S} →
  Trace Step s t → Trace Step t u → Trace Step s u
appendTrace stop q = q
appendTrace (step e p) q = step e (appendTrace p q)

tracePreserves : {lS lE lP : Level} {S : UU lS} {Step : S → S → UU lE}
  (P : S → UU lP) → ((s t : S) → Step s t → P s → P t) →
  {s t : S} → Trace Step s t → P s → P t
tracePreserves P keep stop ps = ps
tracePreserves P keep (step {s} {t} e p) ps = tracePreserves P keep p (keep s t e ps)

FiniteSuccess : {lS lE lD : Level} {S : UU lS} →
  (S → S → UU lE) → S → (S → UU lD) → UU (lS ⊔ lE ⊔ lD)
FiniteSuccess {S = S} Step initial Done = Σ S (λ s → (Trace Step initial s) × Done s)
