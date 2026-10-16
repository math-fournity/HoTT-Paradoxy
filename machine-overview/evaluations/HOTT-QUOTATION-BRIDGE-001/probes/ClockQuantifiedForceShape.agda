{-# OPTIONS --safe #-}

-- A pure type-shape control for CCTT's clock-quantified force.  The evaluator
-- does not pretend this abstract module implements CCTT; it checks the
-- quantifier dependency that the fixed primary source declares.

module ClockQuantifiedForceShape where

module Bridge (Cl : Set) (Later : Cl → Set → Set) where
  GlobalLater : (Cl → Set) → Set
  GlobalLater A = (k : Cl) → Later k (A k)

  ForceGlobal : Set₁
  ForceGlobal = {A : Cl → Set} → GlobalLater A → (k : Cl) → A k

  useGlobal : ForceGlobal → {A : Cl → Set} → GlobalLater A → (k : Cl) → A k
  useGlobal force delayed k = force delayed k

  -- A fixed-clock delayed value can be promoted only when a caller supplies
  -- explicit reindexing data for every clock.
  useLocalWithReindex : ForceGlobal → {A : Cl → Set} → (k : Cl)
                      → ((k' : Cl) → Later k (A k) → Later k' (A k'))
                      → Later k (A k) → A k
  useLocalWithReindex force k reindex delayed =
    force (λ k' → reindex k' delayed) k

