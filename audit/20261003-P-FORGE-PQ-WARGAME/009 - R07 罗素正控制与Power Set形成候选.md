<!-- governance-shard:v2
logical_id: P_FORGE_PQ_WARGAME_AUDIT
shard_id: 009
index: ../20261003-P-FORGE-PQ-WARGAME.md
-->

# R07 罗素正控制与Power Set形成候选

> **状态：** `COMPLETE / RK-0_CAPABILITY_CALIBRATION_RETAINED / Q_NARROW_WITHOUT_Q1 / NO_NEW_METHOD_REPAIR`。

## 1. 轮次身份与起始状态

**时间与证据宇宙。** 本轮只消费 H049--H053 已封存收据：
[`P-DAG RK-0 049–053`](<../20261003-P-DAG-RK0-RUSSELL-POWERSET-049-053-Terra-Max.md>)、
[`P1 formation-origin 自审`](<../20261003-P-DAG-P1-FORMATION-ORIGIN-LANE-SELF-AUDIT.md>)，以及
[`RK-0 共享内核`](<../../dev-docs/模式P三把刀/011 - 罗素最后一跃共享内核.md>)。R06 已要求不从
外部程序补写理论层字段；R07 因而只问来源实际给出的 formation、bridge、guard 与未给出的过程语义。

```text
Target-Q     = Power Set／明确的ZFC变体中，已声明 formation 是否留下一个未被直接支付的
               完成、资格或同一对象上升追问。
Candidate-Q  = NONE at start.
Control-Q    = H050 的脱敏无限制形成正控制；H051 的bare all-subsets profile；
               H052 proof-layer boundary；H053 rank/Foundation guards.
Starting state = ZFC_SITE_SELECTED / Power Set Q-0 UNFORMED.
```

R05留下的具体问题是 `WQ-0005`：恢复 F-lane 后，Power Set 的核心 formation 是否真的能先生成一个
`Q-1 / FORMATION_ORIGIN_PROBE`，随后才谈 P2/P3 或 consumer 的后继核验？

## 2. 实际重放：正控制、formation profile与来源 guard

| 节点 | 实际来源或profile | P/Q作用 |
|---|---|---|
| H049 | 不出现“Power Set”名称的 F-lane profile：给定对象 `a`，形成其全部子对象 `u`。 | F-lane 没有被 consumer-only prompt 再次删掉；但 `u/F` 已直接给出，模型返回 `NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY`。 |
| H050 | 单一 `D` 上任意条件 formation、formation 后立即 promotion、同一对象可再代入。 | 盲态重新识别 `S={x∈D | x∉x}`、same-object reentry与negative bridge；`Update/Done`仍是 `UNKNOWN`。这是 RK-0 的能力正控制，不是 ZFC Candidate-Q。 |
| H051 | 给定 `a` 的 `F(a)=u`，以 `x∈u ↔ x⊆a` 为正向 bridge，`u`可再作输入。 | 没有全域 `D`、任意predicate binder、同域负桥或未支付上升债务；重入为“下一层输入”而非同一 bridge/domain 自代，仍为 `DIRECT_PAYMENT_ONLY`。 |
| H052 | Metamath `ax-pow/pwex`：全子集形成和proof-system接受。 | 固定了 proof/axiom packet 的范围；没有对象层consumer、runtime admission、I/O/Done或negative bridge。 |
| H053 | Metamath `rankpw` 与 `ax-reg`：Power Set rank successor及Foundation排除自成员。 | 是来源报告的对象层guard；successor notation不是P3 lifecycle，Foundation也不补P2 reentry或consumer。 |

这组对照让“罗素模式匹配”变成可反驳的判别，而不是听到“全部子集”就宣布同形：H050说明 P 能在
无限制 formation 中看见 `Bind → Form/Promote → Bridge → Reenter → negative`；H051 说明当输入、bridge
与 polarity 实际改变时，P 不能用同一故事填补缺口。

## 3. 实际 Q 增量与双通道裁定

```text
H050 = Q_CAPABILITY_CALIBRATION on the RK-0 logical kernel.
       Candidate-Q belongs to the deidentified positive control, not to Power Set.
H049/H051/H052/H053 = Q_NARROW for the Power Set candidate space.
Power Set Candidate-Q = NONE throughout this evidence universe.
Power Set state after R07 = Q-0 UNFORMED.
```

`F_LANE` 的结论尤为关键：R05 的修复使 H049/H051 得以公平进入 formation-origin 检查，因而“没有候选”
不再是 consumer-only prompt 的产物；但 F-lane 的低门不是自动生成 Q 的门。它仍要求一个不由 formation
立即支付、且能指向后续 P2/P3／consumer 核验的完成、资格、self-ascent追问。H049/H051没有提供这项追问。

`C_LANE`也未进入：H052是 proof-system Done，H053是规则／guard来源；二者都没有给出同层实际 consumer 的
正向义务。P2/P3的空缺在本轮应保留为 `NOT_SUPPLIED_AT_TESTED_SCOPE`，不能由 rank 的 successor 或
Foundation 的反身禁止偷换成构造阶段语义。

## 4. 兵棋推演：今天的规则会如何约束当时的选择

在当前 `QConvergenceLink` 下，R07 会先冻结两张不同的卡，而不让 H050 的成功感染 Power Set：

```text
RK-0 control card:
  Target-Q = validate the shared logical kernel
  Candidate-Q = deidentified unrestricted-formation negative reentry
  Activation lane = NONE / capability control
  effect = Q_CAPABILITY_CALIBRATION

Power Set source/profile card:
  Target-Q = F-lane formation-origin question about P(a)
  Candidate-Q = NONE
  Activation lane = F_LANE attempted, not entered
  effect = Q_NARROW
  stop = no negative/ascending bridge, unpaid completion trace, or downstream source exists
```

这避免两种相反错误：一是把 H050 的正控制写成“已在ZFC找到Q”；二是把 H051 的无候选写成“F-lane不成立”。
今天的规则会保留H050作为 P 的发现能力校准，也会保留H049/H051作为对 Power Set 具体候选空间的有界收紧。

## 5. 判词、财富和下一依赖

```text
P/Q共同锻造判词 = ALIGNED_CALIBRATION_AND_CANDIDATE_SPACE_NARROWING
IDEA_SPEC_INCOMPLETE = NO（R05的F-lane修复已被正确消费）
TOOL_ONLY_DRIFT = NO（RK-0校准和H051反控制都服务于固定Power Set候选空间）
new blade / new method repair = NO
ZFC_Q_LOCATED = NO
```

| ID | 本轮留下的方向 | 身份 | 反证／升级条件 |
|---|---|---|---|
| `WQ-0005` | F-lane 只有在某个版本固定来源提供“formation 输出已给出以后仍未付”的 completion／qualification／self-ascent追问时，才会形成可继续的`Q-1`；bare all-subsets本身没有做到。 | `HYPOTHESIS`，尚未激活为Candidate-Q | 若一个严格同层来源显示`P(a)`的形成义务已由定义／guard直接清偿，或来源级P2/P3／consumer证明该追问换题，则拒绝该具体卡。 |
| `WQ-0007` | 为Power Set搜寻F-lane时，优先找保留 RK-0 的同一对象bridge并额外明示negative/ascending dependency或未付Done；不能把rank公式、Foundation或下一层输入当作替代。 | `HYPOTHESIS` | 若一个合法F-lane card在没有这些关系时仍通过同一任务来源核验，应修订这条筛选方向。 |

R08将审忒修斯／历史身份 Tool-Birth。它不应因为Power Set裸 formation暂未生成Q而被当作“随便换题”；它要测试的是
一个不同花纹是否给同一对象卡增加了来源支持的 provenance-sensitive Done，或只是另一个表示层故事。R07留下的
硬边界仍有效：新的花纹必须在同一任务上产生实际义务，不能借RK-0或外部直觉填字段。
