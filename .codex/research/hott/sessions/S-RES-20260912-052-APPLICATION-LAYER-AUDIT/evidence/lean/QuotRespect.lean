-- N10 probe A8: the type-level fence.  The relation identifies true and
-- false, so a representative-dependent eliminator does not respect it and
-- must be rejected during elaboration.

def rel (_a _b : Bool) : Prop := True

def Q := Quot rel

-- Expected: elaboration error, because (fun b => b) does not respect rel.
def bad : Q → Bool :=
  Quot.lift (fun b => b) (by intro a b h; rfl)
