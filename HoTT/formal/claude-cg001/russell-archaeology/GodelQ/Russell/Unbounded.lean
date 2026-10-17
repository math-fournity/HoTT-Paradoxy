import GodelQ.Russell.Basic

/-!
# R4（C-435）：负控制——无界概括 ⇒ False

**考古位置**：朴素集合论爆炸解剖的**被删除部件**。无界概括（对任意性质 `P`
无中生有地造出 `S`，使 `z ∈ S ↔ P z`）是罗素悖论的充分燃料：一旦可用，取
`P := fun x => x ∉ x` 就造出无界罗素集，C-432 的对角论证立即爆炸。

**与 C-433 的对照**：分离公理把「`∀ P, ∃ S`」收窄成「`∀ P`，**给定基底 `A`**，
`∃ S`」——多出的 `z ∈ A` 合取项正是对角论证被挡住的位置（见负控制
`GodelQ/Negative/WrongSepContradiction.lean` 的类型失败）。C-435 与 C-433
合起来给出考古结论的机器面：**删除无界概括不是回避矛盾，而是让对角论证
停下来的精确手术位置**。

**命题形态**（交接文档 01 §3.1 方案 B）：无界概括作为 hypothesis 引入
（命题层），不在理论层自建含公理模式的新理论。结论 `False`：任何满足该
前提的成员结构环境都不存在。
-/

namespace GodelQ.Russell

open FFL

variable {V : Type*} [SetStructure V]

/-- **C-435（R4，负控制）核心命题**：无界概括（命题形态）⇒ `False`。证明：
取 `P := fun x => x ∉ x`，前提造出 `R`，其成员刻画正是 C-432 否定掉的
无界罗素集，对角论证接力爆炸。 -/
theorem unboundedComprehensionFalse
    (hcomp : ∀ P : V → Prop, ∃ S : V, ∀ z : V, z ∈ S ↔ P z) : False := by
  obtain ⟨R, hR⟩ := hcomp (fun x => x ∉ x)
  exact noRussellSet ⟨R, hR⟩

end GodelQ.Russell