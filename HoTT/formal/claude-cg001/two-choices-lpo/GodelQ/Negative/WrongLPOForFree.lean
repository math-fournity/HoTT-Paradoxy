import Lean.Elab.Command
import GodelQ.TwoChoices.Core

/-!
# 负控制 MP-CG001-TWO-CHOICES-LPO-NEG-001：不选 A，也能“免费”得到 LPO

被否定的说法：不加 A（不加 `LimBit`、`NatBMC`、`BMCQ`），也能在不预设排中律的底座上得到 LPO。
这里借排中律证出 LPO，然后跑与主包相同的公理审计（不得依赖 `Classical.choice`）。

预期：拒绝。审计报出 `lpo_for_free` 依赖 `Classical.choice`。这说明主包的审计不是空的：
主包里 LPO 只能从 A 推出（C-418），不能从“什么都不加”推出；在经典逻辑里，它来自排中律
（主包 `lpo_classical`，C-421）。
-/

namespace GodelQ.TwoChoices.Negative

open GodelQ.TwoChoices

theorem lpo_for_free : LPO := by
  intro q
  rcases Classical.em (∃ k, q k = true) with h | h
  · exact Or.inr h
  · refine Or.inl (fun k => ?_)
    cases hk : q k with
    | false => rfl
    | true => exact absurd ⟨k, hk⟩ h

end GodelQ.TwoChoices.Negative

open Lean in
run_cmd do
  let axs ← collectAxioms ``GodelQ.TwoChoices.Negative.lpo_for_free
  if axs.contains ``Classical.choice then
    throwError m!"公理审计拒绝：lpo_for_free 依赖 Classical.choice（{axs}）"
