# `ZFC+Q_norm` 过程完成审计规范

> **Proof package:** `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001`。
>
> **身份：** `NORMATIVE_FORMAL_SPECIFICATION / NOT_A_BARE_ZFC_FORMALIZATION`。

这个目录把研究发起人提出的 MetaTheory→SubTheory 审计要求写成一个小的 Lean core contract。它不修改 ZFC，也不宣称数学共同体已经采纳它。它回答的只是：如果一个规范要求理论在将 `FormalDone` 提升为“原任务完成”前审查 bridge，这个规范应如何对三种来源状态作出不同 verdict。

| source/application 状态 | `audit` verdict | 可推出 |
|---|---|---|
| 明示且可用的 `FormalDone → OriginDone` certificate | `originalResolved` | `OriginDone` |
| 明示 task switch | `revisedResolved` | 只说明 revised task 被解决 |
| 没有 bridge payment | `bridgeRequired` | 不输出 original resolution |

`ProcessCompletionAudit.lean` 以 Norton completion contract、paid bridge和missing bridge作为三个控制。来源文字本身由 C5/C0 source cards认证；Lean只证明明确写入的数据结构和命题之间的逻辑后果。

Lean 还在一般 contract 层验证了两个反偷换不变量：`explicitTaskSwitch` 与
`missing` 都不可能产出 `originalResolved`。因此“模型里有 formal completion”本身，
在这项规范下既不是原任务已完成的证据，也不是把改题后的任务重新命名为原任务的许可证。
