# H₀：内容可撤销、审计事件可观察的最小 Cubical 正控制

> 状态：`FORMAL_STATEMENT_FROZEN / PROOF_SOURCE_PERSISTED / RUN_NOT_YET_CAPTURED`
>
> 任务：`T1-H0-APPEND-ONLY-AUDIT-001`；Terra 审计 017 §8 的模型级 countermodel candidate。
>
> Proof ID：`MP-TERRA-T1-H0-001`。

## 精确对象与理论变体

本包使用 Cubical Agda 2.8.0-3d04bac 与 Cubical library v0.9，启用 `--safe --cubical --guardedness`。`H0Audit.agda` 使用 native identity/path、积类型和归纳 `List`；没有 postulate、外部 FHIR SDK、网络、部署或权限系统。

模型固定：

```text
State = Bool × List AuditEvent
step(a, (c, log)) = (apply(a,c), log ++ [recordEvent(a)])
```

`forward` 与 `backward` 都作用为 Bool 的 `not`，因此后者是前者的内容层 inverse。它们不是完整 `State` 上的 inverse：audit log 有意继续保留事件。

## 形式命题

| Claim | Cubical Agda 命题 | 精确支持范围 |
|---|---|---|
| `C-344` | `contentUndo : (c : Bool) (log : AuditLog) → current (step (undo forward) (step forward (c , log))) ≡ c` | 对此固定 Bool action 与任意有限 audit log，两个同一 `step` 后恢复**内容投影**。 |
| `C-345` | `auditAppend : (c : Bool) (log : AuditLog) → audit (step (undo forward) (step forward (c , log))) ≡ log ++ (evForward ∷ evBackward ∷ [])` | 同一两个 primitive steps 内部分别产生并 append 两个 event；不是在 operation 外另加日志步骤。 |
| `C-346` | `fullStateNotReturn : ¬ (afterUndo ≡ initial)`，其中 `initial = (true,[])` 且 `afterUndo = step backward (step forward initial)`。 | 一个明确的完整状态实例不返回初始 state，尽管 `initialContentRestored` 成立。 |

## 不支持的结论

- 不证明所有 `Content`／`Action`／`AuditEvent` 或所有 HoTT representation 均有同一性质；
- 不证明 FHIR server 生成 AuditEvent，或 FHIR/NIST policy 的 authorization、query、retention、WORM、管理员约束或攻击防护；
- 不证明 HPT 的 contractible context、replay 或 merge law；
- 不证明 HoTT 是现实的、没有现实相对悖论，或任何社区原创性结论；
- 只构成对 T1 当前强句的正控制：content-level inverse 与 full-state inverse 是不同合同。
