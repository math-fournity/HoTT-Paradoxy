# H₀：任意 audit metadata payload 的 Cubical 正控制

> 状态：`FORMAL_STATEMENT_FROZEN / PROOF_SOURCE_PERSISTED / RUN_NOT_YET_CAPTURED`
>
> 任务：`T1-H0-APPEND-ONLY-AUDIT-001` 的 metadata 参数化补强；Terra 审计 017 §8。
>
> Proof ID：`MP-TERRA-T1-H0-GENERIC-001`。

## 对象与边界

在 Cubical Agda 中，模块参数为 `Content`、`Actor`、`Action`、`Metadata`、`apply`、`undo` 及内容层 inverse law。`Metadata` 是任意 `Type` 的已给定 payload；例如可实例化为 T1 所需 `code × entity × authorization × source × outcome × recorded × detail` 的乘积类型。`step` 在**同一个 primitive operation**中把 actor、action、before、after 和 metadata append 到 `List AuditEvent`。

本包不声明已构造实际 FHIR datatype，也不验证该 metadata 的语义、时间戳可信性、签名、权限策略或部署持久化。

## 形式命题

| Claim | Cubical Agda 命题 | 精确支持范围 |
|---|---|---|
| `C-351` | `contentUndo` 对任意 supplied actor/action/metadata/content/log 给出内容投影恢复。 | 只要求传入的 `undo-law`；与 metadata 的内部结构无关。 |
| `C-352` | `auditAppend` 对任意 supplied `m₁,m₂` 证明最终 log 逐项含两个 `recordEvent`，其中完整保留 actor/action/before/after/metadata。 | 事件由同一 `step` 生成，不是事后追加；payload 是给定数据。 |
| `C-353` | `contentRestoredAtInitial` 与 `fullStateNotReturn` 对任意 supplied `m₁,m₂,c` 同时成立。 | 内容 reverse 与完整 audit-state reverse 是不同的合同；初始 log 固定为空。 |

## 禁止外推

- 不证明任意 action 系统都具备 `undo-law`；该 law 是本模型的显式输入；
- 不证明具体 FHIR field/profile、FHIR server、NIST access control、retention/WORM 或 cryptographic integrity；
- 不证明所有 metadata 都有值；命题量化的是**已给定** `m₁,m₂`；
- 不证明 HPT merge/replay、整个 T1 deployment、所有 HoTT representation 或 HoTT 没有现实相对悖论。
