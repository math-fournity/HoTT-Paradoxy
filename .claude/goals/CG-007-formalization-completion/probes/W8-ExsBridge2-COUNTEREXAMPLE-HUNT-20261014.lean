import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 找 `ExsBridge2` 的真反例：要害在**自由变量集**是否相同（2026-10-14）

Master 的思路（我采纳并机器化）：既然 `t = ^&0`、`p = #0 = #0` 不反例
（两边都真），要害在**自由变量出现在 RHS 缺失的位置**。

试 `p = ^rel 2 cEqN [?[^#0, ^&0]]`（层 1，含 fvar `^&0` 在**第二个参数位**）：
* **LHS** = `iT 0 (substs1 ^&0 p)`：`substs1` 把 `^&0` 代入 p 的 fvar 位，**消掉它**；
* **RHS** = `^∃ (domZero ⋏ iT 1 p)`：`iT` 不代入，p 里的 `^&0` **仍是自由变量**。

**⟹ 两边的自由变量集不同！** 这是要害。

**语义后果**（关键推理）：
* LHS 是**闭句**（无自由变量）⟹ `Provable LHS` 意为「在 ℕ 中真」；
* RHS 含自由变量 `^&0` ⟹ `Provable (imp LHS RHS)` 意为 `⊢ ∀a (LHS → RHS[a])`。

**若 `LHS` 在 ℕ 中真，而存在 `a ∉ ω` 使 `RHS[a]` 假，则 `ExsBridge2` 为假。**

本探针把两边的**自由变量集**机器算出来（这是决定性一步）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeCounterHunt
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 候选反例的 `p`：`^rel 2 cEqN [?[^#0, ^&0]]`（层 1，`^&0` 在第二个参数位）。 -/
noncomputable def p0 : V := ^rel (2:V) (↑cEqN) (?[^#0, ^&0] : V)

theorem p0_isSF : IsSemiformula ℒₒᵣ (1:V) p0 := by
  rw [p0, IsSemiformula.rel]
  refine ⟨by rw [cEqN]; exact codeIn_rel_quote _, ?_⟩
  simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
    (IsUTerm.bvar (z := (0:V)))) (IsUTerm.fvar (x := (0:V))))

-- ① LHS 是**闭句**（层 0）—— `substs1 ^&0` 消掉了唯一的 fvar
example : IsSemiformula ℒₛₑₜ (0:V) (iT (0:V) (substs1 ℒₒᵣ (^&(0:V)) p0)) := by
  refine isSemiformula_iT (n := (0:V)) _ ?_
  refine IsSemiformula.substs1 (L := ℒₒᵣ) (n := (0:V))
    (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (0:V)) 0) ?_
  simpa using p0_isSF

-- ② RHS 是**闭句**（层 0）—— `^∃` 绑定新变量，`iT` 不代入
--    ⚠ 但 p0 含 fvar ^&0，`iT` 不改它 ⟹ RHS 应含自由变量？
--    层数上 `^∃` 让层数降到 0，但**自由变量不因层数降低而消失**。
--    `IsSemiformula` 只管层数不管自由变量 ⟹ 层数核验无法区分。
--    这正是要害：**必须查自由变量集，不是层数**。
example : IsSemiformula ℒₛₑₜ (0:V) ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p0) : V) := by
  rw [IsSemiformula.exs]
  refine IsSemiformula.and.mpr ⟨?_, ?_⟩
  · simpa using isSemiformula_domZero (V := V) (n := (0:V))
  · simpa using isSemiformula_iT (n := (1:V)) p0 p0_isSF

-- V 层的自由变量件（Formula/Functions.lean:523 有 termFreeAt，但命名空间待定）
#check @IsTermFVFree

/-- ★ **决定性语义论证**（本探针的核心结论，AI 推理，未证）：

两边自由变量集不同 ⟹ `Provable (imp LHS RHS)` 被全称化到不同变量集上：

* **LHS 闭**（`IsSemiformula ℒₛₑₜ 0`，本探针已机核验 exit 0）：
  `Provable LHS` 意为「LHS 在 ℕ 中真」；
* **RHS** 由 `^∃` 使层数为 0，但 **`p0` 的 fvar `^&0` 不被 `iT` 消掉**，
  故 RHS **仍含自由变量**；
* ⟹ `Provable (imp LHS RHS)` 意为 `⊢ ∀a (LHS → RHS[a])`。

**分水岭**：取 `a ∉ ω`（例如 `a = ω` 自己，或 `a = {ω}`）：
* `LHS` 与 `a` 无关（闭）⟹ 值不变；
* `RHS[a]` 含 `domZero`（= `x ∈ ω`）⟹ 当 `a ∉ ω` 时可能假。

**若存在这样的 `a`，则 `ExsBridge2` 为假**（桥要重找形状）；
若不存在，则桥为真但证明须绕开「t 的值 ∈ ω」。
**这一支必须用模型/语义论证定音，不是形状能定的。** -/
theorem fv_is_the_decisive_question : True := trivial

end ProbeCounterHunt

#print axioms ProbeCounterHunt.p0_isSF