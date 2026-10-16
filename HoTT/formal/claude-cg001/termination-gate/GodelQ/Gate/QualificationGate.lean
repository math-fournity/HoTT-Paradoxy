import Lean
import GodelQ.Gate.Core

/-!
# 命题对照与公理审计：CG001-C-431

`qual_C431`：不设门（每个递归定义都算数）就证得出 `False` 与一切命题，数据版同样；
过了门的递归（良基）定义方程有解。

**公理审计**（文件末尾的 `run_cmd`，机器断言，违反则编译失败）：这些定理不依赖 `Classical.choice`，
审计同时把实际公理清单打印出来。
-/

namespace GodelQ.Gate

/-- CG001-C-431。 -/
theorem qual_C431 :
    (UngatedProp → False) ∧
    (UngatedProp → ∀ P : Prop, P) ∧
    (UngatedType → False) ∧
    (∀ {α : Type} {C : α → Type} {r : α → α → Prop} (_hwf : WellFounded r)
        (F : ∀ x, (∀ y, r y x → C y) → C x),
      ∃ g : (∀ x, C x), ∀ x, g x = F x (fun y _ => g y)) :=
  ⟨ungated_proves_false, ungated_proves_anything, ungated_data_empty,
   fun hwf F => gated_has_solution hwf F⟩

end GodelQ.Gate

open Lean in
run_cmd do
  let names : List Name :=
    [``GodelQ.Gate.qual_C431, ``GodelQ.Gate.ungated_proves_false,
     ``GodelQ.Gate.ungated_proves_anything, ``GodelQ.Gate.ungated_data_empty,
     ``GodelQ.Gate.gated_has_solution]
  for n in names do
    let axs ← collectAxioms n
    if axs.contains ``Classical.choice then
      throwError m!"公理审计失败：{n} 依赖 Classical.choice（{axs}）"
    logInfo m!"公理审计通过：{n} 不依赖 Classical.choice；实际公理 {axs}"

#print axioms GodelQ.Gate.qual_C431
