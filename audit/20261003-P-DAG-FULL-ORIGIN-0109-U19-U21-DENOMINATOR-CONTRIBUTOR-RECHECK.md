# 0109 来源分母复核：U19–U21 与重复原文的 contributor evidence

> **身份：** `CANDIDATE_NOT_CURRENT / CONTRIBUTOR_EVIDENCE / SOURCE_COVERAGE_RECHECK_REQUIRED`。本报告只记录当前分支对可读历史来源快照的有限复核；不改 full-origin audit owner，不把本地未跟踪 archive 变成已集成 source，也不构成数学结论。

## 1. 任务与边界

此单元复核 full-origin audit 对 `dev-notes/0109` 的 turn denominator、U19–U21 的 prompt/answer 身份、S12/S13 与 conversation archive 之间的文本重叠，以及审计 shards 中对应 unit 的可定位性。它不重新论证 P1/P2/P3，不复审每个 source card 的数学判词，也不决定任何 ZFC Q。

当前角色是 `CONTRIBUTOR`：用户要求各 worktree 独立推进，而没有指定 canonical integrator/target。本报告与同目录 session audit 只作为本分支 `CANDIDATE_NOT_CURRENT` 证据；`audit/20261002-P-DAG-刀具系统全历史逐段对照审计.md` 及其 shards 保持原样，current-owner 写回待后续集成决定。没有读取先前 worktree。

## 2. 当前可读来源快照

| 来源 | 当前身份 / 计数 | SHA-256 | 状态 |
|---|---|---|---|
| `dev-notes/0102…` | 11 用户提问区块 / 11 archive turn markers | `3fd6c54820ba1d4b60020347f18310a76e80c8b0c07cb3d96e2bed7e25def848` | 与 full-audit 006 的 11-unit 清单一致；当前 worktree untracked。 |
| `dev-notes/0108…` | 7 用户提问区块 / 7 archive turn markers | `cb14057dc2155cfff60e47ec2666abd042f7816f494c1122d66a5014a96f0e62` | 与 full-audit 006 的 C1–C7 清单一致；当前 worktree untracked。 |
| `dev-notes/0109…` | **21** 用户提问区块 / **21** archive turn markers / 17 个不同 prompt SHA | `fdb556b5173f9138880ad94c8e0b1a4d47fb90f73aeeca48f05bb1f9a5e8769c` | 与 full-audit 006 的完整 SHA、1,719 行、141,651 bytes 相符；但 001/006 的 unit count 只写 19；当前 worktree untracked。 |
| Full-origin audit 001 | 文字上列 `U1–U19`，并引用 `0109` 的缩写 `8b7b2f…17dae` | `0a7e893561e4cbfc1a70e9858eb3ce46e2f50208768dbb2c61b8bbbc69932355` | 旧摘要 hash 不以当前完整 SHA 开头；未说明该摘要对应哪个旧快照。 |
| Full-origin audit 006 | 列 0109 完整 SHA `fdb556…8769c`、1,719 / 141,651，并声明 U1–U19 | `2e7f7e9ea88db5c13319b559194932eae756509d04989a379752ce2ba10e9742` | 文件身份匹配，事件分母不匹配。 |

## 3. 18 项来源清单重算

按 full-audit 006 列出的 13 个 prompt files + 5 个 conversation archives（18 个文件），逐项用 Python 标准库重算 `SHA-256(bytes)`、`len(bytes)` 和 `bytes.count(b"\\n")`，18 项都与 006 的完整 hash/lines/bytes 相符。0102、0108 的 turn count 也与当前清单相符；本次明确发现的 raw-event 计数差异集中在 0109。

**证据边界：** 这是对当前本地可读 bytes 的复核。`0108` 与 `0109` 在本 worktree 中未跟踪，故 full-audit 006 的当前 hash 目前只标识这份本地快照，不证明这些 bytes 已被版本化或其他 worktree 具有同一 snapshot。用户来源文件未被修改。

## 4. 0109 的 21 个归档事件与 full-audit 19-unit 分母

0109 的每个 `### 用户提问` 块均有一个不同的 `conversation-archive-turn` turn ID。当前 full-origin audit 001/006 只逐项声明 U1–U19，因此相对归档事件分母有两个未被命名处置的 event。归档内还存在重复 prompt 内容：

| 归档事件 | turn ID | prompt SHA-256 | answer SHA-256 | 可见回复差分 |
|---|---|---|---|---|
| U19 | `skill-turn-3d195a9b315541dc8de06731bbc10e56` | `a8f026a330d0cabe637cf6e68e507f9b353c29958afdb6d34b6aeb63f9ba3331` | `84df8c503771175876bab0c073ce5d777401fe47dbd7a6890d9995a068f68388` | 更新无自动墙钟中止规则、direct-wire trajectory 适配与 H010 P1 部分 replay。 |
| U20 | `skill-turn-c980d46fc6fa446c9dbeb5b0b8bf264a` | 同 U19 | `fec7d8a445a7526689c9905b4c5abccbb9446c03dd0bb899fa190366374cec4` | 报告 full-history audit、D-L7–D-L9、HoTT 限定 replay、ZFC 状态和运行证据。 |
| U21 | `skill-turn-4d3398c25c71415e94066b2ad405dfde` | 同 U19 | `89a65a0358bc39cddc9b2b399bf4263732466b9b18d077d69a506e61f84bc31e` | 报告 D-L10F、RK-0、H049–H053 与 Gemini 旧文作为控制。 |

归档回复实际引用的项目 Git 对象均在当前 repo object database 中可解析；以下完整 OID/subject/path facts 由本轮在当前分支执行 `git show` 得到：

| 用户 turn | 回复里的项目 commit OIDs | 已核实的项目变更范围 |
|---|---|---|
| U19 | `3060452a67a2df7a2010074c178527b4a42affc1`; `a9e796102ef2fddfcd66e0aee0c0a8fb78b0ba61`; `15d2bbd972ff3d0eb6cc2a1c5d589f492597fafa`; `c678f737444ff913e1c9efcbf5645f8fbae7c5ed`; `b810380f715fa1960cf4ab229c45d02cef0937a5` | App Server trajectory audit/H010 NodeCard and source validation、观察/无墙钟中断规则、H010 replay 与打造过程记录。 |
| U20 | `8d4877ad8abd110cb31973408eb46d0155de14fd`; `73989d3bbc6fd7f0e6bd7fe20d7e80f958fc68e2`; `6fe90224a779ddf4ffaee6a992952d14516448d9`; `a4f6ca731f701bb005b421eb9936b66076155dfa`; `754727f55c2bfcf49c1068638a2d23d14bdfef97`; `4faffd4d7e5f3a3826793fefc97680e200c9f2aa`; `137ede0e2350daa6d1e522d842c77a59fd45c0bc`; `d66a78d4ad4ece0e8cd2d403fe3c80c7ede3f94c`; `f32c2293a39db46b6e11a1e055297d97a26c2209` | full-origin report、source-aware/liveness rules、D-L7/D-L8/D-L9、HoTT H015–H018 replay、ZFC H019–H022 source gap、continuation self-audit。 |
| U21 | `3d7918e56b661e17b11ea6a7cc3f31c5939bb773`; `a39e9afac295615d516baf9bb7757323a590959a`; `a4cc5c8861b7e213e103c122c4ca87c3383ce390`; `43eeacd11e141354b147d3f0d981d3a9782b09d4` | formation-origin D-L10F and no-candidate terminal、RK-0 shared kernel、H049–H053 Power Set control evidence. |

U19 的答复还提到了 shared-governance repo 的 reader/runtime commit refs；它们不是本项目 Git 对象，未在本 contributor unit 中对外部 repo 重做核验。上表只审计 `HoTT_AI_HANDOFF_20260911` 当前 repo 中可见、与回答明确关联的 project commits；commit 目标路径可佐证有对应工件，不单独证明回答中的技术/数学结论。

三个 user prompt payload 完全相同；turn IDs 不同，assistant answer SHA 不同，且每次可见回复记录了不同的实际研究／工具状态。这支持两种合法的审计表达，但当前 owner 没有选定其中一种：

1. **Event-level denominator（建议）：** 将 U19、U20、U21 各列一行，标记相同 prompt 的重复请求关系，并分别链接各自不同的答复、commit 和运行证据；或
2. **Semantic-intent denominator：** 说明 19 是归并后的 intent unit 数，把 U20/U21 明确映射到 U19，同时分别保留两个回答与实现变化的审计链接。

不能把“用户内容重复”当作省略两个归档 turn 或其不同回答的理由。一个内部一致性对照是 U13–U15：三个同 prompt hash 的 turn 在 full-audit 001/003 中被分别记作 U13–U15。

## 5. S12/S13 与 archives 的 exact-content overlap

用去空白后的用户消息正文比较 source prompt 与三份直接会话 archives，发现以下内容相同关系：

| Direct source block | Archive block | 比较结果 | 事件身份 |
|---|---|---|---|
| S12 `[1]` | 0108 turn 1 | 去空白后正文相同 | `MESSAGE_IDENTITY_UNKNOWN` |
| S12 `[3]` | 0108 turn 7 | 去空白后正文相同 | `MESSAGE_IDENTITY_UNKNOWN` |
| S12 `[4]` | 0109 U1 | 去空白后正文相同 | `MESSAGE_IDENTITY_UNKNOWN` |
| S12 `[5]` | 0109 U2 | 去空白后正文相同 | `MESSAGE_IDENTITY_UNKNOWN` |
| S12 `[6]` | 0109 U3 | 去空白后正文相同 | `MESSAGE_IDENTITY_UNKNOWN` |
| S13 `[7]` | 0109 U4 | 去空白后正文相同 | `MESSAGE_IDENTITY_UNKNOWN` |
| S12 `[2]` | 0102/0108/0109 已检查用户消息 | 未找到去空白后的正文相同项 | 不作全局缺失结论；S12 本身仍是直接用户来源 |

S12/S13 给出 curation message IDs，conversation archive 给出不同的 `skill-turn-*` turn IDs；当前文件未提供原生 Host message ID 交叉表。正文相同不能单独证明“同一消息被复制”，也不能证明它们是新发出的独立用户消息。因此这是一项 source provenance crosswalk gap，而非删源或数学分歧。

## 6. Full-audit coverage 与 cutoff 的当前判定

- Full-audit 001/006 对 0109 声明 19 个用户 conversation units；实物有 21 个归档 turn markers。当前 owner 没有给 U20/U21 `IN_SCOPE / PRECURSOR / OUT_OF_SCOPE` disposition，也没有记录它们与 U19 的 duplicate/restatement 关系。审计 shard 003 的 U1–U19 表中没有 U20/U21；全 audit owner 内也没有这两个 turn ID。
- U20 与 U21 的 visible answer/action 已在其他 current evidence 上形成局部结果：H049–H053、D-L10F、RK-0 和后续 Git commits 出现在 005/006 或对应 audit assets 中；但“后继行为已列”不能代替“触发该行为的用户事件已逐项登记”。
- 006 的 Git 边界 commit `b810380f`（2026-10-02 15:53 `-0400`）。U19–U21 在 archive 中按顺序位于 H010 后；U21 的 response commits 晚于 `b810380f`。但 archive 只提供日期/顺序与 turn IDs，不提供每个用户 turn 的可靠墙钟时间；assistant commit 时间不能替用户消息时间。当前 source 不能证明原始 `/goal` cutoff 在哪一条 turn，因此 U19–U21 的 `PRE_GOAL_HISTORICAL_CORPUS` vs `GOAL_CONTINUATION_DELTA` 身份仍为 `UNKNOWN / REQUIRES_CUTOFF_SOURCE`。
- U19–U21 用户输入的语义均为同一 wall-clock policy 请求；其回答依次推进 H010/轨迹适配、全历史与 HoTT/ZFC 状态、D-L10F/RK-0/H049–H053。若要保持“每个讨论单元逐项审计”，要么逐事件编号并关联三组答复，要么明确批准按 intent 合并、同时保留所有答复与 cutoff 情况。当前 full-origin 完成声明不能成立。

## 7. 候选 owner 修订（未应用）

作为 contributor，我没有改 full-origin audit 001–006。建议唯一 canonical integrator 后续审核：

1. 修正 001 对 0109 的旧缩写 digest，或只保留指向 006 完整 hash 的 locator；006 的 digest 与当前 source bytes 相符。
2. 更新 001/006 的 U denominator：记录 21 个 archive turn events、17 个 archive prompt payload hashes，并按实际选择明示 event-level 或 semantic-intent-level unit definition。
3. 增加 U20/U21 的 turn ID、answer SHA、用户 intent relation、answer/result/source/Git mapping；保留 distinct response events。
4. 在 003/005 明确 S12/S13 exact-content overlaps 与 native event identity 的未知，并以真实 `/goal` source/cutoff 证据归属 U19–U21；不要由同日日期、文件标题或助手提交时间单独推定。

本报告没有修改原档案、full-origin owner、rulings、Feature、STATE、方向/全景或理念/SOP current owners。当前 Git 状态显示 STATE.json 为 dirty；本单元未写入或暂存它。没有 P1/P2/P3 theory task、source card、Tool-Birth 候选、数学结论或 external worker。
