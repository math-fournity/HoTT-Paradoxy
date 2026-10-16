/-!
# 负控制 MP-CG001-TERMINATION-GATE-NEG-001：拿“x := x”当 `False` 的证明

被否定的说法：一个永远算不完的定义 `loop := loop` 可以当作 `False` 的证明。
主包 C-431 (1) 证明：一旦接受这种定义，什么都证得出。

预期：拒绝。Lean 的终止检查找不到让递归往下走的量，不接受这个定义。这道门在 Lean 里每天运行。
-/

namespace GodelQ.Gate.Negative

def loop : False := loop

end GodelQ.Gate.Negative
