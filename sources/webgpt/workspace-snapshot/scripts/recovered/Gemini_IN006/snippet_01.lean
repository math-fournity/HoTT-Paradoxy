-- 寄存器状态：有限列表
def RegState := List Nat

-- 机器配置：包含程序计数器 (pc)、寄存器状态 (regs) 和停机标志 (halted)
structure Config where
  pc : Nat
  regs : RegState
  halted : Bool
  retval : Nat -- 仅在 halted = true 时有效

-- 确定性步进函数 (依赖于固定的程序代码 c)
def step (c : Code) (q : Config) : Config := ...
