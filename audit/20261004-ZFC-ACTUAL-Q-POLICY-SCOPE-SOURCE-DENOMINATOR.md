# ZFC 实际 Q：完成范围政策 P 的来源分母与当前判词

> **身份：** `PRIMARY_SOURCE_SCOPE_AUDIT / ACTUAL_Q_A4_A5_REFINEMENT / ZENO_POLICY_ESTABLISHED_WITH_SCOPE / CROSS_CASE_SCOPE_UNOBSERVED`。
>
> **任务：** 不再泛问“极限是否幻觉”，而是审查实际来源是否以某个来源归属的完成范围政策，把模型／连续统的 `Done_formal` 提升为其所说原任务的 `Done_origin`；并检验该政策能否进入 C-359 的 HoTT 比较。

## 1. 当前 TaskCard

| 字段 | 当前冻结内容 | 证据状态 |
|---|---|---|
| `T` | ZFC 支撑的经典实数／连续统／极限框架，加上“它解决芝诺运动”的解释或验收层。 | `SOURCE_ESTABLISHED`，但 bare ZFC 仍不是直接被审对象。 |
| `u/F` | 实数时间、连续位置、几何级数或连续运动模型。 | `SOURCE_ESTABLISHED`。 |
| 用户圆环 `OriginDone` | 此前的 M 经指定反向过程复原；不能把另造的圆、紧化对象或静态同胚代替历史过程。 | 用户原文与 ABX 合同已给最小来源／同一对象约束，但完整 `State/input/step/observe` 仍不足，故 `USER_CIRCLE_ORIGIN_DONE_PARTIAL / USER_DONE_ADJUDICATION_REQUIRED`。 |
| Zeno `Done_strict` | 每个 action 已完成，且有限任务直觉会要求最后 action。 | 来源明确给出这一含义。 |
| Zeno `Done_revised` | 做完所有 action，不要求不存在的最后 action。 | Norton、SEP、Roberts 明示采用或讨论。 |
| `P` 的实际来源形态 | Standard Solution 有可定位的 Zeno-side completion policy；另须说明它为何对用户圆环、HoTT Q 或更一般的同类完成契约也适用。 | `SOURCE_ZENO_POLICY_ESTABLISHED_WITH_SCOPE / SOURCE_CROSS_CASE_SCOPE_UNOBSERVED`。 |
| HoTT B | 截断 Q 的 stage-one completion 不反射原 universe Q 的有限 halt。 | `C-360` 已机器证明；跨 kernel／实际任务映射未支付。 |

## 2. 版本固定来源卡

| 来源 | 它实际说了什么 | 对强 P 的判词 |
|---|---|---|
| [Norton, *Zeno’s Paradoxes of Motion*](https://sites.pitt.edu/~jdnorton/teaching/paradox/chapters/Zeno/Zeno.html) | 将有限任务的“所有动作，包括最后动作”改为无限 action 的“做完所有动作”；以每个 passing action 的分配时刻说明路线。 | `TASK_SWITCH_EXPLICIT`：它公开删去 last-action 条件，不把两个 Done 偷写成同一谓词。 |
| [SEP, *Supertasks*](https://plato.stanford.edu/entries/spacetime-supertasks/) | 明说 Zeno walk 没有 final step；一义完成指执行最后动作，另一义完成指做完每步，并明确两义在 supertask 中不等价。它把后者说成 Zeno walk 所具有的完成。 | `TASK_SWITCH_EXPLICIT / POLICY_SCOPE_LOCAL_TO_ZENO_SUPERTASK`：来源明确其语义选择，却没有把该选择扩展为用户圆环或 HoTT Q 的共同政策。 |
| [IEP, *Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/) | Standard Solution 以 calculus、连续 physical path、有限正速度和 point-events 说明 runner reaches goal；它还明确说无 final step 不妨碍 trip completion，并列出为此放弃的直觉。 | `SOURCE_ZENO_POLICY_ESTABLISHED_WITH_SCOPE / ORIGINAL_CIRCLE_BRIDGE_UNOBSERVED`：它有 source-defined runner completion，未定义用户圆环的原过程 contract，也未给 HoTT scope。 |
| [Roberts, *Philosophico-Scientific Adventures*, ch. 2](https://personal.lse.ac.uk/robert49/ebooks/philsciadventures/lecture2.html) | 直接区分“完成任务”与“完成任务的最后一步”，并说明没有逻辑要求每个完成任务都有最后一步。 | `TASK_SWITCH_EXPLICIT / PEDAGOGICAL_POLICY_ONLY`：它是明确的完成语义论证，未承担 ZFC 基础验收或 HoTT 范围。 |
| [Bathfield 2018](https://philsci-archive.pitt.edu/16355/) | 对运动／静止悖论提出独立重读，并被既有 H078 限定为解释／哲学诊断。 | `CRITICAL_BRIDGE_DIAGNOSIS / NOT_POLICY_OWNER`。 |

来源访问和段落核对时间为 2026-10-04。它们支持来源自身的完成术语，不支持用户圆环的完整 `OriginDone`、Zeno–HoTT 的同一实际 Q、或 bare ZFC 的对象语言命题。

## 3. P 的来源级重写

此前只将 P 写为隐藏的 `Done_formal → Done_origin` 容易漏掉两个不同事实：成熟来源可能公开改写 Done；它也可能在其**自身的连续 runner task**中明确判定“到达目标”。因此当前源级定义是：

```text
P_scope(T, C) =
  一个来源 C 归属的完成范围政策：
  它指定哪些 formal completion 可以被称为任务 T 的完成，
  并承担说明其是否保留、改写或排除原 Done 的责任。
```

当来源公开改为 `Done_revised`，它不是“偷偷”把严格 Done 当同一 Done；它仍可能是用户所称 P 的**弱／显式形态**。IEP 的 Standard Solution 更进一步：它在自身定义的连续 runner task 上判定到达目标。这是 `P_Zeno-source`，但其涵盖的 input、operation、observation、Done 和现实 adequacy 前提都由来源自己限定。它只有在声称这一政策同样结清用户圆环／HoTT 的时间过程任务，而没有完成桥时，才成为 C-359 所需的跨案例**强 P**。

这解释了当前证据为何不能直接进入 `ZFC-1` 判词：现有权威来源已经给出 Zeno-side policy，却仍明确完成契约分叉，缺少一个把该政策延伸到用户圆环与 HoTT Q 的 source-owned `PolicyScopeWitness`。详见 [芝诺来源完成政策卡](20261004-ZFC-ACTUAL-Q-ZENO-SOURCE-COMPLETION-CARD.md)。

## 4. 对 C-359 的形式化影响

`ActualQPolicy.lean` 现区分两条路径：

```text
严格路径：SameActualQ = TaskEquiv
  保留 State/input/step/observe/formalDone/originDone

来源路径：PolicyScopeWitness
  由来源说明为何 P 在 Zeno 侧和 HoTT 侧都适用
```

严格 `TaskEquiv` 是防止表面类比的充分控制。跨领域真实比较未必有状态空间双射；它可以由较弱但可审的 scope witness 支持。C-359 的新核心 consequence 因此是：

```text
ZFCOneUse
∧ PolicyScopeWitness(P)
∧ B
⟹ False
```

这没有降低证据门槛。它把门槛从“必须虚构 Zeno 与 HoTT 的状态同构”改为“必须找到一个实际来源能够承担的政策范围理由”。

## 5. 当前 verdict 与下一判别行动

```text
SOURCE_ZENO_POLICY_ESTABLISHED_WITH_SCOPE
SOURCE_TASK_CONTRACT_SPLIT
SOURCE_CROSS_CASE_POLICY_SCOPE_UNOBSERVED
USER_CIRCLE_ORIGIN_DONE_PARTIAL / USER_DONE_ADJUDICATION_REQUIRED
ADJACENT_TYPE_THEORY_TIME_CONTROL
NO_DIRECT_CROSS_CASE_POLICY_SOURCE_WITHIN_DECLARED_QUERY_SET
ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY = NOT_REACHED
```

下一项不再是搜集更多“calculus solves Zeno”的泛化网页。它必须二选一：

1. 找到一个版本固定、理论级的来源，明确把 ZFC-supported completion policy 扩张到用户所要求的原过程 Done 或固定 HoTT completion contract；或
2. 用覆盖清楚的来源分母表明这类扩张没有发生，把当前路线收束为“标准来源有局部 Zeno policy，但未形成可归因的 ZFC—圆环—HoTT 统一政策”。本轮四组 direct cross-case query 已得到有界 `NO_DIRECT_CROSS_CASE_POLICY_SOURCE_WITHIN_DECLARED_QUERY_SET`；邻接的 cubical hybrid-semantics 来源是时间维度控制，不是 scope 支付。

无论结果是哪一个，C-359 的条件 theorem、C-360 的 HoTT 控制、C-361 的极限／端点控制仍保留；它们不会因 source verdict 改变而被误报为 bare ZFC 矛盾。
