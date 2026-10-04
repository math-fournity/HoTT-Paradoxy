# H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP：以模式 P 先定位 Z0，再作来源和机器核验

> **身份：** `TASK_SCOPED_RESEARCH_EXECUTION_SOP / F-050 / GOAL-DRIVEN / RESEARCH_PROFILE_GOVERNED`。
>
> **稳定引用名：** `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP`。
>
> **父结果：** 从 main 的固定 HoTT `H0` 出发，定位并检验 ZFC 的理论精度／完成观察候选；不预设 `ZFC ⊢ False`，不把来源缺失写成 ZFC 缺陷。
>
> **本 SOP 的校正：** 先前 MPIM／cubical-model 追溯保留为模型链反控制；它不是 Z0 的发现入口，也不是本 SOP 的前置依赖。

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

| 槽 | 当前问题 | 下一最小判别行动 | 停止／重开 |
|---|---|---|---|
| `PF-A` | `H0` 给模式 P 提供了什么不可省去的反向样本？ | 冻结 H0→ZFC discovery card 的对象、观察和 Done。 | H0 fingerprint 改变才重开。 |
| `PF-B` | 模式 P 在不见 MPIM、模型论文、既有 ZFC 答案时，会把 ZFC 的哪个显眼基础承诺选为 Z0？ | 三把刀各做一次来源脱敏的 Terra/max discovery。 | 三刀无候选或全部仅公式／直接付款时，记录有界负结果并回审 P。 |
| `PF-C` | 哪个 surviving candidate 有实际 `C_accept`／`AdequacyLift`，值得来源与机器化？ | 只对 surviving card 查一手来源和同一任务控制。 | 该候选被直接付款、换题或变体缺口关闭时退出。 |

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

### PF-1：来源脱敏的三刀发现

对同一 deidentified ZFC profile 创建至多三张 `BLIND_CARD`，每张均用 `gpt-5.6-terra / max`、read-only、无网络、无项目读取、无递归。卡片不得给出 Power Set、MPIM、既有工作结论或候选答案。

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

## 5. 自我审计与新刀具

每轮记录：候选是否真正来自 H0+P，还是来自来源标题；三刀是否把过程／对象／Done 扭曲；是否出现旧刀容纳不了的独立判断；是否因外部文献或旧答案泄漏而污染 discovery。

新刀具只能按 `模式P三把刀/012` 的 `Tool-BirthCard` 产生。发现“现有刀没找到”只说明 `NOT_ENOUGH_EVIDENCE`，不等于 P4。

## 6. `/goal` 启动语

```text
按照 SOP=H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP，继续推进：以 main 的固定 H0 为反向样本，先运行来源脱敏的 P1/P2/P3 ZFC 模式匹配，再按 surviving candidate 的实际 C_accept、同一任务控制与相称机器化核验。MPIM／一般模型论文仅作条件性来源支线。持续执行、写回、审计并管理当前 /goal，直至所有 active lane 到达本 SOP 的有界终态；不得把候选、来源缺口或模型输出升级为 bare ZFC 矛盾。
```

## 7. 方案验收

本 SOP 建立后，第一件可验证的工作不是新建证明，而是 PF-1 的三张来源脱敏 DiscoveryCard。它们必须在不见 MPIM、AWCCRS、Power Set、既有答案和项目文件的条件下，给出可区分的 public MatchTrace。只有这样，才能检验模式 P 是否真的先于文献惯性定位 Z0。
