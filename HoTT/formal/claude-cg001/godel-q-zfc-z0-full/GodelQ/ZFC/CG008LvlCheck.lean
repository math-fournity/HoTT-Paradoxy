import GodelQ.ZFC.CG008ITQuoteProof

/-!
# CG-008 探针（非收据）：层数无关谓词的 `Σ₁` 可定义性

`CG008ITQuoteProof.lean` 查出：`iT` 的 `all`/`exs` 情形**增加层数**
（`allChanges n _ := n + 1`），所以归纳假设 `IsUFormula ℒₛₑₜ (iT 0 p)`
**不直接适用**于 `all`。

**可能的修法**：把谓词改成层数无关的 `P p := ∀ n : V, IsUFormula ℒₛₑₜ (iT n p)`。

**本探针要查**：这个 `P` 是否仍 **Σ₁ 可定义**。

**关键问题**：`∀ n : V` 是**内部全称**——它把谓词的层级从 Σ₁ 推到 **Π₁**。
而 `sigma1_succ_induction` 要 **Σ₁** 谓词。

**所以「层数无关」可能不可行**——这是本探针要固定的。
（`definability` 对 `∀ n` 版本失败，见下。）

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008LvlCheck

open GodelQ.Translate (iT)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`Σ₁` 版本（`iT 0` 固定层数）**可定义**——闸门已过。 -/
example : 𝚺ᴬ₁-Predicate (fun x : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 x)) := by
  definability

-- **查实 2**：层数无关版本 `∀ n, IsUFormula ℒₛₑₜ (iT n x)` 的 `Σ₁` 可定义性
-- **未过**：`definability` 对该形状失败（`∀ n` 把层级推到 Π₁）。
--
-- 结论：**「层数无关」不可行**（至少不能靠 Σ₁）。
-- 下一步须另找修法——例如把 `P` 取成「`iT n p` 对**所有** `n` 都 `IsUFormula`」
-- 之外的形状，或证明 `all`/`exs` 情形其实**不需要**层数无关
-- （例如 `IsUFormula` 对层数不敏感，只需补一条 `iT` 的层数引理）。

end GodelQ.CG008LvlCheck
