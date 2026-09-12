-- 假设 q_trap 是 D_h 编译后对应的陷阱配置
lemma trap_is_fixed_point (q_trap : Config) :
  q_trap.halted = false ∧ step D_h q_trap = q_trap
