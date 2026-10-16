axiom oracle_halt (p x : Nat) : Bool
axiom oracle_correct (p x : Nat) : oracle_halt p x = true ↔ H(p, x)
