# P-FORGE：P/Q 共同涌现与收敛的路线重对齐

> **身份：** `METHOD_REALIGNMENT / IDEA_SPEC_INCOMPLETE_REPAIRED / NOT_A_ZFC_OR_HOTT_THEOREM`。

## 1. 用户纠正的准确含义

研究发起人指出，锻 P1/P2/P3 与发现 ZFC 的 Q 不是两条平行工作线。锻刀的目的，是让 Q 的发现
逐渐变为可规范、可自动化、可被多把刀共同约束的过程；Q 应在同一理论卡的对象、形成、来源、逻辑桥、
构造状态和控制之间逐步涌现、收紧并收敛。

因此，本次自审的问题不是“工具是否还可以更精细”，而是：**每一项工具工作是否让固定 Q 候选的状态发生
可证伪变化？** 如果没有，它不能消耗 P-FORGE 的研究迭代并被叙述成“正在逼近 Q”。

## 2. 对现有路线的判词

现有路线有正确骨架：

- 三刀 009 已写明“锻刀与定位 ZFC Q 是同一个过程”；
- 理念图已把发现、验证和共同锻造连为一条链；
- P-FORGE 要求同一 `T/u/F/C/Q/I/O/Done`、来源、controls、Tool-BirthCard和自审；
- f51a205a 已增加 CAL、来源层和 station，防止把 fixture 或 proof layer 误升为 Q。

但此前缺少强制的 **Q 状态增量**：ForgeIntent 可以只声明修哪个字段、补哪个来源层、改变哪个 CAL 或
station，却不说明它如何影响 Q 的生成、候选空间、三刀 bridge 或同卡会合。这样会允许“工具变精细”在
实践中替代“Q 更可定位”。

本次判为：

```text
original idea      = still aligned
specification      = IDEA_SPEC_INCOMPLETE
execution risk     = TOOL_ONLY_DRIFT (EXECUTION_DEVIATION subtype)
new blade          = NO
current Q verdict  = Power Set Q-0 UNFORMED / ZFC_Q_NOT_LOCATED
```

## 3. 编译进 SOP 的 `QConvergenceLink`

每张 ForgeIntent、TaskCard／NodeCard和自然单元 SelfAudit 现在必须写：

```text
fixed candidate/card and Q state before
expected / observed Q_GENERATE, Q_NARROW, Q_BRIDGE, Q_CONVERGE or Q_REJECT
which P1/P2/P3 field, source or control causes it
why T/u/F/C/Q/I/O/Done remains the same
falsifier and Q state after
```

`Q_SAFETY_REPAIR`只适用于明确保护一张固定卡免于错误分类的修订，且须有回归。无Q状态变化、无候选
空间收紧、无同卡桥接资格、也无这种防护的工作被标为`TOOL_ONLY_DRIFT`；它可作为一般维护，但不计为
P-FORGE 研究推进。

这没有把“Q 涌现”变成自动结论。它只规定：模型产生的发现片段、来源的支付或guard、P2/P3的适用或
不适用，怎样被 Master 合成为同一候选的明确状态变化。只有`Q-4 CONVERGED`才满足原有
`ZFC_Q_LOCATED`的共同锻造判据；仍不推出 ZFC 不一致、UR 或数学定理。

## 4. 对已完成工作的回读

| 材料 | 共同涌现中的准确身份 | 不应误写成 |
|---|---|---|
| `RK-0` 的无限制形成与全子对象对照 | 校准 P 能辨认 domain promotion、negative reentry和bounded guard；收紧可接受Q的形状。 | Power Set 已有 Q。 |
| Round 1 Power Set guards | 对具体候选族的 `Q_NARROW`／`Q_REJECTED_WITH_SCOPE` 控制。 | ZFC 已被全面防住。 |
| H074/H075 `ClEx` stage reflection | 独立 reflection-proof 卡的 `Q_REJECT`：blind site经来源定理包直接支付。 | L-C语义覆盖、Power Set Q或三刀会合。 |
| f51a205a 的 CAL／来源层／station修订 | `Q_SAFETY_REPAIR`：防止把选择层、proof layer或Round stop误报为Q进展。 | 新的Q候选或P4。 |

因此，当前 Power Set 状态不能因为积累了多张 guard 而被写成“越来越接近找到”。它只能如实记为：
`ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`。下一张卡必须给出一个来源可反驳的 Q link。

## 5. C01–C10 影响扫描

| ID | 处置 | 事实 |
|---|---|---|
| C01 用户要求／Feature／ruling | `UPDATE` | 新 ruling 与 F-043 固定 P/Q 共同涌现为验收不变量。 |
| C02 共同锻造与方法设计 | `UPDATE` | 三刀 009、013与理念图说明 Q 生命周期、Q link和工具漂移边界。 |
| C03 SOP／Skill | `UPDATE` | P-FORGE、P-DAG 005、NodeCard合同和调度 Skill 2.0.0 强制Q link。 |
| C04 AGENTS／TASK_ROUTING | `NO_CHANGE` | 触发、权限、角色和暂停边界不变。 |
| C05 入口／恢复 | `UPDATE` | Feature、MEMORY/001、dev-docs README与audit index更新下一次恢复问题。 |
| C06 验证 | `UPDATE` | 运行分片、Pattern-P来源、JSON、链接和diff验证；新的worker行为验收留待未来真实节点。 |
| C07 config／permission | `NO_CHANGE` | 不改App Server、认证、网络或工具权限。 |
| C08 product adapter／runner | `NO_CHANGE` | 不改runner；Skill只增加TaskCard/SelfAudit语义。 |
| C09 Git谱系 | `UPDATE` | 本次方法修订以精确commit保存；不tag、不push。 |
| C10 历史／未知 | `UPDATE` | 004记录改道原因；当前 Q 仍未定位，未来节点须实际检验新合同。 |

## 6. 下一次恢复的首个判据

恢复原有 `P-FORGE-SOP` 时，Master 先提出的不是“下一把刀怎么磨”，而是：

> 哪一张固定候选卡会因这次工作从 `Q-0` 生成、被收紧、获得 P2/P3 bridge、被来源淘汰，或走向同卡会合？

没有答案时，停止该研究节点。若答案只是一项 infrastructure 修复，则它必须指出被保护的旧卡和回归；
否则不得用 P-FORGE 的名义继续运行。
