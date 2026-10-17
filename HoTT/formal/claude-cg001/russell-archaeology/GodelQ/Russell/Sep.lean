import Foundation.FirstOrder.SetTheory.Z.Z

/-!
# R2（C-433）：分离公理层——Zermelo 1908 实际做的事

**考古位置**：朴素集合论爆炸解剖的**部件二被删除后**剩下的东西。Zermelo 1908
把无界概括换成分离公理（Aussonderung）：只允许从**已有**集合 `A` 中切割出
`R_A = {x ∈ A ; x ∉ x}`，并且可证 `R_A ∉ A`。

**关键叙事点**：`R_A ∉ A` **不是矛盾**。理论无矛盾地运行，只是无界的罗素集 `R`
永远没有资格被写出——这是「准入层拒绝」的精确数学形态。

**证明纪律**：核心命题的证明只使用纯逻辑（对角代入），**不使用**正则公理 /
`mem_irrefl` / 任何 foundation 类引理——那是 1930 年代的第二道门（C-434），
混进来会污染「1908 年层面」的考古定位。

**宿主理论说明**：Foundation 库的 `𝗭`（Schindler 教科书口径 `𝗕𝗦𝗧 ∪ 𝗦𝗘𝗣`）
**含**正则公理，与 Zermelo 1908 的历史公理系统（无正则）不同。因此本文件的
考古内容由**自包含前提的核心命题**承载（公理前提显式写出、证明不越界），`𝗭`
只在实例化节作为前提提供者出现。
-/

namespace GodelQ.Russell

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

section Core

variable {V : Type*} [SetStructure V]

/-- **C-433（R2，分离层）核心命题**：设 `R` 满足分离公理式的成员刻画
（`z ∈ R ↔ z ∈ A ∧ z ∉ z`），则 `R ∉ A`。证明是纯逻辑对角代入，不使用
正则公理；结论不是矛盾，是准入层拒绝。 -/
theorem sep_russell_not_mem (A R : V)
    (hR : ∀ z : V, z ∈ R ↔ (z ∈ A ∧ z ∉ z)) : R ∉ A := by
  intro hRA
  have h := hR R
  have hne : R ∉ R := fun hmem => (h.mp hmem).2 hmem
  exact hne (h.mpr ⟨hRA, hne⟩)

end Core

section Z

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

/-- **C-433 实例化**：在 Foundation 库的 `𝗭` 中，`{x ∈ A ; x ∉ x} ∉ A`。
`sep` 的成员刻画来自分离公理（`mem_sep_iff`）。 -/
theorem sep_russell_not_mem' (A : V) : {x ∈ A ; x ∉ x} ∉ A :=
  sep_russell_not_mem A {x ∈ A ; x ∉ x} (fun _ => mem_sep_iff)

end Z

end GodelQ.Russell