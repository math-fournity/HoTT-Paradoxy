# H₀：同一 update、授权 audit query 与事件元数据的 Cubical interface 正控制

> 状态：`FORMAL_STATEMENT_FROZEN / PROOF_SOURCE_PERSISTED / RUN_NOT_YET_CAPTURED`
>
> 任务：`T1-H0-APPEND-ONLY-AUDIT-001` 的 interface 补强；Terra 审计 017 §8。
>
> Proof ID：`MP-TERRA-T1-H0-INTERFACE-001`。

## 对象、理论变体与边界

本包使用 Cubical Agda 2.8.0-3d04bac 与 Cubical library v0.9，选项为 `--safe --cubical --guardedness`。模型只有三个 actor（`updater`、`auditor`、`outsider`）、两个 action 和 Bool content。`step` 的唯一公开效果是同时改变内容并 append 由该 actor/action/前后内容构成的 event；`readAudit` 需要 `CanReadAudit` 见证。

`Permit`／`Denied` 是最小静态 capability 类型。它们证明固定接口中的可用性/不可用性，不编码 FHIR authorization、NIST 实施、管理员权限、密钥、存储、WORM、保留期或攻击模型。

## 形式命题

| Claim | Cubical Agda 命题 | 精确支持范围 |
|---|---|---|
| `C-347` | `forwardPermit` 可居住，且 `forwardEventIsInternal`、`forwardEventCarriesActor`、`forwardEventCarriesAction` 成立。 | 由同一个 `step updater forward` 内部生成、append 的 event 保留 updater/forward 元数据；不是外加的第二操作。 |
| `C-348` | `authorizedQuery : readAudit auditor afterUndo auditReaderPermit ≡ [event updater forward true false, event updater backward false true]`。 | 固定授权 reader 能读取同一两步生成的两条完整 event。 |
| `C-349` | `outsiderCannotUpdate` 与 `outsiderCannotRead`。 | 固定模型内 outsider 的 update/read capability 类型为空。 |
| `C-350` | `contentRestored : current afterUndo ≡ current initial`，同时 `fullStateNotReturn : ¬ (afterUndo ≡ initial)`。 | 内容层逆操作与完整审计 state 逆操作是不同合同。 |

## 禁止外推

- 不证明每个 FHIR R5 server 都生成、保存、保护或允许查询 AuditEvent；
- 不证明固定 capability 模型实现了 NIST 3.3.8/3.3.9，或现实攻击者不能改写日志；
- 不证明所有 action/content/log、HPT merge/replay、全部 HoTT representation 或整个 `X_FHIR`；
- 不以此宣称 HoTT 没有现实相对悖论；它只进一步击败 T1 的“必须在完整 state 上可逆才算同一 action”强句。
