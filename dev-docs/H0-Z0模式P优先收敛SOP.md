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

### PF-2：Master 交叉收敛

Master 不以投票决定候选。对每个输出应用：

1. **明显性筛选：** 是否是 ZFC 的核心基础承诺，而非专门技术或外部算法？
2. **H0 对位：** 是否保住“过程完成／有限交付”而不是只共享“无限”一词？
3. **同一任务卡：** 对象、输入、操作、观察、Done 是否可固定？
4. **P1/P2/P3 容纳：** 是旧刀字段缺口、三刀派生结构，还是出现真正的未容纳花纹？
5. **反控制：** 是否可被有限／有界、显式 guard、直接付款或正常 false 分支解除？

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

### 6.1 方案—闭包绑定

本方案唯一配套的当前认知闭包是
[`H0-Z0-PATTERN-FIRST-CONVERGENCE-CLOSURE`](../认知闭包/2026-10-04-H0-Z0模式P优先收敛-认知闭包.md)。
每次 Host Goal 启动、压缩恢复、主要阶段转换或任何用户修正后，先重读该闭包，再重读本方案的 PF-0～PF-5 与当前 F-050／MEMORY。闭包记录当前证据、并行工作树、未知与 Goal 身份；本方案拥有阶段、验收与停止合同。二者不可互相替代。

```text
按照 SOP=H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP、认知闭包=H0-Z0-PATTERN-FIRST-CONVERGENCE-CLOSURE，继续推进：以 main 的固定 H0 为反向样本，先运行来源脱敏的 P1/P2/P3 ZFC 模式匹配，再按 surviving candidate 的实际 C_accept、同一任务控制与相称机器化核验。MPIM／一般模型论文仅作条件性来源支线。持续执行、写回、审计并管理当前 /goal，直至所有 active lane 到达本 SOP 的有界终态；不得把候选、来源缺口或模型输出升级为 bare ZFC 矛盾。
```

## 7. 方案验收

本 SOP 建立后，第一件可验证的工作不是新建证明，而是 PF-1 的三张来源脱敏 DiscoveryCard。它们必须在不见 MPIM、AWCCRS、Power Set、既有答案和项目文件的条件下，给出可区分的 public MatchTrace。只有这样，才能检验模式 P 是否真的先于文献惯性定位 Z0。
