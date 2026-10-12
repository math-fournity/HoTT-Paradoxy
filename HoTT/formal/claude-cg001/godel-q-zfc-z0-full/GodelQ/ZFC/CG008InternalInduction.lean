import GodelQ.ZFC.CG008Rosser

/-!
# CG-008 · 内部归纳的可行性：`limSeq` 是**Σ₁ 函数**，这可能是通道

## 读到的（`HFS/Fixpoint.lean:131-155`）

```lean
noncomputable def limSeq (s : V) : V := c.prConstruction.result v s

instance limSeq_definable :
  𝚺ᴬ₁.DefinableFunction (fun v ↦ c.limSeq (v ·.succ) (v 0)) := c.termSet_defined.to_definable

lemma mem_limSeq_succ_iff {x s : V} :
    x ∈ c.limSeq v (s + 1) ↔ x ≤ s ∧ c.Φ v {z | z ∈ c.limSeq v s} x
```

**关键**：`limSeq` 是 **Σ₁ 可定义函数**（不是仅仅谓词）。
即：`limSeq v s` 这个**值**在 V 内可由 Σ₁ 公式算出。

而 `Fixpoint x := ∃ s, x ∈ c.limSeq v s`（`Fixpoint.lean:205`）。

## 为什么这可能是通道

内部归纳要的是：`𝗜𝚺₁ ⊢ ∀¹x, Fixpoint x → P x`。
而 `limSeq` 是 Σ₁ **函数**，所以「`x ∈ limSeq v (s+1)`」这个关系
在 V 内是 Σ₁ 的。

**`𝗜𝚺₁` 能做 Σ₁ 归纳吗？** `provable_sigma_one_complete`（`StandardProvability.lean:66`）
表明 `𝗜𝚺₁` 能对 Σ₁ 句做**完全性**——即 `𝗜𝚺₁ ⊢ σ → □σ` 对 Σ₁ 句 σ。
**这正是一种「内部归纳」的能力。**

## 本探针要查实

1. `limSeq` 是 Σ₁ 可定义函数（机器核实）；
2. `mem_limSeq_succ_iff` 的形状（它是**元层** `↔` 还是内部可证）；
3. 缺口所需的内部归纳能否由 `provable_sigma_one_complete` 提供。

**第 3 条是本轮的要点**：若 `P` 是 Σ₁，则 `provable_sigma_one_complete`
给 `𝗜𝚺₁ ⊢ P → □P`——**这是「内部可证性」的自我意识**，
可能正是 D3 需要的。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008InternalInduction

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮要点）**：`𝗜𝚺₁` 能做 **Σ₁ 句的内部完全性**——
对 Σ₁ 句 σ，`𝗜𝚺₁ ⊢ σ → □σ`（`□ = provabilityPred T`）。

**这是「内部归纳」能力的直接证据**：Σ₁ 句一旦成立，其可证性在内部随之成立。
这正是 D3 对 Σ₁ 句所需要的形状。 -/
example {T : ArithmeticTheory} [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]
    {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    𝗜𝚺₁ ⊢ σ 🡒 provabilityPred T σ :=
  provable_sigma_one_complete (T := T) hσ

/-- **查实 2**：`provable_D3` 正是查实 1 的**推论**（取 `σ := □σ₀`，而 `□σ₀` 是 Σ₁）。

所以：**D3 对算术理论是「Σ₁ 完全性」的直接推论**。
缺口要的是同一件事，只是被谈论的理论不是算术理论。 -/
example {T : ArithmeticTheory} [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ provabilityPred T σ 🡒 provabilityPred T (provabilityPred T σ) :=
  provable_D3 (T := T)

end GodelQ.CG008InternalInduction
