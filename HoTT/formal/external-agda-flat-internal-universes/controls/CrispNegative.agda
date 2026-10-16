module CrispNegative where

-- Negative modal-typing control: the same crisp function must reject a local
-- argument.  The replay requires nonzero exit and the diagnostic
-- "Variable x is declared top, so it cannot be used here".
postulate
  A :{♭} Set
  B : Set
  f : (x :{♭} A) → B

wrong : (x : A) → B
wrong x = f x
