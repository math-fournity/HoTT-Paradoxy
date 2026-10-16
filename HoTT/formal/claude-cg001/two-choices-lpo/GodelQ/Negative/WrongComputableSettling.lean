import GodelQ.TwoChoices.Machines

/-!
# 负控制 MP-CG001-TWO-CHOICES-LPO-NEG-003：机器能交出落定的一步

被否定的说法：有一台机器，对每个程序交出它的停机搜索落定的那一步。这里取最简单的候选：
一律回答“第 0 步”。

预期：拒绝。要证 `haltBits e m = haltBits e 0` 对每个程序、每个 `m` 成立，而第 0 步之后才停机的
程序使它为假；`simp` 证不出。主包的正面定理 `no_computable_settling_point`（C-420）证明任何
可计算的候选都不行。
-/

namespace GodelQ.TwoChoices.Negative

open GodelQ GodelQ.TwoChoices

theorem computable_settling :
    ∃ F : Process → ℕ, Computable F ∧ ∀ e, SettlesAt (haltBits e) (F e) :=
  ⟨fun _ => 0, Computable.const 0, fun e m _ => by simp [haltBits]⟩

end GodelQ.TwoChoices.Negative
