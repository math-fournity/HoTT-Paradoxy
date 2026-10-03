<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_LEDGER
shard_id: 002
index: ../20261003-P-FORGE-ATOMIC-LEDGER.md
-->

# 非H候选执行族与run去重待办

## 1. 为什么先登记“执行族”而不急于计数

早期 P-FORGE 记录没有统一使用 H 编号。一个报告可能对应一个外部 CLI session、两个 blind prompts、
多个 source-mapper、三方 Battle，或只是一张未采样 NodeCard。为避免把“Markdown 文件数”伪装成执行数，
本片先登记候选执行族；每行都要在下一阶段回到 run/session/thread/turn identity 后，才可拆成最终原子ID。

`H001--H075`已在001片登记；本片的行不与H编号混计。`PENDING_RUN_DEDUP`不是负结论，也不表示该报告
缺少价值，只表示它尚不能贡献精确总数。

## 2. 已识别的 non-H 候选执行族

| 候选族 | 最小来源报告 | 初步身份 | 去重／拆分任务 |
|---|---|---|---|
| N01 P2逻辑翻译探针 | `20261002-P2-计算逻辑翻译探针-Terra-Max.md` | external calibration | 提取独立session与terminal。 |
| N02 朴素集合论脱敏正控制 | `20261002-模式P-朴素集合论脱敏正控制-Terra-Max.md` | deidentified control | 核对是否单一session及与H050不同。 |
| N03 HoTT无泄漏第一次负控制 | `20261002-模式P-HoTT无泄漏盲重放-Terra-Max.md` | blind negative control | 核对session，排除与H001--H010重叠。 |
| N04/N05 ZFC一遍匹配双prompt | `20261002-模式P一遍匹配ZFC盲测-Terra-Max.md` | two prompt-bounded probes | 分开两个prompt的session／terminal identity。 |
| N06--N09 初始三刀外部fixture | `P2-FORGE-001`、`P3-FORGE-001`、`P1-FORGE-001`、`P3-CIRCLE-001` | four named external CLI sessions | 每份报告核一个还是多个terminal。 |
| N10/N11 中性HoTT P2/P3 | `P2-HOTT-001`、`P3-HOTT-001` | external theory controls | 核session，排除与H卡重跑。 |
| N12/N13 中性ZFC P2/P3 | `P2-ZFC-001`、`P3-ZFC-001` | external theory controls | 核session，排除与COFORGE重叠。 |
| N14/N15 CFTT P2/P3 | `P2-CFTT-001`、`P3-CFTT-001` | source controls | 核session及共同source是否不同运行。 |
| N16 Climber P2 | `P2-CLIMBER-001` | source control | 核single session。 |
| N17--N19 Delay P1/P2/P3 | `P1-DELAY-001`、`P2-DELAY-001`、`P3-DELAY-001` | three source-control sessions | 各自核session，不能按同一source合并。 |
| N20--N23 ZFC-COFORGE | `ZFC-COFORGE-001/003/004/005` | early Power Set calibration | 核每个版本、缺失002及各自session。 |
| N24 Battle-001 | `20261002-P-DAG-BATTLE-001-Terra-Max.md` | source-isolated advocates plus arbiter | 拆出每个立场和arbiter terminal。 |
| N25 SOURCE-001 | `20261002-P-DAG-SOURCE-001-Terra-Max.md` | source consumer / P2 / P3 relay | 抽取每个实际source-mapper terminal。 |
| N26 SOURCE-002 + BATTLE-002 | `20261002-P-DAG-SOURCE-002-与-BATTLE-002-Terra-Max.md` | proof-layer/source/Battle family | 拆source nodes与arbiter，去重同卡重述。 |
| N27 SOURCE-003 | `20261002-P-DAG-SOURCE-003-TIMEOUT-Terra-Max.md` | three cancelled web nodes | 逐一登记无terminal节点。 |
| N28 SOURCE-004 | `20261002-P-DAG-SOURCE-004-NODECARD.md` | pre-sampling connection failure | 作为失败执行单元保留。 |
| N29 SOURCE-005 | `20261002-P-DAG-SOURCE-005-Isabelle-ZF-Cantor-Master.md` | Master direct-source control | 标记无worker／有Master动作。 |
| N30 runner／isolation／qualification | `P-DAG-RUNNER-HEALTH-001`、`RUNNER-ISOLATION-002`、`CODEX-APPSERVER-ISOLATION-003/004/005`、`AppServer-资格检查` | execution-envelope controls | 逐项确认是否采样、是否影响候选卡、是否已经由H007--H010覆盖。 |

## 3. 下阶段的可证伪完成条件

non-H ledger 只有在每个候选族都被裁定为以下之一后，才可合并进总分母：

```text
UNIQUE_ATOMIC_RUNS(n, exact identities)
DUPLICATE_OF(Hxxx or Nxxx, exact reason)
NO_MODEL_SAMPLING_BUT_EXECUTION_UNIT
OUT_OF_SCOPE_WITH_REASON
```

届时才能计算 `H75 + non-H unique runs = exact atomic denominator`。在那之前，R15的`>=85`只是不应再被降低的
下界，不是完成分母。
