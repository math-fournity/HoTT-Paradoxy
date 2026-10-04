# ZFC-QP-ACTUAL-MAPPING-SOP：M1–M5 实际映射终局

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / EVIDENCE_FRONTIER_REACHED_WITH_SCOPE / NOT_A_ZFC_INCONSISTENCY_CONCLUSION`。

## 1. 阶段结果

| 阶段 | 结论 | 证据 |
|---|---|---|
| M1：芝诺 A/P | `TASK_CONTRACT_DIVERGENCE` | H099；IEP/SEP/Bathfield 的 Done 不统一。 |
| M2：圆环 P | `CIRCLE_D_UNRESOLVED` | H100；控制模型没有付 origin Done bridge。 |
| M3：Q | `Q_OBSERVATION_GAP_NOT_SOURCE_MAPPED` | H102；桥缺失不证明 ZFC 缺 Q。 |
| M4：HoTT B | `P_TO_B_NOT_ESTABLISHED` | H101；H0 是 detector，缺 PBacktrace。 |
| M5：Lean actual witness | `NOT_ENABLED` | A↔P、actual adoption、P→B、A⊥B 均无来源实例。 |

## 2. 终局

```text
EVIDENCE_FRONTIER_REACHED_WITH_SCOPE
```

在 TaskCard 冻结的来源分母内，没有一个来源同时给出：

```text
同一 origin D
∧ formal F
∧ promotionClaim(F,D)
∧ ¬ verifiedBridge(F,D)
∧ Q 的实际缺失
∧ 同一任务 PBacktrace 到 HoTT B
```

因此当前不能把条件性 `CommunityObservationPolicy` 代入实际 ZFC，也不能把政策张力升级为对象层矛盾。

## 3. 正面所得

本轮不是“什么也没找到”。它把 P 收紧为可证伪结构，并得到四条强控制：

1. 标准解有自身连续运动 Done，不能被删掉；
2. 圆环原 Done 不能被同胚、端点或离散控制替代；
3. HoTT H0 不能被无 provenance 地当作 P 的后果；
4. 没有来源定义的 Q 缺失，不能把桥不足当作 ZFC 不完备。

这些控制将未来的正面发现压缩为一条明确的来源任务：寻找**实际完成政策**，而不是继续重复极限、`never` 或 bridge 词汇。

## 4. 合法重开条件

| 新证据 | 重开阶段 |
|---|---|
| 指定来源把 F 明说为同一 D 的完成，同时未给 bridge | M1/M2/M3。 |
| 该来源实际采用 P 的规则，且 A↔P 可证 | M1/M5。 |
| 一个 H0 来源把 promotion 产生的 B 写成同一任务后果 | M4/M5。 |
| A、B 在一个明确形式系统内不相容 | M5 的 `False` 分支。 |

除这些触发外，继续新增相似来源节点将构成 `TOOL_ONLY_DRIFT`，不应被算作 P/Q 发现推进。
