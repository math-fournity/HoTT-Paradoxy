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

目前已从 N06--N28 提取出 37 个彼此不同的 session ID，并与 H 报告中可提取的身份交叉检查为无交集，
故它们可以作为原子总分母的已确认 non-H 运行。N01--N05、N29和N30已确认实际发生但没有统一runtime ID；
它们构成11个额外的工作单元，不与37个session run混写。

## 2. 已识别的 non-H 候选执行族

| 候选族 | 最小来源报告 | 初步身份 | 去重／拆分任务 |
|---|---|---|---|
| N01 P2逻辑翻译探针 | `20261002-P2-计算逻辑翻译探针-Terra-Max.md` | 代理已完成、无后代；无独立runtime identity | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N02 朴素集合论脱敏正控制 | `20261002-模式P-朴素集合论脱敏正控制-Terra-Max.md` | 代理已完成、无后代；与后来的H050不可凭名称合并 | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N03 HoTT无泄漏第一次负控制 | `20261002-模式P-HoTT无泄漏盲重放-Terra-Max.md` | 代理已完成、无后代；prompt-bounded run | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N04 ZFC一遍匹配初版 | `20261002-模式P一遍匹配ZFC盲测-Terra-Max.md` §2--§5 | 第一次独立prompt-bounded probe | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N05 ZFC一遍匹配L0--L2复测 | 同报告 §6 | 新的修订prompt probe | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
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
| N21 ZFC-COFORGE-002（文件名沿用003） | `ZFC-COFORGE-003-P1` | unique session `01a0fced-d62d-76a3-a2eb-f1ccdb0c801c`; 锻造史称其为`COFORGE-002-P1` | `UNIQUE_ATOMIC_RUN / NAMING_ALIAS` |
| N22 ZFC-COFORGE-004 | `ZFC-COFORGE-004` | unique session `01a0fcfa-5379-7842-8643-560af9a32ef5` | `UNIQUE_ATOMIC_RUN` |
| N23 ZFC-COFORGE-005 | `ZFC-COFORGE-005-P1` | unique session `01a0fcfd-e6f5-7ff2-a3ac-b920081a0b48` | `UNIQUE_ATOMIC_RUN` |
| N24 Battle-001 | `P-DAG-BATTLE-001` | 3 unique sessions: `01a0fd1b-039b-77e1-895a-b5ff743ce497`; `01a0fd1b-028d-7442-a124-e3e4a6af5577`; `01a0fd1d-180b-7742-8c04-d83975b92ba1` | `UNIQUE_ATOMIC_RUNS(3)` |
| N25 SOURCE-001 | `P-DAG-SOURCE-001` | 4 unique sessions: `01a0fd24-e045-7e53-b290-ae608e851408`; `01a0fd24-e017-7330-8f84-cc677ee47132`; `01a0fd2c-5031-7923-b5a1-b19b5d50c37d`; `01a0fd2c-4f56-7e10-95e5-08e62223ecb8` | `UNIQUE_ATOMIC_RUNS(4)` |
| N26 SOURCE-002 + BATTLE-002 | `P-DAG-SOURCE-002-与-BATTLE-002` | 8 unique sessions; exact IDs frozen in this report and cross-checked against H/non-H registries | `UNIQUE_ATOMIC_RUNS(8)` |
| N27 SOURCE-003 | `P-DAG-SOURCE-003` | 3 unique cancelled sessions: `01a0fd5f-0afa-7773-8245-f873a22e49cc`; `01a0fd5f-0abc-7ec2-82f1-fe67d40bfff3`; `01a0fd5f-0b21-70f0-8a90-7efa8c9ea504` | `UNIQUE_ATOMIC_RUNS(3)` |
| N28 SOURCE-004 | `P-DAG-SOURCE-004` | pre-sampling connection-failure session `01a0fd6f-a6d8-7db1-a4a4-7184ff2ac118` | `UNIQUE_ATOMIC_RUNS(1)` |
| N29 SOURCE-005 | `20261002-P-DAG-SOURCE-005-Isabelle-ZF-Cantor-Master.md` | 一个Master direct-source control | `MASTER_EXECUTION_UNIT(1)` |
| N30a runner-health-001 | `P-DAG-RUNNER-HEALTH-001` NodeCard | 只有预封存卡，未见执行收据 | `NODECARD_ONLY_NOT_COUNTED` |
| N30b runner-isolation-002 | `P-DAG-RUNNER-ISOLATION-002-RESULT` | 实际空home认证执行，401发生在模型采样前 | `NO_MODEL_SAMPLING_BUT_EXECUTION_UNIT(1)` |
| N30c isolation-003 | `CODEX-APPSERVER-ISOLATION-003` | 实际prompt-input gate在auth前停止 | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N30d isolation-004 | `CODEX-APPSERVER-ISOLATION-004` | 实际到达App Server，post-turn API不兼容 | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N30e isolation-005 | `CODEX-APPSERVER-ISOLATION-005` | zero-theory health通过；不是H008 discovery本身 | `DOCUMENTED_EXECUTION_IDENTITY_MISSING(1)` |
| N30f AppServer资格检查 | `20261002-P-DAG-AppServer-资格检查.md` | Master host-capability source inspection | `MASTER_EXECUTION_UNIT(1)` |

## 3. 下阶段的可证伪完成条件

non-H ledger 只有在每个候选族都被裁定为以下之一后，才可合并进总分母：

```text
UNIQUE_ATOMIC_RUNS(n, exact identities)
DUPLICATE_OF(Hxxx or Nxxx, exact reason)
NO_MODEL_SAMPLING_BUT_EXECUTION_UNIT
OUT_OF_SCOPE_WITH_REASON
```

届时才能计算 `H75 + non-H unique runs + classified no-ID/Master units = exact atomic denominator`。
在那之前，R15的`>=112`是身份去重session/run下界，`>=123`是完整锻打工作单元下界，二者都不是完成分母。
