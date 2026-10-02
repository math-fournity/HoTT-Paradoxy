<!-- governance-shard:v2
logical_id: PATTERN_P_DYNAMIC_DAG_ORCHESTRATION
shard_id: 003
index: ../模式P动态DAG调度.md
-->

# Battle、裁决与收据

## 1. Battle 的触发条件

Battle 不是让代理互相辩论。只在下列任一事实条件出现时建立：

| 触发 | 例子 | Battle 要回答的精确问题 |
|---|---|---|
| 字段冲突 | P1 的 `C` 与 P3 的 consumer semantics 不同 | 同一 source 是否真的支持该 C 的输入、输出、Done？ |
| 来源冲突 | 一方声称 rule 双向，另一方读为单向 guard | 哪条原文、定义或源码决定方向与 domain？ |
| 任务冲突 | 一方把 false 当作未完成，另一方当完成分支 | 当前 Done 是否要求 positive result？ |
| 层级冲突 | 规则、库、模型或实现被混作 theory fact | 该 claim 属于哪个层，能否跨层使用？ |
| 控制冲突 | 正控制／反控制改变了结论 | 哪个输入或前提改变了可观察量？ |
| Master claim | Master 提出新 P 或归因 | 独立节点能否从同一 source 支撑或反驳它？ |

没有这些触发时，Master 不因“多一个意见或许更好”而开启 Battle。

## 2. 有界 Battle 子图

```text
sealed Claim A + sealed Claim B + frozen source pack
      → challenge-A / challenge-B（可并行）
      → reply（仅回应明确 source locator）
      → independent arbiter
      → Master evidence decision
```

每一 claim 至多一次 challenge 和一次 reply；arbiter 只看 source pack、claims、challenge/reply 和既定控制。新一轮必须由新原典、可复现实验、任务规格修订或可定位 source conflict 开启。否则结论是 `BATTLE_INCONCLUSIVE`，不能无界延长。

## 3. Master 参与与裁决

Master 可以：

- 提出 `MASTER_CLAIM`，并把它交给独立 challenger；
- 要求双方把自然语言判断压回同一个 `T/u/F/C/Q/I/O/Done`；
- 发现 prompt 漂移、answer leakage、task switch 或证据等级混同后中断节点；
- 依据原典、运行、控制和同一任务判据写最后的 `MasterVerdict`。

Master 不能：以更多代理支持一方作为胜负理由；用自己的原始提示充当来源；把 agent 的自我说明称为其内部因果机制；在 source 尚未支持时宣布 Q 已定位。

证据优先级为：固定一手规则／真实 consumer source → 形式证明或保存运行的范围内事实 → 同一任务控制 → 代理公开 MatchTrace → 多节点一致。低层证据不能覆盖高层冲突。

## 4. Battle 收据与停止

每个 Battle 至少保存：争议字段、A/B source locators、共同 source pack hash、每个 NodeCard 的 access profile、challenge/reply、arbiter verdict、MasterVerdict、未决项与下一触发条件。原始 app-server wire 或完整上下文留在私有目录，不进 Git；公开审计只保留必要的 prompt 身份、可见输出和来源定位。

终态只能是：

```text
RESOLVED_BY_SOURCE
RESOLVED_BY_CONTROL
SOURCE_INSUFFICIENT
TASK_SWITCH_REJECTED
ACCESS_LEAK_SUSPECTED
BATTLE_INCONCLUSIVE
```

终态影响下一张 source card、某一把刀的修订或当前候选的状态；只有 Master 才能把这一变化写回 `模式P三把刀`、Feature、rulings、MEMORY 或其它 current owner。
