/- Positive controls are actual executable definitions, not fake halting oracles. -/
axiom unused_oracle (p x : Nat) : Bool
def safe (_p _x : Nat) : Bool := false
#reduce safe 0 0
#eval safe 0 0
#print axioms safe
