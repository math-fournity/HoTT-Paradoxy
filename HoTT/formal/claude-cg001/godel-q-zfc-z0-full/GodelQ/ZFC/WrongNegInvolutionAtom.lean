import GodelQ.ZFC.NegInvolution

/-!
# 负控制：`neg` 对合律的 `and` 支把德摩根写错时被内核拒绝

`neg_neg_code` 的 `and` 支用 `neg_or`：`neg (y₁ ⋎ y₂) = neg y₁ ⋏ neg y₂`（**合取**）。
本文件故意把结论写成析取（`p ^⋎ q`），内核应当拒绝：改写之后剩下
`p ^⋏ q = p ^⋎ q`，不是定义相等。

本文件**不是**任何运行的编译源；它的用途只是证明对合律的分支不是空转。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.NegInvolution

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 错误的德摩根侧（应为 `p ^⋏ q`）：内核必须拒绝。 -/
example {p q y₁ y₂ : V} (hu₁ : IsUFormula ℒₒᵣ y₁) (hu₂ : IsUFormula ℒₒᵣ y₂)
    (ihp : neg ℒₒᵣ y₁ = p) (ihq : neg ℒₒᵣ y₂ = q) :
    neg ℒₒᵣ (y₁ ^⋎ y₂) = (p ^⋎ q : V) := by
  rw [neg_or (L := ℒₒᵣ) hu₁ hu₂, ihp, ihq]

end GodelQ.NegInvolution
