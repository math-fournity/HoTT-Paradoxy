/- Probe: inspect a declared data axiom. No oracle correctness is asserted here. -/
axiom oracle_halt (p x : Nat) : Bool
noncomputable def chi (p x : Nat) : Bool := oracle_halt p x
#check chi
#print axioms chi
#reduce chi 0 0
