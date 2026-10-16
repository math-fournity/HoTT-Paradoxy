module CrispPositive where

-- Positive modal-typing control corresponding to LOPS 2018 §4: a function
-- that requires a crisp argument accepts a crisp variable.
postulate
  A :{♭} Set
  B : Set
  f : (x :{♭} A) → B

right : (x :{♭} A) → B
right x = f x
