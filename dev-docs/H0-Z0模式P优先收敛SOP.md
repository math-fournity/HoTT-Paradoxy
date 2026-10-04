# H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP：以模式 P 先定位 Z0，再作来源和机器核验

> **身份：** `TASK_SCOPED_RESEARCH_EXECUTION_SOP / F-050 / GOAL-DRIVEN / RESEARCH_PROFILE_GOVERNED`。
>
> **稳定引用名：** `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP`。
>
> **父结果：** 从 main 的固定 HoTT `H0` 出发，定位并检验 ZFC 的理论精度／完成观察候选；不预设 `ZFC ⊢ False`，不把来源缺失写成 ZFC 缺陷。
>
> **本 SOP 的校正：** 先前 MPIM／cubical-model 追溯保留为模型链反控制；它不是 Z0 的发现入口，也不是本 SOP 的前置依赖。
>
> **当前阶段：** `H0_Z0_PATTERN_FIRST_PASS_001_COMPLETE_WITH_SCOPE`。本轮所有候选已到达有界状态；没有 active `Z0_CANDIDATE`。后续只能由第 4 节所列重开条件启动，不能把“继续推进”误读成继续漫游式地产生无穷对象或模型论文候选。

## 1. 目标与四层证据纪律

### 1.1 固定的 H0

`H0` 是 main 已保存的固定 Cubical Agda `QuestioningDelay`：对 `Type ℓ-zero`，逐层询问相同是否在某有限 h-level 落定；在精确的 Cubical Agda 2.8.0 + cubical 0.9、Eilenberg–MacLane HIT、`Delay`／finite-fuel 语义中，内核接受：对每一个 `Judge`，问题等于 `never`，并无有限 halt witness。它是固定形式系统中一个带正控制的程序性质。

`H0` 的 UR／现实读法仍是研究发起人的解释与桥接问题；本 SOP 不把它改写成 HoTT 内部不一致。

### 1.2 要发现的 Z0

`Z0` 不是“集合论里另一个无限过程”。它是 ZFC 的显眼基础承诺中，一个可能把总体、形成、可用性或完成一次性交付给后续理论使用的具体位置。候选必须能写出：

```text
T_ZFC / u / F / original task / operation / observation / Done
H0 relation / P1-P3 trace / local counterfactual
```

发现态的 `Z0_CANDIDATE` 不是 ZFC 问题的定论。它只说明模式 P 发现了值得进入来源与反控制检验的理论位置。

### 1.3 Q 与 P 的身份

`Q` 是该理论位置面对的、关于形成、可用性或时间化完成的具体追问。`P` 是把尚未支付的过程条件改写成可立即使用／已经完成的跃迁候选。只有出现真实 `C_accept` 或同一理论内的实际消费者、正义务和同一任务映射，才可把 `Q` 从发现态升级为来源级候选。

### 1.4 四层分开

| 层 | 允许结论 | 不允许结论 |
|---|---|---|
| 内在知识／模式匹配 | 候选位置、机制假设、TaskCard 草案 | 某论文、共同体或 ZFC 已经作出某验收判词 |
| 固定 H0 机器证据 | 固定 Cubical 程序的 `never`／halt 性质 | 实际现实过程或 ZFC 的结论 |
| 来源合同 | 某精确来源、版本、理论变体和消费者的实际承诺 | 未被该来源支付的跨层提升 |
| 机器化 | 明确规格下的形式命题 | 规格之外的哲学、历史或现实结论 |

## 2. 研究图与活跃前沿

本任务采用 `RESEARCH_PROFILE_GOVERNED`：它跨 Session、来源与形式化阶段，且任一候选都可能改变父结果。当前只有三个活跃槽，防止把模型论文、工具锻打与候选发现混成并行主线。

| 槽 | 当前状态 | 已完成的最小判别行动 | 停止／重开 |
|---|---|---|---|
| `PF-A` | `H0` 已固定；H096–H100 已将外部模型／consumer 支线收为来源控制。 | 固定 H0 的 subject、step、有限观察与 Done，并记录 exact H0 transport／consumer 的来源缺口。 | 只有 H0 fingerprint 改变、实际 H0 consumer 或 exact semantic transport 才重开。 |
| `PF-B` | 匿名 Power Set 只重定位 formation site；命名 ZFC 的 P1 选出 `ω`；二者均未产生同一卡 P2/P3 会合。 | 先用 PF-B2 检查 process-anchor，再完成匿名、命名理论和 A/B 对位的来源脱敏 P1/P2/P3。 | 已完成为有界控制；只接受新的 A/B bridge card 或真实过程来源作为重开。 |
| `PF-C` | 没有 surviving `Z0_CANDIDATE`。 | 对 `ω` 固定 Metamath 的静态 totality 范围，并拒绝 limit-union 的未支付 A/B bridge。 | 只有新卡先通过 A/B 门，才查候选特异的 `C_accept`／`AdequacyLift`。 |

`MPIM`、Chain-A、AWCCRS 目前属于 `PARKED_SOURCE_CONTROL`：只有 PF-C 的具体来源引用它们，或它们成为 exact `H0Map` 的最小证据路径时，才重新激活。

### 2.1 A/B 同一政策门：任何 Z0 候选的前置资格

本 SOP 的靶不是“ZFC 中有无穷总体”这一单独现象。所有候选都必须服从下列固定角色：

| 符号 | 固定角色 | 禁止替换 |
|---|---|---|
| **A** | 芝诺／圆环线中，被数学共同体接受的完成性结果：连续统／极限或其修订完成合同使原来无最后一步的过程被判为“已解决”。 | 不能把 A 缩成一个几何级数等式、任意无穷对象或普通有限近似。 |
| **B** | main 的 fixed `H0`：Cubical Agda `QuestioningDelay` 在 `Type ℓ-zero` 对任意 `Judge` 为 `never`，没有有限 halt witness。 | 不能把 B 换成泛泛的高阶结构、任何不终止程序或某篇模型论文。 |
| **Q** | 基础验收对于 formal completion 与原过程／有限完成之间是否必须审查、保持或支付 bridge 的观察责任。 | 不能由研究者自定义布尔值取代真实来源政策。 |
| **P** | 未支付的完成／adequacy promotion：把一种形式对象、极限、模型或静态总体提升为原任务的已完成。 | 不能把任意存在公理或公理接受本身自动称为 P。 |
| **Z0** | ZFC 的核心承诺或实际基础验收接口，只有同时有 AProjection、BProjection 与 SameQBridge 的候选才成为真正 Z0。 | 不能把单独的 ω、Power Set、模型或语义论文提升为 Z0。 |

因此，任何只呈现“无限阶段 + 静态总体”的对象都标为：

```text
P_CANDIDATE_NOT_YET_A_B_BRIDGE
```

它可保留为 P 的候选材料，却不能消耗主线、进入 ZFC Q 结论或机器化。此前 `ω` 卡正处于这一状态。

## 3. 执行阶段

### PF-0：重置入口与反漂移检查

1. 重新读 H0 fingerprint、核心认知中 KC-000056–062、刀具系统理念与当前 F-050。
2. 明确写出本轮的禁止替换：不以 MPIM、generic cubical model、ZFC 可编码程序、既有 Power Set guard 或 C-364 取代 Z0 的发现。
3. 冻结 DiscoveryCard，给出 `H0`, `T_ZFC`, `candidate class`, `original task`, `Done`, source visibility 和正负控制。

### PF-B2：过程锚点再审

若一张发现卡只给出 `a → F(a) → F(F(a))` 一类 formation ascent，而 P2/P3 都因没有同一过程、再入或 lifecycle 停止，Master 必须先把它归为**画像不足**，不能把空结果读成 ZFC 已有防线。这个 `Q_SAFETY_REPAIR` 固定 H0 的六个过程锚：

```text
subject u / native operation F / local step-or-observation /
process-wide Q / finite Done / finite-or-bounded positive control
```

后续 profile 必须能用理论原生材料填写这些字段；不能把静态 totality、外加时间叙事、未声明 checker 或 prospective equality 偷塞为过程。P1 先选或拒绝一张冻结父卡；只有该父卡存在，P2/P3 才能对**同一张卡**接力。完整来由见[PF-B2 过程锚点再审](../audit/20261004-H0-Z0-PATTERN-FIRST-PF-B2-过程锚点再审.md)。

### PF-1：来源脱敏的三刀发现

对同一 deidentified ZFC profile 创建至多三张 `BLIND_CARD`，每张均用 `gpt-5.6-terra / max`、read-only、无网络、无项目读取、无递归。卡片不得给出 Power Set、MPIM、既有工作结论或候选答案。P1 必须先建立或拒绝父卡；P2/P3 不得重选对象或补造 `C/I/O/Done`。

| 刀 | 发现职责 | 合格输出 |
|---|---|---|
| P1 | 从 ZFC 的原生形成／总体承诺中，选一个理论不能绕开的主对象和 prospective completion question。 | `MODEL_RECALL_SITE_CANDIDATE` 或受界无候选；不得把公理名直接当 Q。 |
| P2 | 从计算—存在—自指的逻辑翻译检查同一候选是否有真实再入、极性或 guard 张力。 | 可迁移关系和反控制；不得把“自指”这个词当命中。 |
| P3 | 从过程、准入、使用与 Done 的次序检查同一候选是否有理论原生的 lifecycle／admission 问题。 | 明确 `Draft/Need/Use/Done`，或 `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`。 |

每张 NodeCard 必须冻结 `T/u/F/C/Q/I/O/Done`、`QConvergenceLink`、source visibility、停止条件和禁止外推。每次 terminal run 必须做 trajectory receipt；单次模型输出只创建候选，不裁定理论。

### PF-1B：命名理论、答案脱敏的直接模式匹配

PF-1 的匿名轮廓控制“描述是否偷偷把答案塞进模型”。它不能替代研究发起人要求的另一件事：让模型直接调用自己关于 **ZFC** 的既有数学知识。完成至少一张 PF-1 匿名控制卡之后，允许一张 `BLIND_CARD` 只显示理论名 `ZFC` 与 H0 的抽象完成结构，而仍禁止项目答案、来源、Power Set、模型论文和历史候选。

PF-1B 的任务是：由 ZFC 的核心承诺中独立选出至多两个显眼站位，并写出为何它们可能承载 H0 同形的完成问题。它不是文献来源，不能声称该站位已是 ZFC Q；其价值是检验模式 P 加已有数学知识能否一次定位，而不是让匿名轮廓的贫乏替模型作出选择。若 PF-1B 只重选已知 Power Set，必须回到现有 guard ledger；若它选出新站位，才进入 PF-2。

### PF-1C：A/B 对位、答案脱敏的桥接发现

PF-1B 的单端 H0 匹配不足。PF-1C 必须在不见项目答案、既有 ZFC candidate、MPIM、模型论文和来源结论的条件下，同时给出 A 的抽象完成形状与 B 的抽象有限证书失败形状，并且只命名理论 `ZFC`。它要求 P1 从 ZFC 的显眼核心承诺中选择一个**可能解释同一完成 promotion 的桥接接口**。

PF-1C 的最小输出必须列：`AProjection`、`BProjection`、`SameQBridge`、`P` 的可能位置、一个反控制和后续来源义务。若任何一项缺失，terminal 只能是候选不足；不得因为选中了 ω 或任何无穷对象而放行。

### PF-2：Master 交叉收敛

Master 不以投票决定候选。对每个输出应用：

1. **明显性筛选：** 是否是 ZFC 的核心基础承诺，而非专门技术或外部算法？
2. **H0 对位：** 是否保住“过程完成／有限交付”而不是只共享“无限”一词？
3. **同一任务卡：** 对象、输入、操作、观察、Done 是否可固定？
4. **P1/P2/P3 容纳：** 是旧刀字段缺口、三刀派生结构，还是出现真正的未容纳花纹？
5. **反控制：** 是否可被有限／有界、显式 guard、直接付款或正常 false 分支解除？

6. **A/B 同一政策：** 候选是否真正提供 AProjection、BProjection 和 SameQBridge？若仅有 P 的单端形状，登记 `P_CANDIDATE_NOT_YET_A_B_BRIDGE` 并回到 PF-1C。

最多保留两张 `Z0_CANDIDATE`；其它记录为 `REJECTED_WITH_SCOPE`。只有出现字段冲突才启动一次有界 Battle。

### PF-3：候选特异来源核验

每张 surviving card 只查最小的一手分母：精确 ZFC 或扩展、实际 consumer、输入、输出、Done、明示 payment 和同一任务映射。问题是：

```text
该来源是否真正要求/使用该 candidate？
它是否把 FormalDone 升为 OriginDone 或 foundation adequacy？
它是否已对 Q 付款，或保留一个未支付的正义务？
```

模型论文只在其为该来源的明确依赖时读取。没有 `C_accept` 时，结束为 `SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE`，不以继续搜论文取代发现。

### PF-4：形式化与机器核验

只在 PF-3 得到版本固定的 source contract 或保真 H0Map 后，才创建 proof package。形式命题必须来自来源所声明的 I/O/Done，至少包含一个正控制和一个类型／反例控制。已有 C-357、C-358、C-364 仅可作为控制库。

### PF-5：收敛、写回与下一轮

每个自然单元更新：TaskCard、QConvergenceLink、SelfAuditCard、F-050／MEMORY／方向 owner、底层 evidence。一次单元必须回答：

```text
本轮让 Q 生成、收紧、桥接、拒绝还是保持未定？
H0 是否仍是实际 B，而非一个装饰性类比？
MPIM／模型线是否被错误抬回主线？
```

若所有 active candidate 都到达有界终态，执行一次 H0→Z0 总裁决：列出候选、来源支付、未支付缺口、可机器化项和重开条件。只有父目标实际完成时才将 Host goal 标为 complete。

## 4. 结果状态与停止规则

| 状态 | 含义 | 后续 |
|---|---|---|
| `P_MATCH_NO_SITE_WITH_SCOPE` | 固定 P 和固定 ZFC profile 未产生合格显眼站位。 | 回审 P 的表达，不能以扩展文献替代。 |
| `Z0_CANDIDATE` | 三刀或 Master 收敛出可审站位。 | 进入 PF-3。 |
| `SOURCE_DIRECT_PAYMENT_CONTROL` | 来源已明示支付同一 Q。 | 该候选退出，保留防御。 |
| `SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE` | 没有真实 consumer／adequacy contract。 | 结束该来源支线。 |
| `H0_Q_PRESERVED_WITH_SCOPE` | 保真映射明确保存 relevant H0 observation。 | 该映射是防御。 |
| `H0_Z0_UNPAID_ADEQUACY_LIFT_CANDIDATE` | 同一来源有 H0Map 和 adequacy lift，却未支付 observation。 | 进入 PF-4。 |
| `H0_Z0_ACTUAL_POLICY_CONFLICT_WITH_SCOPE` | A/B/Q/P 的实际同一政策已逐字段固定。 | 允许对相应条件命题机器化；仍不称 bare ZFC 矛盾。 |
| `P_CANDIDATE_NOT_YET_A_B_BRIDGE` | 理论对象只提供静态总体、formation 或单端 P 形状。 | 保留为候选材料；不进入 PF-C 或机器化。 |
| `A_B_BRIDGE_CANDIDATE_REJECTED_WITH_SCOPE` | P1 提出桥接接口，但 P2/P3或来源未支付 AProjection、BProjection 或 SameQBridge。 | 关闭该卡；不以相同词汇重新打开。 |
| `ACTUAL_Z0_NOT_LOCATED` | 当前所有活跃卡均已受界处置，仍无同时支付三项 A/B 门的接口。 | 结束本轮；只按显式重开条件继续。 |

### 4.1 本轮冻结判词

`Convergence 001` 的最终状态为：

```text
POWERSET = RELOCATED_SITE / Q_UNSET
OMEGA = STATIC_TOTALITY_P_CANDIDATE / NOT_YET_A_B_BRIDGE
META_SEMANTIC_ADEQUACY = NO_CONCRETE_CONSUMER
LIMIT_UNION = A_B_BRIDGE_CANDIDATE_REJECTED
ACTUAL_Z0 = NOT_LOCATED
ACTUAL_SAME_Q_BRIDGE = NOT_LOCATED
```

这张表保存下一步的边界，不提供“ZFC 无问题”的结论。其逐节点、来源与 trajectory 范围由[Convergence 001 Master 报告](../audit/20261004-H0-Z0-PATTERN-FIRST-CONVERGENCE-001-Master.md)拥有。

## 5. 自我审计与新刀具

每轮记录：候选是否真正来自 H0+P，还是来自来源标题；三刀是否把过程／对象／Done 扭曲；是否出现旧刀容纳不了的独立判断；是否因外部文献或旧答案泄漏而污染 discovery。

新刀具只能按 `模式P三把刀/012` 的 `Tool-BirthCard` 产生。发现“现有刀没找到”只说明 `NOT_ENOUGH_EVIDENCE`，不等于 P4。

## 6. `/goal` 启动语

本方案的当前认知闭包是[H0→Z0 模式 P 优先收敛：可审计认知闭包](../认知闭包/2026-10-04-H0-Z0模式P优先收敛-认知闭包.md)。每次 Host Goal 启动、压缩恢复、主要阶段转换或用户修正后，先重读该闭包、本 SOP 的 PF-0～PF-5、当前 F-050／MEMORY 与 `Convergence 001`。闭包记录本轮证据、冲突与当前前沿；本 SOP 拥有阶段、验收与停止合同。

```text
按照 SOP=H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP、认知闭包=CC-20261004-h0-z0-pattern-first-convergence，先核验是否出现第4节允许的重开证据。若没有，确认本轮已达有界终态并结束当前 Goal；若有，才以 main 的固定 H0 为反向样本运行相应的 P1/P2/P3、来源合同或机器化阶段。MPIM／一般模型论文仅作条件性来源支线。不得把候选、来源缺口或模型输出升级为 bare ZFC 矛盾。
```

## 7. 方案验收

本 SOP 的首轮验收已经完成：匿名 formation、命名 ZFC、ω 来源、泛语义和 A/B 对位五类卡均有 public MatchTrace 与 trajectory receipt。下一次验收只在重开时发生，并必须证明它既没有把答案塞进 profile，也没有把 A、B 或 SameQBridge 替换成一般无穷叙事。
