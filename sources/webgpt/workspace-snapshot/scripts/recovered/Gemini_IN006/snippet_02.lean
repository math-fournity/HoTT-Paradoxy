lemma return_absorbing (c : Code) (q : Config) (v : Nat) :
  q.halted = true ∧ q.retval = v →
  step c q = q
