-- 迭代执行 n 步
def run (c : Code) (q : Config) (n : Nat) : Config :=
  match n with
  | 0 => q
  | n' + 1 => step c (run c q n')

lemma fixed_point_no_return (q_trap : Config) (n : Nat) (v : Nat) :
  trap_is_fixed_point q_trap →
  ¬ (run D_h q_trap n).halted = true
