import GodelQ.Diagonal.Core
import GodelQ.Diagonal.MathlibCodes

/-!
# 命题对照与公理审计：CG001-C-422

* `qual_C422`（构造一侧）：说谎者形状 `P ↔ ¬P` 推出矛盾；在任何有翻转程序的编程系统里，没有程序
  恰好认出“永不停机”，也没有完全的停机判定器；正控制：去掉翻转程序，认出者可以存在。
* `qual_C422_codes`（实例，经典）：Mathlib 的计算模型有翻转程序；于是那里没有程序恰好认出
  “永不停机”，也没有完全的停机判定器。

**公理审计**（文件末尾的 `run_cmd`，机器断言，违反则编译失败）：
1. 构造一侧的定理不依赖 `Classical.choice`。实际上它们不依赖任何公理，审计也把公理清单打印出来。
2. 对照：实例一侧（`code_flip`、`codeSystem`、`qual_C422_codes`）与 Mathlib 自己的
   `ComputablePred.halting_problem` 都依赖 `Classical.choice`。经典的只是“翻转程序存在”这一句
   正面的编程事实；“认不全”的那一步来自构造一侧。
-/

namespace GodelQ.Diagonal

/-- CG001-C-422（构造一侧）。 -/
theorem qual_C422 :
    (∀ P : Prop, ¬ (P ↔ ¬ P)) ∧
    (∀ S : ProgSystem, ¬ ∃ d, RecognizesNever S d) ∧
    (∀ (S : ProgSystem) (SaysYes : Nat → Nat → Nat → Prop), ¬ ∃ d, Decides S SaysYes d) ∧
    (∃ (H : Nat → Nat → Prop) (N : Nat → Nat → Nat → Prop) (d : Nat),
      (∀ e x, N d e x ↔ ¬ H e x) ∧ ¬ (∀ d, ∃ f, ∀ x, H f x ↔ N d x x)) :=
  ⟨no_liar, no_never_recognizer, no_decider, recognizer_without_flip⟩

/-- CG001-C-422（实例，经典）：Mathlib 的计算模型。 -/
theorem qual_C422_codes :
    (∀ d, ∃ f, ∀ x, codeHalts f x ↔ codeSaysNo d x x) ∧
    (¬ ∃ d, ∀ e x, codeSaysNo d e x ↔ ¬ codeHalts e x) ∧
    (¬ ∃ d, ∀ e x, (codeSaysYes d e x ↔ codeHalts e x) ∧ (codeSaysNo d e x ↔ ¬ codeHalts e x)) :=
  ⟨code_flip, turing_codes.1, turing_codes.2⟩

end GodelQ.Diagonal

open Lean in
run_cmd do
  let constructive : List Name :=
    [``GodelQ.Diagonal.qual_C422, ``GodelQ.Diagonal.no_liar,
     ``GodelQ.Diagonal.no_never_recognizer, ``GodelQ.Diagonal.no_decider,
     ``GodelQ.Diagonal.recognizer_without_flip]
  for n in constructive do
    let axs ← collectAxioms n
    if axs.contains ``Classical.choice then
      throwError m!"公理审计失败：{n} 依赖 Classical.choice（{axs}）"
    logInfo m!"公理审计通过：{n} 不依赖 Classical.choice；实际公理 {axs}"
  let classical : List Name :=
    [``GodelQ.Diagonal.code_flip, ``GodelQ.Diagonal.codeSystem,
     ``GodelQ.Diagonal.qual_C422_codes, ``ComputablePred.halting_problem]
  for n in classical do
    let axs ← collectAxioms n
    unless axs.contains ``Classical.choice do
      throwError m!"对照失败：{n} 本应依赖 Classical.choice（{axs}）"
    logInfo m!"对照：{n} 依赖 Classical.choice；实际公理 {axs}"

#print axioms GodelQ.Diagonal.qual_C422
#print axioms GodelQ.Diagonal.qual_C422_codes
