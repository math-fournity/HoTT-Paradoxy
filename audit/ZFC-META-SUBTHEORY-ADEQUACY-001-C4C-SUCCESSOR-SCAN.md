# C4C 后继扫描：共同规范化 completion control

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / A_DIRECTION_FORMALIZATION`。
>
> **前叶：** [C4C same-task audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C4C-DENSE-QUANTIZED-SAME-TASK-AUDIT.md)。
>
> **结果：** `C4C_LOCAL_LEAF_CLOSED / C4D_SELECTED / TOTAL_GATE_UNSATISFIED`。

## 为什么不是立刻结案或立刻归因

- source已明示 continuous completion不要求最后步骤；这排除了“它暗中把 finite-stage completion 当作已完成”的弱写法；
- source也没有给出 user/C2C finite-stage contract与dense endpoint的同一任务等价；
- 因此尚须先把控制模型中的两个 completion predicate放入同一可检查规格，避免下一步的 adequacy讨论自己混同两个 Done。

## 自动选择：`C4D-DENSE-QUANTIZED-COMPLETION-DIVERGENCE-MACHINE-CONTROL`

固定：共同规范化初态、dense 余量、quantized 余量、各自的 finite-stage Done、continuous endpoint正控制、反向错误同一化负控制。该机证仅服务 C4 的任务合同卫生；它不承担来源、物理或 bare-ZFC conclusion。
