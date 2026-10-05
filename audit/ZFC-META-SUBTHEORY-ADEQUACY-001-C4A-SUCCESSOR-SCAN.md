# C4A 后继扫描：将 ApplicationAdequacy 固定为可形式化的 C5 合同

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C4A bridge payment](ZFC-META-SUBTHEORY-ADEQUACY-001-C4A-IEP-STANDARD-SOLUTION-BRIDGE-PAYMENT.md)。
>
> **结果：** `C4A_LOCAL_LEAF_CLOSED / C5A_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. 当前可用的 actual contract

```text
M = TG/MML as a ZFC-founded mathematical context
S = rich continuous real-analysis model fragment
Q_model = time-parameterized trajectory mathematics
Q_physical = IEP runner/course target
FormalDone = model endpoint / continuous-differentiable trajectory result
P = IEP Standard Solution application claim
Bridge = model-to-physical relation; source-to-spec payment not supplied
```

此处唯一尚未精确固定的核心字段是 `Adequacy`：哪个来源支持“P若谈物理完成，应披露足以支持该完成说法的 representation/completion relation”。C0C1已给出一般来源基础，C5A必须把它编译成有限、可反驳的 contract。

## 2. 后继比较

| 后继 | 能改变什么 | 裁决 |
|---|---|---|
| `C5A`：ApplicationAdequacyContract | 将R4 criterion变成明确的 `RequiresBridge(P,Q)` 而不冒充 ZFC axiom。 | **已选**。 |
| `C0B2` | 可给另一个 model/formalization；不改变当前 bridge gap的解释。 | 保留为外部 control。 |
| `C6A` | 需要 C5 exact contract。 | 未释放。 |
| `C0D` H0 | SameQ仍未付。 | 保持 control。 |

## 3. 自动选择：`C5A-APPLICATION-ADEQUACY-CONTRACT`

C5A 必须写出：

1. 该 contract 的 source fields（R3/R4，不是 bare ZFC axiom）；
2. `RequiresBridge` 的触发条件；
3. `BridgePaid` 与 explicit task switch 两种满足路径；
4. 正控制：model-internal completed task；负控制：physical claim但无bridge；
5. 不能由此推出 `ZFC ⊢ False` 或“ZFC不能表示时间”。

若 C5A 不能形成非任意 contract，则关闭这一 adequacy route并转 C0B2；绝不拿现有 gap直接宣布 failure。
