-- N10 probe A5 (positive): Lean 4.33.1 core quotients as a delivery backend.
-- A quotient eliminator that respects the relation is computable in #eval.

def rel (_a _b : Bool) : Prop := True

def Q := Quot rel

def g : Q → Bool :=
  Quot.lift (fun _ => true) (by intro a b h; rfl)

#eval g (Quot.mk rel true)
#eval g (Quot.mk rel false)
