# 修订记录：ObservationCompletionBridge

## 2026-10-03：run 01 的作用域失败与最小修复

`20261003-CG001-OBSERVATION-COMPLETION-BRIDGE-01`原本预计接受，但Agda在
`ObservationCompletionBridge.agda:39`报告`[NotInScope] ¬`。它尚未进入类型检查，因此不说明
`coarseCompletionCreatesNoRestoration`为假。

当时的源码已由[run 01 snapshot](../../../verification/runs/20261003-CG001-OBSERVATION-COMPLETION-BRIDGE-01/source-snapshot/ObservationCompletionBridge.agda)保留，并与其source-manifest哈希对应。唯一修复是在正式源码中导入`Cubical.Relation.Nullary`的`¬_`。后继run使用新ID，不能覆盖或改写run 01。

## 2026-10-03：run 02 的 parser failure 与最小修复

run 02已经看到`¬_`，但三重合取中`×`（优先级5）与前缀`¬`（优先级3）的组合缺少显式括号，Agda报告`[NoParseForApplication]`。该run同样未进入类型检查。其源码保存在[run 02 snapshot](../../../verification/runs/20261003-CG001-OBSERVATION-COMPLETION-BRIDGE-02/source-snapshot/ObservationCompletionBridge.agda)。唯一修复是在第三个合取项外加括号：`× (¬ (...))`。后继run使用新ID，不改写run 02。

## 2026-10-03：负控制 run 01 的错误拒绝层与修复

`WrongObservationCompletionBridge.agda`的第一个错误项把`Type ℓ-zero`作为`TU → Type ℓ-zero`的常值输出。Agda在`[UnequalSorts] Type₁ != Type`处拒绝，尚未触及被意图检验的逐元素恢复等式。该源码由[negative run 01 snapshot](../../../verification/runs/20261003-CG001-OBSERVATION-COMPLETION-BRIDGE-NEG-01/source-snapshot/WrongObservationCompletionBridge.agda)保存。后继负控制改用同层`Bool`作为常值输出，使拒绝必须检验`Bool ≡ A`这一真正的错误恢复要求；它使用新run ID，不改写旧收据。
