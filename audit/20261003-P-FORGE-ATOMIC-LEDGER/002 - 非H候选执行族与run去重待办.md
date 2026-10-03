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

目前已从下表 N06--N23 提取出 18 个彼此不同的 session ID，并与 H 报告中可提取的身份交叉检查为无交集，
故它们可以作为原子总分母的已确认 non-H 运行。N01--N05及N24之后仍须继续拆分。

## 2. 已识别的 non-H 候选执行族

| 候选族 | 最小来源报告 | 初步身份 | 去重／拆分任务 |
|---|---|---|---|
| N01 P2逻辑翻译探针 | `20261002-P2-计算逻辑翻译探针-Terra-Max.md` | external calibration | 提取独立session与terminal。 |
| N02 朴素集合论脱敏正控制 | `20261002-模式P-朴素集合论脱敏正控制-Terra-Max.md` | deidentified control | 核对是否单一session及与H050不同。 |
| N03 HoTT无泄漏第一次负控制 | `20261002-模式P-HoTT无泄漏盲重放-Terra-Max.md` | blind negative control | 核对session，排除与H001--H010重叠。 |
| N04/N05 ZFC一遍匹配双prompt | `20261002-模式P一遍匹配ZFC盲测-Terra-Max.md` | two prompt-bounded probes | 分开两个prompt的session／terminal identity。 |
| N06 P2-FORGE | `P2-FORGE-001` | unique session `01a0fca3-9498-71f0-b8d6-255b9a65648b` | `UNIQUE_ATOMIC_RUN` |
| N07 P3-FORGE | `P3-FORGE-001` | unique session `01a0fca5-f826-7cd0-9731-09428db42c6d` | `UNIQUE_ATOMIC_RUN` |
| N08 P1-FORGE | `P1-FORGE-001` | unique session `01a0fca9-2ca7-76b2-b5fc-14812da9f046` | `UNIQUE_ATOMIC_RUN` |
| N09 P3-CIRCLE | `P3-CIRCLE-001` | unique session `01a0fcac-51d5-7da1-b10b-52b3cfa4a9c3` | `UNIQUE_ATOMIC_RUN` |
| N10 P2-HOTT | `P2-HOTT-001` | unique session `01a0fcb1-2dda-7d52-920c-3ae4abcea104` | `UNIQUE_ATOMIC_RUN` |
| N11 P3-HOTT | `P3-HOTT-001` | unique session `01a0fcb3-a8b7-76b1-ac58-a3f62bcc741b` | `UNIQUE_ATOMIC_RUN` |
| N12 P2-ZFC | `P2-ZFC-001` | unique session `01a0fcb5-5011-7172-9b42-c09b4b9f52ee` | `UNIQUE_ATOMIC_RUN` |
| N13 P3-ZFC | `P3-ZFC-001` | unique session `01a0fcb8-10ad-7942-ac49-43fd51af318d` | `UNIQUE_ATOMIC_RUN` |
| N14 P2-CFTT | `P2-CFTT-001` | unique session `01a0fcba-b793-79d1-8aa4-2ba3de0e84fd` | `UNIQUE_ATOMIC_RUN` |
| N15 P3-CFTT | `P3-CFTT-001` | unique session `01a0fcbd-4cd8-7ed3-b65d-08f821e9761d` | `UNIQUE_ATOMIC_RUN` |
| N16 P2-CLIMBER | `P2-CLIMBER-001` | unique session `01a0fcbf-b44f-7eb1-9465-6d937ced16e5` | `UNIQUE_ATOMIC_RUN` |
| N17 P1-DELAY | `P1-DELAY-001` | unique session `01a0fccc-a8d1-7061-837b-fa9cd0575af2` | `UNIQUE_ATOMIC_RUN` |
| N18 P2-DELAY | `P2-DELAY-001` | unique session `01a0fccf-8409-7853-8596-7787a618b4f8` | `UNIQUE_ATOMIC_RUN` |
| N19 P3-DELAY | `P3-DELAY-001` | unique session `01a0fcca-f61a-7850-9366-b1dacbd4ac31` | `UNIQUE_ATOMIC_RUN` |
| N20 ZFC-COFORGE-001 | `ZFC-COFORGE-001` | unique session `01a0fce9-bb7a-7723-9a12-44f0390c4abd` | `UNIQUE_ATOMIC_RUN` |
| N21 ZFC-COFORGE-003 | `ZFC-COFORGE-003-P1` | unique session `01a0fced-d62d-76a3-a2eb-f1ccdb0c801c` | `UNIQUE_ATOMIC_RUN` |
| N22 ZFC-COFORGE-004 | `ZFC-COFORGE-004` | unique session `01a0fcfa-5379-7842-8643-560af9a32ef5` | `UNIQUE_ATOMIC_RUN` |
| N23 ZFC-COFORGE-005 | `ZFC-COFORGE-005-P1` | unique session `01a0fcfd-e6f5-7ff2-a3ac-b920081a0b48` | `UNIQUE_ATOMIC_RUN` |
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

届时才能计算 `H75 + non-H unique runs = exact atomic denominator`。在那之前，R15的`>=93`只是不应再被降低的
下界，不是完成分母。
