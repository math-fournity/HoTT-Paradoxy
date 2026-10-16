axiom oracle_halt (p x : Nat) : Bool
noncomputable def chi (p x : Nat) : Bool := oracle_halt p x
