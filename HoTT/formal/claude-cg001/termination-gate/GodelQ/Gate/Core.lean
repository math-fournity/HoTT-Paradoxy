/-!
# 终止检查是这道门：不设门，什么都证得出（CG001-C-431）

研究发起人 2026-10-14【原话】：“而是否可停机、可计算，恰恰是必须考察的 —— 它被哥德尔提出，
被图灵重新表述，在算法设计中，更是一个算法合法的最根本的前提。”

把程序当证明的系统（Agda、Lean、Coq 一类）每天都在运行这道门：一个递归定义，只有在证得出它的
计算会停时才被接受，即每一次递归调用都沿一个良基的序往下走。本文件只用 Lean 内核，证明四件事。

* `ungated_proves_false`：不设门的定义原则是“任何 x := f x 的递归定义都算数”，也就是每个命题上的
  每个自映射都有不动点。有了它就证得出 `False`：取 f 为恒等，“x := x”这个永远算不完的定义交出了
  `False` 的证明。
* `ungated_proves_anything`：推论，每个命题都证得出。
* `ungated_data_empty`：对数据也一样，空类型里出现了元素。
* `gated_has_solution`：正控制。过了门的递归，即每次调用都沿良基关系往下走、计算会停，它的定义
  方程有解：存在 g，使 g x 等于 F 在 x 处用 g 的较小值算出的结果。这里没有任何矛盾。

负控制 `GodelQ/Negative/WrongLoop.lean`：在 Lean 里直接写 `loop : False := loop`，被 Lean 的终止检查
拒绝。我们自己的每一个 Lean 与 Agda 证明，都过了这道门。
-/

namespace GodelQ.Gate

universe u v

/-- 不设门的定义原则（命题版）：每个命题上的每个自映射都有不动点，
即每个递归定义 `x := f x` 都算数，不问它的计算停不停。 -/
def UngatedProp : Prop := ∀ α : Prop, (α → α) → α

/-- C-431 (1)：不设门，就证得出 `False`。“x := x”这个永远算不完的定义交出了它。 -/
theorem ungated_proves_false (fix : UngatedProp) : False := fix False id

/-- C-431 (2)：不设门，每个命题都证得出。 -/
theorem ungated_proves_anything (fix : UngatedProp) (P : Prop) : P := fix P id

/-- 不设门的定义原则（数据版）。 -/
def UngatedType : Type 1 := ∀ α : Type, (α → α) → α

/-- C-431 (3)：对数据也一样，空类型里出现了元素。 -/
theorem ungated_data_empty (fix : UngatedType) : False := (fix Empty id).elim

/-- C-431 (4)，正控制：过了门的递归有解。每次递归调用都沿良基关系 `r` 往下走（计算会停）时，
定义方程 `g x = F x (g 在更小处的值)` 有解。 -/
theorem gated_has_solution {α : Sort u} {C : α → Sort v} {r : α → α → Prop}
    (hwf : WellFounded r) (F : ∀ x, (∀ y, r y x → C y) → C x) :
    ∃ g : (∀ x, C x), ∀ x, g x = F x (fun y _ => g y) :=
  ⟨WellFounded.fix hwf F, fun x => WellFounded.fix_eq hwf F x⟩

end GodelQ.Gate
