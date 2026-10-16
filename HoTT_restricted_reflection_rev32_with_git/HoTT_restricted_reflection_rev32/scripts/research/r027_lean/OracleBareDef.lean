/- Probe: ordinary Lean compilation, not a model of HoTT or a genuine halting oracle.
   Expect a code-generation diagnostic for the default computable def. -/
axiom oracle_halt (p x : Nat) : Bool
def chi (p x : Nat) : Bool := oracle_halt p x
