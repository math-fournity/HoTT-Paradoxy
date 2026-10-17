import Lean
import GodelQ.Russell.Sep
import GodelQ.Russell.Foundation
import GodelQ.Russell.Unbounded

/-!
# 命题对照与公理审计：罗素解决考古（C-432–C-435）

四条命题的逻辑核合取在一条定理里，全部零集合论公理（环境只有 `SetStructure V`，
即 `Membership V V`）；`𝗭`（Foundation 库的 Zermelo 集合论）只作为公理前提的
提供者在各文件的实例化节出现。

- C-432（R1，对角层）：`¬ ∃ R, ∀ x, x ∈ R ↔ x ∉ x`——纯逻辑。
- C-433（R2，分离层）：分离公理的成员刻画前提 ⇒ `R ∉ A`——不是矛盾。
- C-434（R3，正则层）：正则公理 + 单元素集 ⇒ `∀ x, x ∉ x`——准入禁止。
- C-435（负控制）：无界概括（命题形态）⇒ `False`——爆炸的充分条件。

**公理审计**（文件末尾）：四条逻辑核不依赖 `propext`、`Classical.choice`、`Quot.sound`
以外的任何东西（纯逻辑核预期公理清单为空）。
-/

namespace GodelQ.Russell

open FFL

/-- **C-432–C-435 命题对照**。四条逻辑核，环境只有成员关系，无任何集合论公理。 -/
theorem qual_russell_arch :
    (∀ {V : Type*} [SetStructure V], ¬ ∃ R : V, ∀ x : V, x ∈ R ↔ x ∉ x) ∧
    (∀ {V : Type*} [SetStructure V] (A R : V),
      (∀ z : V, z ∈ R ↔ (z ∈ A ∧ z ∉ z)) → R ∉ A) ∧
    (∀ {V : Type*} [SetStructure V],
      (∀ s : V, (∃ w : V, w ∈ s) → ∃ y ∈ s, ∀ z ∈ s, z ∉ y) →
      (∀ x : V, ∃ s : V, ∀ z : V, z ∈ s ↔ z = x) →
      ∀ x : V, x ∉ x) ∧
    (∀ {V : Type*} [SetStructure V],
      (∀ P : V → Prop, ∃ S : V, ∀ z : V, z ∈ S ↔ P z) → False) :=
  ⟨@noRussellSet, @sep_russell_not_mem, @foundation_irrefl, @unboundedComprehensionFalse⟩

end GodelQ.Russell

open Lean in
run_cmd do
  let names : List Name :=
    [``GodelQ.Russell.noRussellSet, ``GodelQ.Russell.sep_russell_not_mem,
     ``GodelQ.Russell.foundation_irrefl, ``GodelQ.Russell.unboundedComprehensionFalse,
     ``GodelQ.Russell.qual_russell_arch]
  for n in names do
    let axs ← collectAxioms n
    if axs.contains ``Classical.choice then
      throwError m!"公理审计失败：{n} 依赖 Classical.choice（{axs}）"
    logInfo m!"公理审计通过：{n}；实际公理 {axs}"

#print axioms GodelQ.Russell.qual_russell_arch