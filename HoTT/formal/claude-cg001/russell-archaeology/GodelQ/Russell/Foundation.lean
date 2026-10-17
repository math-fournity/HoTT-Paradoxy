import Foundation.FirstOrder.SetTheory.Z.Z

/-!
# R3（C-434）：正则公理层——第三种准入手段

**考古位置**：ZFC 的「安全」来自**两道独立的准入限制**，不是一条「解决」定理。
分离（1908，C-433）之外，正则公理（Foundation / Regularity，1930 年代
von Neumann–Zermelo 路线；历史时间线由步骤 2 落实，落盘时点为待核）是第二道：
连自含集合都**禁止存在**——`∀ x, x ∉ x` 是通过禁止实现的，又一个「宣布 vs 手段」
的实例。

**命题形态**：核心命题把正则公理（每个非空集合有 ∈-极小元）与单元素集存在
（配对公理的 singleton 实例，标准教科书推导用它造 `{x}`）作为**显式前提**，
结论 `∀ x, x ∉ x`。库内对应引理为 `Z/Z.lean` 的 `foundation` 与 `mem_irrefl`
（后者正是 `simpa using foundation ({x} : V)` 的推导）；本包独立重述以承载
考古定位，不主张数学内容原创。

**宿主理论说明**：同 `Sep.lean`——Foundation 库的 `𝗭` 含正则公理（Schindler
口径），与 1908 年历史系统不同；考古内容靠显式前提的核心命题承载。
-/

namespace GodelQ.Russell

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

section Core

variable {V : Type*} [SetStructure V]

/-- **C-434（R3，正则层）核心命题**：正则公理（每个非空集合有 ∈-极小元的
显式形式）+ 单元素集存在 ⇒ `∀ x, x ∉ x`。证明走标准教科书路径：对 `{x}`
用正则公理，极小元只能是 `x` 自己，于是 `x ∉ x`。 -/
theorem foundation_irrefl
    (hfoundation : ∀ s : V, (∃ w : V, w ∈ s) → ∃ y ∈ s, ∀ z ∈ s, z ∉ y)
    (hsingle : ∀ x : V, ∃ s : V, ∀ z : V, z ∈ s ↔ z = x) :
    ∀ x : V, x ∉ x := by
  intro x
  obtain ⟨s, hs⟩ := hsingle x
  obtain ⟨y, hy, hmin⟩ := hfoundation s ⟨x, (hs x).mpr rfl⟩
  have hyx : y = x := (hs y).mp hy
  have hxny : x ∉ y := hmin x ((hs x).mpr rfl)
  rwa [hyx] at hxny

end Core

section Z

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

/-- **C-434 实例化**：在 Foundation 库的 `𝗭` 中，从库的正则公理引理 `foundation`
（`Z/Z.lean:496`）与单元素集构造出发，`∀ x, x ∉ x`。库内同内容引理为
`mem_irrefl`（`Z/Z.lean:503`）；此处从公理前提独立推导。 -/
theorem foundation_irrefl' : ∀ x : V, x ∉ x := by
  refine foundation_irrefl ?_ ?_
  · intro s hs
    obtain ⟨w, hw⟩ := hs
    haveI : IsNonempty s := ⟨w, hw⟩
    exact foundation s
  · intro x
    exact ⟨{x}, fun z => mem_singleton_iff⟩

end Z

end GodelQ.Russell