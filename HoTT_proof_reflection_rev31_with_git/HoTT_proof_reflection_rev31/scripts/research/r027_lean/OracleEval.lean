/- Probe: expected refusal, not a predicted infinite loop. -/
axiom oracle_halt (p x : Nat) : Bool
noncomputable def chi (p x : Nat) : Bool := oracle_halt p x
#eval chi 0 0
