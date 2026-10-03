# HMZ-006：预检覆盖与配对要求

## 覆盖

| 项 | 状态 |
|---|---|
| 原始作者 PDF | `ARCHIVED_AND_HASHED` |
| 全 9 张 slide | `READ` |
| ZFC／Coq／unnatural／universe／computation 关键词定位 | `COMPLETE_FOR_THIS_SOURCE` |
| 具名 ZFC-in-Coq 实现、其代码或论文 | `NOT_NAMED_BY_SOURCE` |
| 同一任务的 ZFC consumer 与 I/O/Done | `NOT_SUPPLIED` |

本预检的完成不是文献分母完成；它只完整处理了一个九页作者来源，初始处置为 `PAIRING_SOURCE_REQUIRED`。HMZ-007 后来满足了项目内的可比配对，但没有解决 Voevodsky 原话的历史指称。

## 配对来源与尚未解决的历史指称

HMZ-007 已以 Werner 1997 与 `rocq-archive/zfc` 提供一个可审计的 **comparable** ZFC-in-CIC pairing，并完整固定了
`u/F/C/I/O/Done`、Choice payment 和 Russell/Power controls。WoLLIC 没有点名 Werner，因此这满足项目的分析配对，
却不满足“作者所指对象已被历史确认”的更强命题。

下列条件只在要主张这种**历史指称**时才需要：

1. 一个能精确识别 Voevodsky 所说 ZFC-based proof-assistant formalization 的项目／论文／代码库；
2. 该来源中的 ZFC variant、encoding、对象 `u`、formation `F` 和真实 consumer `C`；
3. 同一 I/O/Done：何谓“自然”或“不自然”的可检验任务，不能只保留修辞；
4. 该实现是否显式支付 representation、universe、choice、axiom、proof search 或 software-engineering 成本；
5. 一条可将作者话语与具体项目连起来的历史证据，而非只凭日期、主题或作者网络推断。

任何只重复“ZFC 曾导致不自然构造”而仍不给这些来源，不能改变 HMZ-007 对 payment／guard 的范围判词。
