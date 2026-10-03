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

`H001--H075`已在001片登记；本片的行不与H编号混计。003 已完成 A0：本片保留候选族的原始路线，
但以 003 的 exact identity、branch disposition 和最终计数为唯一 current 判词。

canonical current branch 的 non-H 集合现为 **40** 个 exact session、**7** 个无 session 但独立可证的执行、
以及 **2** 个 Master 单位，共 **49** 个单位。此前的37/11只是冻结前下界：P1-HOTT 被漏列，ISOLATION-004/005
又已从私有 direct wire 恢复 exact session identity。未合入 branch 的三个独立 Tool-Birth 节点由003单列，
不能同 current H060--H062 按名字合并。

## 2. 已识别的 non-H 候选执行族

| 候选族 | 最小来源报告 | 初步身份 | 去重／拆分任务 |
|---|---|---|---|
| N01 P2逻辑翻译探针 | `20261002-P2-计算逻辑翻译探针-Terra-Max.md` | 代理已完成、无后代；独立设计 prompt／输出，未返 runtime ID | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| N02 朴素集合论脱敏正控制 | `20261002-模式P-朴素集合论脱敏正控制-Terra-Max.md` | 代理已完成、无后代；与后来的H050输入、runner与输出不同 | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| N03 HoTT无泄漏第一次负控制 | `20261002-模式P-HoTT无泄漏盲重放-Terra-Max.md` | 独立 prompt-bounded run；外加 resizing 的拒绝形成 L3 修复 | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| N04 ZFC一遍匹配初版 | `20261002-模式P一遍匹配ZFC盲测-Terra-Max.md` §2--§5 | 第一次独立prompt-bounded probe，Ord/V 输出 | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| N05 ZFC一遍匹配L0--L2复测 | 同报告 §6 | 修订后输入与唯一 Power Set 输出不同于N04 | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| N06 P2-FORGE | `P2-FORGE-001` | unique session `01a0fca3-9498-71f0-b8d6-255b9a65648b` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N07 P3-FORGE | `P3-FORGE-001` | unique session `01a0fca5-f826-7cd0-9731-09428db42c6d` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N08 P1-FORGE | `P1-FORGE-001` | unique session `01a0fca9-2ca7-76b2-b5fc-14812da9f046` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N09 P3-CIRCLE | `P3-CIRCLE-001` | unique session `01a0fcac-51d5-7da1-b10b-52b3cfa4a9c3` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N10 P2-HOTT | `P2-HOTT-001` | unique session `01a0fcb1-2dda-7d52-920c-3ae4abcea104` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N11 P3-HOTT | `P3-HOTT-001` | unique session `01a0fcb3-a8b7-76b1-ac58-a3f62bcc741b` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N12 P2-ZFC | `P2-ZFC-001` | unique session `01a0fcb5-5011-7172-9b42-c09b4b9f52ee` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N13 P3-ZFC | `P3-ZFC-001` | unique session `01a0fcb8-10ad-7942-ac49-43fd51af318d` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N14 P2-CFTT | `P2-CFTT-001` | unique session `01a0fcba-b793-79d1-8aa4-2ba3de0e84fd` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N15 P3-CFTT | `P3-CFTT-001` | unique session `01a0fcbd-4cd8-7ed3-b65d-08f821e9761d` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N16 P2-CLIMBER | `P2-CLIMBER-001` | unique session `01a0fcbf-b44f-7eb1-9465-6d937ced16e5` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N17 P1-DELAY | `P1-DELAY-001` | unique session `01a0fccc-a8d1-7061-837b-fa9cd0575af2` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N18 P2-DELAY | `P2-DELAY-001` | unique session `01a0fccf-8409-7853-8596-7787a618b4f8` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N19 P3-DELAY | `P3-DELAY-001` | unique session `01a0fcca-f61a-7850-9366-b1dacbd4ac31` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N20 ZFC-COFORGE-001 | `ZFC-COFORGE-001` | unique session `01a0fce9-bb7a-7723-9a12-44f0390c4abd` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N21 ZFC-COFORGE-002（文件名沿用003） | `ZFC-COFORGE-003-P1` | unique session `01a0fced-d62d-76a3-a2eb-f1ccdb0c801c`; 锻造史称其为`COFORGE-002-P1` | `UNIQUE_ATOMIC_RUN / NAMING_ALIAS / ATOMIC_AUDIT_COMPLETE` |
| N22 ZFC-COFORGE-004 | `ZFC-COFORGE-004` | unique session `01a0fcfa-5379-7842-8643-560af9a32ef5` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N23 ZFC-COFORGE-005 | `ZFC-COFORGE-005-P1` | unique session `01a0fcfd-e6f5-7ff2-a3ac-b920081a0b48` | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE` |
| N31 P1-HOTT | `P1-HOTT-001` | unique session `01a0fcae-e115-7ac1-a4fb-12bfdabd7a46`；独立中性 HoTT P1 定位，不属于 H001--H075 | `UNIQUE_ATOMIC_RUN` |
| N32 P2-FORGE首次CLI参数失败 | `P2-FORGE-001`同一报告 §运行身份 | 首次命令在模型启动前因全局参数位置错误退出；第二次才产生N06 session，失败改变实际可运行命令 | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| F24（legacy N24）Battle-001 | `P-DAG-BATTLE-001` | 3 unique sessions: `01a0fd1b-039b-77e1-895a-b5ff743ce497`; `01a0fd1b-028d-7442-a124-e3e4a6af5577`; `01a0fd1d-180b-7742-8c04-d83975b92ba1` | `FAMILY_LABEL_ONLY / SPLIT_INTO(N24A,N24B,N24C)`；005拥有稳定ID与顺序 |
| F25（legacy N25）SOURCE-001 | `P-DAG-SOURCE-001` | 4 unique sessions: `01a0fd24-e045-7e53-b290-ae608e851408`; `01a0fd24-e017-7330-8f84-cc677ee47132`; `01a0fd2c-5031-7923-b5a1-b19b5d50c37d`; `01a0fd2c-4f56-7e10-95e5-08e62223ecb8` | `FAMILY_LABEL_ONLY / SPLIT_INTO(N25A,N25B,N25C,N25D)`；005拥有稳定ID与顺序 |
| F26（legacy N26）SOURCE-002 + BATTLE-002 | `P-DAG-SOURCE-002-与-BATTLE-002` | 8 unique sessions; exact IDs frozen in this report and cross-checked against H/non-H registries | `FAMILY_LABEL_ONLY / SPLIT_INTO(N26A…N26H)`；005拥有稳定ID与顺序 |
| F27（legacy N27）SOURCE-003 | `P-DAG-SOURCE-003` | 3 unique cancelled sessions: `01a0fd5f-0afa-7773-8245-f873a22e49cc`; `01a0fd5f-0abc-7ec2-82f1-fe67d40bfff3`; `01a0fd5f-0b21-70f0-8a90-7efa8c9ea504` | `FAMILY_LABEL_ONLY / SPLIT_INTO(N27A,N27B,N27C)`；005拥有稳定ID与顺序 |
| N28 SOURCE-004 | `P-DAG-SOURCE-004` | pre-sampling connection-failure session `01a0fd6f-a6d8-7db1-a4a4-7184ff2ac118` | `UNIQUE_ATOMIC_RUNS(1) / ATOMIC_AUDIT_COMPLETE` |
| N29 SOURCE-005 | `20261002-P-DAG-SOURCE-005-Isabelle-ZF-Cantor-Master.md` | 一个Master direct-source control | `MASTER_EXECUTION_UNIT(1) / ATOMIC_AUDIT_COMPLETE` |
| N30a runner-health-001 | `P-DAG-RUNNER-HEALTH-001` NodeCard | 只有预封存卡，未见执行收据 | `NODECARD_ONLY_NOT_COUNTED` |
| N30b runner-isolation-002 | `P-DAG-RUNNER-ISOLATION-002-RESULT` | 实际空home认证执行，401发生在模型采样前；独立 prompt／empty-home receipt | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE` |
| N30c isolation-003 | `CODEX-APPSERVER-ISOLATION-003` | prompt-input gate在auth前停止；run id `p-dag-appserver-health-003` 与 receipt 独立 | `UNIQUE_DOCUMENTED_EXECUTION(1) / ATOMIC_AUDIT_COMPLETE_EVIDENCE_INSUFFICIENT_WITH_SCOPE` |
| N30d isolation-004 | `CODEX-APPSERVER-ISOLATION-004` | exact direct-wire session `01a0fdd4-36a9-77e3-bd87-63a3d17077ee`，post-turn API不兼容 | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE_SOURCE_REPORTED_NOT_REPLAYED` |
| N30e isolation-005 | `CODEX-APPSERVER-ISOLATION-005` | exact direct-wire session `01a0fdd5-71bd-76c2-983e-d2b802ee8199`，zero-theory health通过；不是H008 discovery | `UNIQUE_ATOMIC_RUN / ATOMIC_AUDIT_COMPLETE_SOURCE_REPORTED_NOT_REPLAYED` |
| N30f AppServer资格检查 | `20261002-P-DAG-AppServer-资格检查.md` | Master host-capability source inspection，未启动 worker | `UNIQUE_MASTER_DECISION(1)` |

## 3. 下阶段的可证伪完成条件

A0 已将本片候选族裁定为以下之一；branch-qualified 实际节点与最终计数见003：

```text
UNIQUE_ATOMIC_RUNS(n, exact identities)
UNIQUE_DOCUMENTED_EXECUTION(n, source/run identity rationale)
UNIQUE_MASTER_DECISION(n, exact source action)
DUPLICATE_OF(Hxxx or Nxxx, exact reason)
NO_MODEL_SAMPLING_BUT_EXECUTION_UNIT
OUT_OF_SCOPE_WITH_REASON
```

004 已修正为 `H75 + canonical non-H50 + branch candidate3 = D_atomic 128`。R15的`>=112`与`>=123`保留为当时的
下界历史，不再是 current 分母。
