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

U19–U21 的 user prompt payload 完全相同；turn IDs 不同，assistant answer SHA 不同，且每次可见回复记录了不同的实际研究／工具状态。结合 U13–U15 的 range-row precedent，当前证据更支持把 archive event IDs 作为主要分母，并把重复 prompt payload／语义归并作为独立投影。完整 owner 尚未声明 19 是 raw event count 还是另一个单位分母；U13–U15 的例子说明 range-row 本身不等于去重。

因此，contributors 建议的 repair 以 event-level denominator 为主：补列 U20/U21 并保留 U19–U21 三个 distinct event IDs、answer hashes 与回答／工件映射；unique prompt SHA 与任何 semantic-intent grouping 另列为辅助计数。若 integrator 认为 owner 现有 19 已采用别的语义单位，仍须逐项映射 21 个 archive turn 到那些单位，不能由相同 prompt 自动推定。

不能把“用户内容重复”当作省略两个归档 turn 或其不同回答的理由。一个内部一致性对照是 U13–U15：三个同 prompt hash 的 turn 在 full-audit 001/003 中被分别记作 U13–U15。

### U13–U15 的 range-row 对照

我回到原文与 full-origin owner 003 §4 核验这个对照。0109 中三个 archive markers 分别是 skill-turn-c9af5d7ba12343139a157a1e845e7e81、skill-turn-42a48323f15842c684252dd3181b530e、skill-turn-6f847ba1ef9c4ba098c18ead343be605；prompt SHA 均为 377a580b17c77b477c13d882fcbcc73b652fcfc07a0c3b38facce8735cca0baa，三个 answer SHA 分别为 03d87de54dc356d3ea8763c5184bac6c8a32555c37e48549d0337afe1436a01f、e679f216af78cabb05c48a796d8659ce03d0b5ef7d71ce06a1495920539cb6de、8fbe60f995273b98f705b04c121b5b6e4e1a885dac438d9eefedd7a2aca5ceab。

Owner 003 把要求呈现成一行 U13–U15，仍保留三个编号；这支持把 archive-event identity 与表格 presentation grouping 分开。它没有证明语义意图只有一个，也没有给三条答复各自的完整 artifact map。对 U19–U21，event-level denominator 因而更适合作为首选 contributor 修订：每个 turn ID / answer hash 都要保留；如另报语义归并，必须有显式 event-to-intent mapping，不能从 prompt SHA 相同自动推出。

### Cross-session branch-integrity prompt match: 0110-T1 / 0111-T1

本 worktree 中的 parent-session archive 0110-T1 与 child-thread archive 0111-T1 也有完全相同的 prompt payload SHA-256 f76b8c736de742a4ee0c57156f39c6925dc669e0259d2f23ff39272aa402446e；可见正文都询问 Branch Session into New Git Worktree 是否会带来未提交内容完整性问题。它们分别属于 session 01a0ff8e-7790-7441-b7e6-791cca626a08 / turn skill-turn-6f102b0439554d8bb17caa88d24835d3，和 session 01a0ffa6-1527-7802-b534-9030d6f06e79 / turn skill-turn-348e1c0380ac459f9bd6eeb2491d7464；answer SHA-256 分别为 9b225e33a66d2e16f16c04d91bdef948d1d1bd374f56d5a3c64da3f5de57b8e0 与 f5b2f12809d359478b5280ba17436d85527c6a1117d124f7223f8e9398cb31db。

这证明当前可读的两个 archive copies 含有两个 distinct session/turn records 和同一 prompt payload；它不提供 native message-ID crosswalk，也不足以判断这是 fork 复制同一条输入还是用户在两个 thread 分别重发。按 worktree independence 边界，本单元仅比较当前 checkout 中已存在的 archive copies，没有打开任何其他 worktree、parent raw trajectory 或 Git checkout。此操作性重复只作 continuation/source identity 背景，不并入刀具形成前的 pre-goal denominator，也不为 parent Goal cutoff 定时。

## 12. 0102 / 0108 / 0109 archive prompt-block 与 Goal-envelope 计数核验

为检验 0109 的 21 个 markers 是否含有自动注入的 Goal continuation 包装，本单元对当前本地三个 archive snapshots 按原文结构重新计数：conversation-archive-turn markers、用户提问标题、codex_internal_context source=goal openings。结果如下：

| archive | SHA-256 | archive markers | user-prompt blocks | Goal-context envelopes |
|---|---|---:|---:|---:|
| 0102 | 3fd6c54820ba1d4b60020347f18310a76e80c8b0c07cb3d96e2bed7e25def848 | 11 | 11 | 0 |
| 0108 | cb14057dc2155cfff60e47ec2666abd042f7816f494c1122d66a5014a96f0e62 | 7 | 7 | 0 |
| 0109 | fdb556b5173f9138880ad94c8e0b1a4d47fb90f73aeeca48f05bb1f9a5e8769c | 21 | 21 | 0 |

因此在这三份本地快照中，所有 archive markers 都对应直接记录的用户提问 block；0109 的 U20/U21 不能用“Goal wrapper capture event”解释掉。0102 中 R10/R11 仍按 full-origin owner 的既定 scope 作为直接捕获但排除于刀具语义分母；0108 的 C1–C7 和 0109 的 21 个 direct prompt blocks 则保持各自来源范围。此结构计数不提供 Host native message IDs、不决定同文 prompt 是否为同一个原始 UI action，也不确定任何单条消息相对 parent Goal 的精确时刻。parent Goal cutoff 仍 UNKNOWN。

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

S12/S13 以 curation block ordinals（如 `S12[1]`、`S13[7]`）定位，conversation archive 则给出不同的 `skill-turn-*` turn IDs；当前文件未提供原生 Host message ID 交叉表。正文相同不能单独证明“同一消息被复制”，也不能证明它们是新发出的独立用户消息。因此这是一项 source provenance crosswalk gap，而非删源或数学分歧。

本单元又核了这些文件自己的来源字段：S12/S13 明确说明原始记录只稳定提供日期，并以 `[1]–[6]`、`[7]` 保留同日相对顺序；正文未带原生 `message_id`、`turn_id` 或精确消息时刻。0108/0109 archive 的 frontmatter 有 Session 级 `session_id`、`first_turn_id`、`created_at`，逐条 marker 则是 `skill-turn-*`；这些字段没有把 S12/S13 block ordinal 映射到具体 archive turn。因此六处相同正文只能留为 `CONTENT_MATCH_CANDIDATE / EVENT_ID_UNKNOWN`。如不读 parent trajectory 或取得新的用户来源交叉表，这个 event identity 未知应保留，不用文字相同代替身份。

## 6. Full-audit coverage 与 cutoff 的当前判定

- Full-audit 001/006 对 0109 声明 19 个用户 conversation units；实物有 21 个归档 turn markers。当前 owner 没有给 U20/U21 `IN_SCOPE / PRECURSOR / OUT_OF_SCOPE` disposition，也没有记录它们与 U19 的 duplicate/restatement 关系。审计 shard 003 的 U1–U19 表中没有 U20/U21；全 audit owner 内也没有这两个 turn ID。
- U20 与 U21 的 visible answer/action 已在其他 current evidence 上形成局部结果：H049–H053、D-L10F、RK-0 和后续 Git commits 出现在 005/006 或对应 audit assets 中；但“后继行为已列”不能代替“触发该行为的用户事件已逐项登记”。
- 上一轮把本 worktree Goal 的时间用于分类 U19–U21，是对象身份错配，现撤回。当前子线程的 rollout locator `rollout-2026-10-02T22-44-29-01a0ffa6-1527-7802-b534-9030d6f06e79.jsonl:5` 记录了一个 Goal event，时间为 `2026-10-02T22:45:22.640-04:00`；但 full-origin audit 已在 commit `8d4877ad`（`2026-10-02T16:14:59-04:00`）落盘，其索引用 `b810380f`（`15:53:28-04:00`）划分 parent Goal 的 historical/continuation 阶段。故 22:45 的 child-thread Goal 不能替代 full-origin audit 所指的 earlier parent Goal cutoff。
- `dev-notes/0109` 的 exact-hash snapshot mtime `2026-10-02T22:18:41-04:00`、21 个 turn markers 及 U19–U21 answer commits 最晚 `22:01:27-04:00`，只能证明这些材料在**当前 child Goal** 之前已存在。它不能证明它们在 parent Goal 之前已存在。U20/U21 所引 commits 晚于 audit owner 当前登记的 `b810380f`；这是 continuation 方向的佐证，但不是每条用户消息的 event timestamp。因为按用户“两个 worktree 各自独立”的边界，本分支不读取 previous-worktree trajectory，U19–U21 相对 parent Goal 的 phase assignment 必须保持 `UNKNOWN / PARENT_CUTOFF_NOT_REOBSERVED`。不能从这个 child Goal 推出 U19–U21 都属于 pre-goal。
- U19–U21 用户输入正文 SHA 相同，turn IDs 与 answer SHA 各异；答复依次涉及 H010／轨迹适配、全历史与 HoTT/ZFC 状态、D-L10F/RK-0/H049–H053。来源事件分母仍须保留三个独立 turn；其 parent-Goal phase 暂不裁定。full-origin current owner 仍没有 U20/U21 两行，因此全历史完成声明仍不成立。
## 7. 候选 owner 修订（未应用）

作为 contributor，我没有改 full-origin audit 001–006。建议唯一 canonical integrator 后续审核：

1. 修正 001 对 0109 的旧缩写 digest，或只保留指向 006 完整 hash 的 locator；006 的 digest 与当前 source bytes 相符。
2. 更新 001/006 的 U denominator：记录 21 个 archive turn events、17 个 archive prompt payload hashes，并按实际选择明示 event-level 或 semantic-intent-level unit definition。
3. 增加 U20/U21 的 turn ID、answer SHA、用户 intent relation、answer/result/source/Git mapping；保留 distinct response events。
4. 在 003/005 明确 S12/S13 exact-content overlaps 与 native event identity 的未知；不要用当前 child Goal 的 trajectory event 替代 full-origin audit 对应的 parent Goal。继续把 `b810380f` 标作 owner 已登记的阶段代理边界，并区分已观察提交时间与未观察的 parent 用户 turn 时间；在不读取 previous-worktree trajectory 的范围内，U19–U21 的 parent-phase 保持 `UNKNOWN`。

### 7.1 可供 integrator 评审的精确分母修订（未应用）

| Current owner | Candidate delta | Evidence / boundary |
|---|---|---|
| 001 §1.2、§2 | 将 0109 archive row 从 19 更新为 21 个 captured turn events；在 event ledger 增列 U20/U21。说明 U19 是该字面请求的首次出现，U19–U21 是同一 `prompt_sha256=a8f026…3331` 的三次 distinct archive turn，但后两次有自己的 turn ID 与 answer SHA；它们增加 event denominator，不增加新的 unique prompt payload。 | 0109 当前 bytes：21 `conversation-archive-turn` markers、21 user sections、17 unique prompt SHA；SHA `fdb556…8769c`。该来源在本 worktree 为 untracked snapshot。 |
| 003 §6 后 | 增加 U20、U21 两行：沿用 U19 的相同 wall-clock request 内容／prompt SHA，分别登记 turn ID、answer SHA、答案摘要及本报告 §4 的 commit/artifact map；intent relation 标记 `SAME_PROMPT_AS_U19 / DISTINCT_ARCHIVE_EVENT_AND_ANSWER`。 | U20 的回答记录 full-origin report、D-L7–D-L9、H015–H018、H019–H022；U21 记录 D-L10F、RK-0、H049–H053。事件身份来自本地 archive marker，技术结果仅由答复和提交路径定位，未重新审数学内容。 |
| 001/003 的 S12/S13 overlap 处 | 保留 S12[1]/[3]/[4]/[5]/[6]、S13[7] 与 archive C1/C7/U1–U4 的文本命中，但标 `CONTENT_MATCH_CANDIDATE / EVENT_ID_UNKNOWN`，不作为 event deduplication crosswalk。 | direct-source headers 只提供日期与 block ordinals；archive headers/markers 提供 session/turn 视图，未提供两者间 native message-ID mapping。 |
| 005 与 cutoff 说明 | 保留当前 owner 的 `b810380f` 阶段代理边界，明确它不是被 raw parent Goal event 直接观测到的时间戳；在不读取 previous-worktree trajectory 的前提下，U19–U21 relative phase 写 `UNKNOWN / PARENT_CUTOFF_NOT_REOBSERVED`。不要用本 child thread 的 Goal 时间或 0109 mtime 代替 parent Goal。 | full-origin audit commit `8d4877ad` 早于本 thread child Goal；这证明两者不能混用，但不单独确定 parent Goal 的真实启动时刻。U20/U21 cited response commits 晚于 `b810380f`，只说明工件在记录边界之后。 |
| 006 §1 与合计 | 将 0109 的行数／字节／SHA 保持为 1,719 / 141,651 / `fdb556…8769c`，unit coverage 改为 U1–U21、21 archive events、17 unique prompt payloads；若保留 archive-event 合计字段，把 2+11+7+19 从 39 修正为 41。R10–R11 仍保留为 capture events、按原既定规则排除于刀具语义分母。 | raw-event denominator 与 semantic-intent denominator 必须并列说明，避免把重复 prompt 直接去重或把 capture count 冒充 unique intent count。001 中旧缩写 digest 是独立漂移项，应另行修正。 |

这些是 owner-ready 的候选变更，不是当前真值；本分支不触碰 001/003/005/006。父 Goal cutoff 未闭合前，不能把 U20/U21 填成 `PRE_GOAL` 或 `GOAL_CONTINUATION` 来让表格看起来完整。

本报告没有修改原档案、full-origin owner、rulings、Feature、STATE、方向/全景或理念/SOP current owners。当前 Git 状态显示 STATE.json 为 dirty；本单元未写入或暂存它。没有 P1/P2/P3 theory task、source card、Tool-Birth 候选、数学结论或 external worker。

## 8. `dev-notes/0110`：Goal 文本恢复与 parent-session continuation 来源

当前 worktree 中还有 parent session 的 `dev-notes/0110` 归档副本：SHA-256 `574e5a84690c5f65734633f658b373788efeefc02a7a700f28568ca608c340cb`，325 行／20,261 bytes，mode `0600`；frontmatter 给出 `session_id=01a0ff8e-7790-7441-b7e6-791cca626a08`、`first_turn_id=skill-turn-6f102b0439554d8bb17caa88d24835d3`、archive `created_at=2026-10-02T22:33:07-04:00`，当前文件 mtime 为 `22:43:33-04:00`。它含 3 个 distinct archive turn：

| turn | user request / source role | prompt SHA-256 | answer SHA-256 | continuation relevance |
|---|---|---|---|---|
| `0110-T1` / `skill-turn-6f102b0439554d8bb17caa88d24835d3` | 询问 Branch Session into New Git Worktree 会否丢弃未提交内容；这是 worktree 内容与边界问题。 | `f76b8c736de742a4ee0c57156f39c6925dc669e0259d2f23ff39272aa402446e` | `9b225e33a66d2e16f16c04d91bdef948d1d1bd374f56d5a3c64da3f5de57b8e0` | 为当前 contributor 与 previous-worktree 隔离边界提供直接语境，不是 P1/P2/P3 规格。 |
| `0110-T2` / `skill-turn-a6bfba8c42384058b676c6f260e56469` | 直接提到“我们的/goal之后的内容”，要求重现最后两次改动。 | `2a6c3d4cfcdb58756fd318af9d961da7b4136e58d4950bf5eca1977c484d24cf` | `bef9d5e68c1cd4f03bf9716b3b70b881b1661bd5799d60cc321068b80c45beab` | 直接证明 parent session 中用户当时把 Goal 视为已在运行；answer 内 Git diff 不由此自动升级为本单元核实的实现事实。 |
| `0110-T3` / `skill-turn-4b1adac945c84dacb4a96837743edd2d` | 用户纠正 AI：`/goal` 后是简体中文 prompt，并在消息中完整重述“继续推进……一一自我审计、对照”的目标文本。 | `5923592ff696050c8a2b8b20db7c6d1006702f500069d1687b3e617606babd49` | `7edc199beb7104bbaa252d8cc168574189b59ae7e581fcb9ac1445fb3dec4ad3` | 是 Goal 文本恢复的直接用户来源，属于继续运行时的目标澄清，不是刀具形成前的新理论规格。 |

该 archive/session snapshot 的 `created_at=22:33:07-04:00` 晚于 owner-declared `b810380f` 和 full-origin audit commit `8d4877ad`；因此它是 continuation delta 来源，不应混入 pre-goal denominator。它提供了三条 continuation user-turn 证据，并把用户自己的 Goal 原文定位出来。archive/session `created_at` 与 file mtime 不是逐条 message 的 Host clock；0110-T2/T3 表明当时 Goal 已存在，但不确定 Goal 的精确启动时刻，也不能把 U19–U21 相对于 Goal 的 phase 由此补定。此 worktree 只读了本地 archive 副本，没有打开 parent raw trajectory 或 parent 工作目录。

候选 owner 处置是：在 continuation delta 入口单独登记 0110-T1/T2/T3 及上述 source provenance，不并入 `PRE_GOAL_HISTORICAL_CORPUS` 的 0102/0108/0109 分母；保留 T1 的工作树边界，T2/T3 的 Goal 文本恢复语义，并继续把 parent Goal precise start 标作 `UNKNOWN`，直到出现获准的直接时间来源。

## 9. 0111：当前 child thread 归档事件与独立工作区边界

本节只记录当前 worktree 内的 dev-notes/0111 archive snapshot，不以它推断或读取任何其它 checkout。观测快照身份为 SHA-256 `156c222e1c2b08867038dc9a18d330a847fc158af5781b97184c40fca108947b`、69,669 bytes、671 lines、mode 0600、mtime 2026-10-03T06:00:27-0400；frontmatter 的 session_id 是 01a0ffa6-1527-7802-b534-9030d6f06e79，与当前 Goal thread ID 相同，first_turn_id 为 skill-turn-348e1c0380ac459f9bd6eeb2491d7464。该 digest 标识本段观察时的 pre-current-turn archive snapshot；本轮最终答复归档后，0111 会追加新 turn，届时文件 digest 和事件数会变化。

该快照有 11 个 conversation-archive-turn markers。其中 4 个 prompt block 直接载有可见用户消息；另 7 个 prompt block 载有 codex_internal_context source=goal 包装，并在 assistant response 前闭合。按来源身份，这 7 个是 goal-continuation context envelope 捕获事件，不应当作为 7 条新的用户原话或 7 项独立要求；其中包裹的 objective 文本仍保留其 user-provided-data 身份。故快照分母为 11 个 archive capture events、4 个直接用户 prompt blocks，以及 7 个 goal-context envelopes；三种计数不能互相代替。

四个直接 prompt 中，T2、T3、T4 的用户正文完全相同，即“我的本意是，你跟之前的worktree，各玩各的。”三者共用 prompt SHA-256 28565a11886fcce2c23a1aec13eeb19c1f6c8635599ab1b8f994bcbdcbe4b8c6，但分别有 turn IDs skill-turn-34fe95cdb3ec4078bfebf51e3a7df6a3、skill-turn-ea9766b15cdd43b5816c61b75e39a757、skill-turn-c856e1b4ce3246ccb851e395443e0c36，及不同 answer SHA-256。它们因此是三个不同归档事件、一个重复 prompt payload group。当前 live 用户消息再次逐字重申同一边界；它不在上面观测到的 pre-current-turn snapshot 中，尚无本 turn 的 archive marker。

对本 contributor 线的操作含义是：只在当前 branch/worktree 形成、验证与提交自己的候选证据；不把另一个 worktree 的文件、Git 状态或结论作为当前行动前提。本轮只检查本 checkout 中的 0111 archive 和当前分支记录，没有打开、读取、复制、比较或写入另一个 worktree，也没有读取 parent/previous-worktree trajectory。此本地 archive census 不改 full-origin audit 的 0102/0108/0109 历史分母，不决定 U19–U21 相对 parent Goal 的 phase；该 cutoff 继续 UNKNOWN / PARENT_CUTOFF_NOT_REOBSERVED。没有改变 P1/P2/P3、ZFC_Q、Tool-Birth 或任何数学结论。

## 10. T12：最终答复前归档回执与第四次独立边界 prompt

上一单元 final 发送前的 dev-notes helper 已把 T12 追加到当前 thread 的本地 0111 archive。当前快照为 SHA-256 78d7255cdd1d2049a72a6e57dc513e25a8c3e557976a92504a4816340249ecc1、71,403 bytes、689 lines、mode 0600、mtime 2026-10-03T07:08:34-0400；包含 12 个 archive markers。对照 marker 与 prompt block 结构，当前是 5 个直接用户 prompt blocks 与 7 个 Goal-context envelopes。该结果是 T12 写入后的本地快照；本轮 Goal continuation envelope 尚未进入本快照。

T12 的 turn ID 为 skill-turn-46680583595f4d82aa63890e827a0a27，prompt SHA-256 为 28565a11886fcce2c23a1aec13eeb19c1f6c8635599ab1b8f994bcbdcbe4b8c6，answer SHA-256 为 cef5e5b4577900de9511a3c73bea0af9b830e83e674209336401968b6670efe6。其直接用户 prompt 与 T2–T4 完全相同；因此边界陈述现有四个 distinct direct archive turns、一个重复 prompt payload group、四个不同答复身份。helper receipt 显示 status=ARCHIVED 且 stage_removed=true；这是项目内 archive helper 的写入核验，不是 Host 对最终 UI 字节的事后收据。

T12 加强了当前 thread continuation 的事件分母，不改变 0102/0108/0109 的 full-origin historical denominator，也不为 U19–U21 相对 parent Goal 提供 cutoff 证据。全程只使用当前 checkout 里的 archive 与报告；没有访问或读取另一 worktree 或 parent trajectory。
