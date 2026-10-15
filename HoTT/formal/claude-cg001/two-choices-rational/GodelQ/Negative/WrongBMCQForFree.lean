import Lean.Elab.Command
import GodelQ.TwoChoices.RationalConstructive

/-!
# 负控制 MP-CG001-TWO-CHOICES-RATIONAL-NEG-001：不选 A，也能“免费”得到有理数的单调收敛

被否定的说法：不加 A，也不加 LPO，就能在不预设排中律的底座上得到 `BMCQ`（每个有界单调的有理数列
都收敛）。这里借排中律证出它，再跑与主包相同的公理审计（不得依赖 `Classical.choice`）。

预期：拒绝。审计报出 `bmcQ_for_free` 依赖 `Classical.choice`。这说明主包的审计不是空的：主包里
`BMCQ` 只能从 LPO 推出（C-425），不能从“什么都不加”推出；在经典逻辑里，它来自排中律。
-/

namespace GodelQ.TwoChoices.Negative

open GodelQ.TwoChoices

theorem bmcQ_for_free : BMCQ := by
  apply bmcQ_of_lpo
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
  let axs ← collectAxioms ``GodelQ.TwoChoices.Negative.bmcQ_for_free
  if axs.contains ``Classical.choice then
    throwError m!"公理审计拒绝：bmcQ_for_free 依赖 Classical.choice（{axs}）"
